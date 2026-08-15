# -*- coding: utf-8 -*-
"""Tests for the M6 (REAL) deliverable: raport/KR-OFFICE-OSINT.md + tracking docs.

M6 -- real contract (PLAN.md / ARCHITECTURE.md / CONTEXT.md): the risk synthesis
must be GROUNDED on the already-verified M1–M5 findings and close the report:
- końcowa tabela podsumowująca `Sekcja | Znaleziska | Ocena ryzyka` (M1–M6),
- sekcja „Czerwone Flagi" (real signals only; the two observation signals from
  M1/M2/M5 are carried forward: 91 udziałów = 4 550 zł vs 5 000 zł, and the VAT
  restoration Art. 96 ust. 9h / 2025-06-27),
- rekomendacja (final/decisive — the DRAFT "warunkowa / dokończ pass 2" framing
  must be gone),
- pełna scalona lista źródeł z datami dostępu (M6 synthesizes the M1–M5 sources),
- metodologia i ograniczenia (final, no longer "warunkowe … po uziemieniu M6"),
- końcowa ocena ryzyka = Niskie/Średnie/Wysokie, consistent between the M6 section
  and the summary table.

This file also owns the FINAL pass-2 progression snapshot: all M1..M6 reals are
done, no pending reals remain, and ARCH declares pass 2 (REAL) complete.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

M6_HEADING = "Sekcja M6 — Synteza ryzyka"

# A milestone checkbox line looks like: "  - [x] M6 -- real"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = ("M1", "M2", "M3", "M4", "M5", "M6")
# FINAL snapshot after M6 -- real lands: every real is done, nothing pending.
DONE_REALS = {"M1", "M2", "M3", "M4", "M5", "M6"}
ALLOWED_RISK = ("Niskie", "Średnie", "Wysokie")

# Each partial area must appear in the synthesis table with its Średnie rating.
SYNTHESIS_ROWS = (
    "Identyfikacja i metryka | Średnie",
    "Status prawny i podatkowy | Średnie",
    "Reputacja | Średnie",
    "Jakość usług i specjalizacja | Średnie",
    "Stabilność finansowa | Średnie",
)


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


def _summary_row(text: str, milestone: str):
    for row in _summary_rows(text):
        if row and milestone in row[0]:
            return row
    return None


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


class TestM6RealDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load(DELIVERABLE)
        cls.m6 = _section(cls.text, M6_HEADING)
        cls.header = cls.text.split("---")[0]

    # -- grounding / pass-2 state -------------------------------------------

    def test_01_m6_grounded_not_draft(self):
        self.assertIn("REAL", self.m6, "M6 REAL must mark the section as REAL")
        self.assertIn("pass 2", self.m6, "M6 REAL must tie the synthesis to pass 2")
        # The DRAFT "remains to be grounded / will be updated" framing must be gone.
        self.assertNotIn("pozostała do uziemienia", self.m6,
                         "M6 REAL must not say the section remains to be grounded")
        self.assertNotIn("zostanie zaktualizowana", self.m6,
                         "M6 REAL must not say the rating will be updated in pass 2")
        self.assertNotIn("charakter warunkowy", self.m6,
                         "M6 REAL must not describe the rating as 'warunkowy' (DRAFT)")

    def test_02_m6_synthesis_grounded_not_unverified(self):
        self.assertNotIn("niezweryfikowane", self.m6,
                         "M6 REAL must not leave the synthesis as 'niezweryfikowane'")
        self.assertNotIn("nie otwarto źródeł", self.m6,
                         "M6 REAL must not claim the synthesis sources were not opened")

    # -- synthesis content ----------------------------------------------------

    def test_03_m6_synthesizes_all_partial_ratings(self):
        for marker in ("Obszar", "Ocena cząstkowa"):
            self.assertIn(marker, self.m6,
                          f"M6 synthesis table missing column: {marker}")
        for row_marker in SYNTHESIS_ROWS:
            self.assertIn(row_marker, self.m6,
                          f"M6 synthesis table must rate area as Średnie: {row_marker}")

    def test_04_m6_carries_forward_both_observation_signals(self):
        # (a) the share/capital discrepancy (91 udzialy = 4550 zl vs 5000 zl)
        for marker in ("91 udziałów", "4 550 zł", "450 zł"):
            self.assertIn(marker, self.m6,
                          f"M6 REAL must carry the share/capital discrepancy: {marker}")
        # (b) the VAT restoration signal
        for marker in ("Art. 96 ust. 9h", "2025-06-27"):
            self.assertIn(marker, self.m6,
                          f"M6 REAL must carry the VAT restoration signal: {marker}")

    def test_05_m6_final_risk_rating_present(self):
        self.assertIn("Końcowa ocena ryzyka", self.m6,
                      "M6 must state the final risk rating")
        self.assertIn("Średnie", self.m6, "M6 final rating must be Średnie")
        self.assertNotIn("w pass 2 (real).", self.m6,
                         "M6 must not defer the rating to pass 2 (real)")

    def test_06_m6_recommendation_final_not_conditional(self):
        self.assertIn("Rekomendacja", self.m6,
                      "M6 must contain a recommendation subsection")
        self.assertNotIn("charakter warunkowy", self.m6,
                         "M6 recommendation must not be 'warunkowy' (DRAFT)")
        self.assertNotIn("dokończyć pass 2", self.m6,
                         "M6 recommendation must not defer to 'dokończyć pass 2'")

    def test_07_m6_links_red_flags_and_summary(self):
        for marker in ("Czerwone Flagi", "Podsumowanie tabelaryczne"):
            self.assertIn(marker, self.m6,
                          f"M6 must cross-reference the '{marker}' section")

    # -- summary / red-flags / sources / methodology -------------------------

    def test_08_risk_rating_consistent_section_vs_summary(self):
        m = re.search(r"Końcowa ocena ryzyka:\s*(Niskie|Średnie|Wysokie)", self.m6)
        self.assertIsNotNone(m, "M6 section must state 'Końcowa ocena ryzyka: ...'")
        section_risk = m.group(1)
        self.assertIn(section_risk, ALLOWED_RISK)
        row = _summary_row(self.text, "M6")
        self.assertIsNotNone(row, "summary table must contain an M6 row")
        self.assertIn(section_risk, row[2],
                      "summary M6 risk cell must match the M6 section rating")

    def test_09_summary_m6_row_grounded_not_draft(self):
        row = _summary_row(self.text, "M6")
        self.assertIsNotNone(row, "summary table must contain an M6 row")
        findings = row[1]
        self.assertNotIn("warunkow", findings,
                         "M6 summary findings must not describe the recommendation as conditional")
        self.assertNotIn("dokończenia pass 2", findings,
                         "M6 summary findings must not defer the decision to pass 2")
        self.assertNotIn("nieukończoną syntezą", findings,
                         "M6 summary findings must not say the synthesis is unfinished")

    def test_10_document_status_marks_m6_complete(self):
        self.assertNotIn("pozostaje w statusie DRAFT/stub", self.header,
                         "status note must no longer mark M6 as DRAFT/stub")
        self.assertNotIn("M6 nadal DRAFT/stub", self.text,
                         "Metryka must no longer mark M6 as 'nadal DRAFT/stub'")
        self.assertNotIn("zachowuje charakter wstępny", self.text,
                         "summary note must no longer say the M6 row is preliminary")
        self.assertIn("M6", self.header, "status note must still mention M6 (as done)")

    def test_11_sources_m6_block_grounded(self):
        sec = _section(self.text, "Źródła")
        self.assertNotIn("zostanie dopisana pełna, scalona lista", sec,
                         "M6 source block must not promise a future merged list")
        self.assertNotIn("nadal zawiera planowane źródła", sec,
                         "Źródła intro must not say M6 still has planned sources")
        block = _sources_block(self.text, "M6")
        self.assertTrue(block, "Źródła must contain an M6 source block")
        self.assertIn("2026-08-15", block,
                      "M6 (REAL) source block must carry the access date 2026-08-15")
        # M6 is a synthesis of the already-ground M1–M5 sources.
        self.assertTrue(("M1" in block and "M5" in block),
                        "M6 source block must reference the grounded M1–M5 blocks")

    def test_12_methodology_final_not_conditional(self):
        sec = _section(self.text, "Metodologia i ograniczenia")
        self.assertNotIn("po uziemieniu sekcji M6", sec,
                         "Metodologia must not defer the M6 synthesis to a later pass")
        self.assertNotIn("na tym etapie są **warunkowe**", sec,
                         "Metodologia must not describe the M6 rating as 'warunkowe' (DRAFT)")

    def test_13_red_flags_m6_final(self):
        sec = _section(self.text, "Czerwone Flagi")
        self.assertIn("M6", sec, "Czerwone Flagi section must address M6")
        self.assertIn("Średnie", sec, "M6 red-flags entry must state the Średnie rating")
        self.assertNotIn("do rozstrzygnięcia w pass 2", sec,
                         "M6 red-flags entry must not defer issues to pass 2")

    # -- hygiene -------------------------------------------------------------

    def test_14_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M6 REAL must carry at least one access date")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15",
                                 f"access date must not be post-dated: {d}")

    def test_15_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


class TestM6RealTracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    def test_16_plan_m6_real_marked_done(self):
        self.assertTrue(self.statuses.get(("M6", "real"), False),
                        "PLAN.md must mark M6 -- real as [x]")

    def test_17_plan_parent_m6_marked_done(self):
        self.assertTrue(_plan_parent_done(self.plan, "M6"),
                        "parent M6 milestone must be checked now that M6 -- real is done")

    def test_18_plan_done_reals_exactly_m1_through_m6(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        self.assertEqual(done_real, DONE_REALS,
                         "exactly M1, M2, M3, M4, M5 and M6 -- real must be checked")

    def test_19_plan_all_stubs_remain_done(self):
        for m in ALL_MILESTONES:
            self.assertTrue(self.statuses.get((m, "stub"), False),
                            f"PLAN.md must keep {m} -- stub as [x]")

    def test_20_plan_real_milestones_done_in_order(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        done_idx = {i for i, m in enumerate(ALL_MILESTONES) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_21_arch_m6_real_entry_present_and_grounded(self):
        self.assertIn("**M6 -- real:**", self.wdrozenie,
                      "ARCH must list the M6 -- real entry")
        self.assertIn("uziemion", self.wdrozenie,
                      "ARCH M6 -- real entry must say the synthesis is grounded")
        for marker in ("Synteza", "końcowa ocena", "rekomendacja", "Czerwone Flagi"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH M6 -- real entry must record: {marker}")

    def test_22_arch_declares_pass2_complete(self):
        self.assertIn("Pass 2 (REAL) zakończon", self.wdrozenie,
                      "ARCH must declare pass 2 (REAL) complete after M6 -- real")
        self.assertNotIn("Pass 2 (REAL) w toku", self.wdrozenie,
                         "ARCH must no longer say pass 2 (REAL) is in progress")
        self.assertNotIn("pozostała praca", self.wdrozenie,
                         "ARCH must not leave a 'remaining work' bullet after M6 -- real")


if __name__ == "__main__":
    unittest.main(verbosity=2)
