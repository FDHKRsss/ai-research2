# -*- coding: utf-8 -*-
"""Tests for the M2 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the M2 -- Status prawny i podatkowy section against the
requirement contract in docs/PLAN.md / docs/ARCHITECTURE.md (research deliverable,
no application code exists in this project).

M2 contract (PLAN.md): Biała Lista VAT (czynny podatnik VAT), VIES, status w KRS,
publiczne rejestry dłużników (KRZ, MSiG) oraz komercyjne BIG (KRD/ERIF/InfoMonitor)
z jawnym opisem ograniczeń dostępu. W pass 1 (stub) wszystko musi być oznaczone
"(do weryfikacji)" / "(brak danych publicznych)" / "(założenie)" -- zero fabrykacji.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

M2_HEADING = "Sekcja M2 — Status prawny i podatkowy"

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


class TestM2StubDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()
        cls.m2 = _section(cls.text, M2_HEADING)

    # -- structure -----------------------------------------------------------

    def test_01_m2_section_present(self):
        self.assertIn(f"## {M2_HEADING}", self.text, "missing M2 top-level section")

    def test_02_m2_summary_row_present_with_3_columns(self):
        rows = _summary_rows(self.text)
        m2 = [r for r in rows if r and "M2" in r[0]]
        self.assertTrue(m2, "summary table must contain an M2 row")
        self.assertEqual(len(m2[0]), 3, f"M2 summary row must have 3 columns, got {len(m2[0])}")

    # -- coverage of required sub-areas ---------------------------------------

    def test_03_m2_covers_biala_lista_vat(self):
        for marker in ("Biała Lista", "podatnik", "VAT", "wl-api.mf.gov.pl", "7011222044"):
            self.assertIn(marker, self.m2, f"M2 missing Biała Lista marker: {marker}")

    def test_04_m2_covers_vies_vat_ue(self):
        for marker in ("VIES", "PL7011222044", "ec.europa.eu", "VAT-UE"):
            self.assertIn(marker, self.m2, f"M2 missing VIES marker: {marker}")

    def test_05_m2_covers_krs_status(self):
        for marker in ("KRS", "0001126380", "ekrs.ms.gov.pl", "aktywny"):
            self.assertIn(marker, self.m2, f"M2 missing KRS marker: {marker}")
        # must check for insolvency/restructuring/liquidation markers
        self.assertTrue(
            any(m in self.m2 for m in ("upadłości", "upadłość", "restrukturyzacji", "restrukturyzacyjne", "likwidacji", "likwidacja")),
            "M2 must address insolvency/restructuring/liquidation in KRS",
        )

    def test_06_m2_covers_public_debt_registers(self):
        for marker in (
            "Krajowy Rejestr Zadłużonych",
            "KRZ",
            "krz.ms.gov.pl",
            "Monitor Sądowy i Gospodarczy",
            "MSiG",
            "imsig.pl",
        ):
            self.assertIn(marker, self.m2, f"M2 missing public debt register marker: {marker}")

    def test_07_m2_commercial_big_explicit_limitation(self):
        for big in ("KRD", "ERIF", "InfoMonitor"):
            self.assertIn(big, self.m2, f"M2 missing commercial BIG marker: {big}")
        # limitation must be explicit (no login/fee = cannot guess contents)
        self.assertIn("(brak danych publicznych)", self.m2,
                      "M2 must explicitly flag commercial BIG as 'brak danych publicznych'")
        self.assertTrue(
            any(m in self.m2 for m in ("brak dostępu", "bez dostępu", "logowani", "logowania", "opłat", "ograniczenie")),
            "M2 must describe the access limitation to commercial BIG",
        )

    # -- honesty / no fabrication in the DRAFT --------------------------------

    def test_08_m2_draft_disclaimer_sources_not_opened(self):
        # The DRAFT must explicitly say official sources have not been opened yet.
        self.assertTrue(
            any(m in self.m2 for m in (
                "nie otwierano",
                "nie otwarto",
                "nie zostały jeszcze sprawdzone",
                "nie były jeszcze sprawdzane",
            )),
            "M2 DRAFT must state that official sources have not been opened yet",
        )

    def test_09_m2_flags_everything_for_verification(self):
        self.assertGreaterEqual(self.m2.count("(do weryfikacji"), 3,
                                "M2 must flag multiple findings as '(do weryfikacji)'")
        self.assertIn("do potwierdzenia", self.m2,
                      "M2 must mark status fields as 'do potwierdzenia'")

    def test_10_m2_no_fabricated_confirmed_status(self):
        # A confirmed positive status ("Podmiot aktywny") belongs to the REAL pass,
        # never to the stub. Any 'aktywny' in the stub must stay qualified.
        self.assertNotIn("Podmiot aktywny", self.text,
                         "M2 stub must not fabricate a confirmed 'Podmiot aktywny' status")
        self.assertNotIn("czynny podatnik VAT — tak", self.m2)
        self.assertNotIn("jest czynnym podatnikiem VAT", self.m2)

    # -- risk consistency ------------------------------------------------------

    def test_11_m2_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m2, "M2 section must state Ocena: Średnie")
        m2 = [r for r in _summary_rows(self.text) if r and "M2" in r[0]]
        self.assertTrue(m2, "summary table must contain an M2 row")
        risk_cell = m2[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M2 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M2 risk cell must match M2 section (Średnie)")

    def test_12_m2_summary_row_is_honest_unverified(self):
        m2 = [r for r in _summary_rows(self.text) if r and "M2" in r[0]]
        findings = m2[0][1]
        self.assertIn("do weryfikacji", findings,
                      "M2 summary findings must be flagged as 'do weryfikacji'")
        self.assertTrue(
            any(m in findings for m in ("bez dostępu", "brak dostępu", "ograniczenie")),
            "M2 summary findings must note the commercial BIG access limitation",
        )

    # -- cross-cutting hygiene -------------------------------------------------

    def test_13_m2_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )

    def test_14_sources_planned_for_m2_no_fabricated_dates(self):
        sec = _section(self.text, "Źródła")
        for marker in ("Biała Lista", "VIES", "Krajowy Rejestr Zadłużonych", "Monitor Sądowy i Gospodarczy", "KRD", "ERIF", "InfoMonitor"):
            self.assertIn(marker, sec, f"Źródła section missing planned M2 source: {marker}")
        self.assertIn("nie podaję dat dostępu", sec,
                      "DRAFT sources must explicitly say no access dates yet")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", sec),
            "DRAFT sources section must not contain a fabricated access date",
        )

    def test_15_document_status_note_mentions_m2(self):
        # The crash-safe status note at the top should list M2 as now complete.
        self.assertIn("M2 — Status prawny i podatkowy", self.text,
                      "document status note should record M2 as complete")

    def test_16_red_flags_m2_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M2", sec, "Czerwone Flagi section must address M2")
        self.assertTrue(
            any(m in sec for m in ("nie stwierdzono", "nie zostały jeszcze sprawdzone")),
            "M2 red-flags entry must be honest (no negative findings, sources not yet checked)",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
