# -*- coding: utf-8 -*-
"""Tests for the M6 *tracking* state in docs/PLAN.md and docs/ARCHITECTURE.md.

The M6 deliverable section itself is validated by tests/test_m6_stub.py and the
pass-2 grounding by tests/test_m6_real.py. This file validates the M6 bookkeeping
plus the durable cross-milestone invariants.

Forward-compatible by design: completed milestones stay completed, so M6 -- stub
and M6 -- real are asserted as DONE, and the parent-M6 checkbox is asserted to
MATCH the M6 -- real status (derived from PLAN.md, not a hardcoded snapshot).
The exact "which reals are done" snapshot lives in the current milestone's real
test (tests/test_m6_real.py).
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

# A milestone checkbox line looks like: "  - [x] M6 -- stub"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = {f"M{i}" for i in range(1, 7)}
ORDER = ("M1", "M2", "M3", "M4", "M5", "M6")
# All six stubs must remain done; later milestones may additionally be done.
DONE_STUBS_EXPECTED = {"M1", "M2", "M3", "M4", "M5", "M6"}


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


class TestM6Tracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    # -- PLAN.md --------------------------------------------------------------

    def test_01_plan_m6_stub_marked_done(self):
        self.assertTrue(
            self.statuses.get(("M6", "stub"), False),
            "PLAN.md must mark M6 -- stub as [x]",
        )

    def test_02_plan_m6_real_marked_done(self):
        self.assertTrue(
            self.statuses.get(("M6", "real"), False),
            "PLAN.md must mark M6 -- real as [x] (completed in pass 2)",
        )

    def test_03_plan_exactly_m1_through_m6_stubs_done(self):
        done = {m for (m, p), d in self.statuses.items() if p == "stub" and d}
        self.assertEqual(done, DONE_STUBS_EXPECTED,
                         "exactly M1/M2/M3/M4/M5/M6 -- stub may be checked")

    def test_04_plan_real_milestones_done_in_order(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        done_idx = {i for i, m in enumerate(ORDER) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_05_plan_parent_m6_matches_m6_real_status(self):
        m6_real = self.statuses.get(("M6", "real"), False)
        found = False
        for line in self.plan.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [") and "**M6" in line:
                self.assertEqual(
                    stripped.startswith("- [x]"), m6_real,
                    "parent M6 checkbox must match the M6 -- real status",
                )
                found = True
                break
        self.assertTrue(found, "parent M6 milestone checkbox line not found")

    # -- ARCHITECTURE.md ------------------------------------------------------

    def test_06_arch_m6_stub_entry_present_and_green(self):
        self.assertIn("**M6 -- stub:**", self.wdrozenie, "ARCH must list the M6 stub entry")
        self.assertIn("gotowy", self.wdrozenie, "ARCH M6 entry must record M6 as ready")

    def test_07_arch_m6_stub_entry_lists_coverage(self):
        for marker in ("Synteza ryzyka", "ocen cząstkowych", "końcowa ocena ryzyka",
                       "rekomendacja", "Czerwone Flagi", "Źródła", "Metodologia"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH M6 entry must list covered dimension: {marker}")

    def test_08_arch_m6_stub_entry_states_risk_and_honesty(self):
        self.assertIn("ocena ryzyka M6 = Średnie", self.wdrozenie,
                      "ARCH M6 entry must state the M6 risk rating (Średnie)")
        self.assertIn("sfabrykowanego potwierdzenia", self.wdrozenie,
                      "ARCH M6 entry must note no fabricated confirmation of facts")

    def test_09_arch_pass1_complete_and_pass2_state_derived_from_plan(self):
        self.assertIn("Pass 1 (DRAFT/stub) zakończony", self.wdrozenie,
                      "ARCH must declare pass 1 (DRAFT/stub) complete")
        pending = [m for m in ORDER if not self.statuses.get((m, "real"), False)]
        if pending:
            self.assertIn("Pass 2 (REAL) w toku", self.wdrozenie,
                          "ARCH must state pass 2 (REAL) is in progress while reals are pending")
            self.assertIn("do wykonania", self.wdrozenie,
                          "ARCH remaining-work bullet must say 'do wykonania'")
            self.assertIn(" → ".join(pending), self.wdrozenie,
                          "ARCH remaining work must list the pending reals (derived from PLAN.md)")
        else:
            self.assertIn("Pass 2 (REAL) zakończon", self.wdrozenie,
                          "ARCH must declare pass 2 (REAL) complete once all reals are done")
            self.assertNotIn("Pass 2 (REAL) w toku", self.wdrozenie,
                             "ARCH must not claim pass 2 is in progress when all reals are done")

    def test_10_arch_earlier_entries_intact(self):
        for marker in ("11 testów zielonych", "tests.test_m1_stub",
                       "16 testów zielonych", "tests.test_m2_stub",
                       "15 testów zielonych", "tests.test_m3_stub",
                       "**M4 -- stub:**", "**M5 -- stub:**"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH must keep earlier M1/M2/M3/M4/M5 stub entry intact: {marker}")

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
