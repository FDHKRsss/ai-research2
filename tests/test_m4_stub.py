# -*- coding: utf-8 -*-
"""Tests for the M4 deliverable section: raport/KR-OFFICE-OSINT.md.

NOTE: M4 has progressed from stub to REAL in pass 2. The section's contract
(oferta, specjalizacja IT/transport/inne, PKD, ubezpieczenie OC biura,
certyfikaty, doświadczenie kadry, kanały kontaktu, disambiguation by NIP/KRS)
is still validated here, together with the pass-2 grounding (concrete offer +
OC self-declaration + URLs + access dates). The detailed REAL grounding is
validated in tests/test_m4_real.py; this file keeps the durable contract checks
(mirroring tests/test_m2_stub.py).
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


class TestM4Deliverable(unittest.TestCase):
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
        self.assertIn("powiązane z M1", self.m4,
                      "M4 must cross-reference PKD back to M1")

    def test_04_m4_covers_specialization_it_transport_inne(self):
        for marker in ("Specjalizacja", "IT", "transport", "inne"):
            self.assertIn(marker, self.m4, f"M4 missing specialization marker: {marker}")

    def test_05_m4_covers_oc_insurance_honestly(self):
        # OC is required by the goal. In pass 2 a self-declaration was found in pkt.pl;
        # the section must record it honestly and refuse to invent scope/limit.
        for marker in ("ubezpieczenie OC", "Firma ubezpieczona OC",
                       "nie wymyślam zakresu ani limitu"):
            self.assertIn(marker, self.m4, f"M4 missing OC marker: {marker}")

    def test_06_m4_covers_certificates_experience_contact(self):
        for marker in ("Certyfikaty i uprawnienia", "Doświadczenie kadry", "Kanały kontaktu"):
            self.assertIn(marker, self.m4, f"M4 missing service-quality marker: {marker}")
        self.assertIn("Pydynowska", self.m4,
                      "M4 must identify the kadra (prezes Katarzyna Pydynowska)")

    def test_07_m4_disambiguates_by_nip_krs_address(self):
        for marker in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(marker, self.m4, f"M4 missing disambiguation identifier: {marker}")
        self.assertIn("Stefana Batorego 18", self.m4, "M4 must anchor the address street")
        self.assertIn("02-591 Warszawa", self.m4, "M4 must anchor the address city/zip")

    # -- pass 2 (REAL): grounded offer / OC -----------------------------------

    def test_08_m4_grounded_with_sources_and_access_dates(self):
        self.assertIn("2026-08-15", self.m4, "M4 REAL must carry the access date 2026-08-15")
        self.assertIn("ksiąg rachunkowych", self.m4,
                      "M4 REAL must ground the offer (prowadzenie ksiąg rachunkowych)")
        block = _sources_block(self.text, "M4")
        self.assertTrue(block, "Źródła must contain an M4 source block")
        self.assertIn("2026-08-15", block,
                      "M4 (REAL) source block must carry the access date 2026-08-15")
        self.assertTrue(
            any(d in block for d in ("oferteo.pl", "pkt.pl", "gowork.pl", "aleo.com")),
            "M4 (REAL) source block must cite a concrete public profile",
        )

    def test_09_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M4 REAL must carry access dates")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15", f"access date must not be post-dated: {d}")

    # -- risk consistency ------------------------------------------------------

    def test_10_m4_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m4, "M4 section must state Ocena: Średnie")
        m4 = [r for r in _summary_rows(self.text) if r and "M4" in r[0]]
        self.assertTrue(m4, "summary table must contain an M4 row")
        risk_cell = m4[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M4 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M4 risk cell must match M4 section (Średnie)")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_11_m4_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M4", sec, "Czerwone Flagi section must address M4")
        self.assertIn("nie stwierdzono", sec,
                      "M4 red-flags entry must be honest (no negative findings)")
        self.assertIn("ubezpieczona OC", sec,
                      "M4 red-flags entry must record the OC self-declaration")

    def test_12_m4_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
