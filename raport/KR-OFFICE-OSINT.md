# Wywiad gospodarczy (OSINT) — KR Office sp. z o.o.

> **Status dokumentu:** WERSJA ROBOCZA — pass 1 (DRAFT / stub).
> Dokument powstaje sekwencyjnie (po jednym kroku milestona). Obecnie wypełnione i kompletne są sekcje:
> **M1 — Identyfikacja podmiotu i metryka**, **M2 — Status prawny i podatkowy** oraz
> **M3 — Reputacja**. Pozostałe sekcje (M4–M6) zostaną dopisane w kolejnych krokach pass 1,
> a w pass 2 (REAL) całość zostanie zweryfikowana i uziemiona źródłami (URL + data dostępu).

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

> Pozostałe wiersze (M4–M6) zostaną dopisane wraz z ukończeniem odpowiednich sekcji w pass 1.

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

---

## Metodologia i ograniczenia

- **Metoda:** OSINT na źródłach publicznych i urzędowych; priorytet dla źródeł pierwotnych (KRS, Biała Lista,
  VIES, KRZ/MSiG); lustra (rejestr.io, aleo.com itp.) wyłącznie pomocniczo.
- **Ograniczenia (pass 1):** wszystkie dane M1, M2 i M3 mają status rozpoznania wstępnego i nie zostały
  jeszcze potwierdzone w rejestrze urzędowym ani w źródłach opinii. Rejestry publiczne (Biała Lista, VIES,
  KRS, KRZ, MSiG) oraz portale opinii (Google Maps, GoWork, Oferteo, Facebook) zostaną sprawdzone w pass 2.
- **Ograniczenie — komercyjne BIG:** KRD, ERIF i BIG InfoMonitor wymagają logowania/opłat, więc ich zawartość
  jest poza zasięgiem tego raportu — odnotowane jako jawne ograniczenie, bez zgadywania zawartości.
- **Ograniczenie — reputacja:** młody wiek spółki (rejestracja 2024-09-11) i mała skala działalności mogą
  oznaczać niewielką liczbę opinii lub brak profilu na części portali; brak opinii będzie traktowany jako
  ograniczenie danych, nie jako opinia negatywna.
- **Zasada „brak danych ≠ dane negatywne":** młody wiek spółki może oznaczać brak sprawozdań/opinii — będzie
  to odnotowywane jako ograniczenie, a nie domniemanie negatywne.
