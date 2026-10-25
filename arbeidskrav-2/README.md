### Viktoriia Protasova

# Nettbutikk – database

I denne oppgaven har jeg laget en database for en liten nettbutikk med tabellene `customers`, `products` og `orders`.

Databasesystem jeg har brukt: MySQL

## Slik kjører du løsningen

1. `[filnavn].sql` – jeg oppretter databasen og tabellene her
2. `[filnavn].sql` – jeg legger inn eksempeldata her

## Merknad om relasjonene

Jeg la merke til at diagrammet i oppgaven og teksten i oppgaven ikke sier det samme. Diagrammet viser `1..n` (kråkefot med strek) på `orders`-siden, som betyr at en kunde eller et produkt har minst én bestilling. Teksten sier derimot `0..*`: en kunde kan ha 0 til mange bestillinger, og et produkt kan forekomme i 0 til mange bestillinger.

Jeg har fulgt teksten. Min antakelse er at diagrammet er laget automatisk av et verktøy som ikke vet om en kunde eller et produkt må ha en bestilling.

Slik har jeg løst det i databasen:

- `customer_id` og `product_id` i `orders` er fremmednøkler og `NOT NULL`. Da tilhører hver bestilling nøyaktig én kunde og ett produkt.
- Jeg har ikke laget noen regel som krever at en kunde eller et produkt har en bestilling, så de kan eksistere uten bestillinger.
- Valg jeg har tatt:
`customer_id` , `product_id` og `order_id` er PRIMARY KEY og AUTO_INCREMENT. Jeg har likevel skrevet NOT NULL eksplisitt. En primærnøkkel kan aldri være NULL, så det er egentlig overflødig, men da stemmer tabellen med diagrammet i oppgaven.

## Bruk av KI

Jeg har brukt KI (Claude) som støtteverktøy. Jeg bestemte at KI ikke skal skrive SQL-kode for meg, men bare forklare og gi hint. KI har skrevet utkastet til denne README-filen, og jeg har lest gjennom og tilpasset den.

Jeg var den som la merke til at diagrammet ikke stemte med teksten. Jeg forventet 0..* med kråkefot, men diagrammet viser 1..n. KI bekreftet forskjellen. Jeg valgte å følge oppgaveteksten, ikke diagrammet.

