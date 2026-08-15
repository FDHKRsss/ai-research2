# -*- coding: utf-8 -*-
"""Validate the fix to docs/lessons/failures.md (the real-pass "no regression" note).

The corrected second bullet must accurately describe what actually happened:
- the *real* tests were written forward-compatible from the start, so there was NO
  regression when a later real milestone landed (the earlier claim that "testy real
  pękły hurtowo / 21 stale failures" was unsupported and must be gone),
- the "which reals are done" snapshot has a SINGLE owner — the latest completed
  real's test (e.g. tests/test_m4_real.py deliberately hardcodes DONE_REALS /
  PENDING_REALS),
- the first bullet (the genuine tests/test_m5_tracking.py tracking regression) is
  preserved.

The tests cross-check the text against the actual test source, so the lesson is
grounded in code rather than a re-fabricated claim.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FAILURES = REPO / "docs" / "lessons" / "failures.md"
TESTS_DIR = REPO / "tests"

M1_REAL = TESTS_DIR / "test_m1_real.py"
M2_REAL = TESTS_DIR / "test_m2_real.py"
M4_REAL = TESTS_DIR / "test_m4_real.py"

# A standalone (not "MUST_BE_DONE_REALS") hardcoded snapshot assignment.
SNAPSHOT_DONE_RE = re.compile(r"(?<!\w)DONE_REALS\s*=\s*\{")
SNAPSHOT_PENDING_RE = re.compile(r"(?<!\w)PENDING_REALS\s*=\s*\(")


def _load(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _bullets(text: str) -> list:
    """Return the list-item bodies of a lessons markdown file (lines starting '- ')."""
    return [
        line.strip()[2:]
        for line in text.splitlines()
        if line.strip().startswith("- ")
    ]


def _bullet_containing(text: str, needle: str) -> str:
    for bullet in _bullets(text):
        if needle in bullet:
            return bullet
    return ""


class TestFailuresLessonFix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load(FAILURES)
        cls.bullets = _bullets(cls.text)
        cls.m5_bullet = _bullet_containing(cls.text, "test_m5_tracking.py")
        cls.real_bullet = _bullet_containing(cls.text, "testy real")

    # -- the genuine first bullet must be preserved --------------------------

    def test_01_first_bullet_preserved(self):
        self.assertTrue(self.m5_bullet, "failures.md must keep the test_m5_tracking.py bullet")
        for marker in ("test_m5_tracking.py", "M6 -- stub", "forward-compatible",
                       "docs/PLAN.md"):
            self.assertIn(marker, self.m5_bullet,
                          f"first bullet must still record the tracking regression ({marker})")
        # It records a real regression that DID happen.
        self.assertIn("pękł", self.m5_bullet,
                      "first bullet must record that test_m5_tracking.py broke")

    # -- the corrected second bullet must tell the truth ---------------------

    def test_02_second_bullet_states_no_real_regression(self):
        self.assertTrue(self.real_bullet, "failures.md must keep the real-tests bullet")
        self.assertIn("regresji nie było", self.real_bullet,
                      "second bullet must state there was NO real-test regression")
        self.assertIn("forward-compatible", self.real_bullet,
                      "second bullet must say the real tests are forward-compatible")

    def test_03_second_bullet_names_single_snapshot_owner(self):
        for marker in ("test_m1_real.py", "test_m2_real.py", "test_m4_real.py",
                       "JEDNEGO właściciela", "celowo hardkoduje"):
            self.assertIn(marker, self.real_bullet,
                          f"second bullet must name the single-owner design ({marker})")

    def test_04_false_regression_claim_is_gone(self):
        for forbidden in ("pękły hurtowo", "21 stale failures", "testy real pękły"):
            self.assertNotIn(forbidden, self.text,
                             f"failures.md must not assert the unsupported claim: {forbidden}")
        # The false claim blamed the *earlier* real tests for hardcoding the snapshot
        # (plural "zahardkodowały"). The truth is the single-owner test does it on
        # purpose (singular "celowo hardkoduje").
        self.assertNotIn("zahardkodowały", self.real_bullet,
                         "second bullet must not blame the earlier real tests for hardcoding")

    # -- cross-check the lesson against the actual test source ----------------

    def test_05_early_real_tests_do_not_hardcode_the_snapshot(self):
        # The corrected bullet claims test_m1_real.py / test_m2_real.py derive the
        # done-reals set from PLAN.md instead of hardcoding it. Verify in code.
        for path in (M1_REAL, M2_REAL):
            src = _load(path)
            self.assertNotRegex(
                src, SNAPSHOT_DONE_RE,
                f"{path.name} must not hardcode DONE_REALS = {{...}}",
            )
            self.assertNotRegex(
                src, SNAPSHOT_PENDING_RE,
                f"{path.name} must not hardcode PENDING_REALS = (...)",
            )

    def test_06_single_owner_test_hardcodes_the_snapshot(self):
        # The corrected bullet's example: test_m4_real.py is the snapshot owner.
        src = _load(M4_REAL)
        self.assertRegex(src, SNAPSHOT_DONE_RE,
                         "test_m4_real.py must hardcode DONE_REALS = {...} (single owner)")
        self.assertRegex(src, SNAPSHOT_PENDING_RE,
                         "test_m4_real.py must hardcode PENDING_REALS = (...) (single owner)")

    def test_07_doc_has_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "failures.md must not contain TODO/TBD/lorem/placeholder markers",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
