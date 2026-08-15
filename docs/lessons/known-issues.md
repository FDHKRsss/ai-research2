# Known issues

_Recurring walls/gotchas and how to get past them. One bullet each._

- Testy/audyty „brak TODO": naiwne szukanie podciągu `todo` daje fałszywy traf na polskich słowach (np. „metodologia") — dopasowuj tylko samodzielne markery placeholderów (granice słowa / regex `\b[Tt][Oo][Dd][Oo]\b`), nie goły podciąg.
- Daty: graniczne okna i daty dostępu wyliczaj z faktycznej daty systemowej (tu 2026-08-15) i sprawdzaj spójność między PLAN/ARCHITECTURE/raportem — ręcznie wpisane daty potrafią się rozjechać (zdarzyło się 2026-08-14 zamiast 2026-08-15).
- Wpisy w samym `docs/lessons/*` (zwłaszcza `failures.md`) też bywają błędne — agent zapisał „regresję" real-testów, której kod nie wykazuje (wyłapał to krytyk, tester dodał test krzyżujący treść lekcji z kodem). Zanim zapiszesz lekcję o testach/kodzie, zweryfikuj ją w samym kodzie; nie ufaj prozie ani podsumowaniom agentów.
