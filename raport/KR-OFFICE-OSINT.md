# Wywiad gospodarczy (OSINT) — KR Office sp. z o.o.

> **Status dokumentu:** WERSJA ROBOCZA — pass 1 (DRAFT / stub).
> Dokument powstaje sekwencyjnie (po jednym kroku milestona). Obecnie wypełnione i kompletne są sekcje:
> **M1 — Identyfikacja podmiotu i metryka**, **M2 — Status prawny i podatkowy**,
> **M3 — Reputacja**, **M4 — Jakość usług i specjalizacja** oraz **M5 — Stabilność finansowa**.
> Pozostała sekcja (M6 — Synteza ryzyka) zostanie dopisana w kolejnym kroku pass 1, a w pass 2 (REAL)
> całość zostanie zweryfikowana i uziemiona źródłami (URL + data dostępu).

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
| M2 — Status prawny i podatkowy | Biała Lista VAT, VIES, status KRS oraz rejestry dłużników (KRZ/MSiG) do weryfikacji w źródłach urzędowych; komercyjne BIG (KRD/ERIF/InfoMonitor) bez dostępu (jawne ograniczenie). Brak stwierdzonych negatywnych wpisów na etapie DRAFT. | **Średnie** — dane niezweryfikowane (do weryfikacji) i ograniczenie dostępu do BIG |
| M3 — Reputacja | Opinie z Google Maps, GoWork, Oferteo i Facebooka do zebrania i weryfikacji; merytoryka, oceny i daty (priorytet ostatnich 12 mies.) nieznane na etapie DRAFT. Brak sfabrykowanych ocen ani treści opinii. | **Średnie** — dane nie zebrane (do weryfikacji), brak potwierdzonej reputacji |
| M4 — Jakość usług i specjalizacja | Oferta, specjalizacja (IT/transport/inne), certyfikaty, doświadczenie kadry, kanały kontaktu oraz OC biura do ustalenia i weryfikacji; PKD 69.20.Z (powiązane z M1). Nieznane na etapie DRAFT. | **Średnie** — dane nie zweryfikowane (do weryfikacji), wzmianka o OC nie znaleziona z braku otwarcia źródeł |
| M5 — Stabilność finansowa | Sprawozdania finansowe (KRS/MSiG), kapitał zakładowy, wiek firmy, historia zmian oraz powiązania osobowe/kapitałowe do ustalenia i weryfikacji. Nieznane na etapie DRAFT; brak sfabrykowanych wielkości finansowych. | **Średnie** — dane nie zweryfikowane (do weryfikacji); młody wiek i minimalny kapitał jako ograniczenie danych |

> Pozostałe wiersze (M6) zostaną dopisane wraz z ukończeniem odpowiednich sekcji w pass 1.

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

## Sekcja M2 — Status prawny i podatkowy

### 2.1. Cel i zakres

Sekcja odpowiada na pytanie o **status prawny i podatkowy** badanego podmiotu — w szczególności, czy
KR Office sp. z o.o. jest **czynnym podatnikiem VAT** (Biała Lista), czy figuruje w **VIES** (VAT-UE), jaki
ma **status w KRS** oraz czy nie widnieje w **publicznych rejestrach dłużników** (KRZ, MSiG). Komercyjne
biura informacji gospodarczej (KRD, ERIF, BIG InfoMonitor) są ujęte jako osobny punkt z jawnym opisem
ograniczeń dostępu.

> **Uwaga (pass 1 — DRAFT/stub):** na tym etapie **nie otwierano jeszcze źródeł urzędowych** — wszystkie
> ustalenia M2 mają status `(do weryfikacji)` albo są jawnie opisane jako `(brak danych publicznych)` /
> `(założenie)`. Uziemienie źródłami (URL + data dostępu) nastąpi w pass 2 (M2 — real).

### 2.2. Biała Lista podatników VAT

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| NIP sprawdzany | 7011222044 | kotwica identyfikacyjna |
| Status „czynny podatnik VAT" | do potwierdzenia | (do weryfikacji na Białej Liście — podatki.gov.pl / API MF `wl-api.mf.gov.pl`) |
| Data rejestracji jako podatnik VAT | do potwierdzenia | (do weryfikacji na Białej Liście) |
| Rachunek rozliczeniowy (wykaz rachunków) | do potwierdzenia | (do weryfikacji na Białej Liście) |

- **Co sprawdzamy i dlaczego:** wpis na Białej Liście potwierdza, że kontrahent jest zarejestrowany jako
  czynny podatnik VAT. Dla klienta biura rachunkowego to istotny sygnał, że podmiot formalnie funkcjonuje
  w obrocie gospodarczym i że faktury wystawiane przez biuro mają status dokumentów od podatnika VAT.
- **Status na etapie DRAFT:** brak potwierdzenia — nie formułuję twierdzenia o statusie VAT, dopóki nie
  wykonam zapytania do API MF / wyszukiwarki Białej Listy `(do weryfikacji)`.

### 2.3. VIES (VAT-UE)

- **Sprawdzany identyfikator:** PL7011222044 (NIP z prefiksem PL).
- **Status VAT-UE:** do potwierdzenia w VIES (`ec.europa.eu/taxation_customs/vies`) `(do weryfikacji)`.
- **Uwaga:** rejestracja VAT-UE jest potrzebna głównie przy transakcjach wewnątrzwspólnotowych. Brak wpisu
  w VIES u lokalnego biura rachunkowego nie jest sam w sobie sygnałem negatywnym — będzie interpretowany
  w kontekście profilu działalności `(założenie metodologiczne)`.

### 2.4. Status w KRS

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Numer KRS | 0001126380 | kotwica identyfikacyjna |
| Rejestr | Rejestr Przedsiębiorców KRS | (do weryfikacji w odpisie aktualnym — ekrs.ms.gov.pl / PRS) |
| Status podmiotu | aktywny (działający) — do potwierdzenia | (do weryfikacji w KRS) |
| Postępowanie upadłościowe / restrukturyzacyjne / likwidacja | brak informacji — do potwierdzenia | (do weryfikacji w dziale odpisu KRS / KRZ) |

- **Co sprawdzamy:** w KRS szukamy potwierdzenia, że podmiot jest wpisany i **aktywny**, oraz czy w dziale
  dotyczącym postępowań nie ma wzmianek o upadłości, restrukturyzacji lub likwidacji. To kluczowy „twardy"
  wskaźnik statusu prawnego `(do weryfikacji)`.

### 2.5. Publiczne rejestry dłużników

| Rejestr | Zakres | Status na etapie DRAFT |
|---|---|---|
| Krajowy Rejestr Zadłużonych (KRZ) — krz.ms.gov.pl | podmioty, wobec których toczy się postępowanie upadłościowe/restrukturyzacyjne, zakaz prowadzenia działalności | do sprawdzenia po NIP/KRS `(do weryfikacji)` |
| Monitor Sądowy i Gospodarczy (MSiG) — imsig.pl | ogłoszenia wymagane (m.in. o upadłości, restrukturyzacji, zmianach w KRS) | do sprawdzenia po KRS/NIP `(do weryfikacji)` |
| KRD, ERIF, BIG InfoMonitor (komercyjne) | bazy dłużników komercyjnych | **brak dostępu bez logowania/opłaty — jawne ograniczenie** `(brak danych publicznych)` |

- **KRZ i MSiG** są publiczne i bezpłatne — zostaną sprawdzone w pass 2 (M2 — real). Na etapie DRAFT nie
  formułuję twierdzeń o wpisach; zapis „brak wpisów" będzie możliwy dopiero po faktycznym zapytaniu.
- **Komercyjne BIG (KRD/ERIF/InfoMonitor):** wymagają konta i/lub opłaty. Zgodnie z zasadą uczciwości
  **nie zgaduję** ich zawartości — to jawne ograniczenie raportu. Wynik negatywny w rejestrach publicznych
  nie zastępuje pełnej weryfikacji w BIG `(założenie metodologiczne)`.

### 2.6. Analiza i ocena ryzyka — M2

**Ocena: Średnie.** Na etapie DRAFT brak jest potwierdzonych danych urzędowych o statusie VAT, VIES, KRS
i rejestrach dłużników (wszystko `(do weryfikacji)`), a komercyjne BIG pozostają poza zasięgiem (jawne
ograniczenie). Nie odnotowano żadnego negatywnego wpisu ani sprzeczności — brak potwierdzenia wynika
z nieotwarcia źródeł, a nie ze stwierdzonego problemu. Po uziemieniu w pass 2 ocena może zostać obniżona do
**Niskiej** (jeśli Biała Lista potwierdzi czynny VAT, a KRZ/MSiG nie wykażą wpisów) lub podniesiona do
**Wysokiej** (w razie negatywnych wpisów).

---

## Sekcja M3 — Reputacja

### 3.1. Cel i zakres

Sekcja odpowiada na pytanie o **reputację** badanego podmiotu w oczach klientów (i — o ile występuje —
pracowników). Zbieram opinie z czterech wymaganych źródeł: **Google Maps, GoWork, Oferteo, Facebook**.
Analizuję:

- **merytorykę** — co konkretnie klienci chwalą lub krytykują (np. terminowość, kontakt, znajomość
  przepisów, ceny),
- **oceny** — średnią ocenę i rozkład (ile opinii pozytywnych/neutralnych/negatywnych),
- **daty** — priorytet dla opinii z **ostatnich 12 miesięcy** (okno: 2025-08-15 → 2026-08-15); opinie
  starsze odnotowuję z ich datą, ale nie traktuję jako miarodajne dla bieżącej jakości,
- **liczbę opinii** — mała liczba opinii u młodej firmy to ograniczenie, a nie automatyczny sygnał
  negatywny.

**Dezambiguacja podmiotu:** przy wyszukiwaniu opinii kieruję się **adresem ul. Stefana Batorego 18 lok. 108,
02-591 Warszawa** oraz identyfikatorami **NIP 7011222044 / KRS 0001126380**, a nie samą nazwą „KR Office"
— w obrocie może działać wiele biur o zbliżonej nazwie `(założenie metodologiczne)`.

> **Uwaga (pass 1 — DRAFT/stub):** na tym etapie **nie otwierano jeszcze źródeł opinii** — wszystkie
> ustalenia M3 mają status `(do weryfikacji)` albo są opisane jako `(brak danych publicznych)`. **Nie
> fabrykuję** żadnych ocen, liczby opinii ani treści recenzji.

### 3.2. Google Maps

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Profil / wizytówka firmy | do ustalenia (wyszukiwanie po nazwie + adresie ul. Stefana Batorego 18, 02-591 Warszawa) | (do weryfikacji na google.com/maps) |
| Liczba opinii | nieznana na etapie DRAFT | (do weryfikacji) |
| Średnia ocena (gwiazdki) | nieznana na etapie DRAFT | (do weryfikacji) |
| Rozkład ocen | nieznany na etapie DRAFT | (do weryfikacji) |
| Merytoryka (powtarzające się atuty/zastrzeżenia) | nieznana na etapie DRAFT | (do weryfikacji) |
| Daty opinii (priorytet ostatnich 12 mies.) | do ustalenia | (do weryfikacji) |

- **Czego szukam:** liczby i dat opinii oraz treści (merytoryki). Opinie z ostatnich 12 miesięcy (2025-08-15 →
  2026-08-15) mają pierwszeństwo; starsze odnotowuję z datą. Wzorzec powtarzających się zarzutów (np. błędy
  księgowe, brak kontaktu) byłby czerwoną flagą — na etapie DRAFT żadnego nie stwierdzam `(do weryfikacji)`.

### 3.3. GoWork

- **Charakter źródła:** GoWork to portal z opiniami o **pracodawcach** (głównie z perspektywy pracowników).
  Dla małego biura rachunkowego wpis może **nie istnieć** — brak wpisu traktuję jako ograniczenie danych,
  a nie jako informację negatywną `(założenie metodologiczne)`.
- **Status na etapie DRAFT:** do sprawdzenia, czy podmiot ma profil/opinie na GoWork `(do weryfikacji)`.
  Nie formułuję żadnych twierdzeń o ocenach ani treści, dopóki nie wykonam wyszukiwania.

### 3.4. Oferteo

- **Charakter źródła:** Oferteo to portal z opiniami **klientów o firmach usługowych** (w tym o biurach
  rachunkowych). To źródło o najwyższej wartości dla reputacji klienckiej — sprawdzam liczbę opinii, ocenę
  oraz merytorykę (terminowość, komunikacja, ceny) `(do weryfikacji)`.
- **Status na etapie DRAFT:** do sprawdzenia, czy biuro ma profil na Oferteo i jakie ma opinie. **Nie
  fabrykuję** ocen ani treści `(do weryfikacji)`.

### 3.5. Facebook

- **Charakter źródła:** profil firmowy (fanpage) — sprawdzam istnienie profilu, aktywność (daty postów),
  obecność recenzji/opinii oraz ocenę. Część małych biur nie prowadzi aktywnie fanpage'a; brak profilu lub
  niska aktywność to ograniczenie, nie sygnał negatywny `(założenie metodologiczne)`.
- **Status na etapie DRAFT:** do sprawdzenia, czy podmiot ma fanpage i recenzje `(do weryfikacji)`. Nie
  formułuję twierdzeń o treści postów ani recenzji.

### 3.6. Analiza i ocena ryzyka — M3

**Ocena: Średnie.** Na etapie DRAFT reputacja jest **nieznana** — żadne z czterech źródeł (Google Maps,
GoWork, Oferteo, Facebook) nie zostało jeszcze otwarte, a oceny, liczby i treści opinii mają status
`(do weryfikacji)`. Brak danych wynika z **niezebrania opinii**, a nie ze stwierdzonego problemu; nie
odnotowano żadnego negatywnego wzorca. Po uziemieniu w pass 2 ocena może zostać obniżona do **Niskiej**
(jeśli opinie z ostatnich 12 miesięcy będą pozytywne i merytoryczne) lub podniesiona do **Wysokiej**
(w razie powtarzających się negatywnych opinii, np. o błędach księgowych lub braku kontaktu).

---

## Sekcja M4 — Jakość usług i specjalizacja

### 4.1. Cel i zakres

Sekcja odpowiada na pytanie o **jakość usług** badanego biura rachunkowego: co oferuje, w czym się
**specjalizuje**, czy posiada **ubezpieczenie OC**, jakie ma **certyfikaty** i **doświadczenie kadry** oraz
jakimi **kanałami kontaktu** dysponuje. Uzupełnia obszar „JAKOŚĆ USŁUG" z celu analizy i pomaga ocenić, czy
biuro jest w stanie obsłużyć konkretny profil klienta (np. spółki IT / transportowe).

**Dezambiguacja podmiotu:** ustalenia M4 dotyczą wyłącznie KR Office sp. z o.o. identyfikowanej przez
**NIP 7011222044 / KRS 0001126380**, ul. Stefana Batorego 18 lok. 108, 02-591 Warszawa — nie innych firm
o zbliżonej nazwie `(założenie metodologiczne)`.

> **Uwaga (pass 1 — DRAFT/stub):** na tym etapie **nie otwierano** strony WWW biura, opisów oferty,
> ogłoszeń ani profili branżowych — wszystkie ustalenia M4 mają status `(do weryfikacji)` albo
> `(brak danych publicznych)`. **Nie fabrykuję** zakresu usług, specjalizacji, certyfikatów ani
> szczegółów polisy OC.

### 4.2. Oferta i zakres usług

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Zakres oferty | do ustalenia (księgowość pełna/uproszczona, kadry-płace, rozliczenia ZUS/US, doradztwo podatkowe) | (do weryfikacji na stronie WWW / w opisach oferty) |
| Profil klienta | do ustalenia (JDG / spółki kapitałowe / spółki IT / transportowe) | (do weryfikacji) |
| Cennik / model rozliczeń | nieznany na etapie DRAFT | (do weryfikacji) |
| PKD działalności | 69.20.Z — działalność rachunkowo-księgowa; doradztwo podatkowe | (do weryfikacji w KRS — powiązane z M1) |

- **Czego szukam:** publicznego opisu oferty (np. „prowadzenie ksiąg rachunkowych", „obsługa
  kadrowo-płacowa", „rozliczenia ZUS/US") oraz profilu obsługiwanych klientów. Zakres oferty weryfikuję
  w pass 2 na podstawie strony WWW i opisów usług `(do weryfikacji)`.

### 4.3. Specjalizacja (IT / transport / inne)

- **Szukana informacja:** czy biuro deklaruje specjalizację branżową — np. obsługa spółek **IT**,
  **transportowych**, e-commerce, budowlanych lub inną niszę (wymóg celu: „Poszukaj informacji
  o specjalizacji, np. obsługa spółek IT / transportowych").
- **Status na etapie DRAFT:** specjalizacja **nieznana** — nie potwierdzono ani nie wykluczono żadnej
  branży `(do weryfikacji)`. Nie formułuję twierdzenia typu „biuro specjalizuje się w IT/transporcie",
  dopóki nie znajdę potwierdzenia w materiałach własnych biura `(do weryfikacji)`.
- **Interpretacja:** brak deklarowanej specjalizacji nie jest sygnałem negatywnym — wiele małych biur
  obsługuje klientów wielobranżowo `(założenie metodologiczne)`.

### 4.4. Ubezpieczenie OC biura

- **Wymóg celu:** jeśli pojawi się wzmianka o ubezpieczeniu OC biura rachunkowego, należy ją uwzględnić
  w raporcie.
- **Status na etapie DRAFT:** **nie znaleziono informacji o OC** — nie otwierano strony WWW, regulaminów
  ani ogłoszeń, w których taka wzmianka mogłaby wystąpić `(do weryfikacji)`. Brak wzmianki **nie jest
  równoznaczny** z brakiem polisy — to wyłącznie brak danych na etapie DRAFT `(założenie metodologiczne)`.
- **Czego NIE robię:** nie wymyślam zakresu ani limitu (sumy gwarancyjnej) polisy OC. Takie dane będzie
  można podać dopiero po ich faktycznym znalezieniu w pass 2 `(do weryfikacji)`.

### 4.5. Certyfikaty i uprawnienia

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Certyfikat księgowy / licencja doradcy podatkowego | do ustalenia | (do weryfikacji — np. w rejestrach branżowych / materiałach biura) |
| Członkostwo w organizacjach branżowych | do ustalenia | (do weryfikacji) |
| Inne uprawnienia (np. pełnomocnictwo, biegły rewident) | do ustalenia | (do weryfikacji) |

- **Czego szukam:** publicznych potwierdzeń uprawnień (np. wpis na listę doradców podatkowych, certyfikat
  księgowy MF, członkostwo w Stowarzyszeniu Księgowych w Polsce). Na etapie DRAFT **nie stwierdzam** żadnego
  certyfikatu `(do weryfikacji)`.

### 4.6. Doświadczenie kadry

- **Szukana informacja:** doświadczenie i wykształcenie osób zarządzających/księgowych (np. prezes
  Katarzyna Pydynowska) — staż w księgowości, uprawnienia, historia zatrudnienia.
- **Status na etapie DRAFT:** doświadczenie kadry **nieznane** — wymaga weryfikacji w materiałach biura,
  profilach zawodowych lub opisie firmy `(do weryfikacji)`. Młody wiek spółki (rejestracja 2024-09-11) nie
  przesądza o braku doświadczenia jej właścicieli — to odrębna kwestia do sprawdzenia
  `(założenie metodologiczne)`.

### 4.7. Kanały kontaktu

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Telefon | do ustalenia | (do weryfikacji) |
| E-mail | do ustalenia | (do weryfikacji) |
| Strona WWW | do ustalenia | (do weryfikacji) |
| Profil Facebook / inne social media | do ustalenia (powiązane z M3) | (do weryfikacji) |
| Adres stacjonarny | ul. Stefana Batorego 18 lok. 108, 02-591 Warszawa | (do weryfikacji w KRS) |

- **Czego szukam:** aktualnych, publicznie dostępnych kanałów kontaktu. Brak łatwo dostępnego kontaktu
  (np. brak telefonu/e-maila w źródłach publicznych) byłby odnotowany jako utrudnienie — na etapie DRAFT
  nie stwierdzam takiego braku, bo źródeł nie otwierano `(do weryfikacji)`.

### 4.8. Analiza i ocena ryzyka — M4

**Ocena: Średnie.** Na etapie DRAFT jakość usług jest **nieznana**: oferta, specjalizacja, certyfikaty,
doświadczenie kadry i kanały kontaktu mają status `(do weryfikacji)`, a wzmianka o OC **nie została
znaleziona** (z braku otwarcia źródeł). Brak danych wynika z nieprzeprowadzenia weryfikacji, a nie ze
stwierdzonego problemu; nie odnotowano żadnego sygnału negatywnego. Po uziemieniu w pass 2 ocena może zostać
obniżona do **Niskiej** (jeśli oferta i specjalizacja będą spójne z profilem klienta, potwierdzone i wystąpi
wzmianka o OC) lub podniesiona do **Wysokiej** (w razie rażąco niekompletnej oferty, braku kontaktu lub
sprzeczności).

---

## Sekcja M5 — Stabilność finansowa

### 5.1. Cel i zakres

Sekcja odpowiada na pytanie o **stabilność finansową** badanego podmiotu (wymóg OBJECTIVE, uzupełnienie
obszaru „stabilność finansowa"). Analizuję:

- **sprawozdania finansowe** składane do KRS i ogłaszane w MSiG (bilans, rachunek zysków i strat,
  ewentualna opinia biegłego),
- **kapitał zakładowy** i jego relację do minimalnych wymogów dla sp. z o.o.,
- **wiek firmy** (historia działalności od rejestracji),
- **historię zmian** (zmiany w KRS — zarząd, wspólnicy, siedziba, przedmiot działalności),
- **powiązania osobowe i kapitałowe** (wspólnicy, członkowie zarządu, podmioty powiązane).

**Dezambiguacja podmiotu:** ustalenia M5 dotyczą wyłącznie KR Office sp. z o.o. identyfikowanej przez
**NIP 7011222044 / KRS 0001126380**, ul. Stefana Batorego 18 lok. 108, 02-591 Warszawa — nie innych firm
o zbliżonej nazwie `(założenie metodologiczne)`.

> **Uwaga (pass 1 — DRAFT/stub):** na tym etapie **nie otwierano** jeszcze rejestrów (KRS/MSiG) ani
> sprawozdań finansowych — wszystkie ustalenia M5 mają status `(do weryfikacji)` albo `(brak danych
> publicznych)`. **Nie fabrykuję** żadnych wielkości finansowych (przychody, koszty, zysk/strata, aktywa,
> zobowiązania).

### 5.2. Sprawozdania finansowe (KRS / MSiG)

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Sprawozdanie finansowe za ostatni rok obrotowy | do ustalenia | (do weryfikacji w KRS — ekrs.ms.gov.pl / Repozytorium Dokumentów Finansowych) |
| Ogłoszenie sprawozdania w MSiG | do ustalenia | (do weryfikacji w MSiG — imsig.pl) |
| Przychody / koszty / zysk (strata) netto | nieznane na etapie DRAFT | (do weryfikacji — nie fabrykuję wielkości) |
| Aktywa / kapitał własny / zobowiązania | nieznane na etapie DRAFT | (do weryfikacji) |
| Opinia biegłego rewidenta (o ile wymagana) | do ustalenia | (do weryfikacji) |

- **Czego szukam:** czy spółka złożyła sprawozdanie finansowe do KRS (Repozytorium Dokumentów Finansowych)
  i/lub ogłosiła je w MSiG. Młoda spółka (rejestracja 2024-09-11) może jeszcze nie mieć złożonych
  sprawozdań — brak sprawozdania będzie traktowany jako **ograniczenie danych**, a nie jako dowód złej
  kondycji `(założenie metodologiczne)`.
- **Status na etapie DRAFT:** brak potwierdzenia — nie formułuję żadnych twierdzeń o wielkościach
  finansowych `(do weryfikacji)`.

### 5.3. Kapitał zakładowy

- **Wartość wstępna:** 5 000 zł — jest to **ustawowe minimum** kapitału zakładowego spółki z o.o.
  (art. 154 § 1 k.s.h.) `(do weryfikacji w KRS)`.
- **Interpretacja:** minimalny kapitał zakładowy sam w sobie nie przesądza o złej kondycji (typowy dla
  małych, nowo zakładanych biur), ale oznacza **niewielki bufor kapitałowy** na pokrycie ewentualnych
  zobowiązań — podwyższona uwaga przy ocenie ryzyka `(założenie metodologiczne)`.
- **Niespójność do rozstrzygnięcia (powiązane z M1):** zadeklarowane „91 udziałów = 4 550 zł" nie sumuje
  się do kapitału 5 000 zł — do wyjaśnienia na pełnym odpisie KRS `(do weryfikacji)`.

### 5.4. Wiek firmy

- **Data rejestracji (wstępna):** 2024-09-11 — na dzień analizy (2026-08-15) spółka działa **krócej niż
  2 lata** `(do weryfikacji w KRS)`.
- **Interpretacja:** krótka historia działalności to **ograniczenie dostępności danych** (brak wieloletnich
  sprawozdań, ograniczona liczba opinii), a nie automatyczny sygnał negatywny. Podwyższa jednak niepewność
  co do stabilności finansowej `(założenie metodologiczne)`.

### 5.5. Historia zmian

| Pole | Wartość (wstępna) | Status |
|---|---|---|
| Zmiany w zarządzie | do ustalenia (czy były zmiany od rejestracji) | (do weryfikacji w KRS — dział 2) |
| Zmiany wspólników / struktury kapitałowej | do ustalenia | (do weryfikacji w KRS — dział 1) |
| Zmiany siedziby / adresu | do ustalenia | (do weryfikacji w KRS) |
| Zmiany przedmiotu działalności (PKD) | do ustalenia | (do weryfikacji w KRS) |
| Postępowania (upadłość/restrukturyzacja) — powiązane z M2 | do ustalenia | (do weryfikacji w KRS/KRZ) |

- **Czego szukam:** częstych zmian zarządu lub wspólników, które mogłyby być sygnałem niestabilności. Brak
  historii zmian u młodej spółki jest neutralny; **liczne zmiany** byłyby odnotowane jako czynnik ryzyka
  `(założenie metodologiczne)`. Na etapie DRAFT nie stwierdzam żadnych zmian `(do weryfikacji)`.

### 5.6. Powiązania osobowe i kapitałowe

- **Wspólnik / zarząd (wstępnie):** Katarzyna Pydynowska — prezes zarządu i wspólnik (91 udziałów =
  4 550 zł) `(do weryfikacji w pełnym odpisie KRS)`.
- **Szukane informacje:** inne podmioty, w których Katarzyna Pydynowska pełni funkcje (powiązania
  osobowe) oraz ewentualni pozostali wspólnicy (powiązania kapitałowe). Koncentracja własności w jednej
  osobie jest typowa dla małego biura, ale oznacza **uzależnienie ciągłości działania od jednej osoby**
  `(założenie metodologiczne)`.
- **Status na etapie DRAFT:** powiązania **nieznane** — wymagają weryfikacji w KRS (działy 1 i 2) oraz
  ewentualnie w publicznych wyszukiwarkach powiązań osobowych `(do weryfikacji)`. Nie formułuję twierdzeń
  o powiązaniach z innymi podmiotami.

### 5.7. Analiza i ocena ryzyka — M5

**Ocena: Średnie.** Na etapie DRAFT stabilność finansowa jest **nieznana**: sprawozdania finansowe
(KRS/MSiG), historia zmian i powiązania osobowe/kapitałowe mają status `(do weryfikacji)`, a żadne
wielkości finansowe nie są znane (nie są fabrykowane). Dodatkowo **młody wiek spółki** i **minimalny
kapitał zakładowy** ograniczają dostępność danych i podnoszą niepewność — to ograniczenia, a nie
stwierdzone problemy. Po uziemieniu w pass 2 ocena może zostać obniżona do **Niskiej** (jeśli sprawozdania
wykażą stabilność i brak negatywnych zmian) lub podniesiona do **Wysokiej** (w razie strat, braku
sprawozdań mimo obowiązku, licznych zmian zarządu lub negatywnych wpisów).

---

## Czerwone Flagi

- **Nie stwierdzono jednoznacznych czerwonych flag** na etapie M1.
- **Sygnał do obserwacji (nie flaga):** rozbieżność „91 udziałów = 4 550 zł" vs. „kapitał zakładowy 5 000 zł"
  — może wskazywać na drugiego wspólnika lub niepełny odczyt; do rozstrzygnięcia na pełnym odpisie KRS.
- **M2 — nie stwierdzono** negatywnych wpisów w rejestrach publicznych na etapie DRAFT. Rejestry (Biała
  Lista, VIES, KRS, KRZ/MSiG) nie zostały jeszcze sprawdzone, a komercyjne BIG pozostają poza dostępem —
  brak wpisów ma tu status `(do weryfikacji)` / `(brak danych publicznych)`, a nie potwierdzonego „czystego"
  wyniku.
- **M3 — nie stwierdzono** negatywnych opinii na etapie DRAFT. Źródła opinii (Google Maps, GoWork, Oferteo,
  Facebook) nie zostały jeszcze otwarte — brak negatywnych wpisów ma status `(do weryfikacji)`, a nie
  potwierdzonej „dobrej reputacji". Powtarzający się wzorzec negatywnych recenzji z ostatnich 12 miesięcy
  byłby traktowany jako czerwona flaga — na ten moment takiego wzorca nie odnotowano.
- **M4 — nie stwierdzono** negatywnych sygnałów jakościowych na etapie DRAFT. Strona WWW, oferta,
  certyfikaty i kanały kontaktu nie zostały jeszcze otwarte/sprawdzone, a brak wzmianki o OC ma status
  `(do weryfikacji)` — nie jest to potwierdzony „brak ubezpieczenia".
- **M5 — nie stwierdzono** negatywnych sygnałów finansowych na etapie DRAFT. Sprawozdania finansowe
  (KRS/MSiG), historia zmian i powiązania osobowe/kapitałowe nie zostały jeszcze otwarte/sprawdzone —
  brak danych ma status `(do weryfikacji)`, a nie potwierdzonej „stabilności finansowej". Młody wiek
  spółki (rejestracja 2024-09-11) i minimalny kapitał zakładowy (5 000 zł) to sygnał do obserwacji
  (ograniczenie danych / podwyższona uwaga), a nie czerwona flaga sam w sobie.

---

## Źródła

W pass 1 (stub) nie otwierano jeszcze źródeł — z tego powodu **nie podaję dat dostępu** (daty dostępu
zostaną dodane w pass 2 dla źródeł faktycznie otwartych). Planowane źródła do weryfikacji:

**M1 — Identyfikacja i metryka:**
- KRS / e-KRS — ekrs.ms.gov.pl (odpis aktualny i pełny) — potwierdzenie nazwy, KRS, adresu, kapitału, zarządu, udziałowców, PKD.
- Biała Lista podatników VAT — podatki.gov.pl / API MF (`wl-api.mf.gov.pl`) — potwierdzenie NIP i statusu VAT (M2).
- Rejestr REGON — potwierdzenie REGON.

**M2 — Status prawny i podatkowy:**
- Biała Lista podatników VAT — podatki.gov.pl / API MF (`wl-api.mf.gov.pl`) — status czynnego podatnika VAT, data rejestracji, rachunek rozliczeniowy.
- VIES — ec.europa.eu/taxation_customs/vies — status VAT-UE (PL7011222044).
- KRS / e-KRS — ekrs.ms.gov.pl — status podmiotu, postępowania upadłościowe/restrukturyzacyjne/likwidacyjne.
- Krajowy Rejestr Zadłużonych (KRZ) — krz.ms.gov.pl — ewentualne wpisy po NIP/KRS.
- Monitor Sądowy i Gospodarczy (MSiG) — imsig.pl — ogłoszenia wymagane po KRS/NIP.
- KRD / ERIF / BIG InfoMonitor — dostęp komercyjny (konto/opłata); jawne ograniczenie, bez zgadywania zawartości.

**M3 — Reputacja:**
- Google Maps — google.com/maps — profil/wizytówka firmy, liczba i treść opinii, oceny, daty (priorytet ostatnich 12 mies.).
- GoWork — gowork.pl — opinie o pracodawcy (o ile wpis istnieje).
- Oferteo — oferteo.pl — opinie klientów o usługach księgowych.
- Facebook — facebook.com — profil firmowy, recenzje i oceny (o ile istnieje).

**M4 — Jakość usług i specjalizacja:**
- Strona WWW biura (adres do ustalenia) — oferta, specjalizacja (IT/transport/inne), cennik, kanały kontaktu, ewentualna wzmianka o OC.
- KRS / e-KRS — ekrs.ms.gov.pl — PKD 69.20.Z, skład zarządu (kadra) i ewentualne wpisy o uprawnieniach.
- Rejestry branżowe (np. lista doradców podatkowych, certyfikat księgowy MF) — certyfikaty i uprawnienia kadry.
- Profile firmy / wizytówki usługowe — Google Maps, Oferteo, Facebook — opis oferty i specjalizacji (pokrywa się z M3).
- Ogłoszenia / materiały własne biura — ewentualna wzmianka o ubezpieczeniu OC biura.

**M5 — Stabilność finansowa:**
- KRS / e-KRS — ekrs.ms.gov.pl — sprawozdania finansowe (Repozytorium Dokumentów Finansowych), kapitał zakładowy, data rejestracji (wiek firmy), historia zmian (działy 1 i 2), powiązania osobowe/kapitałowe.
- Monitor Sądowy i Gospodarczy (MSiG) — imsig.pl — ogłoszenia o sprawozdaniach finansowych i zmianach w KRS.
- Rejestr REGON — potwierdzenie daty rejestracji / wieku firmy.
- Biała Lista podatników VAT — podatki.gov.pl / API MF (`wl-api.mf.gov.pl`) — ewentualny rachunek rozliczeniowy (powiązane z M2).

---

## Metodologia i ograniczenia

- **Metoda:** OSINT na źródłach publicznych i urzędowych; priorytet dla źródeł pierwotnych (KRS, Biała Lista,
  VIES, KRZ/MSiG); lustra (rejestr.io, aleo.com itp.) wyłącznie pomocniczo.
- **Ograniczenia (pass 1):** wszystkie dane M1–M5 mają status rozpoznania wstępnego i nie zostały jeszcze
  potwierdzone w rejestrze urzędowym, w źródłach opinii ani w materiałach o ofercie/jakości usług i
  stabilności finansowej. Rejestry publiczne (Biała Lista, VIES, KRS, KRZ, MSiG), portale opinii (Google
  Maps, GoWork, Oferteo, Facebook), strona WWW / materiały o ofercie oraz sprawozdania finansowe (KRS/MSiG)
  zostaną sprawdzone w pass 2.
- **Ograniczenie — komercyjne BIG:** KRD, ERIF i BIG InfoMonitor wymagają logowania/opłat, więc ich zawartość
  jest poza zasięgiem tego raportu — odnotowane jako jawne ograniczenie, bez zgadywania zawartości.
- **Ograniczenie — reputacja:** młody wiek spółki (rejestracja 2024-09-11) i mała skala działalności mogą
  oznaczać niewielką liczbę opinii lub brak profilu na części portali; brak opinii będzie traktowany jako
  ograniczenie danych, nie jako opinia negatywna.
- **Ograniczenie — jakość usług i OC:** oferta, specjalizacja i certyfikaty są weryfikowane na podstawie
  materiałów własnych biura (strona WWW, ogłoszenia), które mogą być niekompletne lub nieaktualne. Wzmianka
  o ubezpieczeniu OC nie została na etapie DRAFT znaleziona (nie otwierano źródeł) — to brak danych, a nie
  potwierdzenie braku polisy; zakres/suma OC nie są zgadywane.
- **Ograniczenie — stabilność finansowa:** młoda spółka (rejestracja 2024-09-11) może nie mieć jeszcze
  złożonych sprawozdań finansowych w KRS/MSiG; brak sprawozdań traktowany jako ograniczenie danych, a nie
  domniemanie negatywne. Kapitał zakładowy 5 000 zł (minimum ustawowe) sam w sobie nie przesądza o kondycji,
  ale oznacza niewielki bufor kapitałowy. Powiązania osobowe/kapitałowe weryfikowane wyłącznie na podstawie
  odpisu KRS.
- **Zasada „brak danych ≠ dane negatywne":** młody wiek spółki może oznaczać brak sprawozdań/opinii — będzie
  to odnotowywane jako ograniczenie, a nie domniemanie negatywne.
