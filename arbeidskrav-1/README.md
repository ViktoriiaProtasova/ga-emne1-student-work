### Bruk av KI

KI (ChatGPT) er brukt som hjelpemiddel i arbeidet. Nedenfor dokumenteres
forespørsler og svar som helt eller delvis har påvirket løsningen.

### Oppgave 1.1 – Beregn tidsbruk

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
