# -*- coding: utf-8 -*-
"""Tests for the M1 (REAL) deliverable: raport/KR-OFFICE-OSINT.md + tracking docs.

M1 -- real contract (PLAN.md / ARCHITECTURE.md / CONTEXT.md): the subject must be
identified and its registry data GROUNDED in primary sources actually opened in
pass 2:
- KRS via API Ministerstwa Sprawiedliwości (api-krs.ms.gov.pl) — current + full excerpt,
- Biała Lista VAT via API MF (wl-api.mf.gov.pl) — NIP/REGON/KRS/name/address + VAT status,
- the 91 udzialy = 4 550 zł vs 5 000 zł capital discrepancy is CONFIRMED in the KRS
  excerpt and remains OPEN (not resolved by guessing),
- the VAT restoration signal (Art. 96 ust. 9h, 2025-06-27) is surfaced for M2,
- every grounded source carries a URL + access date (<= 2026-08-15); no post-dated dates,
- risk rating M1 = Średnie, consistent between the M1 section and the summary table.

The pass-2 *progression* snapshot (which reals are done / remaining work) is owned
by the current milestone's tracking test (tests/test_m4_real.py after M4 -- real
landed). This file only asserts the M1 invariants plus the cross-milestone
invariants (all stubs done, reals completed in order).
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

M1_HEADING = "Sekcja M1 — Identyfikacja podmiotu i metryka"

# A milestone checkbox line looks like: "  - [x] M1 -- real"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

CONFIRMED_IDENTIFIERS = {
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

ALL_MILESTONES = ("M1", "M2", "M3", "M4", "M5", "M6")


def _load(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _section(text: str, heading: str) -> str:
    """Return the text of a single '## <heading>' section (up to the next '## ')."""
    marker = f"## {heading}"
    idx = text.find(marker)
    if idx == -1:
        return ""
    rest = text[idx + len(marker):]
    nxt = rest.find("\n## ")
    return rest if nxt == -1 else rest[:nxt]


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


def _plan_statuses(text: str) -> dict:
    """Map (milestone, pass) -> done from PLAN.md milestone checkboxes."""
    statuses = {}
    for line in text.splitlines():
        m = MILESTONE_RE.match(line)
        if m:
            statuses[(m.group(2), m.group(3))] = m.group(1).lower() == "x"
    return statuses


def _plan_parent_done(plan: str, milestone: str) -> bool:
    """Whether the parent milestone line ('- [x] **M# ...') is checked."""
    for line in plan.splitlines():
        s = line.strip()
        if s.startswith("- [x]") and f"**{milestone}" in line:
            return True
    return False


def _arch_wdrozenie(text: str) -> str:
    """Return the '## Stan wdrożenia' section (up to the next '## ')."""
    marker = "## Stan wdrożenia"
    idx = text.find(marker)
    if idx == -1:
        return ""
    rest = text[idx + len(marker):]
    nxt = rest.find("\n## ")
    return rest if nxt == -1 else rest[:nxt]


class TestM1RealDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load(DELIVERABLE)
        cls.m1 = _section(cls.text, M1_HEADING)
        cls.statuses = _plan_statuses(_load(PLAN))

    def test_01_m1_grounded_in_primary_sources(self):
        for marker in ("api-krs.ms.gov.pl", "wl-api.mf.gov.pl", "2026-08-15"):
            self.assertIn(marker, self.m1,
                          f"M1 REAL must cite the primary source / access date: {marker}")
        self.assertIn("potwierdzone", self.m1,
                      "M1 REAL must state the registry data is confirmed")

    def test_02_primary_source_urls_in_sources_section(self):
        sec = _section(self.text, "Źródła")
        self.assertIn("api-krs.ms.gov.pl/api/krs/OdpisAktualny", sec,
                      "Źródła must cite the KRS current-excerpt API URL")
        self.assertIn("api-krs.ms.gov.pl/api/krs/OdpisPelny", sec,
                      "Źródła must cite the KRS full-excerpt API URL")
        self.assertIn("wl-api.mf.gov.pl", sec,
                      "Źródła must cite the MF White List API URL")

    def test_03_all_identifiers_confirmed(self):
        for label, value in CONFIRMED_IDENTIFIERS.items():
            self.assertIn(value, self.m1,
                          f"M1 REAL missing confirmed identifier {label}: {value}")

    def test_04_ownership_confirmed(self):
        for value in ("Katarzyna Pydynowska", "prezes zarządu", "91 udziałów", "4 550 zł"):
            self.assertIn(value, self.m1, f"M1 REAL missing ownership value: {value}")

    def test_05_share_capital_discrepancy_confirmed_and_open(self):
        for marker in ("czyPosiadaCaloscUdzialow", "450 zł", "do weryfikacji"):
            self.assertIn(marker, self.m1,
                          f"M1 REAL must confirm+flag the share/capital discrepancy ({marker})")
        self.assertIn("całości udziałów", self.m1,
                      "M1 REAL must record that the shareholder does not hold all shares")

    def test_06_vat_restoration_signal_surfaced_for_m2(self):
        for marker in ("Art. 96 ust. 9h", "2025-06-27"):
            self.assertIn(marker, self.m1, f"M1 REAL missing VAT restoration marker: {marker}")
        self.assertIn("M2", self.m1, "the VAT restoration signal must be deferred to M2")

    def test_07_risk_rating_consistent_between_section_and_summary(self):
        self.assertIn("Ocena: Średnie", self.m1, "M1 section must state Ocena: Średnie")
        m1 = [r for r in _summary_rows(self.text) if r and "M1" in r[0]]
        self.assertTrue(m1, "summary table must contain an M1 row")
        self.assertIn("Średnie", m1[0][2],
                      "summary M1 risk cell must match M1 section (Średnie)")

    def test_08_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M1 REAL must carry at least one access date")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15",
                                 f"access date must not be post-dated: {d}")

    def test_09_document_status_note_reflects_real_progress(self):
        header = self.text.split("---")[0]
        self.assertIn("M1 — Identyfikacja podmiotu i metryka", header,
                      "status note must record M1 as REAL")
        self.assertTrue(
            any(s in header.lower() for s in ("uziemione", "uziemienie")),
            "status note must record the grounded (real) sections",
        )
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        pending = [m for m in ALL_MILESTONES if m not in done_real]
        if pending:
            for m in pending:
                self.assertIn(m, header, f"status note must mention still-pending {m}")
            self.assertIn("DRAFT/stub", header,
                          "status note must mark the pending sections as DRAFT/stub")
        else:
            self.assertIn("pass 2", header,
                          "status note must record pass 2 once all reals are done")
            self.assertNotIn("DRAFT/stub", header,
                             "status note must not mark sections DRAFT/stub once pass 2 is complete")


class TestM1RealTracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    def test_10_plan_m1_real_marked_done(self):
        self.assertTrue(self.statuses.get(("M1", "real"), False),
                        "PLAN.md must mark M1 -- real as [x]")

    def test_11_plan_parent_m1_marked_done(self):
        self.assertTrue(_plan_parent_done(self.plan, "M1"),
                        "parent M1 milestone must be checked now that M1 -- real is done")

    def test_12_plan_all_stubs_remain_done(self):
        for m in ALL_MILESTONES:
            self.assertTrue(self.statuses.get((m, "stub"), False),
                            f"PLAN.md must keep {m} -- stub as [x]")

    def test_13_plan_real_milestones_done_in_order(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        done_idx = {i for i, m in enumerate(ALL_MILESTONES) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_14_arch_m1_real_entry_present(self):
        self.assertIn("**M1 -- real:**", self.wdrozenie,
                      "ARCH must list the M1 -- real entry")
        self.assertIn("uziemion", self.wdrozenie,
                      "ARCH M1 -- real entry must say the section is grounded")


if __name__ == "__main__":
    unittest.main(verbosity=2)
