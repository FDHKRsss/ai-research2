# -*- coding: utf-8 -*-
"""Tests for the M3 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the M3 -- Reputacja section against the requirement contract
in docs/PLAN.md / docs/ARCHITECTURE.md (research deliverable, no application code
exists in this project).

M3 contract (PLAN.md): opinie Google Maps, GoWork, Oferteo, Facebook; merytoryka,
oceny, daty (priorytet ostatnich 12 mies.) oraz liczba opinii. W pass 1 (stub)
wszystko musi być oznaczone "(do weryfikacji)" / "(brak danych publicznych)" /
"(założenie)" -- zero fabrykacji ocen, liczby opinii ani treści recenzji.
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


class TestM3StubDeliverable(unittest.TestCase):
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
        for marker in ("merytoryk", "ocen", "dat", "liczbę opinii"):
            self.assertIn(marker, self.m3, f"M3 missing analysis dimension marker: {marker}")

    def test_05_m3_states_12_month_priority_window_with_correct_dates(self):
        self.assertIn("ostatnich 12 miesięcy", self.m3,
                      "M3 must state the 12-month priority window")
        self.assertIn("2025-08-15", self.m3, "M3 12-month window must start 2025-08-15")
        self.assertIn("2026-08-15", self.m3, "M3 12-month window must end 2026-08-15")

    def test_06_m3_disambiguates_by_nip_krs_and_address(self):
        # The goal/context requires disambiguation by identifiers, not just the name.
        for marker in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(marker, self.m3, f"M3 missing disambiguation identifier: {marker}")
        self.assertIn("Stefana Batorego 18", self.m3, "M3 must anchor the address street")
        self.assertIn("02-591 Warszawa", self.m3, "M3 must anchor the address city/zip")

    # -- honesty / no fabrication in the DRAFT --------------------------------

    def test_07_m3_draft_disclaimer_sources_not_opened(self):
        self.assertTrue(
            any(m in self.m3 for m in (
                "nie otwierano",
                "nie otwarto",
                "nie zostały jeszcze otwarte",
                "nie zostało jeszcze otwarte",
            )),
            "M3 DRAFT must state that the opinion sources have not been opened yet",
        )

    def test_08_m3_flags_everything_for_verification(self):
        self.assertGreaterEqual(self.m3.count("(do weryfikacji"), 3,
                                "M3 must flag multiple findings as '(do weryfikacji)'")
        self.assertTrue(
            any(m in self.m3 for m in ("do sprawdzenia", "do ustalenia")),
            "M3 must mark the platforms as 'do sprawdzenia'/'do ustalenia'",
        )

    def test_09_m3_no_fabricated_opinion_metrics(self):
        # No invented review counts, scores or copied exemplar percentages in the stub.
        self.assertIsNone(
            re.search(r"\d+\s*opinii", self.m3),
            "M3 must not fabricate a review count (e.g. '5 opinii')",
        )
        self.assertNotIn("80%", self.m3, "M3 stub must not copy the exemplar's '80%' rating")
        self.assertIn("nieznana na etapie DRAFT", self.m3,
                      "M3 must mark unknown ratings/review counts as 'nieznana na etapie DRAFT'")
        self.assertTrue(
            any(m in self.m3 for m in ("fabrykuję", "sfabrykowanych")),
            "M3 must state it does not fabricate ratings/review contents",
        )

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

    def test_11_m3_summary_row_is_honest_unverified(self):
        m3 = [r for r in _summary_rows(self.text) if r and "M3" in r[0]]
        findings = m3[0][1]
        self.assertIn("do zebrania i weryfikacji", findings,
                      "M3 summary findings must flag opinions as not yet gathered/verified")
        self.assertIn("nieznane na etapie DRAFT", findings,
                      "M3 summary findings must say the details are unknown in the DRAFT")

    # -- cross-cutting hygiene -------------------------------------------------

    def test_12_m3_red_flags_honest(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M3", sec, "Czerwone Flagi section must address M3")
        self.assertIn("nie stwierdzono", sec,
                      "M3 red-flags entry must be honest (no negative findings)")
        self.assertTrue(
            any(m in sec for m in ("nie zostały jeszcze otwarte", "nie zostały jeszcze sprawdzone")),
            "M3 red-flags entry must note the opinion sources have not been opened yet",
        )

    def test_13_m3_sources_planned_no_fabricated_dates(self):
        sec = _section(self.text, "Źródła")
        for platform in PLATFORMS:
            self.assertIn(platform, sec, f"Źródła section missing planned M3 source: {platform}")
        self.assertIn("nie podaję dat dostępu", sec,
                      "DRAFT sources must explicitly say no access dates yet")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", sec),
            "DRAFT sources section must not contain a fabricated access date",
        )

    def test_14_document_status_note_mentions_m3(self):
        self.assertIn("M3 — Reputacja", self.text,
                      "document status note should record M3 as complete")

    def test_15_m3_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo").
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


if __name__ == "__main__":
    unittest.main(verbosity=2)
