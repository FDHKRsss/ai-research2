# PLAN

## Goal(s)

Północna gwiazda (north star) tego planu — jeden nadrzędny cel badawczy, z którego wynikają wszystkie kroki:

1. **Dostarczyć kompleksowy, osadzony w źródłach wywiad gospodarczy (OSINT) firmy KR Office sp. z o.o.
   (ul. Stefana Batorego 18 lok 108, 02-591 Warszawa)**, odpowiadający na pytanie o **ryzyko nawiązania
   współpracy** w trzech wymaganych obszarach:
   - **REPUTACJA** — opinie z Google Maps, GoWork, Oferteo, Facebook (merytoryka + daty, priorytet ostatnich 12 mies.),
   - **STATUS PRAWNY** — Biała Lista (czynny podatnik VAT) + publiczne rejestry dłużników + KRS,
   - **JAKOŚĆ USŁUG** — specjalizacja (np. obsługa spółek IT / transportowych), oferta, ubezpieczenie OC.
   Dodatkowo (wynika z OBJECTIVE) raport obejmuje **stabilność finansową** oraz końcową **ocenę ryzyka**
   (Niskie/Średnie/Wysokie) i sekcję **„Czerwone Flagi"**.

2. **Produkt końcowy to JEDEN dokument Markdown** (`raport/KR-OFFICE-OSINT.md`), w języku polskim, w formacie
   tabelarycznym `Sekcja | Znaleziska | Ocena ryzyka`, z sekcją „Czerwone Flagi", listą źródeł (URL + data
   dostępu) i sekcją metodologia/ograniczenia. Dokument musi być użyteczny samodzielnie na KAŻDYM etapie
   (crash-safe: tworzony wcześnie i aktualizowany w miejscu).

## Twarde fakty identyfikacyjne (kotwica — do potwierdzenia w rejestrze urzędowym)

Te identyfikatory odróżniają badany podmiot od firm o podobnej nazwie i są kluczem do rejestrów:

| Pole | Wartość (z wstępnego rozpoznania) | Do potwierdzenia w |
|---|---|---|
| Firma | KR OFFICE SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ | KRS |
| KRS | 0001126380 | ekrs.ms.gov.pl / rejestr.io |
| NIP | 7011222044 | Biała Lista (podatki.gov.pl / API MF) |
| REGON | 529621586 | rejestr REGON / KRS |
| Adres | ul. Stefana Batorego 18/108, 02-591 Warszawa | KRS |
| Forma prawna | sp. z o.o. (kapitał zakładowy 5 000 zł) | KRS |
| Data rejestracji | 2024-09-11 | KRS |
| PKD | 69.20.Z — działalność rachunkowo-księgowa; doradztwo podatkowe | KRS |
| Zarząd / udziałowiec | Katarzyna Pydynowska (prezes; 91 udziałów = 4 550 zł) | KRS (pełny odpis) |

Uwaga metodologiczna: liczba udziałów (91) vs kapitał 5 000 zł wskazuje na możliwy drugi pakiet udziałów —
do rozstrzygnięcia na podstawie pełnego odpisu KRS (M1 -- real).

## Tryb pracy: dwie przepustki nad TYM SAMYM plikiem

Projekt jest badawczy — nie budujemy oprogramowania. „Stub" i „real" tłumaczą się tak:

- **Pass 1 (STUB / DRAFT)** — napisać KOMPLETNĄ pierwszą wersję `raport/KR-OFFICE-OSINT.md`: wszystkie sekcje
  i pytania wypełnione w całości najlepszą dostępną wiedzą. Wątpliwości oznaczamy jawnie inline `(do
  weryfikacji)` / `(założenie)` / `(brak danych publicznych)`. ŻADNYCH placeholderów „TODO" — dokument ma być
  wysyłalny „as-is".
- **Pass 2 (REAL)** — zweryfikować i uziemić (ugruntować) KAŻDĄ sekcję w źródłach, doprecyzować/zweryfikować
  ten sam plik IN PLACE (nie restartować), dopisać URL + daty dostępu, usunąć wątpliwości lub zamienić je na
  jawne ograniczenia.

Weryfikacja („test") = czy dana sekcja jest UZIEMIONA (źródło albo jawne oznaczenie założenia), wewnętrznie
spójna, odpowiada na pytanie z celu i NIC nie jest zmyślone. PASS = sekcja poprawna; FAIL = błędna,
niepoparta źródłem lub poza celem.

## Milestones (cała funkcjonalność; każdy = stub + real)

- [x] **M1 -- Identyfikacja podmiotu i metryka** — potwierdzenie KRS/NIP/REGON, forma prawna, kapitał, zarząd,
      udziałowcy, data rejestracji, adres, PKD. (służy celowi: rozróżnienie podmiotu i podstawa dalszych rejestrów)
  - [x] M1 -- stub
  - [x] M1 -- real
- [x] **M2 -- Status prawny i podatkowy** — Biała Lista VAT (czynny podatnik VAT), VIES, status w KRS,
      publiczne rejestry dłużników: Krajowy Rejestr Zadłużonych (KRZ), MSiG; komercyjne (KRD/ERIF/BIG
      InfoMonitor) — z jawnym opisem ograniczeń dostępu. (służy celowi: status prawny)
  - [x] M2 -- stub
  - [x] M2 -- real
- [x] **M3 -- Reputacja** — opinie Google Maps, GoWork, Oferteo, Facebook; merytoryka, oceny, daty,
      priorytet ostatnich 12 mies.; liczba opinii. (służy celowi: reputacja)
  - [x] M3 -- stub
  - [x] M3 -- real
- [x] **M4 -- Jakość usług i specjalizacja** — oferta, specjalizacja (IT / transport / inne), PKD,
      ubezpieczenie OC biura, certyfikaty, doświadczenie kadry, kanały kontaktu. (służy celowi: jakość usług)
  - [x] M4 -- stub
  - [x] M4 -- real
- [ ] **M5 -- Stabilność finansowa** — sprawozdania finansowe (KRS/MSiG), kapitał zakładowy, wiek firmy,
      historia zmian, powiązania osobowe/kapitałowe. (służy celowi: stabilność finansowa z OBJECTIVE)
  - [x] M5 -- stub
  - [ ] M5 -- real
- [ ] **M6 -- Synteza ryzyka** — tabela podsumowująca `Sekcja | Znaleziska | Ocena ryzyka`, sekcja
      „Czerwone Flagi" (jeśli są niepokojące sygnały), rekomendacja, pełna lista źródeł z datami dostępu,
      metodologia i ograniczenia. (służy celowi: końcowa ocena ryzyka i użyteczność decyzyjna)
  - [x] M6 -- stub
  - [ ] M6 -- real

Kolejność: **Pass 1** — wszystkie `-- stub` (kompletny dokument od razu). **Pass 2** — wszystkie `-- real`
(uziemienie źródłami), M1 → M6.

## Zasady uziemienia i uczciwości (obowiązują przy każdym kroku)

- Każde twierdzenie faktograficzne ma źródło (URL + data dostępu) LUB jest jawnie oznaczone jako
  założenie/otwarte pytanie. Zero fabrykacji liczb, opinii i źródeł.
- Preferujemy źródła pierwotne/urzędowe: KRS (ekrs.ms.gov.pl), Biała Lista (podatki.gov.pl / API MF
  `wl-api.mf.gov.pl`), VIES (ec.europa.eu), KRZ/MSiG. Lustra (aleo.com, krs-pobierz.pl, rejestr.io) traktujemy
  jako pomocnicze i weryfikujemy w rejestrze urzędowym.
- Jeśli rejestr jest płatny/wymaga logowania (KRD, ERIF, BIG InfoMonitor) — zapisujemy to jako jawne
  ograniczenie, NIE zgadujemy zawartości.
- Data dostępu nigdy późniejsza niż 2026-08-15; nie podajemy daty dostępu dla źródeł, których nie otwarto.

## Human notes

_(brak na ten moment — sekcja aktualizowana, gdy człowiek dopisze uwagi w README)_
