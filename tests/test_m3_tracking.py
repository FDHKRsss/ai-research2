# -*- coding: utf-8 -*-
"""Tests for the M3 stub *tracking* state in docs/PLAN.md and docs/ARCHITECTURE.md.

The M3 deliverable section itself is validated by tests/test_m3_stub.py. This file
validates the bookkeeping that wraps it: PLAN.md must mark `M3 -- stub` done (and
nothing prematurely), and ARCHITECTURE.md "Stan wdrożenia" must record the M3 stub
as ready while narrowing the remaining stub work to M4–M6.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

# A milestone checkbox line looks like: "  - [x] M3 -- stub"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = {f"M{i}" for i in range(1, 7)}
DONE_STUBS_EXPECTED = {"M1", "M2", "M3"}


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


class TestM3Tracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    # -- PLAN.md --------------------------------------------------------------

    def test_01_plan_m3_stub_marked_done(self):
        self.assertTrue(
            self.statuses.get(("M3", "stub"), False),
            "PLAN.md must mark M3 -- stub as [x]",
        )

    def test_02_plan_m3_real_still_pending(self):
        self.assertFalse(
            self.statuses.get(("M3", "real"), True),
            "PLAN.md must keep M3 -- real as [ ] (only stub is done)",
        )

    def test_03_plan_only_m1_m2_m3_stubs_done(self):
        done = {m for (m, p), d in self.statuses.items() if p == "stub" and d}
        self.assertEqual(done, DONE_STUBS_EXPECTED,
                         "only M1/M2/M3 -- stub may be checked; M4-M6 must stay pending")

    def test_04_plan_no_real_milestone_marked_done(self):
        for (m, p), d in self.statuses.items():
            if p == "real":
                self.assertFalse(d, f"PLAN.md must not mark {m} -- real as done in pass 1")

    def test_05_plan_parent_m3_milestone_not_prematurely_done(self):
        found = False
        for line in self.plan.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [") and "**M3" in line:
                self.assertTrue(
                    stripped.startswith("- [ ]"),
                    "parent M3 milestone must stay unchecked until its real pass is done",
                )
                found = True
                break
        self.assertTrue(found, "parent M3 milestone checkbox line not found")

    # -- ARCHITECTURE.md ------------------------------------------------------

    def test_06_arch_m3_stub_entry_present_and_green(self):
        self.assertIn("**M3 -- stub:**", self.wdrozenie, "ARCH must list the M3 stub entry")
        for marker in ("gotowy", "15 testów zielonych", "tests.test_m3_stub"):
            self.assertIn(marker, self.wdrozenie, f"ARCH M3 entry missing marker: {marker}")

    def test_07_arch_m3_stub_entry_lists_coverage(self):
        for platform in ("Google Maps", "GoWork", "Oferteo", "Facebook"):
            self.assertIn(platform, self.wdrozenie,
                          f"ARCH M3 entry must list covered platform: {platform}")

    def test_08_arch_m3_stub_entry_states_12_month_window(self):
        self.assertIn("2025-08-15", self.wdrozenie, "ARCH M3 entry missing window start")
        self.assertIn("2026-08-15", self.wdrozenie, "ARCH M3 entry missing window end")

    def test_09_arch_remaining_work_narrowed_to_m4_m6(self):
        self.assertIn("M4–M6 -- stub", self.wdrozenie,
                      "ARCH remaining-work bullet must be M4–M6 -- stub")
        self.assertIn("do wykonania", self.wdrozenie,
                      "ARCH remaining-work bullet must say 'do wykonania'")
        # The old too-wide bullet must be gone.
        self.assertNotIn("M3–M6 -- stub", self.wdrozenie)
        self.assertNotIn("M3-M6 -- stub", self.wdrozenie)

    def test_10_arch_m1_m2_entries_intact(self):
        for marker in ("11 testów zielonych", "tests.test_m1_stub",
                       "16 testów zielonych", "tests.test_m2_stub"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH must keep earlier M1/M2 stub entry intact: {marker}")

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
