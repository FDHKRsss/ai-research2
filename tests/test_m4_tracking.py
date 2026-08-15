# -*- coding: utf-8 -*-
"""Tests for the M4 *tracking* state in docs/PLAN.md and docs/ARCHITECTURE.md.

The M4 deliverable section itself is validated by tests/test_m4_stub.py and the
pass-2 grounding by tests/test_m4_real.py. This file validates the M4 bookkeeping
plus the durable cross-milestone invariants.

Forward-compatible by design: completed milestones stay completed, so M4 -- stub
and M4 -- real are asserted as DONE, and the parent-M4 checkbox is asserted to
MATCH the M4 -- real status (derived from PLAN.md, not a hardcoded snapshot). The
exact "which reals are done" snapshot lives in tests/test_m4_real.py.
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
ORDER = ("M1", "M2", "M3", "M4", "M5", "M6")
# M1–M4 must remain done; later milestones may additionally be done.
MIN_DONE_STUBS = {"M1", "M2", "M3", "M4"}


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

    def test_02_plan_m4_real_marked_done(self):
        self.assertTrue(
            self.statuses.get(("M4", "real"), False),
            "PLAN.md must mark M4 -- real as [x] (completed in pass 2)",
        )

    def test_03_plan_m1_through_m4_stubs_remain_done(self):
        done = {m for (m, p), d in self.statuses.items() if p == "stub" and d}
        self.assertTrue(
            MIN_DONE_STUBS <= done,
            "M1/M2/M3/M4 -- stub must remain checked (later milestones may also be done)",
        )

    def test_04_plan_real_milestones_done_in_order(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        done_idx = {i for i, m in enumerate(ORDER) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_05_plan_parent_m4_matches_m4_real_status(self):
        m4_real = self.statuses.get(("M4", "real"), False)
        found = False
        for line in self.plan.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [") and "**M4" in line:
                self.assertEqual(
                    stripped.startswith("- [x]"), m4_real,
                    "parent M4 checkbox must match the M4 -- real status",
                )
                found = True
                break
        self.assertTrue(found, "parent M4 milestone checkbox line not found")

    # -- ARCHITECTURE.md ------------------------------------------------------

    def test_06_arch_m4_stub_entry_present_and_green(self):
        self.assertIn("**M4 -- stub:**", self.wdrozenie, "ARCH must list the M4 stub entry")
        self.assertIn("gotowy", self.wdrozenie, "ARCH M4 entry must record M4 as ready")

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

    def test_09_arch_remaining_work_is_a_later_milestone(self):
        self.assertIn("do wykonania", self.wdrozenie,
                      "ARCH remaining-work bullet must say 'do wykonania'")
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
