# -*- coding: utf-8 -*-
"""Tests for the M5 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the M5 -- Stabilność finansowa section against the
requirement contract in docs/PLAN.md / docs/ARCHITECTURE.md (research deliverable,
no application code exists in this project).

M5 contract (PLAN.md / OBJECTIVE): sprawozdania finansowe (KRS/MSiG), kapitał
zakładowy, wiek firmy, historia zmian, powiązania osobowe/kapitałowe. W pass 1
(stub) wszystko musi być oznaczone "(do weryfikacji)" / "(brak danych publicznych)"
/ "(założenie)" -- zero fabrykacji wielkości finansowych (przychody/koszty/
zysk/strata/aktywa/zobowiązania).
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

M5_HEADING = "Sekcja M5 — Stabilność finansowa"

ALLOWED_RISK = ("Niskie", "Średnie", "Wysokie")


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


class TestM5StubDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()
        cls.m5 = _section(cls.text, M5_HEADING)

    # -- structure -----------------------------------------------------------

    def test_01_m5_section_present(self):
        self.assertIn(f"## {M5_HEADING}", self.text, "missing M5 top-level section")

    def test_02_m5_summary_row_present_with_3_columns(self):
        rows = _summary_rows(self.text)
        m5 = [r for r in rows if r and "M5" in r[0]]
        self.assertTrue(m5, "summary table must contain an M5 row")
        self.assertEqual(len(m5[0]), 3, f"M5 summary row must have 3 columns, got {len(m5[0])}")

    # -- coverage of required sub-areas ---------------------------------------

    def test_03_m5_covers_financial_statements_krs_msig(self):
        for marker in ("Sprawozdania finansowe", "KRS", "MSiG", "ekrs.ms.gov.pl",
                       "Repozytorium Dokumentów Finansowych", "imsig.pl"):
            self.assertIn(marker, self.m5, f"M5 missing financial-statements marker: {marker}")

    def test_04_m5_covers_share_capital(self):
        for marker in ("Kapitał zakładowy", "5 000 zł", "ustawowe minimum", "art. 154"):
            self.assertIn(marker, self.m5, f"M5 missing share-capital marker: {marker}")

    def test_05_m5_covers_company_age(self):
        for marker in ("Wiek firmy", "2024-09-11"):
            self.assertIn(marker, self.m5, f"M5 missing company-age marker: {marker}")
        self.assertIn("krócej niż", self.m5, "M5 must reason about the (young) company age")

    def test_06_m5_covers_change_history(self):
        for marker in ("Historia zmian", "Zmiany w zarządzie", "Zmiany wspólników",
                       "Zmiany siedziby", "Zmiany przedmiotu działalności"):
            self.assertIn(marker, self.m5, f"M5 missing change-history marker: {marker}")

    def test_07_m5_covers_personal_and_capital_links(self):
        for marker in ("Powiązania osobowe i kapitałowe", "Katarzyna Pydynowska"):
            self.assertIn(marker, self.m5, f"M5 missing personal/capital-links marker: {marker}")

    def test_08_m5_disambiguates_by_nip_krs_address(self):
        for marker in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(marker, self.m5, f"M5 missing disambiguation identifier: {marker}")
        self.assertIn("Stefana Batorego 18", self.m5, "M5 must anchor the address street")
        self.assertIn("02-591 Warszawa", self.m5, "M5 must anchor the address city/zip")

    def test_09_m5_cross_references_share_capital_discrepancy_to_m1(self):
        # The 91 udzialy = 4550 zl vs 5000 zl kapital issue belongs to M1 but must be
        # re-flagged here (single source of truth).
        for marker in ("91 udziałów", "4 550 zł"):
            self.assertIn(marker, self.m5, f"M5 missing share-count value: {marker}")
        self.assertIn("powiązane z M1", self.m5,
                      "M5 must cross-reference the share/capital discrepancy back to M1")

    # -- honesty / no fabrication in the DRAFT --------------------------------

    def test_10_m5_draft_disclaimer_sources_not_opened(self):
        self.assertTrue(
            any(m in self.m5 for m in ("nie otwierano", "nie otwarto")),
            "M5 DRAFT must state that KRS/MSiG and financial statements have not been opened",
        )

    def test_11_m5_flags_everything_for_verification(self):
        self.assertGreaterEqual(self.m5.count("(do weryfikacji"), 3,
                                "M5 must flag multiple findings as '(do weryfikacji)'")
        self.assertIn("do ustalenia", self.m5,
                      "M5 must mark unknown fields as 'do ustalenia'")
        self.assertIn("nieznane na etapie DRAFT", self.m5,
                      "M5 must mark unknown financials as 'nieznane na etapie DRAFT'")

    def test_12_m5_no_fabricated_financial_figures(self):
        self.assertIn("fabrykuję", self.m5,
                      "M5 must state it does not fabricate financial figures")
        # No invented revenue/cost/profit/asset/liability amounts in the DRAFT.
        for pattern in (r"przychod[yw]\b.*\d", r"zysk.*\d", r"strat[ay]\b.*\d",
                        r"aktywa.*\d", r"zobowiązani[ae].*\d"):
            self.assertIsNone(
                re.search(pattern, self.m5, re.IGNORECASE),
                f"M5 must not fabricate a financial figure matching: {pattern}",
            )

    # -- risk consistency ------------------------------------------------------

    def test_13_m5_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m5, "M5 section must state Ocena: Średnie")
        m5 = [r for r in _summary_rows(self.text) if r and "M5" in r[0]]
        self.assertTrue(m5, "summary table must contain an M5 row")
        risk_cell = m5[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M5 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M5 risk cell must match M5 section (Średnie)")

    def test_14_m5_summary_row_is_honest_unverified(self):
        m5 = [r for r in _summary_rows(self.text) if r and "M5" in r[0]]
        findings = m5[0][1]
        self.assertIn("do ustalenia i weryfikacji", findings,
                      "M5 summary findings must flag financial stability as not yet established")
        self.assertIn("Nieznane na etapie DRAFT", findings,
                      "M5 summary findings must say the details are unknown in the DRAFT")
        self.assertIn("sfabrykowanych", findings,
                      "M5 summary findings must note that no financial figures are fabricated")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_15_m5_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M5", sec, "Czerwone Flagi section must address M5")
        self.assertIn("nie stwierdzono", sec,
                      "M5 red-flags entry must be honest (no negative findings)")
        self.assertTrue(
            any(m in sec for m in ("nie zostały jeszcze otwarte", "nie zostały jeszcze sprawdzone")),
            "M5 red-flags entry must note the financial sources have not been opened yet",
        )

    def test_16_m5_sources_planned_no_fabricated_dates(self):
        sec = _section(self.text, "Źródła")
        for marker in ("M5 — Stabilność finansowa", "ekrs.ms.gov.pl", "imsig.pl",
                       "Rejestr REGON", "Repozytorium Dokumentów Finansowych"):
            self.assertIn(marker, sec, f"Źródła section missing planned M5 source: {marker}")
        self.assertIn("nie podaję dat dostępu", sec,
                      "DRAFT sources must explicitly say no access dates yet")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", sec),
            "DRAFT sources section must not contain a fabricated access date",
        )

    def test_17_m5_methodology_limitation_present(self):
        sec = _section(self.text, "Metodologia i ograniczenia")
        self.assertIn("stabilność finansowa", sec,
                      "Metodologia section must describe the M5 (financial stability) limitation")

    def test_18_document_status_note_mentions_m5(self):
        self.assertIn("M5 — Stabilność finansowa", self.text,
                      "document status note should record M5 as complete")

    def test_19_m5_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo").
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
