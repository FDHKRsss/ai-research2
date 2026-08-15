# -*- coding: utf-8 -*-
"""Tests for the M3 deliverable section: raport/KR-OFFICE-OSINT.md.

NOTE: M3 has progressed from stub to REAL in pass 2. The section's contract
(opinie Google Maps / GoWork / Oferteo / Facebook; merytoryka / oceny / daty /
liczba opinii; 12-month priority window; disambiguation by NIP/KRS/address) is
still validated here, together with the pass-2 grounding (verified 0 opinii,
URLs + access dates). This mirrors tests/test_m2_stub.py, which keeps validating
the M2 contract after M2 -- real landed.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

M3_HEADING = "Sekcja M3 — Reputacja"
PLATFORMS = ("Google Maps", "GoWork", "Oferteo", "Facebook")
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


class TestM3Deliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()
        cls.m3 = _section(cls.text, M3_HEADING)

    # -- structure -----------------------------------------------------------

    def test_01_m3_section_present(self):
        self.assertIn(f"## {M3_HEADING}", self.text, "missing M3 top-level section")

    def test_02_m3_summary_row_present_with_3_columns(self):
        rows = _summary_rows(self.text)
        m3 = [r for r in rows if r and "M3" in r[0]]
        self.assertTrue(m3, "summary table must contain an M3 row")
        self.assertEqual(len(m3[0]), 3, f"M3 summary row must have 3 columns, got {len(m3[0])}")

    # -- coverage of the required platforms and analysis dimensions -----------

    def test_03_m3_covers_all_four_platforms(self):
        for platform in PLATFORMS:
            self.assertIn(platform, self.m3, f"M3 missing required platform: {platform}")

    def test_04_m3_addresses_merytoryka_oceny_daty_liczba_opinii(self):
        for marker in ("merytoryk", "ocen", "dat", "liczba opinii"):
            self.assertIn(marker, self.m3, f"M3 missing analysis dimension marker: {marker}")

    def test_05_m3_states_12_month_priority_window_with_correct_dates(self):
        self.assertIn("ostatnich 12 miesięcy", self.m3,
                      "M3 must state the 12-month priority window")
        self.assertIn("2025-08-15", self.m3, "M3 12-month window must start 2025-08-15")
        self.assertIn("2026-08-15", self.m3, "M3 12-month window must end 2026-08-15")

    def test_06_m3_disambiguates_by_nip_krs_and_address(self):
        for marker in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(marker, self.m3, f"M3 missing disambiguation identifier: {marker}")
        self.assertIn("Stefana Batorego 18", self.m3, "M3 must anchor the address street")
        self.assertIn("02-591 Warszawa", self.m3, "M3 must anchor the address city/zip")

    # -- pass 2 (REAL): grounded, verified 0 opinions -------------------------

    def test_07_m3_records_zero_opinions_honestly(self):
        self.assertIn("0 opinii", self.m3, "M3 must record the verified 0-opinion result")
        self.assertIn("sprawdzone 2026-08-15", self.m3,
                      "M3 must record the 2026-08-15 check date")
        self.assertNotIn("80%", self.m3, "M3 must not copy the exemplar's '80%' rating")

    def test_08_m3_sources_grounded_with_access_dates(self):
        sec = _section(self.text, "Źródła")
        for platform in PLATFORMS:
            self.assertIn(platform, sec, f"Źródła section missing M3 source: {platform}")
        block = _sources_block(self.text, "M3")
        self.assertTrue(block, "Źródła must contain an M3 source block")
        self.assertIn("2026-08-15", block,
                      "M3 (REAL) source block must carry the access date 2026-08-15")

    def test_09_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M3 REAL must carry access dates")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15", f"access date must not be post-dated: {d}")

    # -- risk consistency ------------------------------------------------------

    def test_10_m3_risk_rating_consistent_summary_vs_section(self):
        self.assertIn("Ocena: Średnie", self.m3, "M3 section must state Ocena: Średnie")
        m3 = [r for r in _summary_rows(self.text) if r and "M3" in r[0]]
        self.assertTrue(m3, "summary table must contain an M3 row")
        risk_cell = m3[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M3 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )
        self.assertIn("Średnie", risk_cell, "summary M3 risk cell must match M3 section (Średnie)")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_11_m3_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M3", sec, "Czerwone Flagi section must address M3")
        self.assertIn("nie stwierdzono", sec,
                      "M3 red-flags entry must be honest (no negative findings)")
        self.assertIn("0 opinii", sec,
                      "M3 red-flags entry must record the 0-opinion result")

    def test_12_m3_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
