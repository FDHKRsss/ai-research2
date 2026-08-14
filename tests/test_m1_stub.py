# -*- coding: utf-8 -*-
"""Tests for the M1 (stub) deliverable: raport/KR-OFFICE-OSINT.md.

These tests validate the RESEARCH deliverable against the requirement contract in
docs/PLAN.md / docs/ARCHITECTURE.md (no application code exists in this project).
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"

# Anchor facts from docs/PLAN.md (must appear, flagged "(do weryfikacji)" in the DRAFT).
ANCHOR_IDENTIFIERS = {
    "KRS": "0001126380",
    "NIP": "7011222044",
    "REGON": "529621586",
    "adres (ulica)": "Stefana Batorego 18",
    "adres (miasto/kod)": "02-591 Warszawa",
    "forma prawna": "spółka z ograniczoną odpowiedzialnością",
    "kapitał zakładowy": "5 000 zł",
    "data rejestracji": "2024-09-11",
    "PKD": "69.20.Z",
}

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
                # separator row
                continue
            rows.append(cells)
    return rows


class TestM1StubDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load()

    def test_01_file_exists_and_nonempty(self):
        self.assertTrue(DELIVERABLE.exists(), "deliverable file must exist")
        self.assertGreater(len(self.text), 500, "deliverable must have substantive content")

    def test_02_required_top_level_sections_present(self):
        for heading in (
            "Metryka dokumentu",
            "Podsumowanie tabelaryczne",
            "Sekcja M1 — Identyfikacja podmiotu i metryka",
            "Czerwone Flagi",
            "Źródła",
            "Metodologia i ograniczenia",
        ):
            self.assertIn(f"## {heading}", self.text, f"missing section: {heading}")

    def test_03_metryka_has_core_fields(self):
        sec = _section(self.text, "Metryka dokumentu")
        for field in ("Badany podmiot", "Cel analizy", "Data analizy", "Metoda", "Status"):
            self.assertIn(field, sec, f"metryka missing field: {field}")
        # date of analysis must be today's date (never post-dated)
        self.assertIn("2026-08-15", sec, "metryka must state analysis date 2026-08-15")

    def test_04_summary_table_header_and_m1_risk(self):
        rows = _summary_rows(self.text)
        self.assertGreaterEqual(len(rows), 2, "summary table needs a header + at least M1 row")
        header = rows[0]
        self.assertEqual(len(header), 3, f"summary table must have 3 columns, got {len(header)}")
        for col in ("Sekcja", "Znaleziska", "Ocena ryzyka"):
            self.assertIn(col, header, f"summary table header missing '{col}'")
        m1 = [r for r in rows[1:] if r and "M1" in r[0]]
        self.assertTrue(m1, "summary table must contain an M1 row")
        risk_cell = m1[0][2]
        self.assertTrue(
            any(v in risk_cell for v in ALLOWED_RISK),
            f"M1 risk cell must use Niskie/Średnie/Wysokie, got: {risk_cell!r}",
        )

    def test_05_m1_contains_all_anchor_identifiers(self):
        sec = _section(self.text, "Sekcja M1 — Identyfikacja podmiotu i metryka")
        for label, value in ANCHOR_IDENTIFIERS.items():
            self.assertIn(value, sec, f"M1 missing anchor identifier {label}: {value}")

    def test_06_m1_contains_ownership_anchor_values(self):
        sec = _section(self.text, "Sekcja M1 — Identyfikacja podmiotu i metryka")
        for value in ("Katarzyna Pydynowska", "prezes zarządu", "91 udziałów", "4 550 zł"):
            self.assertIn(value, sec, f"M1 missing ownership value: {value}")

    def test_07_share_vs_capital_inconsistency_is_flagged(self):
        # PLAN requires the 91 udzialy = 4550 zl vs 5000 zl kapital issue to be explicitly raised.
        text = self.text
        self.assertIn("91", text)
        self.assertIn("5 000", text)
        flagged = any(
            phrase in text
            for phrase in ("nie sumuje się", "drugiego pakietu", "rozbieżność", "drugiego wspólnika")
        )
        self.assertTrue(flagged, "share-vs-capital inconsistency must be explicitly flagged")

    def test_08_no_todo_placeholders(self):
        # Only standalone placeholder markers count ("metodologia" contains "todo" as a substring).
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(), "deliverable must not contain '[WSTAW' placeholders")

    def test_09_sources_have_no_fabricated_access_dates(self):
        sec = _section(self.text, "Źródła")
        self.assertIn("nie podaję dat dostępu", sec,
                      "DRAFT sources must explicitly say no access dates yet")
        self.assertIsNone(
            re.search(r"\b20\d{2}-\d{2}-\d{2}\b", sec),
            "DRAFT sources section must not contain a fabricated access date",
        )

    def test_10_language_is_polish(self):
        for marker in ("działalność", "Źródła", "Czerwone", "spółka z ograniczoną odpowiedzialnością"):
            self.assertIn(marker, self.text, f"document must be in Polish (missing: {marker})")

    def test_11_risk_rating_consistent_between_summary_and_m1(self):
        sec = _section(self.text, "Sekcja M1 — Identyfikacja podmiotu i metryka")
        self.assertIn("Ocena: Średnie", sec, "M1 section must state Ocena: Średnie")
        m1 = [r for r in _summary_rows(self.text) if r and "M1" in r[0]]
        self.assertIn("Średnie", m1[0][2], "summary M1 risk cell must match M1 section (Średnie)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
