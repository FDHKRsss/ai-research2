# -*- coding: utf-8 -*-
"""Tests for the M4 stub *tracking* state in docs/PLAN.md and docs/ARCHITECTURE.md.

The M4 deliverable section itself is validated by tests/test_m4_stub.py. This file
validates the bookkeeping that wraps it: PLAN.md must mark `M4 -- stub` done (and
nothing prematurely beyond M4), and ARCHITECTURE.md "Stan wdrożenia" must record the
M4 stub as ready while narrowing the remaining stub work to M5–M6.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

# A milestone checkbox line looks like: "  - [x] M4 -- stub"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = {f"M{i}" for i in range(1, 7)}
DONE_STUBS_EXPECTED = {"M1", "M2", "M3", "M4"}


def _load(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _plan_statuses(text: str) -> dict:
    """Map (milestone, pass) -> done from PLAN.md milestone checkboxes."""
    statuses = {}
    for line in text.splitlines():
        m = MILESTONE_RE.match(line)
        if m:
            statuses[(m.group(2), m.group(3))] = m.group(1).lower() == "x"
    return statuses


def _arch_wdrozenie(text: str) -> str:
    """Return the '## Stan wdrożenia' section (up to the next '## ')."""
    marker = "## Stan wdrożenia"
    idx = text.find(marker)
    if idx == -1:
        return ""
    rest = text[idx + len(marker):]
    nxt = rest.find("\n## ")
    return rest if nxt == -1 else rest[:nxt]


class TestM4Tracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    # -- PLAN.md --------------------------------------------------------------

    def test_01_plan_m4_stub_marked_done(self):
        self.assertTrue(
            self.statuses.get(("M4", "stub"), False),
            "PLAN.md must mark M4 -- stub as [x]",
        )

    def test_02_plan_m4_real_still_pending(self):
        self.assertFalse(
            self.statuses.get(("M4", "real"), True),
            "PLAN.md must keep M4 -- real as [ ] (only stub is done)",
        )

    def test_03_plan_only_m1_m2_m3_m4_stubs_done(self):
        done = {m for (m, p), d in self.statuses.items() if p == "stub" and d}
        self.assertEqual(done, DONE_STUBS_EXPECTED,
                         "only M1/M2/M3/M4 -- stub may be checked; M5-M6 must stay pending")

    def test_04_plan_no_real_milestone_marked_done(self):
        for (m, p), d in self.statuses.items():
            if p == "real":
                self.assertFalse(d, f"PLAN.md must not mark {m} -- real as done in pass 1")

    def test_05_plan_parent_m4_milestone_not_prematurely_done(self):
        found = False
        for line in self.plan.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [") and "**M4" in line:
                self.assertTrue(
                    stripped.startswith("- [ ]"),
                    "parent M4 milestone must stay unchecked until its real pass is done",
                )
                found = True
                break
        self.assertTrue(found, "parent M4 milestone checkbox line not found")

    # -- ARCHITECTURE.md ------------------------------------------------------

    def test_06_arch_m4_stub_entry_present_and_green(self):
        self.assertIn("**M4 -- stub:**", self.wdrozenie, "ARCH must list the M4 stub entry")
        for marker in ("gotowy", "nie znaleziono informacji o OC"):
            self.assertIn(marker, self.wdrozenie, f"ARCH M4 entry missing marker: {marker}")

    def test_07_arch_m4_stub_entry_lists_coverage(self):
        for marker in ("specjalizacja", "ubezpieczenie OC", "certyfikaty",
                       "doświadczenie kadry", "kanały kontaktu"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH M4 entry must list covered dimension: {marker}")
        for ident in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(ident, self.wdrozenie,
                          f"ARCH M4 entry must record disambiguation identifier: {ident}")

    def test_08_arch_m4_stub_entry_states_risk(self):
        self.assertIn("ocena ryzyka M4 = Średnie", self.wdrozenie,
                      "ARCH M4 entry must state the M4 risk rating (Średnie)")

    def test_09_arch_remaining_work_narrowed_to_m5_m6(self):
        self.assertIn("M5–M6 -- stub", self.wdrozenie,
                      "ARCH remaining-work bullet must be M5–M6 -- stub")
        self.assertIn("do wykonania", self.wdrozenie,
                      "ARCH remaining-work bullet must say 'do wykonania'")
        # The old too-wide bullets must be gone.
        self.assertNotIn("M4–M6 -- stub", self.wdrozenie)
        self.assertNotIn("M4-M6 -- stub", self.wdrozenie)
        self.assertNotIn("M3–M6 -- stub", self.wdrozenie)

    def test_10_arch_earlier_entries_intact(self):
        for marker in ("11 testów zielonych", "tests.test_m1_stub",
                       "16 testów zielonych", "tests.test_m2_stub",
                       "15 testów zielonych", "tests.test_m3_stub"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH must keep earlier M1/M2/M3 stub entry intact: {marker}")

    # -- cross-consistency ----------------------------------------------------

    def test_11_cross_consistency_plan_vs_arch_done_stubs(self):
        arch_done = set()
        for m in ALL_MILESTONES:
            marker = f"**{m} -- stub:**"
            for line in self.wdrozenie.splitlines():
                if marker in line:
                    if "gotowy" in line:
                        arch_done.add(m)
                    break
        plan_done = {m for (m, p), d in self.statuses.items() if p == "stub" and d}
        self.assertEqual(plan_done, arch_done,
                         "PLAN done stubs must match ARCH 'gotowy' stub entries")


if __name__ == "__main__":
    unittest.main(verbosity=2)
