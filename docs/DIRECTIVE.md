# Quality directive (the codebase must conform to these rules)

Research (OSINT) project — the "code" is the single Polish deliverable
`raport/KR-OFFICE-OSINT.md` plus the test suite that guards it. Quality here means
honesty, internal consistency and cleanliness. Whether the goal's requirements are met
is the auditor's job, not this rulebook's.

## Honesty — zero fabrication
- Every factual claim is either sourced (URL + data dostępu) or flagged inline with one
  of `(do weryfikacji)` / `(założenie)` / `(brak danych publicznych)`. Never invent
  facts, figures, names or sources; when data is missing, say so — "brak danych" is a
  limitation, not a negative finding.
- Access dates are stamped only for sources actually opened, and never later than the
  real system date. Time windows (e.g. "ostatnie 12 miesięcy") are computed from that
  same date.

## No scaffolding, no placeholders
- No `TODO`/`TBD`/`lorem`/`placeholder`/`fixme` markers and no `[WSTAW …]` leftovers —
  doubts are written out inline, never left as placeholders.
- No debug prints, commented-out code blocks, or scratch notes.

## One source of truth, consistent cross-references
- Each fact has one owner in the report; when it is cross-referenced (M1↔M5,
  sekcja↔"Podsumowanie tabelaryczne", PLAN↔ARCHITECTURE), all mentions are updated in the
  same change so nothing drifts.
- Risk ratings use only Niskie/Średnie/Wysokie and must match between a section and its
  "Podsumowanie tabelaryczne" row; "Czerwone Flagi" lists only real signals and says
  "nie stwierdzono" when none exist.
- Findings are bound to NIP 7011222044 / KRS 0001126380, never to a bare company name.

## Sourcing discipline
- Prefer primary/official sources (KRS, Biała Lista API MF, VIES, KRZ/MSiG) over
  mirrors (rejestr.io, aleo.com, krs-pobierz.pl); paywalled registers
  (KRD/ERIF/InfoMonitor) are an explicit limitation, never guessed.

## Tests and code hygiene
- Tests assert real, specific behavior — no vacuous/always-true tests.
- No dead/unreachable code, unused imports/symbols, or duplicated logic; one job is done
  one way. Test files are intentionally self-contained (one per milestone, runnable
  standalone), so a small local parsing helper may repeat there rather than introduce a
  shared module.
- Names and messages tell the truth (no lying labels).
- Tests stay green; a change that breaks tests is reverted, not patched over.
