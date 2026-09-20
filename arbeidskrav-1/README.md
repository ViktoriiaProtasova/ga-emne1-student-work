# Oppgave 1 – Grunnleggende programflyt

## Oppgave 1.1 – Beregn tidsbruk

### Bruk av KI

KI (ChatGPT) er brukt som hjelpemiddel i arbeidet. Nedenfor dokumenteres
forespørsler og svar som helt eller delvis har påvirket løsningen.

**Prompt 1**

**Koden:**

```python
while True:
    number_of_sessions = input("Enter number of sessions: ")
    try:
        number_of_sessions = int(number_of_sessions)
        if number_of_sessions > 0:
            break
        else:
            print("Invalid input. Please enter a positive whole number. Try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")
        continue

while True:
    minutes_per_session = input("Enter minutes per session: ")
    try:
        minutes_per_session = int(minutes_per_session)
        if minutes_per_session > 0:
            break
        else:
            print("Invalid input. Please enter a positive whole number. Try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")
        continue

hours = number_of_sessions * minutes_per_session // 60
minutes = number_of_sessions * minutes_per_session % 60

print(f"Number of study sessions: {number_of_sessions}")
print(f"Minutes per session: {minutes_per_session}")
print(f"Total time spent: {hours} hours and {minutes} minutes")
```
**Forespørsel:**

> To variabler er understreket på slutten i PyCharm fordi det er usikkert om de inneholder et tall eller en streng etter `try/except`. Kan jeg fjerne understrekingen eller gjøre det på en annen måte?

**Svar fra KI:**

> Understrekingen er ikke en feil — koden din kjører helt fint. Det er editoren (typesjekkeren, altså verktøyet som gjetter hvilken datatype hver variabel har) som klager.
> Den beste løsningen for denne oppgaven er å konvertere input til `int` direkte inne i `try`-blokken:
>
> ```python
> while True:
>     try:
>         number_of_sessions = int(input("Enter number of sessions: "))
>         if number_of_sessions > 0:
>             break
>         print("Invalid input. Please enter a positive whole number. Try again.")
>     except ValueError:
>         print("Invalid input. Please enter a positive whole number. Try again.")
> ```
>
> Det samme kan gjøres for `minutes_per_session`:
>
> ```python
> while True:
>     try:
>         minutes_per_session = int(input("Enter minutes per session: "))
>         if minutes_per_session > 0:
>             break
>         print("Invalid input. Please enter a positive whole number. Try again.")
>     except ValueError:
>         print("Invalid input. Please enter a positive whole number. Try again.")
> ```
>
> Denne løsningen er kortere, og etter en vellykket `int()`-konvertering vet PyCharm at variablene er av typen `int`. Derfor forsvinner type-varselet.
> En liten ting jeg endret på veien: `continue` helt nederst i en løkke gjør ingenting, siden løkka uansett går videre til neste runde, så den kan droppes.

**Hvordan svaret påvirket løsningen:**

Jeg brukte forslaget om å konvertere input til `int` direkte inne i `try`-blokken. Dette fjernet type-varselet i PyCharm og gjorde koden kortere.
Jeg fjernet også `continue` helt nederst i løkken.




# Oppgave 2 – Datastrukturer og behandling av data

## Datastruktur

Studieøktene lagres i en liste (`study_sessions`), der hver økt er et **dict** med tre felt: `topic` (tekst), `duration_minutes` (positivt heltall) og `status` (`planned` eller `completed`).

Jeg valgte `dict` i stedet for `tuple` fordi feltene har navn (`session["topic"]`, `session["duration_minutes"]`), noe som gjør koden lettere å lese enn å huske posisjonen til hvert felt i en tuple (`session[0]`, `session[1]`). En `tuple` er uforanderlig (immutable) – man kan ikke endre en verdi inne i en tuple etter at den er opprettet. Selv om dette ikke er nødvendig i den nåværende versjonen av programmet, valgte jeg `dict` for at koden skal være lettere å lese og for at strukturen skal være fleksibel hvis programmet senere skal utvides til å endre felt i en eksisterende økt.

## Funksjonalitet

Programmet viser en meny med sju valg: registrere en økt, vise alle økter, vise kun fullførte økter, søke etter tema, sortere etter varighet, vise samlet/gjennomsnittlig varighet for fullførte økter, og avslutte. Ugyldig inndata (tomt tema, negativ eller ikke-numerisk varighet, ugyldig status, ugyldig menyvalg) gir en forklarende feilmelding, og brukeren kan prøve på nytt.

## Testing

Programmet er testet manuelt for hvert menyvalg, inkludert både gyldige verdier og typiske feilsituasjoner (tomt tema, negativ varighet, tekst i stedet for tall, ugyldig status, søk uten treff, ugyldig menyvalg).


## Bruk av kunstig intelligens (KI)

Jeg brukte Claude (Anthropic) for å forstå oppgavekravene og få hjelp med konkrete kodeproblemer. Jeg skrev koden selv og testet alle forslagene ved å kjøre programmet.

### Spørsmål og svar (oversatt fra ukrainsk, kort oppsummert)

**1. "Hvordan legger jeg til en ny nøkkel og verdi i et dict i Python?"**
Svar: Bruk hakeparentes, f.eks. `session["status"] = "planned"`. Dette la grunnlaget for hvordan jeg registrerer nye studieøkter i listen.

**2. "Hvorfor får jeg feilmelding når jeg prøver `sorted(study_sessions)` direkte?"**
Svar: `sorted()` vet ikke hvilket felt i dict-et den skal sortere etter. Løsningen er å bruke parameteren `key` med en `lambda`-funksjon, f.eks. `key=lambda session: session["duration_minutes"]`. Dette avgjorde hvordan sorteringsdelen (menyvalg 5) ble skrevet.

**3. "Hvordan kan jeg sjekke om en del av et ord finnes i temaet til øktene i listen?"**
Svar: Bruk `in` for å sjekke om søketeksten er en del av `session["topic"]`, f.eks. `if search_text in session["topic"]`. Dette avgjorde hvordan søkefunksjonen (menyvalg 4) ble bygget opp, slik at brukeren finner treff selv om bare en del av temaet skrives inn.

**4. "Kan jeg normalisere (gjøre om til små bokstaver) et tema jeg henter fra listen, for søk som ikke skiller mellom store og små bokstaver?"**
Svar: Bruk `.lower()` på begge sider av sammenligningen, kun ved selve sammenligningen – ikke lagre om selve dataene. Dette gjorde at søket fungerer uansett om brukeren skriver med store eller små bokstaver.

**5. "Kan jeg skrive treffene fra søket til en vanlig liste med en `for`-løkke og `.append()`?"**
Svar: Ja, det gjøres ved å opprette en tom liste før løkken, og legge til (`.append()`) hver økt som matcher søket inne i løkken. Etter løkken viser jeg en feilmelding hvis listen er tom, og resultatene hvis den ikke er det. Denne fremgangsmåten brukte jeg til å bygge søkefunksjonen (menyvalg 4).

**6. "Hvordan sorterer jeg listen slik at den lengste økten vises først?"**
Svar: Legg til parameteren `reverse=True` i `sorted()`, f.eks. `sorted(study_sessions, key=lambda session: session["duration_minutes"], reverse=True)`. Dette avgjorde hvordan jeg fikk økten med lengst varighet til å vises øverst, slik oppgaven krevde.

### Hva KI hjalp med

- Forklarte hvorfor `sorted()` krever `key` for å sortere en liste med dict.
- Viste hvordan `reverse=True` sorterer listen i synkende rekkefølge, slik at lengste økt vises først.
- Forklarte hvordan `in` kan brukes for å finne treff når bare en del av temaet skrives inn, og hvorfor `.lower()` må brukes på begge sider ved søk uten hensyn til store/små bokstaver.
- Viste hvordan søketreff kan samles i en liste med en vanlig `for`-løkke og `.append()`, som jeg valgte å bruke i den endelige koden.





# Oppgave 3 – Funksjoner og dokumentasjon
## Testtilfeller

### Gyldige testtilfeller

| # | Inndata | Forventet resultat |
|---|---------|--------------------|
| 1 | Meny: `1`, dato: `25.02.2028` | Datoen legges til i listen |
| 2 | Meny: `2` rett etter oppstart | Meldingen "No study sessions planned yet." vises, og menyen vises på nytt |
| 3 | Datoer: `20.12.2024`, `01.01.2019`, `22.02.2020` | Listen er sortert: `01.01.2019`, `22.02.2020`, `20.12.2024` |
| 4 | Dato: `29.02.2024` (skuddår) | Datoen godtas |

### Ugyldige testtilfeller

| # | Inndata | Forventet resultat |
|---|---------|--------------------|
| 5 | Meny: `5` | Meldingen "Invalid option. Please try again." vises, og menyen vises på nytt |
| 6 | Meny: `abc` | Meldingen "Invalid option. Please try again." vises |
| 7 | Dato: `31.02.2025` | Meldingen "Invalid option. Please try again." vises |
| 8 | Dato: `2025-02-10` | Meldingen "Invalid option. Please try again." vises |
| 9 | Dato: tom inndata | Meldingen "Invalid option. Please try again." vises
## Dokumentasjon

- Python `datetime` – Basic date and time types (grunnleggende dato- og tidstyper):
  https://docs.python.org/3/library/datetime.html
- Formatkoder for `strftime()` og `strptime()`:
  https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
- Python Sorting Techniques (sorteringsteknikker):
  https://docs.python.org/3/howto/sorting.html

## Bruk av kunstig intelligens (KI)

Jeg brukte Claude (Anthropic) for å forstå kravene til oppgaven og feilene i koden. Jeg skrev koden selv og testet alle endringene ved å kjøre programmet.

### Spørsmål og svar (oversatt fra ukrainsk, kort oppsummert)

**1. "Hvorfor blir datoene i listen overskrevet i stedet for å legges til?"**
Svar: Listen ble opprettet på nytt (`list_of_dates = []`) inne i løkken hver gang alternativ 1 ble valgt. Løsningen er å opprette listen én gang, før løkken.

**2. "Hvorfor er ikke datoene sortert i riktig rekkefølge?"**
Svar: Datoene var lagret som tekst, og tekst sammenlignes tegn for tegn, så dagen ble sammenlignet før året. Løsningen er å lagre datoene som datoobjekter fra `datetime` og bare gjøre dem om til tekst når de vises.

**3. "Forklar kravet om å dokumentere gyldige og ugyldige testtilfeller i README.md og hvordan man gjør det riktig?"**
Svar: Gyldige testtilfeller er riktige inndata som programmet skal godta. Ugyldige testtilfeller er feil inndata der programmet skal vise en feilmelding uten å krasje. Testene kan skrives som en tabell med inndata og forventet resultat, sammen med tittel og nettadresse til dokumentasjonen.

**4. "Hvilken meny kan jeg opprette for dette programmet?"**
Svar: En meny med fire valg: planlegge en økt, vise økter i datorekkefølge, telle dager mellom to datoer og avslutte. Slik brukes alle de obligatoriske funksjonene i menyen.

**5. "Hvorfor vises bare én dato når jeg velger menyalternativ 2?"**
Svar: Først sto `return` inne i `for`-løkken, så funksjonen stoppet etter første dato. Senere sto `print` utenfor løkken, så bare siste dato ble vist. Løsningen er en funksjon som returnerer hele den sorterte listen med `sorted()`, og en løkke i menyen som skriver ut hver dato.

**6. "Hjelp meg å beskrive bruken av KI i README.md, kort og på norsk."**
Svar: En kort seksjon på norsk med spørsmålene mine (oversatt fra ukrainsk), en kort oppsummering av hvert svar og en liste over hva KI hjalp med.

### Hva KI hjalp med

- Forklarte feil i koden: listen ble opprettet i løkken, `return` og `print` hadde feil innrykk, og datoene ble sortert som tekst.
- Foreslo å bruke `datetime`, `sorted()` og å dele opp funksjonene etter ansvar.
- Laget et utkast til testtabellen, som jeg kontrollerte ved å kjøre programmet.
- Hjalp med å skrive, oversette til norsk og formatere README.md.




# Oppgave 4 – Les, analyser og håndter CSV-data

## Oppgave 4.1 – Les og kontroller data

Jeg brukte `csv.DictReader` for å lese `supporthenvendelser.csv` rad for rad. Filen åpnes med UTF-8-koding og `with open()` slik at filen lukkes automatisk etter bruk.

Jeg kontrollerte at alle feltene har en verdi, at `id` er et positivt heltall, at `minutes` er et heltall på null eller mer, og at `is_resolved` er enten `yes` eller `no`.

Ugyldige rader hoppes over med `continue`, og en feilmelding med radnummer og problemet vises i terminalen. Jeg brukte `try/except` for `FileNotFoundError` og `ValueError` ved konvertering til heltall.

## Oppgave 4.2 – Analyser data

Jeg brukte bare de gyldige radene til analysen. Programmet beregner:

* antall gyldige henvendelser
* antall henvendelser i hver kategori
* samlet og gjennomsnittlig tidsbruk
* antall løste og uløste henvendelser
* kategorien med flest henvendelser
* uløste henvendelser sortert etter tidsbruk, med den mest tidkrevende først

Gjennomsnittlig tid vises med én desimal.

## Oppgave 4.3 – Skriv rapport

Programmet oppretter `support-rapport.txt` eller overskriver filen hvis den allerede finnes. Rapporten inneholder resultatene fra analysen med tydelige overskrifter.

Feilmeldinger for ugyldige CSV-rader vises bare i terminalen og skrives ikke til rapporten.

## Oppgave 4.4 – Finn og rett feil

Jeg fant og rettet fire feil i funksjonen.

1. Jeg endret `=` til `==`. Ett likhetstegn brukes for å tilordne en verdi, mens to likhetstegn brukes for å sammenligne verdier.

2. Jeg endret `total = request["minutes"]` til `total += request["minutes"]`. Den første koden erstattet `total` for hver iterasjon. Jeg måtte legge til minuttene fra hver løste henvendelse for å få den totale tiden.

3. Jeg endret `return total_minutes` til `return total`, fordi `total_minutes` ikke var definert i funksjonen.

4. Jeg endret funksjonskallet til `sum_resolved_minutes(valid_requests)`, fordi funksjonen trenger listen med gyldige henvendelser som argument.

Etter endringene fungerer funksjonen og returnerer total tid for løste henvendelser.

## Bruk av kunstig intelligens

Jeg brukte ChatGPT som støtte under arbeidet. Følgende forklaringer fra AI påvirket løsningen min:

* Jeg fikk forklart hvordan `csv.DictReader` fungerer, og hvordan CSV-rader kan leses som dictionaries.
* Jeg fikk forklart hvordan `continue` kan brukes for å hoppe over en ugyldig rad og fortsette med neste rad.
* Jeg fikk forklart hvordan `sorted()` fungerer med `key=lambda`, slik at jeg kunne sortere uløste henvendelser etter tidsbruk.
* Jeg fikk forklart hvordan formatering med `<` og `>` fungerer når jeg skriver tabellen til rapportfilen, for eksempel `{category:<15}` og `{count:>5}`.
* I oppgave 4.4 fikk jeg forklart type hints i funksjonen, blant annet `list[dict[str, str | int]]` og `-> int`, og hva pilen betyr.
