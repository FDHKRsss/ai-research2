# -*- coding: utf-8 -*-
"""Tests for the M6 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the M6 -- Synteza ryzyka section against the requirement
contract in docs/PLAN.md / docs/ARCHITECTURE.md (research deliverable, no
application code exists in this project).

M6 contract (PLAN.md / OBJECTIVE): tabela podsumowująca `Sekcja | Znaleziska |
Ocena ryzyka`, sekcja „Czerwone Flagi" (jeśli są niepokojące sygnały), rekomendacja,
pełna lista źródeł z datami dostępu, metodologia i ograniczenia. W pass 1 (stub)
wszystko musi być oznaczone "(do weryfikacji)" / "(założenie)" / "(brak danych
publicznych)" -- zero fabrykacji potwierdzonego stanu faktycznego; rekomendacja
i końcowa ocena ryzyka mają charakter warunkowy.
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


class TestM6StubDeliverable(unittest.TestCase):
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

    def test_04_m6_explains_uniform_unverified_rating(self):
        self.assertIn("niezweryfikowane", self.m6,
                      "M6 must explain that the uniform rating is due to unverified data")
        self.assertIn("nie otwarto źródeł", self.m6,
                      "M6 must tie the rating to sources not yet being opened")

    def test_05_m6_final_risk_rating_present(self):
        self.assertIn("Końcowa ocena ryzyka: Średnie", self.m6,
                      "M6 must state the final risk rating (Średnie)")

    def test_06_m6_recommendation_is_conditional(self):
        self.assertIn("Rekomendacja", self.m6, "M6 must contain a recommendation subsection")
        self.assertIn("warunkow", self.m6,
                      "M6 recommendation must be conditional on the DRAFT stage")

    def test_07_m6_links_red_flags_and_summary(self):
        for marker in ("Czerwone Flagi", "Podsumowanie tabelaryczne"):
            self.assertIn(marker, self.m6,
                          f"M6 must cross-reference the '{marker}' section")

    def test_08_m6_states_direction_of_change_in_pass2(self):
        for marker in ("pass 2", "Niskiej", "Wysokiej"):
            self.assertIn(marker, self.m6,
                          f"M6 must state the possible direction of change in pass 2 ({marker})")

    # -- honesty / no fabricated confirmation in the DRAFT --------------------

    def test_09_m6_draft_disclaimer_sources_not_opened(self):
        self.assertTrue(
            any(m in self.m6 for m in ("nie zostały jeszcze otwarte", "nie otwarto")),
            "M6 DRAFT must state that no official/opinion sources have been opened yet",
        )

    def test_10_m6_flags_findings_for_verification(self):
        self.assertGreaterEqual(self.m6.count("(do weryfikacji"), 3,
                                "M6 must flag multiple findings as '(do weryfikacji)'")
        self.assertIn("sfabrykowanych", self.m6,
                      "M6 must note it does not fabricate ratings/confirmations")

    def test_11_m6_no_fabricated_positive_confirmation(self):
        # The DRAFT must not claim a confirmed clean/positive status.
        for pattern in (r"potwierdzon[eyao].*czynny", r"czysty.*status.*potwierdzon",
                        r"bez negatywnych wpisów\."):
            self.assertIsNone(
                re.search(pattern, self.m6, re.IGNORECASE),
                f"M6 must not fabricate a confirmed status matching: {pattern}",
            )

    # -- risk consistency ------------------------------------------------------

    def test_12_m6_risk_rating_consistent_summary_vs_section(self):
        m6 = [r for r in _summary_rows(self.text) if r and "M6" in r[0]]
        self.assertTrue(m6, "summary table must contain an M6 row")
        risk_cell = m6[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M6 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell,
                      "summary M6 risk cell must match M6 section (Średnie)")

    def test_13_m6_summary_row_is_honest_unverified(self):
        m6 = [r for r in _summary_rows(self.text) if r and "M6" in r[0]]
        findings = m6[0][1]
        self.assertIn("rekomendacja warunkowa", findings,
                      "M6 summary findings must state the recommendation is conditional")
        self.assertIn("pass 2", findings,
                      "M6 summary findings must defer the decision to pass 2 (real)")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_14_m6_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M6 — synteza", sec, "Czerwone Flagi section must address M6 synthesis")
        self.assertIn("końcowa ocena ryzyka", sec,
                      "M6 red-flags entry must state the final risk rating")
        self.assertIn("Średnie", sec, "M6 red-flags entry must state the Średnie rating")
        self.assertIn("potwierdzonej", sec,
                      "M6 red-flags entry must honestly say no confirmed red flag exists")

    def test_15_m6_sources_block_present_no_fabricated_dates(self):
        sec = _section(self.text, "Źródła")
        self.assertIn("M6 — Synteza ryzyka", sec, "Źródła section missing the M6 block")
        self.assertIn("scalona lista źródeł", sec,
                      "M6 sources block must promise a merged source list in pass 2")
        # M6 is still DRAFT: its source block must not carry a fabricated access date.
        block = _sources_block(self.text, "M6")
        self.assertTrue(block, "Źródła must contain an M6 source block")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", block),
            "M6 (DRAFT) source block must not contain a fabricated access date",
        )

    def test_16_m6_methodology_limitation_present(self):
        sec = _section(self.text, "Metodologia i ograniczenia")
        self.assertIn("synteza ryzyka", sec,
                      "Metodologia section must describe the M6 synthesis limitation")
        self.assertIn("warunkowe", sec,
                      "Metodologia must state the final rating/recommendation are conditional")
        self.assertIn("nie stanowi rekomendacji do zawarcia umowy", sec,
                      "Metodologia must say the document is not a standalone basis to contract")

    def test_17_document_status_note_mentions_m6(self):
        # In pass 2 the status note groups the still-pending sections (currently M3–M6)
        # and must keep recording M6 as pending until M6 -- real lands.
        header = self.text.split("---")[0]
        self.assertIn("M6", header,
                      "document status note should record M6 as still pending real")
        self.assertIn("DRAFT/stub", header,
                      "document status note must mark M6 (and siblings) as DRAFT/stub")

    def test_18_m6_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo").
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
