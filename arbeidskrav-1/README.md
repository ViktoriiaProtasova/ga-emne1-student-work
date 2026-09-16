
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
## Oppgave 3 – Funksjoner og dokumentasjon
### Testtilfeller

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
