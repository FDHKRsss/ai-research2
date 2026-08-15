# Failures

_Regressions: what broke, the proven root cause, and the fix._

- `tests/test_m5_tracking.py` (snapshot „M1–M5 = ostatnie ukończone stuby") pękł, gdy ukończono M6 -- stub: test zahardkodował bieżący stan trackingu zamiast wyprowadzać go z `docs/PLAN.md`. Przyczyna: założenie „ten krok jest ostatnim stubem" (powtórka błędu z M3/M4). Fix: testy trackingu pisać forward-compatible i wyprowadzać oczekiwany stan z PLAN — stosować do KAŻDEGO testu trackingu, nie tylko najnowszego.
- Ten sam wzorzec „snapshota postępu" dotyczy testów `-- real` (nie tylko trackingu), ale tu regresji nie było — testy real pisane są od razu forward-compatible: wcześniejsze testy (`tests/test_m1_real.py`, `tests/test_m2_real.py`) asertują tylko własne inwarianty + inwariant „reals w kolejności bez luk" i wyprowadzają zbiór DONE_REALS z `docs/PLAN.md` (nie wklejają go na sztywno). Snapshot „które reals są ukończone" ma JEDNEGO właściciela — test najnowszego ukończonego reala (np. `tests/test_m6_real.py` celowo hardkoduje `DONE_REALS = {M1..M6}`).
