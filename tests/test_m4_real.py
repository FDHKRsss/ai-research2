# -*- coding: utf-8 -*-
"""Tests for the M4 (REAL) deliverable: raport/KR-OFFICE-OSINT.md + tracking docs.

M4 -- real contract (PLAN.md / ARCHITECTURE.md / CONTEXT.md): the service-quality
section must be GROUNDED in sources actually opened in pass 2:
- oferta i zakres usług (concrete, sourced offer — not "do ustalenia"),
- specjalizacja (IT / transport / inne) — resolved, not left as "nieznana",
- PKD 69.20.Z cross-referenced to M1 and grounded in KRS,
- ubezpieczenie OC biura — if a mention was found it must be included; otherwise an
  explicit "nie znaleziono wzmianki o OC" AFTER actually opening the sources (the DRAFT
  excuse "z braku otwarcia źródeł" must be gone),
- certyfikaty / doświadczenie kadry / kanały kontaktu — grounded or explicitly marked
  as "brak danych publicznych",
- every grounded claim carries a URL + access date (<= 2026-08-15),
- risk rating M4 = Niskie/Średnie/Wysokie, consistent between the M4 section and the
  summary table.

This file also owns the pass-2 *progression* snapshot after M4 -- real: the done reals
are exactly M1, M2, M3, M4; M5 and M6 -- real remain pending; all M1..M6 stubs stay
done; and the ARCH "remaining work" advances to M5 → M6.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

M4_HEADING = "Sekcja M4 — Jakość usług i specjalizacja"

# A milestone checkbox line looks like: "  - [x] M4 -- real"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = ("M1", "M2", "M3", "M4", "M5", "M6")
# Progression snapshot after M4 -- real lands: M1..M4 real done, M5/M6 pending.
DONE_REALS = {"M1", "M2", "M3", "M4"}
PENDING_REALS = ("M5", "M6")
ALLOWED_RISK = ("Niskie", "Średnie", "Wysokie")


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


def _subsection(text: str, heading: str) -> str:
    """Return the text of a '### <heading>' block up to the next '### ' or '## '."""
    marker = f"### {heading}"
    idx = text.find(marker)
    if idx == -1:
        return ""
    rest = text[idx + len(marker):]
    nxt = rest.find("\n### ")
    nxt2 = rest.find("\n## ")
    if nxt2 != -1 and (nxt == -1 or nxt2 < nxt):
        nxt = nxt2
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


class TestM4RealDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load(DELIVERABLE)
        cls.m4 = _section(cls.text, M4_HEADING)

    # -- grounding / pass-2 state -------------------------------------------

    def test_01_m4_is_grounded_not_draft(self):
        self.assertIn("pass 2", self.m4,
                      "M4 REAL must declare pass 2 (real grounding)")
        self.assertIn("REAL", self.m4,
                      "M4 REAL must mark the section as REAL")
        # The DRAFT "sources not opened yet" disclaimer must be gone.
        self.assertNotIn("nie otwierano", self.m4,
                         "M4 REAL must not claim the sources were not opened")
        self.assertNotIn("z braku otwarcia źródeł", self.m4,
                         "M4 REAL must not excuse the OC finding with unopened sources")
        self.assertNotIn("na etapie DRAFT", self.m4,
                         "M4 REAL must not leave findings in the DRAFT state")
        # DRAFT-only unresolved cells must be resolved or marked "brak danych publicznych".
        self.assertNotIn("do ustalenia", self.m4,
                         "M4 REAL must not leave fields as 'do ustalenia'")

    def test_02_m4_cites_opened_sources_with_access_date(self):
        self.assertIn("2026-08-15", self.m4,
                      "M4 REAL must carry the access date 2026-08-15")
        domains = ("oferteo.pl", "gowork.pl", "ekrs.ms.gov.pl", "aleo.com",
                   "pkt.pl", "gov.pl", "maps.google")
        self.assertTrue(
            any(d in self.m4 for d in domains),
            "M4 REAL must cite at least one concrete source domain/URL",
        )

    # -- offer / specialization / OC ----------------------------------------

    def test_03_offer_and_scope_grounded(self):
        offer = _subsection(self.m4, "4.2. Oferta i zakres usług")
        self.assertTrue(offer, "M4 missing the offer subsection")
        # The offer must be concrete and sourced, not "do ustalenia"/"(do weryfikacji)".
        self.assertIn("ksiąg rachunkowych", offer,
                      "M4 REAL must ground the offer (e.g. 'prowadzenie ksiąg rachunkowych')")
        self.assertIn("kadrow", offer,
                      "M4 REAL must ground the HR/payroll scope")
        self.assertIn("powiązane z M1", offer,
                      "M4 REAL must cross-reference PKD back to M1")
        self.assertNotIn("do ustalenia", offer,
                         "M4 REAL offer must not be 'do ustalenia'")
        self.assertNotIn("(do weryfikacji", offer,
                         "M4 REAL offer must not be '(do weryfikacji)'")

    def test_04_specialization_resolved(self):
        self.assertIn("Specjalizacja", self.m4, "M4 REAL missing specialization block")
        # DRAFT said "specjalizacja **nieznana**"; REAL must resolve it.
        self.assertNotIn("specjalizacja **nieznana**", self.m4,
                         "M4 REAL must resolve the specialization (no longer 'nieznana')")
        # Either a found specialization or an explicit "not found" statement.
        self.assertTrue(
            ("brak" in self.m4 and "specjalizac" in self.m4)
            or any(w in self.m4 for w in ("IT", "transport", "e-commerce")),
            "M4 REAL must state a found specialization or an explicit absence of one",
        )

    def test_05_oc_insurance_honest_and_actually_checked(self):
        oc = _subsection(self.m4, "4.4. Ubezpieczenie OC biura")
        self.assertTrue(oc, "M4 missing the OC-insurance subsection")
        # After actually checking sources: either a mention was found, or it is
        # honestly recorded as not found (without the DRAFT "unopened" excuse).
        found_or_absent = ("nie znaleziono" in oc) or ("ubezpieczeni" in oc and "OC" in oc)
        self.assertTrue(found_or_absent,
                        "M4 REAL must record OC as found or as 'nie znaleziono' after checking")
        self.assertNotIn("(do weryfikacji", oc,
                         "M4 REAL OC block must not leave the finding '(do weryfikacji)'")
        self.assertNotIn("nie otwierano", oc,
                         "M4 REAL OC block must not excuse itself with unopened sources")

    # -- kadra / certyfikaty / kontakt --------------------------------------

    def test_06_certificates_experience_contact_grounded(self):
        for marker in ("Certyfikaty", "Doświadczenie kadry", "Kanały kontaktu"):
            self.assertIn(marker, self.m4, f"M4 REAL missing block: {marker}")
        # The managing person is a known, verified fact from M1; kadra must be named.
        self.assertIn("Pydynowska", self.m4,
                      "M4 REAL must identify the kadra (prezes Katarzyna Pydynowska)")
        kontakt = _subsection(self.m4, "4.7. Kanały kontaktu")
        self.assertTrue(kontakt, "M4 missing the contact-channels subsection")
        self.assertNotIn("do ustalenia", kontakt,
                         "M4 REAL contact channels must not be 'do ustalenia'")
        self.assertNotIn("(do weryfikacji", kontakt,
                         "M4 REAL contact channels must not be '(do weryfikacji)'")

    def test_07_disambiguated_by_nip_krs(self):
        for ident in ("NIP 7011222044", "KRS 0001126380"):
            self.assertIn(ident, self.m4, f"M4 REAL missing identifier: {ident}")

    # -- risk consistency ----------------------------------------------------

    def test_08_risk_rating_consistent_section_vs_summary(self):
        m = re.search(r"Ocena:\s*(Niskie|Średnie|Wysokie)", self.m4)
        self.assertIsNotNone(m, "M4 section must state 'Ocena: Niskie/Średnie/Wysokie'")
        section_risk = m.group(1)
        row = _summary_row(self.text, "M4")
        self.assertIsNotNone(row, "summary table must contain an M4 row")
        risk_cell = row[2]
        self.assertIn(section_risk, risk_cell,
                      "summary M4 risk cell must match the M4 section rating")
        self.assertIn(section_risk, ALLOWED_RISK)

    def test_09_summary_m4_row_grounded_not_draft(self):
        row = _summary_row(self.text, "M4")
        self.assertIsNotNone(row, "summary table must contain an M4 row")
        findings = row[1]
        self.assertIn("OC", findings, "M4 summary findings must mention OC")
        self.assertNotIn("Nieznane na etapie DRAFT", findings,
                         "M4 summary findings must no longer be 'Nieznane na etapie DRAFT'")
        self.assertNotIn("do ustalenia i weryfikacji", findings,
                         "M4 summary findings must not leave the offer as unestablished")

    # -- hygiene -------------------------------------------------------------

    def test_10_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M4 REAL must carry at least one access date")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15",
                                 f"access date must not be post-dated: {d}")

    def test_11_no_todo_placeholders(self):
        self.assertIsNone(
            re.search(r"\b(todo|tbd|lorem|placeholder|fixme)\b", self.text, re.IGNORECASE),
            "deliverable must not contain TODO/TBD/lorem/placeholder markers",
        )
        self.assertNotIn("[wstaw", self.text.lower(),
                         "deliverable must not contain '[WSTAW' placeholders")


class TestM4RealTracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    def test_12_plan_m4_real_marked_done(self):
        self.assertTrue(self.statuses.get(("M4", "real"), False),
                        "PLAN.md must mark M4 -- real as [x]")

    def test_13_plan_parent_m4_marked_done(self):
        self.assertTrue(_plan_parent_done(self.plan, "M4"),
                        "parent M4 milestone must be checked now that M4 -- real is done")

    def test_14_plan_done_reals_exactly_m1_through_m4(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        self.assertEqual(done_real, DONE_REALS,
                         "exactly M1, M2, M3 and M4 -- real may be checked right now")

    def test_15_plan_m5_m6_real_still_pending(self):
        for m in PENDING_REALS:
            self.assertFalse(self.statuses.get((m, "real"), True),
                             f"PLAN.md must keep {m} -- real as [ ]")

    def test_16_plan_all_stubs_remain_done(self):
        for m in ALL_MILESTONES:
            self.assertTrue(self.statuses.get((m, "stub"), False),
                            f"PLAN.md must keep {m} -- stub as [x]")

    def test_17_plan_real_milestones_done_in_order(self):
        done_real = {m for (m, p), d in self.statuses.items() if p == "real" and d}
        done_idx = {i for i, m in enumerate(ALL_MILESTONES) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_18_arch_m4_real_entry_present_and_grounded(self):
        self.assertIn("**M4 -- real:**", self.wdrozenie,
                      "ARCH must list the M4 -- real entry")
        self.assertIn("uziemion", self.wdrozenie,
                      "ARCH M4 -- real entry must say the section is grounded")
        for marker in ("oferta", "specjalizac", "OC"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH M4 -- real entry must record: {marker}")

    def test_19_arch_remaining_work_is_m5_to_m6_real(self):
        self.assertIn("Pass 2 (REAL) w toku", self.wdrozenie,
                      "ARCH must state pass 2 (REAL) is in progress")
        self.assertIn("M5 → M6", self.wdrozenie,
                      "ARCH remaining work must be M5 → M6 (after M4 -- real landed)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
