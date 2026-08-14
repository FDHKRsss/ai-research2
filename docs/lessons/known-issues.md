# Known issues

_Recurring walls/gotchas and how to get past them. One bullet each._

- Testy/audyty „brak TODO": naiwne szukanie podciągu `todo` daje fałszywy traf na polskich słowach (np. „metodologia") — dopasowuj tylko samodzielne markery placeholderów (granice słowa / regex `\b[Tt][Oo][Dd][Oo]\b`), nie goły podciąg.
