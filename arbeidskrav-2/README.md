# Nettbutikk – database

**Viktoriia Protasova**

I denne oppgaven har jeg laget en database for en liten nettbutikk med tabellene `customers`, `products` og `orders`.

**Databasesystem:** MySQL

## Filer og rekkefølge

Jeg har delt løsningen i tre filer som kjøres i denne rekkefølgen:

1. `oppgave-1-database.sql` – oppretter databasen og tabellene. Filen starter med `DROP DATABASE IF EXISTS nettbutikk;`, slik at den kan kjøres på nytt uten å slette databasen manuelt.
2. `oppgave-2-database.sql` – legger inn eksempeldata.
3. `oppgave-3-sporringer.sql` – inneholder SELECT-spørringene jeg bruker til å utforske dataene.

## Merknad om relasjonene

Jeg la merke til at diagrammet i oppgaven og teksten i oppgaven ikke sier det samme. Diagrammet viser `1..n` (kråkefot med strek) på `orders`-siden, som betyr at en kunde eller et produkt har minst én bestilling. Teksten sier derimot `0..*`: en kunde kan ha 0 til mange bestillinger, og et produkt kan forekomme i 0 til mange bestillinger.

Jeg har fulgt teksten. KI foreslo som forklaring at diagrammet trolig er laget automatisk av et verktøy som ikke vet om en kunde eller et produkt må ha en bestilling. Jeg har ikke kunnet bekrefte dette, så det er en antakelse.

Slik har jeg løst det i databasen:

- `customer_id` og `product_id` i `orders` er fremmednøkler og `NOT NULL`. Da tilhører hver bestilling nøyaktig én kunde og ett produkt.
- Jeg har ikke laget noen regel som krever at en kunde eller et produkt har en bestilling, så de kan eksistere uten bestillinger.

## Valg jeg har tatt

- `customer_id`, `product_id` og `order_id` er `PRIMARY KEY` og `AUTO_INCREMENT`. Jeg har likevel skrevet `NOT NULL` eksplisitt. En primærnøkkel kan aldri være `NULL`, så det er egentlig overflødig, men da stemmer tabellene med diagrammet i oppgaven.
- `email` i `customers` har en `UNIQUE`-begrensning, slik oppgaven krever.
- I spørringen som teller bestillinger per kunde grupperer jeg på `customers.customer_id`, `first_name` og `last_name`. `customer_id` er primærnøkkel og identifiserer kunden entydig. Jeg grupperte først bare på etternavn, men da ville to kunder med samme etternavn blitt slått sammen til én rad, og antall bestillinger ville blitt feil. MySQL tillater å gruppere bare på `customer_id`, siden fornavn og etternavn avhenger av primærnøkkelen. Likevel tok jeg med alle tre kolonnene, fordi vi har lært på forelesningen at alle kolonner i `SELECT` som ikke står i en aggregatfunksjon, også skal stå i `GROUP BY`. Da fungerer spørringen i alle databasesystemer.

## Bruk av KI

Jeg har brukt KI (Claude) som støtteverktøy. Jeg bestemte at KI ikke skulle skrive SQL-kode for meg, men bare forklare og gi hint. Det eneste unntaket er én spørring i oppgave 15, se under. Jeg brukte KI til å lage utkastet til denne README-filen, og jeg har lest gjennom og tilpasset den.

- Jeg la merke til at diagrammet ikke stemte med teksten. Jeg forventet `0..*` med kråkefot, men diagrammet viser `1..n`. Jeg spurte KI om symbolene og fikk bekreftet forskjellen. Jeg valgte å følge oppgaveteksten, ikke diagrammet.
- Jeg la merke til at den korte versjonen (bare `customer_id` i `GROUP BY`) ikke stemte med regelen fra forelesningen, og spurte KI om det. Jeg fikk forklart hvorfor MySQL likevel tillater det, og jeg bestemte selv å ta med alle tre kolonnene.
- I oppgave 15 (høyest samlet verdi per kunde) fikk jeg hint om at min første spørring ikke summerte bestillingene per kunde. Jeg skrev selv den rettede versjonen med `LIMIT 1`.
- For å vise alle kunder hvis flere har lik høyeste verdi, skrev jeg selv hovedspørringen, og med veiledning fra KI laget jeg delen som finner den høyeste samlede verdien (MAX i en underspørring). Jeg klarte ikke å sette alt sammen med HAVING i riktig rekkefølge, så KI skrev den ferdig sammensatte spørringen. Denne koden er skrevet av KI, og jeg har valgt å ta den med i besvarelsen. Jeg har gått gjennom spørringen del for del og forstår hvordan den fungerer.
- Jeg fikk også forklaringer og hint om hvordan scriptet kan kjøres på nytt (`DROP DATABASE IF EXISTS`), forskjellen på `PRIMARY KEY` og `UNIQUE`, at `NOT NULL` er overflødig på en primærnøkkel, og at det var feil å gruppere på etternavn i spørringen om bestillinger per kunde.
- Legge til en bestilling i `orders`-tabellen: KI-en forklarte hvordan man kan bruke subqueries i en INSERT.
- Sjekke priser før en UPDATE: KI-en forklarte at man vanligvis kjører en egen SELECT først for å se hva som vil endres, og at man bør bruke WHERE og gjerne en transaksjon for å kunne angre endringer.