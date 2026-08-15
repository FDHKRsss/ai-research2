# -*- coding: utf-8 -*-
"""Tests for the M2 deliverable section: raport/KR-OFFICE-OSINT.md.

NOTE: M2 has progressed from stub to REAL in pass 2. The section's contract
(coverage of Biała Lista / VIES / KRS / KRZ / MSiG / commercial BIG, risk
consistency, no placeholders, honest red-flags) is still validated here; the
pass-2 grounding (confirmed status + primary-source URLs + access dates) is
validated in detail in tests/test_m2_real.py.
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


class TestM2Deliverable(unittest.TestCase):
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
        self.assertTrue(
            any(m in self.m2 for m in ("upadłości", "upadłość", "restrukturyzacji",
                                       "restrukturyzacyjne", "likwidacji", "likwidacja")),
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
        self.assertIn("(brak danych publicznych)", self.m2,
                      "M2 must explicitly flag commercial BIG as 'brak danych publicznych'")
        self.assertTrue(
            any(m in self.m2 for m in ("brak dostępu", "bez dostępu", "logowani",
                                       "logowania", "opłat", "ograniczenie")),
            "M2 must describe the access limitation to commercial BIG",
        )

    # -- pass 2 (REAL): grounded, confirmed status ----------------------------

    def test_08_m2_status_confirmed_in_primary_sources(self):
        for marker in ("potwierdzone", "Czynny", "wl-api.mf.gov.pl",
                       "ec.europa.eu/taxation_customs/vies", "ekrs.ms.gov.pl",
                       "imsig.pl", "2026-08-15"):
            self.assertIn(marker, self.m2,
                          f"M2 REAL missing confirmed status / source / date: {marker}")

    # -- risk consistency ------------------------------------------------------

    def test_09_m2_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m2, "M2 section must state Ocena: Średnie")
        m2 = [r for r in _summary_rows(self.text) if r and "M2" in r[0]]
        self.assertTrue(m2, "summary table must contain an M2 row")
        risk_cell = m2[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M2 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M2 risk cell must match M2 section (Średnie)")

    def test_10_m2_summary_row_reflects_confirmed_status_and_limitations(self):
        m2 = [r for r in _summary_rows(self.text) if r and "M2" in r[0]]
        findings = m2[0][1]
        for marker in ("Czynny", "aktywny"):
            self.assertIn(marker, findings,
                          f"M2 summary findings must record the confirmed status: {marker}")
        self.assertTrue(
            any(m in findings for m in ("ograniczenie", "brak dostępu", "bez dostępu")),
            "M2 summary findings must note the KRZ/BIG access limitation",
        )

    # -- cross-cutting hygiene -------------------------------------------------

    def test_11_m2_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )

    def test_12_m2_sources_grounded_with_access_dates(self):
        sec = _section(self.text, "Źródła")
        for marker in ("Biała Lista", "VIES", "Krajowy Rejestr Zadłużonych",
                       "Monitor Sądowy i Gospodarczy", "KRD", "ERIF", "InfoMonitor"):
            self.assertIn(marker, sec, f"Źródła section missing M2 source: {marker}")
        block = _sources_block(self.text, "M2")
        self.assertTrue(block, "Źródła must contain an M2 source block")
        self.assertIn("2026-08-15", block,
                      "M2 (REAL) source block must carry the access date 2026-08-15")
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M2 REAL must carry access dates")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15",
                                 f"access date must not be post-dated: {d}")

    def test_13_document_status_note_mentions_m2(self):
        self.assertIn("M2 — Status prawny i podatkowy", self.text,
                      "document status note should record M2 as complete")

    def test_14_red_flags_m2_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M2", sec, "Czerwone Flagi section must address M2")
        self.assertIn("status potwierdzony", sec,
                      "M2 red-flags entry must record the confirmed status")
        self.assertIn("przywrócenie", sec,
                      "M2 red-flags entry must surface the VAT-restoration observation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
