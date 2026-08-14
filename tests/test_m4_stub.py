# -*- coding: utf-8 -*-
"""Tests for the M4 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the M4 -- Jakość usług i specjalizacja section against the
requirement contract in docs/PLAN.md / docs/ARCHITECTURE.md (research deliverable,
no application code exists in this project).

M4 contract (PLAN.md): oferta, specjalizacja (IT / transport / inne), PKD,
ubezpieczenie OC biura, certyfikaty, doświadczenie kadry, kanały kontaktu.
W pass 1 (stub) wszystko musi być oznaczone "(do weryfikacji)" / "(brak danych
publicznych)" / "(założenie)" -- zero fabrykacji oferty/specjalizacji/OC.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

M4_HEADING = "Sekcja M4 — Jakość usług i specjalizacja"

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


class TestM4StubDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()
        cls.m4 = _section(cls.text, M4_HEADING)

    # -- structure -----------------------------------------------------------

    def test_01_m4_section_present(self):
        self.assertIn(f"## {M4_HEADING}", self.text, "missing M4 top-level section")

    def test_02_m4_summary_row_present_with_3_columns(self):
        rows = _summary_rows(self.text)
        m4 = [r for r in rows if r and "M4" in r[0]]
        self.assertTrue(m4, "summary table must contain an M4 row")
        self.assertEqual(len(m4[0]), 3, f"M4 summary row must have 3 columns, got {len(m4[0])}")

    # -- coverage of required sub-areas ---------------------------------------

    def test_03_m4_covers_offer_and_scope(self):
        for marker in ("Oferta i zakres usług", "księgowość", "kadry", "69.20.Z"):
            self.assertIn(marker, self.m4, f"M4 missing offer/scope marker: {marker}")
        # PKD must be cross-referenced back to M1 (single source of truth).
        self.assertIn("powiązane z M1", self.m4,
                      "M4 must cross-reference PKD back to M1")

    def test_04_m4_covers_specialization_it_transport_inne(self):
        for marker in ("Specjalizacja", "IT", "transport", "inne"):
            self.assertIn(marker, self.m4, f"M4 missing specialization marker: {marker}")

    def test_05_m4_covers_oc_insurance_and_honesty(self):
        # OC is required by the goal; the stub must record "no info found" honestly.
        for marker in ("ubezpieczenie OC", "nie znaleziono informacji o OC",
                       "nie wymyślam zakresu ani limitu"):
            self.assertIn(marker, self.m4, f"M4 missing OC marker: {marker}")

    def test_06_m4_covers_certificates_experience_contact(self):
        for marker in ("Certyfikaty i uprawnienia", "Doświadczenie kadry", "Kanały kontaktu"):
            self.assertIn(marker, self.m4, f"M4 missing service-quality marker: {marker}")

    def test_07_m4_disambiguates_by_nip_krs_address(self):
        for marker in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(marker, self.m4, f"M4 missing disambiguation identifier: {marker}")
        self.assertIn("Stefana Batorego 18", self.m4, "M4 must anchor the address street")
        self.assertIn("02-591 Warszawa", self.m4, "M4 must anchor the address city/zip")

    # -- honesty / no fabrication in the DRAFT --------------------------------

    def test_08_m4_draft_disclaimer_sources_not_opened(self):
        self.assertTrue(
            any(m in self.m4 for m in ("nie otwierano", "nie otwarto")),
            "M4 DRAFT must state that the WWW/offer/certificate sources have not been opened",
        )

    def test_09_m4_flags_everything_for_verification(self):
        self.assertGreaterEqual(self.m4.count("(do weryfikacji"), 3,
                                "M4 must flag multiple findings as '(do weryfikacji)'")
        self.assertIn("do ustalenia", self.m4,
                      "M4 must mark unknown fields as 'do ustalenia'")

    def test_10_m4_no_fabricated_offer_specialization_or_oc(self):
        # Specialization must stay unknown; OC scope/limit must not be invented.
        self.assertIn("specjalizacja **nieznana**", self.m4,
                      "M4 must state specialization is unknown in the DRAFT")
        self.assertIn("fabrykuję", self.m4,
                      "M4 must state it does not fabricate offer/specialization/OC")
        # The section must explicitly decline to assert a positive specialization.
        self.assertIn("formułuję twierdzenia", self.m4,
                      "M4 must decline to claim a positive specialization")
        # No invented OC coverage amount / limit in the M4 section.
        self.assertNotIn("suma gwarancyjna w wysokości", self.m4)

    # -- risk consistency ------------------------------------------------------

    def test_11_m4_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m4, "M4 section must state Ocena: Średnie")
        m4 = [r for r in _summary_rows(self.text) if r and "M4" in r[0]]
        self.assertTrue(m4, "summary table must contain an M4 row")
        risk_cell = m4[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M4 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M4 risk cell must match M4 section (Średnie)")

    def test_12_m4_summary_row_is_honest_unverified(self):
        m4 = [r for r in _summary_rows(self.text) if r and "M4" in r[0]]
        findings = m4[0][1]
        self.assertIn("OC", findings, "M4 summary findings must mention OC")
        self.assertIn("do ustalenia", findings,
                      "M4 summary findings must flag service quality as not yet established")
        self.assertIn("Nieznane na etapie DRAFT", findings,
                      "M4 summary findings must say the details are unknown in the DRAFT")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_13_m4_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M4", sec, "Czerwone Flagi section must address M4")
        self.assertIn("nie stwierdzono", sec,
                      "M4 red-flags entry must be honest (no negative findings)")
        self.assertTrue(
            any(m in sec for m in ("nie zostały jeszcze otwarte", "nie zostały jeszcze sprawdzone")),
            "M4 red-flags entry must note the quality sources have not been opened yet",
        )

    def test_14_m4_sources_planned_no_fabricated_dates(self):
        sec = _section(self.text, "Źródła")
        for marker in ("M4 — Jakość usług i specjalizacja", "Strona WWW",
                       "Rejestry branżowe", "OC"):
            self.assertIn(marker, sec, f"Źródła section missing planned M4 source: {marker}")
        self.assertIn("nie podaję dat dostępu", sec,
                      "DRAFT sources must explicitly say no access dates yet")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", sec),
            "DRAFT sources section must not contain a fabricated access date",
        )

    def test_15_document_status_note_mentions_m4(self):
        self.assertIn("M4 — Jakość usług i specjalizacja", self.text,
                      "document status note should record M4 as complete")

    def test_16_m4_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo").
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
