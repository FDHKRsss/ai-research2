# ARCHITEKTURA

## Cel dokumentu

Opisuje projekt badawczy (OSINT) — NIE oprogramowanie. „Architektura" to tu projekt struktury raportu,
wybór źródeł i zasady rzetelności, żeby wynik był odporny na błędy (zła identyfikacja podmiotu, brak danych,
paywalle) i użyteczny decyzyjnie.

## Kluczowa decyzja: jeden plik, aktualizowany w miejscu

- **Deliverable:** `raport/KR-OFFICE-OSINT.md` — pojedynczy dokument Markdown w języku polskim.
- **Dlaczego jeden plik:** cel to raport wysyłalny/cytaowalny jako całość; wiele plików zwiększa ryzyko
  niespójności i utrudnia „crash-safe" aktualizację. Plik jest tworzony NA POCZĄTKU i tylko uzupełniany
  w miejscu (write_file trwale zapisuje na dysk), więc nawet przy przerwaniu runu na dysku jest kompletna
  robocza wersja.
- **Dwie przepustki na tym samym pliku:** DRAFT (kompletny, z jawnymi wątpliwościami) → REAL (uziemienie
  źródłami, doprecyzowanie). Nie restartujemy pliku w drugiej przepustce.

## Struktura raportu (kontrakt)

1. **Metryka** — badany podmiot, identyfikatory (KRS/NIP/REGON), adres, data analizy, zakres i metoda.
2. **Podsumowanie tabelaryczne** — `Sekcja | Znaleziska | Ocena ryzyka: Niskie/Średnie/Wysokie` (wymóg formatu).
3. **Sekcje szczegółowe** (po jednej na obszar):
   - Identyfikacja i metryka (M1)
   - Status prawny i podatkowy (M2)
   - Reputacja (M3)
   - Jakość usług i specjalizacja (M4)
   - Stabilność finansowa (M5)
4. **Czerwone Flagi** — wyłącznie realne niepokojące sygnały (np. liczne zmiany zarządu, brak kontaktu,
   negatywne wpisy w rejestrach); brak flag = jawny zapis „nie stwierdzono".
5. **Źródła** — każda pozycja: URL + data dostępu (≤ 2026-08-15) + co potwierdza.
6. **Metodologia i ograniczenia** — czego nie dało się zweryfikować i dlaczego (paywall, brak danych publicznych).

## Wybór źródeł (opcje i uzasadnienie)

| Obszar | Źródło pierwotne/urzędowe (preferowane) | Lustro / pomocnicze | Uzasadnienie |
|---|---|---|---|
| Rejestr sądowy | KRS — ekrs.ms.gov.pl (odpis aktualny/pełny) | rejestr.io, aleo.com, krs-pobierz.pl | urzędowy odpis jest źródłem prawdy; lustra do szybkiej lokalizacji i NIP/KRS |
| VAT | Biała Lista — podatki.gov.pl wyszukiwarka + API MF `wl-api.mf.gov.pl` (po NIP) | — | jedyny autorytatywny wykaz czynnych podatników VAT |
| VAT-UE | VIES — ec.europa.eu/taxation_customs/vies | — | potwierdzenie statusu dla kontrahentów unijnych |
| Dłużnicy | Krajowy Rejestr Zadłużonych (KRZ), MSiG (ogłoszenia) | KRD, ERIF, BIG InfoMonitor | KRZ/MSiG publiczne i bezpłatne; komercyjne BIG wymagają logowania/opłat → jawne ograniczenie |
| Opinie | Google Maps, GoWork, Oferteo, Facebook (profil firmy) | aleo.com „Opinie" | wymagane przez cel; rejestrujemy datę, ocenę i merytorykę, nie fabrykujemy treści |

## Zasady rzetelności (odporność na typowe błędy)

- **Dezambiguacja podmiotu:** wiele firm może nazywać się podobnie do „KR Office". Każde ustalenie wiążemy z
  NIP `7011222044` / KRS `0001126380`, nie z samą nazwą. To eliminuje pomylenie z innymi biurami.
- **Brak danych ≠ dane negatywne:** młoda spółka (rejestracja 2024-09-11) może nie mieć jeszcze sprawozdań
  finansowych ani opinii — zapisujemy to jako fakt/ograniczenie, a nie domysł.
- **Paywall/logowanie:** rejestry BIG (KRD/ERIF/InfoMonitor) bez dostępu = jawne ograniczenie, nie zgadujemy.
- **Daty:** priorytet dla opinii z ostatnich 12 miesięcy (okno od 2025-08-15 do 2026-08-15); opinie starsze
  oznaczamy datą. Dostęp do źródeł datujemy dniem faktycznego otwarcia, nigdy później niż 2026-08-15.
- **Wątpliwości inline:** `(do weryfikacji)`, `(założenie)`, `(brak danych publicznych)` — żadnych „TODO".
- **OC biura:** jeśli znajdziemy wzmiankę o ubezpieczeniu OC (strona/www/ogłoszenie), odnotowujemy ją w M4;
  brak wzmianki = „nie znaleziono informacji o OC", NIE wymyślamy zakresu/limitu.

## Ocena ryzyka (spójna skala)

- **Niskie** — dane urzędowe w porządku, brak sygnałów negatywnych, historia/merytoryka pozytywna.
- **Średnie** — niepełne dane (np. brak opinii/sprawozdań z powodu młodego wieku), pojedyncze zastrzeżenia,
  dane do potwierdzenia.
- **Wysokie** — negatywne wpisy w rejestrach, brak czynnego VAT, wzorzec negatywnych opinii, sprzeczności.
Każda ocena ma jawne uzasadnienie powiązane ze znaleziskami.

## Tryby awarii i sposób radzenia sobie

| Awaria | Objawy | Reakcja |
|---|---|---|
| Pomyłka podmiotu | trafiamy na inne „KR Office" | weryfikacja wyłącznie przez NIP/KRS; odrzucenie niespójnych adresów |
| Brak profilu w rejestrze/opinii | 0 wyników | zapis „brak publicznych danych" + ocena ryzyka Średnie, nie zgadywanie |
| Paywall (BIG) | wymagane logowanie | ograniczenie jawne w sekcji „Metodologia i ograniczenia" |
| Lustro nieaktualne | data aktualizacji starsza od stanu urzędowego | porównanie z KRS/API MF; urzędowe wygrywa |
| Sprzeczne dane (np. udziałowcy) | liczba udziałów ≠ kapitał | rozstrzygnięcie na pełnym odpisie KRS; do czasu — jawne oznaczenie |

## Co „będzie w kodzie" (tu: w dokumentach)

W tym projekcie nie ma kodu. Wytwarzane pliki:
- `raport/KR-OFFICE-OSINT.md` — właściwy deliverable (wszystkie sekcje M1–M6).
- `docs/PLAN.md` — cel + milestones (stub/real) + status.
- `docs/ARCHITECTURE.md` — niniejszy projekt i decyzje.
- `docs/CONTEXT.md` — trwałe dyrektywy (nie zmieniać treści celu; tylko ewentualnie doprecyzować esencję).

## Stan wdrożenia (pass 1 — DRAFT/stub zakończony; pass 2 — REAL zakończony)

- **M1 -- stub:** gotowy i przetestowany (11 testów zielonych: `python -m unittest tests.test_m1_stub -v`).
  W `raport/KR-OFFICE-OSINT.md` obecne i kompletne: metryka dokumentu, podsumowanie tabelaryczne (wiersz M1),
  sekcja M1 (dane rejestrowe, zarząd/udziałowiec, analiza spójności, ocena ryzyka), Czerwone Flagi, Źródła,
  Metodologia i ograniczenia. Dane mają status `(do weryfikacji)`; rozbieżność udziałów vs kapitał jawnie
  oznaczona.
- **M2 -- stub:** gotowy i przetestowany (16 testów zielonych: `python -m unittest tests.test_m2_stub -v`).
  W `raport/KR-OFFICE-OSINT.md` dopisana sekcja M2 (Status prawny i podatkowy): Biała Lista VAT (po NIP
  7011222044, API MF `wl-api.mf.gov.pl`), VIES (`PL7011222044`), status KRS (aktywny + upadłość/restrukturyzacja/
  likwidacja), publiczne rejestry dłużników (KRZ, MSiG) oraz komercyjne BIG (KRD/ERIF/InfoMonitor) z jawnym
  ograniczeniem `(brak danych publicznych)`. Wszystko oznaczone `(do weryfikacji)`; brak sfabrykowanego
  potwierdzonego statusu; ocena ryzyka M2 = Średnie, spójna między sekcją a podsumowaniem. Dodany wiersz M2
  w podsumowaniu oraz wpisy w Czerwonych Flagach i Źródłach.
- **M3 -- stub:** gotowy i przetestowany (15 testów zielonych: `python -m unittest tests.test_m3_stub -v`).
  W `raport/KR-OFFICE-OSINT.md` dopisana sekcja M3 (Reputacja): opinie z czterech wymaganych platform
  (Google Maps, GoWork, Oferteo, Facebook), merytoryka/oceny/daty/liczba opinii, jawne okno priorytetowe
  ostatnich 12 miesięcy (2025-08-15 → 2026-08-15), dezambiguacja przez NIP/KRS. Wszystko oznaczone
  `(do weryfikacji)` i bez sfabrykowanych metryk opinii; ocena ryzyka M3 = Średnie, spójna między sekcją
  a podsumowaniem. Dodany wiersz M3 w podsumowaniu oraz wpisy w Czerwonych Flagach i Źródłach.
- **M4 -- stub:** gotowy i przetestowany. W `raport/KR-OFFICE-OSINT.md` dopisana sekcja M4 (Jakość usług i specjalizacja): oferta i zakres usług, specjalizacja (IT/transport/inne), ubezpieczenie OC (jawny zapis „nie znaleziono informacji o OC" z braku otwarcia źródeł — bez wymyślania zakresu/limitu), certyfikaty i uprawnienia, doświadczenie kadry, kanały kontaktu; dezambiguacja przez NIP 7011222044 / KRS 0001126380. Wszystko oznaczone `(do weryfikacji)`; brak sfabrykowanej oferty/specjalizacji/OC; ocena ryzyka M4 = Średnie, spójna między sekcją a podsumowaniem. Dodany wiersz M4 w podsumowaniu oraz wpisy w Czerwonych Flagach, Źródłach i Metodologii.
- **M5 -- stub:** gotowy i przetestowany. W `raport/KR-OFFICE-OSINT.md` dopisana sekcja M5 (Stabilność finansowa): sprawozdania finansowe (KRS/MSiG), kapitał zakładowy (5 000 zł), wiek firmy (rejestracja 2024-09-11), historia zmian, powiązania osobowe/kapitałowe; dezambiguacja przez NIP 7011222044 / KRS 0001126380. Wszystko oznaczone `(do weryfikacji)`; brak sfabrykowanych wielkości finansowych (przychody/zysk/strata nie wymyślane); ocena ryzyka M5 = Średnie, spójna między sekcją a podsumowaniem. Dodany wiersz M5 w podsumowaniu oraz wpisy w Czerwonych Flagach, Źródłach i Metodologii.
- **M6 -- stub:** gotowy. W `raport/KR-OFFICE-OSINT.md` dopisana sekcja M6 (Synteza ryzyka): synteza
  ocen cząstkowych M1–M5, końcowa ocena ryzyka, rekomendacja (warunkowa na etapie DRAFT) oraz powiązanie
  z sekcjami „Czerwone Flagi", „Źródła" i „Metodologia i ograniczenia". Wszystko oznaczone
  `(do weryfikacji)`; brak sfabrykowanego potwierdzenia stanu faktycznego; ocena ryzyka M6 = Średnie,
  spójna między sekcją a podsumowaniem. Dodany wiersz M6 w podsumowaniu oraz wpisy w Czerwonych Flagach,
  Źródłach i Metodologii.
- **M1 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M1 (Identyfikacja i metryka)
  zweryfikowana w źródłach urzędowych: KRS (API MS — odpis aktualny i pełny, `api-krs.ms.gov.pl`) oraz
  Biała Lista VAT (API MF, `wl-api.mf.gov.pl`). Potwierdzone: nazwa, forma prawna (sp. z o.o.), KRS
  0001126380, NIP 7011222044, REGON 529621586, adres Stefana Batorego 18/108, 02-591 Warszawa, kapitał
  5 000 zł, rejestracja 2024-09-11, PKD 69.20.Z, prezes/wspólnik Katarzyna Pydynowska (91 udziałów =
  4 550 zł). Rozbieżność udziałów vs kapitał (brak 9 udziałów / 450 zł) potwierdzona w odpisie KRS
  („nie posiada całości udziałów") i pozostaje otwarta; dodatkowo odnotowany sygnał przywrócenia
  rejestracji VAT (Biała Lista: „Art. 96 ust. 9h", 2025-06-27) do analizy w M2. Ocena ryzyka M1 =
  Średnie, spójna między sekcją a podsumowaniem. Zaktualizowane w tym samym kroku: metryka dokumentu,
  wiersz M1 w podsumowaniu, Czerwone Flagi, Źródła (URL + data dostępu 2026-08-15) i Metodologia.
- **M2 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M2 (Status prawny i podatkowy)
  zweryfikowana w źródłach urzędowych: Biała Lista VAT (API MF — status „Czynny", data rejestracji jako
  podatnik VAT 2024-10-08, rachunek rozliczeniowy 52 1160 2202 0000 0006 3037 1440, pola przywrócenia
  „Art. 96 ust. 9h" / 2025-06-27), VIES (API KE — `isValid: true` dla PL7011222044), KRS (status aktywny,
  działy 4–6 puste — brak upadłości/restrukturyzacji/likwidacji) oraz MSiG (status „aktywna", 1 wpis
  rejestracyjny). KRZ — bezpośrednie zapytanie programowe nie wykonane (interaktywna wyszukiwarka);
  komercyjne BIG (KRD/ERIF/InfoMonitor) poza dostępem — jawne ograniczenia. Ocena ryzyka M2 = Średnie,
  spójna między sekcją a podsumowaniem. Zaktualizowane w tym samym kroku: metryka dokumentu, wiersz M2
  w podsumowaniu, Czerwone Flagi, Źródła (URL + data dostępu 2026-08-15) i Metodologia.
- **M3 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M3 (Reputacja) sprawdzona
  w portalach opinii (dostęp 2026-08-15): **0 opinii** na Google Maps, GoWork, Oferteo, Facebook oraz
  w lustrach (aleo.com, pkt.pl) — brak merytoryki, ocen i dat do analizy; dezambiguacja przez NIP 7011222044 /
  KRS 0001126380 (np. KR Group sp. z o.o. to inny podmiot). Brak opinii = ograniczenie danych (młody podmiot,
  rejestracja 2024-09-11), nie sygnał negatywny; ocena ryzyka M3 = Średnie, spójna między sekcją
  a podsumowaniem. Zaktualizowane w tym samym kroku: metryka dokumentu, wiersz M3 w podsumowaniu, Czerwone
  Flagi, Źródła (URL + data dostępu 2026-08-15) i Metodologia.
- **M4 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M4 (Jakość usług
  i specjalizacja) sprawdzona w profilach publicznych (dostęp 2026-08-15): oferta uziemiona (prowadzenie
  ksiąg rachunkowych spółek z o.o./akcyjnych, fundacji, stowarzyszeń + kompleksowa obsługa księgowo-kadrowa —
  Oferteo, pkt.pl; PKD 69.20.Z spójne z KRS), specjalizacja branżowa (IT/transport) nie potwierdzona (profil
  ogólny), znaleziona deklaracja OC („Firma ubezpieczona OC" w pkt.pl) bez szczegółów polisy, certyfikaty/
  doświadczenie kadry/telefon/www — jawne `(brak danych publicznych)`. Ocena ryzyka M4 = Średnie, spójna
  między sekcją a podsumowaniem. Zaktualizowane w tym samym kroku: metryka dokumentu, wiersz M4
  w podsumowaniu, Czerwone Flagi, Źródła (URL + data dostępu 2026-08-15) i Metodologia.
- **M5 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M5 (Stabilność finansowa)
  zweryfikowana w źródłach (dostęp 2026-08-15): **brak złożonych/ogłoszonych sprawozdań finansowych**
  (pierwszy rok obrotowy kończy się 31.12.2025 — KRS/API MS, dział 3; w MSiG wyłącznie 1 wpis rejestracyjny,
  brak ogłoszenia o sprawozdaniu), kapitał zakładowy 5 000 zł = minimum ustawowe (art. 154 § 1 k.s.h.),
  wiek firmy < 2 lata (rejestracja 2024-09-11), **historia zmian: brak zmian po rejestracji** (3 wpisy
  z 11.09.2024: rejestracja + NIP + REGON), powiązania osobowe/kapitałowe: Katarzyna Pydynowska (zarząd +
  wspólnik 91 udziałów = 4 550 zł, beneficjent rzeczywisty) — bez sfabrykowanych wielkości finansowych.
  Ocena ryzyka M5 = Średnie, spójna między sekcją a podsumowaniem. Zaktualizowane w tym samym kroku:
  metryka dokumentu, wiersz M5 w podsumowaniu, Czerwone Flagi, Źródła (URL + data dostępu 2026-08-15)
  i Metodologia.
- **M6 -- real:** gotowy i uziemiony. W `raport/KR-OFFICE-OSINT.md` sekcja M6 (Synteza ryzyka) uziemiona
  na zweryfikowanych ustaleniach M1–M5 (dostęp 2026-08-15): synteza ocen cząstkowych (M1–M5 = Średnie),
  końcowa ocena ryzyka **Średnie**, rekomendacja (finalna, nie warunkowa) oraz powiązanie z sekcjami
  „Czerwone Flagi", „Źródła" i „Metodologia i ograniczenia". Oba sygnały do obserwacji przeniesione
  (rozbieżność 91 udziałów = 4 550 zł vs kapitał 5 000 zł; przywrócenie VAT „Art. 96 ust. 9h" /
  2025-06-27). Zaktualizowane w tym samym kroku: metryka dokumentu, wiersz M6 w podsumowaniu,
  Czerwone Flagi, Źródła (URL + data dostępu 2026-08-15) i Metodologia.
- **Pass 1 (DRAFT/stub) zakończony** — kompletny dokument M1–M6 gotowy. **Pass 2 (REAL) zakończony:**
  uziemiono źródłami wszystkie sekcje **M1**–**M6** (dostęp 2026-08-15); dokument jest kompletny
  i gotowy do użycia decyzyjnego.
