# Patterns

_Reusable techniques that worked, so they are reused not rediscovered._

- Dolepiając kolejną sekcję milestona do jedynego wspólnego deliverable `raport/KR-OFFICE-OSINT.md`, poza testami nowego kroku uruchom też testy wcześniejszych kroków (np. `python -m unittest tests.test_m1_stub -v`) — potwierdzają one, że już zatwierdzony kontrakt nie został naruszony przy rozszerzaniu pliku.
- Pass 1 (stub): każdy milestone dostaje własny test `tests/test_mN_stub.py`, który sprawdza strukturę sekcji, pokrycie wymaganych wymiarów (np. 4 platformy opinii, jawne okno 12 mies., dezambiguacja przez NIP/KRS) oraz zero fabrykacji (deklaracja „nie otwierano źródeł", `(do weryfikacji)` przy każdym ustaleniu, spójność oceny ryzyka sekcja↔podsumowanie). Ten sam szablon przyda się dla M4–M6 i pass 2 (real).
- Po dopisaniu sekcji milestona do `raport/KR-OFFICE-OSINT.md` w TYM SAMYM kroku oznacz `[x]` checkbox w `docs/PLAN.md` i dopisz wpis w sekcji „Stan wdrożenia" `docs/ARCHITECTURE.md` — inaczej tracking zostaje w tyle i krytyk/audyt wyłapuje rozbieżność (zdarzyło się przy M3).
