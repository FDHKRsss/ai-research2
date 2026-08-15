# -*- coding: utf-8 -*-
"""Tests for the M2 (REAL) deliverable: raport/KR-OFFICE-OSINT.md + tracking docs.

M2 -- real contract (PLAN.md / ARCHITECTURE.md / CONTEXT.md): the legal/tax status
must be GROUNDED in primary sources actually opened in pass 2:
- Biała Lista VAT via API MF (wl-api.mf.gov.pl) — status "Czynny", VAT registration
  date 2024-10-08, the settlement account, and the restoration fields
  (Art. 96 ust. 9h / 2025-06-27) must be surfaced and interpreted,
- VIES via EC API (ec.europa.eu/taxation_customs/vies) — isValid: true for PL7011222044,
- KRS via API MS — active status (stanPozycji 1) and empty sections 4-6,
- MSiG (imsig.pl) — "aktywna" and exactly one (registration) entry,
- KRZ — explicit limitation (interactive search, not queried programmatically),
- commercial BIG (KRD/ERIF/InfoMonitor) — explicit access limitation, no guessing,
- risk rating M2 = Średnie, consistent between the M2 section and the summary table,
- every grounded source carries a URL + access date (<= 2026-08-15).

The pass-2 *progression* snapshot (exactly which reals are done) is owned by the
current milestone's tracking test (tests/test_m4_real.py after M4 -- real landed).
This file's tracking tests are forward-compatible: M1 and M2 -- real must REMAIN
done, reals must be completed in order, and the ARCH "remaining work" is derived
from PLAN.md (pending reals), not hardcoded.
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DELIVERABLE = REPO / "raport" / "KR-OFFICE-OSINT.md"
PLAN = REPO / "docs" / "PLAN.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"

M2_HEADING = "Sekcja M2 — Status prawny i podatkowy"

# A milestone checkbox line looks like: "  - [x] M2 -- real"
MILESTONE_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(M\d)\s*--\s*(stub|real)\s*$")

ALL_MILESTONES = ("M1", "M2", "M3", "M4", "M5", "M6")
# M2's own real cannot land without M1 -- real; both must stay done forever after.
MUST_BE_DONE_REALS = {"M1", "M2"}


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


def _done_reals(statuses: dict) -> set:
    return {m for (m, p), d in statuses.items() if p == "real" and d}


def _pending_reals(statuses: dict) -> list:
    return [m for m in ALL_MILESTONES if m not in _done_reals(statuses)]


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


class TestM2RealDeliverable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = _load(DELIVERABLE)
        cls.m2 = _section(cls.text, M2_HEADING)

    def test_01_m2_grounded_in_primary_sources(self):
        for marker in ("wl-api.mf.gov.pl", "ec.europa.eu/taxation_customs/vies",
                       "ekrs.ms.gov.pl", "imsig.pl", "2026-08-15"):
            self.assertIn(marker, self.m2,
                          f"M2 REAL must cite the primary source / access date: {marker}")
        self.assertIn("potwierdzone", self.m2,
                      "M2 REAL must state the legal/tax status is confirmed")

    def test_02_confirmed_vat_status_on_biala_lista(self):
        for marker in ("Czynny", "czynny podatnik VAT", "2024-10-08",
                       "52 1160 2202 0000 0006 3037 1440"):
            self.assertIn(marker, self.m2,
                          f"M2 REAL missing Biała Lista confirmed field: {marker}")

    def test_03_vat_restoration_signal_surfaced_and_interpreted(self):
        for marker in ("Art. 96 ust. 9h", "2025-06-27", "wykreślen", "przywrócon"):
            self.assertIn(marker, self.m2,
                          f"M2 REAL must surface/interpret the VAT restoration ({marker})")

    def test_04_vies_valid_confirmed(self):
        for marker in ("VIES", "PL7011222044", "isValid: true", "ważny"):
            self.assertIn(marker, self.m2, f"M2 REAL missing VIES confirmation: {marker}")

    def test_05_krs_active_and_clean_sections_confirmed(self):
        for marker in ("aktywny", "działy 4", "upadłości", "restrukturyzacji", "likwidacji"):
            self.assertIn(marker, self.m2, f"M2 REAL missing KRS status marker: {marker}")

    def test_06_msig_single_registration_entry_confirmed(self):
        for marker in ("MSiG", "185/2024", "aktywna"):
            self.assertIn(marker, self.m2, f"M2 REAL missing MSiG marker: {marker}")

    def test_07_krz_explicit_limitation(self):
        for marker in ("KRZ", "krz.ms.gov.pl", "interaktywn"):
            self.assertIn(marker, self.m2, f"M2 REAL missing KRZ marker: {marker}")
        self.assertIn("nie wykonane", self.m2,
                      "M2 REAL must state the KRZ programmatic query was not performed")

    def test_08_commercial_big_explicit_limitation(self):
        for big in ("KRD", "ERIF", "InfoMonitor"):
            self.assertIn(big, self.m2, f"M2 REAL missing commercial BIG marker: {big}")
        self.assertIn("(brak danych publicznych)", self.m2,
                      "M2 REAL must flag commercial BIG as 'brak danych publicznych'")

    def test_09_risk_rating_consistent_between_section_and_summary(self):
        self.assertIn("Ocena: Średnie", self.m2, "M2 section must state Ocena: Średnie")
        m2 = [r for r in _summary_rows(self.text) if r and "M2" in r[0]]
        self.assertTrue(m2, "summary table must contain an M2 row")
        self.assertIn("Średnie", m2[0][2],
                      "summary M2 risk cell must match M2 section (Średnie)")

    def test_10_no_post_dated_access_dates(self):
        dates = re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", self.text)
        self.assertTrue(dates, "M2 REAL must carry at least one access date")
        for d in dates:
            self.assertLessEqual(d, "2026-08-15",
                                 f"access date must not be post-dated: {d}")


class TestM2RealTracking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = _load(PLAN)
        cls.arch = _load(ARCH)
        cls.statuses = _plan_statuses(cls.plan)
        cls.wdrozenie = _arch_wdrozenie(cls.arch)

    def test_11_plan_m2_real_marked_done(self):
        self.assertTrue(self.statuses.get(("M2", "real"), False),
                        "PLAN.md must mark M2 -- real as [x]")

    def test_12_plan_parent_m2_marked_done(self):
        self.assertTrue(_plan_parent_done(self.plan, "M2"),
                        "parent M2 milestone must be checked now that M2 -- real is done")

    def test_13_plan_m1_and_m2_reals_remain_done(self):
        done_real = _done_reals(self.statuses)
        self.assertTrue(MUST_BE_DONE_REALS <= done_real,
                        "M1 and M2 -- real must remain done (later reals may also be done)")

    def test_14_plan_done_reals_form_contiguous_prefix(self):
        done_real = _done_reals(self.statuses)
        done_idx = {i for i, m in enumerate(ALL_MILESTONES) if m in done_real}
        self.assertEqual(done_idx, set(range(len(done_idx))),
                         "real milestones must be completed in order (no gaps)")

    def test_15_plan_all_stubs_remain_done(self):
        for m in ALL_MILESTONES:
            self.assertTrue(self.statuses.get((m, "stub"), False),
                            f"PLAN.md must keep {m} -- stub as [x]")

    def test_16_arch_m2_real_entry_present(self):
        self.assertIn("**M2 -- real:**", self.wdrozenie,
                      "ARCH must list the M2 -- real entry")
        self.assertIn("uziemion", self.wdrozenie,
                      "ARCH M2 -- real entry must say the section is grounded")
        for marker in ("Czynny", "2024-10-08", "Art. 96 ust. 9h", "isValid: true"):
            self.assertIn(marker, self.wdrozenie,
                          f"ARCH M2 -- real entry must record the confirmed field: {marker}")

    def test_17_arch_remaining_work_matches_pending_reals(self):
        pending = _pending_reals(self.statuses)
        if pending:
            self.assertIn("Pass 2 (REAL) w toku", self.wdrozenie,
                          "ARCH must state pass 2 (REAL) is in progress")
            remaining = " → ".join(pending)
            self.assertIn(remaining, self.wdrozenie,
                          f"ARCH remaining work must be {remaining} (derived from PLAN.md)")
        else:
            self.assertIn("Pass 2 (REAL) zakończon", self.wdrozenie,
                          "ARCH must declare pass 2 (REAL) complete once all reals are done")
            self.assertNotIn("Pass 2 (REAL) w toku", self.wdrozenie,
                             "ARCH must not claim pass 2 is in progress when all reals are done")


if __name__ == "__main__":
    unittest.main(verbosity=2)
