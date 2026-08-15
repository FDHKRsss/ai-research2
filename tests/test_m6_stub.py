# -*- coding: utf-8 -*-
"""Tests for the M6 deliverable section: raport/KR-OFFICE-OSINT.md.

NOTE: M6 has progressed from stub to REAL in pass 2. The section's contract
(synthesis of the M1–M5 partial ratings, final risk rating, recommendation,
"Czerwone Flagi" cross-reference, merged source list with access dates,
methodology/limitations) is still validated here, together with the pass-2
grounding. This mirrors tests/test_m5_stub.py, which keeps validating the M5
contract after M5 -- real landed. The detailed REAL grounding is validated in
tests/test_m6_real.py.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

M6_HEADING = "Sekcja M6 — Synteza ryzyka"

ALLOWED_RISK = ("Niskie", "Średnie", "Wysokie")

# Each partial area must appear in the synthesis table with its Średnie rating.
SYNTHESIS_ROWS = (
    "Identyfikacja i metryka | Średnie",
    "Status prawny i podatkowy | Średnie",
    "Reputacja | Średnie",
    "Jakość usług i specjalizacja | Średnie",
    "Stabilność finansowa | Średnie",
)


def _load() -> str:
    if not DELIVERABLE.exists():
        return ""
    return DELIVERABLE.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    """Return the text of a single '## <heading>' section (up to the next '## ')."""
    marker = f"## {heading}"
    idx = text.find(marker)
    if idx == -1:
        return ""
    rest = text[idx + len(marker):]
    nxt = rest.find("\n## ")
    if nxt == -1:
        return rest
    return rest[:nxt]


def _sources_block(text: str, milestone: str) -> str:
    """Return the '**M# — ...' source block from the Źródła section."""
    sec = _section(text, "Źródła")
    start = sec.find(f"**{milestone} —")
    if start == -1:
        return ""
    header_end = start + len(f"**{milestone} —")
    nxt = None
    for m in ("M1", "M2", "M3", "M4", "M5", "M6"):
        idx = sec.find(f"**{m} —", header_end)
        if idx != -1 and (nxt is None or idx < nxt):
            nxt = idx
    return sec[start:nxt] if nxt is not None else sec[start:]


def _summary_rows(text: str):
    """Parse the '## Podsumowanie tabelaryczne' markdown table into rows of cells."""
    sec = _section(text, "Podsumowanie tabelaryczne")
    rows = []
    for line in sec.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if set("".join(cells)) <= {"-", ":"}:
                continue
            rows.append(cells)
    return rows


class TestM6Deliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()
        cls.m6 = _section(cls.text, M6_HEADING)

    # -- structure -----------------------------------------------------------

    def test_01_m6_section_present(self):
        self.assertIn(f"## {M6_HEADING}", self.text, "missing M6 top-level section")

    def test_02_m6_summary_row_present_with_3_columns(self):
        rows = _summary_rows(self.text)
        m6 = [r for r in rows if r and "M6" in r[0]]
        self.assertTrue(m6, "summary table must contain an M6 row")
        self.assertEqual(len(m6[0]), 3, f"M6 summary row must have 3 columns, got {len(m6[0])}")

    # -- coverage: synthesis, recommendation, red flags -----------------------

    def test_03_m6_synthesizes_all_partial_ratings(self):
        for marker in ("Obszar", "Ocena cząstkowa", "Kluczowe zastrzeżenie"):
            self.assertIn(marker, self.m6, f"M6 synthesis table missing column: {marker}")
        for row_marker in SYNTHESIS_ROWS:
            self.assertIn(row_marker, self.m6,
                          f"M6 synthesis table must rate area as Średnie: {row_marker}")

    def test_04_m6_final_risk_rating_present(self):
        self.assertIn("Końcowa ocena ryzyka: Średnie", self.m6,
                      "M6 must state the final risk rating (Średnie)")

    def test_05_m6_recommendation_present_and_final(self):
        self.assertIn("Rekomendacja", self.m6, "M6 must contain a recommendation subsection")
        self.assertNotIn("warunkow", self.m6,
                         "M6 recommendation must be final (not conditional on a later pass)")

    def test_06_m6_carries_forward_observation_signals(self):
        for marker in ("91 udziałów", "4 550 zł", "450 zł",
                       "Art. 96 ust. 9h", "2025-06-27"):
            self.assertIn(marker, self.m6, f"M6 missing carried-forward signal: {marker}")

    def test_07_m6_links_red_flags_and_summary(self):
        for marker in ("Czerwone Flagi", "Podsumowanie tabelaryczne"):
            self.assertIn(marker, self.m6,
                          f"M6 must cross-reference the '{marker}' section")

    # -- pass 2 (REAL): grounded synthesis -----------------------------------

    def test_08_m6_grounded_in_pass2(self):
        for marker in ("REAL", "pass 2", "2026-08-15"):
            self.assertIn(marker, self.m6, f"M6 REAL missing grounding marker: {marker}")
        self.assertIn("M1", self.m6, "M6 REAL must reference the M1 findings")
        self.assertIn("M5", self.m6, "M6 REAL must reference the M5 findings")

    # -- risk consistency ------------------------------------------------------

    def test_09_m6_risk_rating_consistent_summary_vs_section(self):
        m6 = [r for r in _summary_rows(self.text) if r and "M6" in r[0]]
        self.assertTrue(m6, "summary table must contain an M6 row")
        risk_cell = m6[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M6 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M6 risk cell must match M6 section (Średnie)")

    def test_10_m6_summary_row_grounded(self):
        m6 = [r for r in _summary_rows(self.text) if r and "M6" in r[0]]
        findings = m6[0][1]
        self.assertNotIn("warunkow", findings,
                         "M6 summary findings must not describe the recommendation as conditional")
        self.assertNotIn("dokończenia pass 2", findings,
                         "M6 summary findings must not defer the decision to pass 2")
        self.assertIn("Średnie", findings, "M6 summary findings must record the Średnie rating")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_11_m6_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M6", sec, "Czerwone Flagi section must address M6")
        self.assertIn("Średnie", sec, "M6 red-flags entry must state the Średnie rating")
        self.assertIn("potwierdzonych", sec,
                      "M6 red-flags entry must honestly say no confirmed red flag exists")
        self.assertIn("dwa sygnały do obserwacji", sec,
                      "M6 red-flags entry must carry the two observation signals")

    def test_12_m6_sources_grounded_with_access_dates(self):
        sec = _section(self.text, "Źródła")
        self.assertIn("M6 — Synteza ryzyka", sec, "Źródła section missing the M6 block")
        block = _sources_block(self.text, "M6")
        self.assertTrue(block, "Źródła must contain an M6 source block")
        self.assertIn("2026-08-15", block,
                      "M6 (REAL) source block must carry the access date 2026-08-15")
        self.assertIn("M1", block, "M6 source block must reference the grounded M1 sources")
        self.assertIn("M5", block, "M6 source block must reference the grounded M5 sources")

    def test_13_m6_methodology_limitation_present(self):
        sec = _section(self.text, "Metodologia i ograniczenia")
        self.assertIn("synteza ryzyka", sec,
                      "Metodologia section must describe the M6 synthesis limitation")
        self.assertIn("rekomendacji do zawarcia umowy", sec,
                      "Metodologia must say the document is not a standalone basis to contract")
        self.assertNotIn("warunkowe", sec,
                         "Metodologia must not leave the M6 rating 'warunkowe' (DRAFT)")

    def test_14_document_status_note_mentions_m6(self):
        header = self.text.split("---")[0]
        self.assertIn("M6 — Synteza ryzyka", header,
                      "document status note should record M6 as complete")
        self.assertIn("pass 2", header, "document status note should record pass 2 (REAL)")
        self.assertNotIn("DRAFT/stub", header,
                         "document status note must not mark M6 as DRAFT/stub")

    def test_15_m6_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo").
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
