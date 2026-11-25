1. Hvor leses skjemadata, hvor opprettes City-objektet, og hvor kjøres SQL?

Skjemadata leses i app.py med request.form.get (). City-objektet opprettes i database.py i funksjonen get_city (). SQL
kjøres i database.py med cursor.execute ().

2. Hvorfor sendes verdiene separat til execute (), og hvorfor trenger skriveoperasjonene commit ()?

Verdiene sendes separat for å unngå SQL-injection. commit () brukes for å lagre endringene permanent i databasen.

3. Hvorfor bruker skjemaene POST selv om SQL-kommandoene heter UPDATE og DELETE?

HTML-skjemaer støtter bare GET og POST som HTTP-metoder for innsending til serveren. POST brukes til å sende data som
skal endres eller slettes i databasen. UPDATE og DELETE er SQL-kommandoer.

4. Hva gjør 303-redirecten, og hvorfor beholder en oppdatert by samme ID?

303-redirecten sender brukeren videre med en GET-forespørsel og hindrer at skjemaet sendes på nytt ved oppdatering av
siden. Byen beholder samme ID fordi UPDATE endrer en eksisterende rad uten å opprette en ny eller endre ID-en.