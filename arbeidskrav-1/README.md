# Oppgave 1 – Grunnleggende programflyt

## Oppgave 1.1 – Beregn tidsbruk

### Om oppgaven

Oppgaven gikk ut på å lage et enkelt program som beregner total tidsbruk basert på antall økter og hvor mange minutter hver økt varer.

Programmet bruker `input()` for å hente verdier fra brukeren og `int()` for å gjøre tekst om til heltall. Beregningen gjøres ved å multiplisere antall økter med antall minutter per økt.

### Bruk av KI

Jeg brukte KI som støtte for å forstå hvordan Python og `try/except` fungerer, og for å forstå hvorfor PyCharm markerte enkelte variabler med understreking.

**KI-verktøy:** ChatGPT

### Prompt

Dette spørsmålet ble stilt i samtalen:

> To variabler er understreket på slutten i PyCharm fordi det er usikkert om de inneholder et tall eller en streng etter `try/except`. Kan jeg fjerne understrekingen eller gjøre det på en annen måte?

### Svar og løsning

KI forklarte at understrekingen ikke nødvendigvis betyr at programmet har en feil. Det er en advarsel fra editoren/type checkeren fordi PyCharm ikke kan være sikker på hvilken datatype variabelen har.

En løsning var å konvertere input direkte til `int` inne i `try`-blokken. Etter en vellykket konvertering vet Python og PyCharm at variabelen er et heltall.

Jeg kunne derfor bruke:

```python
try:
    sessions = int(input("Enter number of sessions: "))
except ValueError:
    ...
```

i stedet for å først lagre input som tekst og konvertere den senere.

### Hvordan KI påvirket løsningen

Jeg brukte denne forklaringen til å endre hvordan inputverdiene ble konvertert. Ved å bruke `int()` direkte inne i `try`-blokken ble koden enklere, og understrekingen i PyCharm forsvant.

Jeg fjernet også en unødvendig `continue` på slutten av løkken fordi programflyten allerede gikk videre naturlig etter en vellykket konvertering.

# Oppgave 2 – Datastrukturer og behandling av data

## Datastruktur

I denne oppgaven lagres studieøkter i en liste:

```python
study_sessions = []
```

Hver studieøkt lagres som en dictionary med følgende nøkler:

* `topic`
* `duration_minutes`
* `status`

Eksempel:

```python
{
    "topic": "Python",
    "duration_minutes": 45,
    "status": "planned"
}
```

Jeg valgte dictionary fordi feltene får tydelige navn. Dette gjør dataene enklere å lese og gir større fleksibilitet enn for eksempel en tuple.

## Funksjonalitet

Programmet har en meny med funksjoner for å:

1. Registrere en ny studieøkt
2. Vise alle studieøkter
3. Vise fullførte studieøkter
4. Søke etter tema
5. Sortere studieøkter etter varighet
6. Vise total og gjennomsnittlig varighet for fullførte økter
7. Avslutte programmet

Programmet håndterer også ugyldig input ved å vise en feilmelding og be brukeren prøve igjen.

## Testing

Jeg testet programmet manuelt med både gyldige og ugyldige inputverdier.

Jeg kontrollerte blant annet:

* registrering av studieøkter
* søk etter tema
* søk uten forskjell på store og små bokstaver
* sortering etter varighet
* visning av fullførte økter
* beregning av total og gjennomsnittlig tid
* ugyldige menyvalg og inputverdier

## Bruk av KI

**KI-verktøy:** Claude (Anthropic)

Jeg brukte KI som støtte for å forstå Python-syntaks, datastrukturer, søking og sortering.

### Spørsmål (oppsummert fra samtalen)

1. Hvordan legger jeg til en ny nøkkel og verdi i et dictionary i Python?

KI forklarte at jeg kan legge til en ny nøkkel direkte:

```python
session["status"] = "planned"
```

2. Hvorfor får jeg feilmelding når jeg prøver `sorted(study_sessions)` direkte?

KI forklarte at Python ikke automatisk vet hvilket felt i dictionaryen som skal brukes til sortering. Derfor kan `sorted()` brukes med `key`, for eksempel:

```python
sorted(study_sessions, key=lambda session: session["duration_minutes"])
```

3. Hvordan kan jeg sjekke om en del av et ord finnes i temaet til øktene i listen?

KI forklarte hvordan `in` kan brukes for å søke etter en del av en tekst.

4. Kan jeg gjøre søket uavhengig av store og små bokstaver?

KI forklarte hvordan `.lower()` kan brukes på både søketeksten og teksten som sammenlignes.

5. Kan jeg skrive treffene fra søket til en vanlig liste med en `for`-løkke og `.append()`?

KI forklarte hvordan en tom liste kan opprettes og treff legges til med `.append()`.

6. Hvordan sorterer jeg listen slik at den lengste økten vises først?

KI forklarte hvordan `reverse=True` kan brukes sammen med `sorted()`.

### Hvordan KI påvirket løsningen

KI ble brukt som forklarings- og feilsøkingsstøtte. Jeg brukte forklaringene til å forstå dictionaries, søk, sortering og behandling av data i en liste.

# Oppgave 3 – Funksjoner og dokumentasjon

## Testtilfeller

Jeg dokumenterte både gyldige og ugyldige testtilfeller for programmet.

### Gyldige testtilfeller

Eksempler på gyldige tester:

* gyldig dato
* gyldig menyvalg
* flere datoer
* datoer i ulik rekkefølge

### Ugyldige testtilfeller

Eksempler på ugyldige tester:

* dato med feil format
* ugyldig menyvalg
* tom eller ugyldig input

Testene ble brukt for å kontrollere at programmet reagerer riktig både på forventede og uventede inputverdier.

## Dokumentasjon

Jeg brukte Python-dokumentasjonen for å forstå funksjonalitet knyttet til datoer og sortering:

* Python `datetime`
* `strftime()` og `strptime()`
* Python Sorting Techniques

## Bruk av KI

**KI-verktøy:** Claude (Anthropic)

KI ble brukt som støtte for å forstå programflyt, datoer, funksjoner, testing og dokumentasjon.

### Spørsmål (oppsummert fra samtalen)

1. Hvorfor blir datoene i listen overskrevet i stedet for å legges til?

KI forklarte at listen ble opprettet på feil sted, slik at den ble laget på nytt i en løkke. Listen måtte opprettes utenfor løkken slik at tidligere verdier ble beholdt.

2. Hvorfor er ikke datoene sortert i riktig rekkefølge?

KI forklarte forskjellen mellom datoer lagret som tekst og datoer behandlet som `datetime`-objekter. For korrekt kronologisk sortering må datoene behandles som datoer.

3. Hvordan dokumenterer jeg gyldige og ugyldige testtilfeller i README.md?

KI forklarte forskjellen mellom gyldige og ugyldige testtilfeller og hvordan de kan dokumenteres i en tabell med input og forventet resultat.

4. Hvilken meny kan jeg opprette for dette programmet?

KI hjalp med å strukturere en enkel meny for funksjonene i programmet.

5. Hvorfor vises bare én dato når jeg velger et menyvalg?

KI forklarte hvordan plasseringen av `return` inne i en løkke kan føre til at funksjonen avsluttes etter første element. Forklaringen ble brukt til å forstå hvordan resultatet burde returneres og vises.

6. Hvordan kan jeg beskrive bruken av KI i README.md?

KI hjalp med å formulere en kort beskrivelse av hvordan KI ble brukt som støtte under utviklingen.

### Hvordan KI påvirket løsningen

KI ble brukt til å forstå feil og forbedre programstrukturen. Jeg brukte forklaringene til å rette problemer med lister, datoer, løkker og `return`, samt til å dokumentere testtilfeller.

# Oppgave 4 – Les, analyser og håndter CSV-data

## Oppgave 4.1 – Les og kontroller data

Programmet leser data fra `supporthenvendelser.csv` ved hjelp av `csv.DictReader`.

Filen åpnes med UTF-8 og `with open()` slik at filen håndteres på en trygg måte.

Programmet kontrollerer blant annet:

* at nødvendige felt finnes
* at ID er et positivt heltall
* at antall minutter er et ikke-negativt heltall
* at `is_resolved` inneholder en gyldig verdi

Ugyldige rader hoppes over med `continue`, og programmet viser en feilmelding med radnummer og informasjon om hva som er galt.

Programmet håndterer også feil som:

* manglende fil med `FileNotFoundError`
* ugyldige tallverdier med `ValueError`

## Oppgave 4.2 – Analyser data

Programmet analyserer de gyldige henvendelsene og beregner blant annet:

* antall gyldige henvendelser
* antall henvendelser per kategori
* total behandlingstid
* gjennomsnittlig behandlingstid
* antall løste henvendelser
* antall uløste henvendelser
* kategorien med flest henvendelser
* uløste henvendelser sortert etter behandlingstid

Gjennomsnittlig behandlingstid vises med én desimal.

## Oppgave 4.3 – Skriv rapport

Resultatet av analysen skrives til:

```text
support-rapport.txt
```

Rapportfilen overskrives dersom den allerede finnes.

## Oppgave 4.4 – Finn og rett feil

Jeg fant og rettet flere feil i programkoden.

Blant annet:

1. `=` ble brukt i stedet for `==` i en sammenligning.
2. En variabel ble overskrevet med `total = ...` i stedet for å øke verdien med `total += ...`.
3. Funksjonen returnerte feil variabel.
4. En funksjon ble kalt med feil argument.

## Bruk av KI

**KI-verktøy:** ChatGPT

KI ble brukt som støtte for å forstå Python-kode, feilmeldinger og hvordan ulike deler av programmet fungerer.

### KI-bidrag

Temaer jeg fikk hjelp til å forstå var blant annet:

* hvordan `csv.DictReader` fungerer
* hvordan `continue` påvirker en løkke
* hvordan `sorted()` kan brukes med `key` og `lambda`
* hvordan formatering som `{category:<15}` og `{count:>5}` fungerer
* hvordan type hints som `list[dict[str, str | int]]` kan brukes
* hvordan returtypen `-> int` fungerer

Jeg brukte forklaringene til å forstå koden og finne feil, men kontrollerte endringene i programmet ved å kjøre og teste det.

# Oppgave 5 – Miniprosjekt: aktivitetsplanlegger

## Om programmet

Oppgave 5 er et miniprosjekt der jeg har laget en enkel aktivitetsplanlegger i Python.

Programmet lar brukeren:

1. registrere aktiviteter
2. vise registrerte aktiviteter
3. søke etter aktiviteter
4. filtrere aktiviteter etter status
5. sortere aktiviteter etter dato eller varighet
6. markere aktiviteter som fullført
7. vise statistikk
8. lagre og laste aktiviteter fra fil
9. avslutte programmet

Programmet bruker objektorientert programmering med én klasse: `Activity`.

Status for en aktivitet kan være:

* `planned`
* `completed`

## Funksjoner

Programmet inneholder funksjonalitet for:

* registrering av aktiviteter
* validering av tittel og kategori
* validering av dato
* validering av positiv varighet
* søk etter tittel eller kategori
* filtrering etter status
* sortering etter dato
* sortering etter varighet
* endring av status til `completed`
* statistikk
* lagring til fil
* lasting fra fil

Søk etter aktivitet bruker case-insensitive søk, slik at store og små bokstaver ikke påvirker resultatet.

## Programstruktur

### Activity-klassen

Klassen `Activity` har følgende attributter:

```text
title
category
date
estimated_minutes
status
```

Klassen inneholder blant annet metoder for å:

* vise aktiviteten
* lagre aktiviteten som tekst
* markere aktiviteten som fullført

### Funksjoner

Programmet bruker også funksjoner utenfor klassen, blant annet for:

* å hente og validere dato
* å hente og validere varighet
* å registrere en ny aktivitet

Dette gjør at ulike deler av programmet har tydelige ansvarsområder.

## Datastruktur og designvalg

Aktivitetene lagres i en liste:

```python
activities = []
```

Hvert element i listen er et `Activity`-objekt.

Jeg valgte en liste fordi programmet trenger å lagre flere aktiviteter og behandle dem samlet.

Jeg valgte en egen `Activity`-klasse fordi hver aktivitet har flere egenskaper og handlinger. Dette gjør programmet mer oversiktlig og følger kravet om enkel objektorientert programmering uten arv.

Datoen lagres i formatet:

```text
dd.mm.yyyy
```

Ved sortering konverteres datoen til et `datetime`-objekt slik at aktivitetene kan sorteres kronologisk.

## Fillagring

Aktivitetene lagres i en tekstfil.

Hver aktivitet lagres på én linje med `|` som skilletegn:

```text
title|category|date|estimated_minutes|status
```

Eksempel:

```text
Study Python|Study|21.09.2026|60|planned
```

Ved lasting deles linjen opp med:

```python
split("|")
```

Programmet kontrollerer at filen inneholder riktig antall felt og at verdiene har gyldig format.

Hvis filen ikke finnes, håndteres dette med `FileNotFoundError`, og brukeren får en forståelig melding.

Ved lasting tømmes den eksisterende listen først. Dette gjør at aktivitetene ikke blir lagt til flere ganger dersom filen lastes mer enn én gang.

## Testing

Jeg testet programmet manuelt med både gyldige og ugyldige inputverdier.

### Test 1 – Registrere aktivitet

**Input:** Gyldig tittel, kategori, dato og varighet.

**Forventet resultat:** Aktiviteten registreres og vises i listen.

**Resultat:** Bestått.

### Test 2 – Ugyldig input ved registrering

Jeg testet:

* tom tittel
* tom kategori
* ugyldig dato
* `0` minutter
* negativ varighet
* tekst i stedet for tall

**Forventet resultat:** Programmet viser en feilmelding og ber om ny input.

**Resultat:** Bestått.

### Test 3 – Søke etter aktivitet

Jeg testet både delvis søk og søk med store og små bokstaver.

**Forventet resultat:** Relevante aktiviteter blir funnet uavhengig av store og små bokstaver.

**Resultat:** Bestått.

### Test 4 – Filtrere etter status

Jeg testet aktiviteter med status `planned` og `completed`.

**Forventet resultat:** Programmet viser bare aktiviteter med valgt status.

**Resultat:** Bestått.

### Test 5 – Sortere aktiviteter

Jeg testet sortering etter:

* dato
* varighet

Sorteringen ble testet med flere aktiviteter med forskjellige datoer og varigheter.

**Forventet resultat:** Aktivitetene vises i riktig sorteringsrekkefølge.

**Resultat:** Bestått.

### Test 6 – Markere aktivitet som fullført

Jeg valgte en aktivitet med status `planned` og markerte den som fullført.

**Forventet resultat:** Status endres til `completed`.

**Resultat:** Bestått.

### Test 7 – Statistikk

Jeg testet statistikkfunksjonen med flere aktiviteter.

**Forventet resultat:** Programmet viser relevant statistikk basert på aktivitetene i listen.

**Resultat:** Bestått.

### Test 8 – Lagre og laste fil

Jeg lagret aktiviteter til fil, startet filinnlesingen og kontrollerte at aktivitetene ble lastet inn igjen.

**Forventet resultat:** Aktivitetene fra filen blir tilgjengelige i programmet.

**Resultat:** Bestått.

### Test 9 – Laste samme fil flere ganger

Jeg testet å laste inn den samme filen flere ganger.

**Forventet resultat:** Aktivitetene skal ikke bli duplisert.

**Resultat:** Bestått.

### Test 10 – Manglende fil

Jeg testet programmet uten at datafilen eksisterte.

**Forventet resultat:** Programmet skal håndtere situasjonen uten å krasje og vise en forståelig melding.

**Resultat:** Bestått.

## Kjente begrensninger

Programmet bruker en enkel tekstfil med `|` som skilletegn.

Dette betyr at dersom brukeren skriver `|` i tittelen eller kategorien, kan filformatet bli vanskelig å lese riktig.

Programmet har også et enkelt terminalbasert brukergrensesnitt.

En manuelt endret datafil kan inneholde ugyldige verdier. Programmet kontrollerer flere slike feil ved lasting, men tekstformatet gir ikke samme struktur og sikkerhet som et mer avansert dataformat.

## Git workflow

Jeg brukte Git-integrasjonen i PyCharm for versjonskontroll.

Arbeidsflyten var:

1. Jeg gjorde endringer i prosjektet i PyCharm.
2. Jeg brukte Git-integrasjonen i PyCharm for å committe endringene.
3. Jeg brukte PyCharm til å sende endringene til GitHub.

Følgende commits ble brukt i prosjektet:

* `Add Activity class and completion method`
* `Fix project file structure`
* `Update README`

Commit-meldingene beskriver konkrete endringer i prosjektet.

## Bruk av KI

Jeg brukte KI som støtte under utviklingen av Oppgave 5. KI ble hovedsakelig brukt til å forklare Python-konsepter, diskutere mulige løsninger, forstå feilmeldinger og kontrollere kode.

Jeg brukte ikke KI til å erstatte testing. Endringer ble testet i programmet etter at jeg hadde forstått hva koden gjorde.

### Spørsmål (oppsummert fra samtalen)

#### Activity-klassen og programstruktur

Jeg fikk hjelp til å forstå hvordan `Activity`-klassen kunne bygges opp med attributtene:

* `title`
* `category`
* `date`
* `estimated_minutes`
* `status`

Jeg diskuterte også forskjellen mellom å ha en global liste som:

```python
activities = []
```

og å lagre aktiviteter som en del av et objekt.

#### `enumerate()`

Jeg fikk forklart hvordan `enumerate()` fungerer, og hvordan det kan brukes for å vise aktiviteter med nummer i menyen.

Eksempel:

```python
for number, activity in enumerate(activities, start=1):
    print(number)
```

Dette ble brukt i visningen av aktiviteter slik at brukeren kan se et nummer foran hver aktivitet.

#### Søking

Jeg fikk hjelp til å forstå hvordan søk etter tittel eller kategori kan gjøres med `in`, og hvordan `.lower()` kan brukes for å gjøre søket uavhengig av store og små bokstaver.

#### Sortering

Jeg fikk hjelp til å forstå hvordan `sorted()` fungerer med `key` og `lambda`.

For eksempel brukes datoen som sorteringsgrunnlag ved å konvertere tekstformatet til et `datetime`-objekt:

```python
sorted_activities = sorted(
    activities,
    key=lambda activity: datetime.strptime(activity.date, "%d.%m.%Y"),
    reverse=True
)
```

Jeg fikk også forklart hvordan aktiviteter kan sorteres etter `estimated_minutes`.

#### Fillagring og lasting

Jeg fikk hjelp til å forstå hvordan aktiviteter kan lagres som tekst med `|` som skilletegn, og hvordan `split("|")` kan brukes når dataene lastes inn igjen.

Jeg diskuterte også hvordan programmet kan kontrollere at data fra filen har riktig format og gyldige verdier.

#### Inputvalidering

Jeg fikk hjelp til å forstå hvordan `try/except` kan brukes for å håndtere ugyldige tall og datoer uten at programmet krasjer.

Dette ble brukt blant annet ved validering av:

* dato
* varighet
* menyvalg

#### Feilsøking og testing

Jeg brukte KI til å diskutere feil som dukket opp under testing, blant annet problemer med:

* ugyldige inputverdier
* lasting av fil
* dupliserte aktiviteter etter flere innlastinger
* feil håndtering av `ValueError`
* sortering av datoer

Jeg testet deretter løsningene selv i programmet.

### Hvordan KI påvirket løsningen

KI hjalp meg først og fremst med å forstå hvorfor ulike løsninger fungerer, i stedet for bare å gi ferdig kode.

Forklaringene påvirket blant annet:

* strukturen til `Activity`-klassen
* bruken av `enumerate()`
* søk med `in` og `.lower()`
* sortering med `sorted()`
* konvertering av datoer med `datetime.strptime()`
* validering med `try/except`
* lagring og lasting fra tekstfil
* håndtering av feil ved innlasting

Jeg brukte deretter kunnskap fra forklaringene til å skrive, endre og teste programmet selv.
