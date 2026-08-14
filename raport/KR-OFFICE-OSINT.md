# Wywiad gospodarczy (OSINT) — KR Office sp. z o.o.

> **Status dokumentu:** WERSJA ROBOCZA — pass 1 (DRAFT / stub).
> Dokument powstaje sekwencyjnie (po jednym kroku milestona). Obecnie wypełniona i kompletna jest
> sekcja **M1 — Identyfikacja podmiotu i metryka**. Pozostałe sekcje (M2–M6) zostaną dopisane w kolejnych
> krokach pass 1, a w pass 2 (REAL) całość zostanie zweryfikowana i uziemiona źródłami (URL + data dostępu).

---

## Metryka dokumentu

| Pole | Wartość |
|---|---|
| Badany podmiot | KR OFFICE spółka z ograniczoną odpowiedzialnością (dalej: „KR Office sp. z o.o.") |
| Cel analizy | Ocena ryzyka nawiązania współpracy — reputacja, status prawny, jakość usług, stabilność finansowa |
| Data analizy | 2026-08-15 |
| Metoda | OSINT — rejestry urzędowe (KRS, Biała Lista/VAT, VIES, KRZ/MSiG) + opinie publiczne (Google Maps, GoWork, Oferteo, Facebook) |
| Status | DRAFT (stub) — dane identyfikacyjne z rozpoznania wstępnego, **do potwierdzenia** w rejestrze urzędowym (KRS) |

---

## Podsumowanie tabelaryczne

| Sekcja | Znaleziska | Ocena ryzyka |
|---|---|---|
| M1 — Identyfikacja i metryka | Podmiot zidentyfikowany wstępnie (KRS 0001126380, NIP 7011222044, REGON 529621586); forma prawna sp. z o.o., kapitał zakładowy 5 000 zł, data rejestracji 2024-09-11, PKD 69.20.Z; zarząd/udziałowiec: Katarzyna Pydynowska. Dane do potwierdzenia w KRS. | **Średnie** — dane wstępne (do weryfikacji), brak sprzeczności blokujących |

> Pozostałe wiersze (M2–M6) zostaną dopisane wraz z ukończeniem odpowiednich sekcji w pass 1.

---

## Sekcja M1 — Identyfikacja podmiotu i metryka

### 1.1. Dane rejestrowe (rozpoznanie wstępne)

Dane pochodzą z rozpoznania wstępnego i **wymagają potwierdzenia w rejestrze urzędowym KRS**
(odpis aktualny/pełny — ekrs.ms.gov.pl) oraz na Białej Liście (podatki.gov.pl / API MF). Do czasu
weryfikacji oznaczam je jako `(do weryfikacji)`.

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Pełna nazwa | KR OFFICE SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ | (do weryfikacji w KRS) |
| Forma prawna | spółka z ograniczoną odpowiedzialnością | (do weryfikacji w KRS) |
| KRS | 0001126380 | (do weryfikacji w KRS) |
| NIP | 7011222044 | (do weryfikacji na Białej Liście) |
| REGON | 529621586 | (do weryfikacji w REGON/KRS) |
| Adres siedziby | ul. Stefana Batorego 18 lok. 108, 02-591 Warszawa | (do weryfikacji w KRS) |
| Kapitał zakładowy | 5 000 zł | (do weryfikacji w KRS) |
| Data rejestracji | 2024-09-11 | (do weryfikacji w KRS) |
| PKD | 69.20.Z — działalność rachunkowo-księgowa; doradztwo podatkowe | (do weryfikacji w KRS) |

### 1.2. Zarząd i struktura właścicielska

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Zarząd | Katarzyna Pydynowska — prezes zarządu | (do weryfikacji w pełnym odpisie KRS) |
| Udziałowiec | Katarzyna Pydynowska — 91 udziałów o łącznej wartości 4 550 zł | (do weryfikacji w pełnym odpisie KRS) |

### 1.3. Analiza spójności identyfikatorów i uwagi metodologiczne

- **Dezambiguacja podmiotu:** w obrocie może występować wiele firm o nazwie zbliżonej do „KR Office".
  Wszystkie dalsze ustalenia (M2–M6) będą wiązane z identyfikatorami **NIP 7011222044 / KRS 0001126380**,
  a nie z samą nazwą — aby uniknąć pomylenia z innymi biurami rachunkowymi.
- **Niespójność do wyjaśnienia:** zadeklarowana liczba udziałów (91) o wartości 4 550 zł nie sumuje się do
  kapitału zakładowego 5 000 zł. Może to oznaczać istnienie **drugiego pakietu udziałów** (np. 9 udziałów
  innego wspólnika) albo błąd/niepełny odczyt danych. Kwestia ta wymaga rozstrzygnięcia na podstawie
  **pełnego odpisu KRS** (M1 — real) `(do weryfikacji)`.
- **Młody podmiot:** data rejestracji 2024-09-11 oznacza firmę działającą krócej niż 2 lata. Brak historii
  sprawozdawczej lub ograniczona liczba opinii nie jest sam w sobie sygnałem negatywnym, lecz **ograniczeniem
  dostępności danych** — będzie traktowany jako taki w sekcjach M2–M5 `(założenie metodologiczne)`.

### 1.4. Ocena ryzyka — M1

**Ocena: Średnie.** Identyfikatory i metryka są wewnętrznie spójne (adres, NIP, KRS, REGON z tego samego
rozpoznania) i typowe dla małej spółki księgowej, ale mają status **danych wstępnych** i wymagają
potwierdzenia w rejestrze urzędowym. Dodatkowo otwarta pozostaje kwestia liczby udziałów vs. kapitału
zakładowego, którą należy rozstrzygnąć w pass 2.

---

## Czerwone Flagi

- **Nie stwierdzono jednoznacznych czerwonych flag** na etapie M1.
- **Sygnał do obserwacji (nie flaga):** rozbieżność „91 udziałów = 4 550 zł" vs. „kapitał zakładowy 5 000 zł"
  — może wskazywać na drugiego wspólnika lub niepełny odczyt; do rozstrzygnięcia na pełnym odpisie KRS.

---

## Źródła

W pass 1 (stub) nie otwierano jeszcze źródeł — z tego powodu **nie podaję dat dostępu** (daty dostępu
zostaną dodane w pass 2 dla źródeł faktycznie otwartych). Planowane źródła do weryfikacji M1:

- KRS / e-KRS — ekrs.ms.gov.pl (odpis aktualny i pełny) — potwierdzenie nazwy, KRS, adresu, kapitału, zarządu, udziałowców, PKD.
- Biała Lista podatników VAT — podatki.gov.pl / API MF (`wl-api.mf.gov.pl`) — potwierdzenie NIP i statusu VAT (M2).
- Rejestr REGON — potwierdzenie REGON.

---

## Metodologia i ograniczenia

- **Metoda:** OSINT na źródłach publicznych i urzędowych; priorytet dla źródeł pierwotnych (KRS, Biała Lista,
  VIES, KRZ/MSiG); lustra (rejestr.io, aleo.com itp.) wyłącznie pomocniczo.
- **Ograniczenia (pass 1):** wszystkie dane M1 mają status rozpoznania wstępnego i nie zostały jeszcze
  potwierdzone w rejestrze urzędowym. Rejestry płatne lub wymagające logowania (np. komercyjne BIG) będą
  opisane jako jawne ograniczenie w sekcji M2/M5 — bez zgadywania ich zawartości.
- **Zasada „brak danych ≠ dane negatywne":** młody wiek spółki może oznaczać brak sprawozdań/opinii — będzie
  to odnotowywane jako ograniczenie, a nie domniemanie negatywne.
