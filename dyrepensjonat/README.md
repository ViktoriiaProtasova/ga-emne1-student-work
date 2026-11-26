# Dyrepensjonat

## Oppgave 1 – Opprett database og implementer datamodellen

### Implementering av ER-diagrammet

Jeg har opprettet en MySQL-database med navnet `dyrepensjonat` basert på ER-diagrammet i eksamensoppgaven.

| Tabell   | Beskrivelse                                         |
|----------|-----------------------------------------------------|
| `owners` | Informasjon om eiere og kontaktopplysninger.        |
| `pets`   | Informasjon om kjæledyr og deres eiere.             |
| `rooms`  | Informasjon om romnummer, romtype og pris per døgn. |
| `stays`  | Informasjon om opphold, kjæledyr, rom og datoer.    |

### Primærnøkler og relasjoner

Alle tabellene har en primærnøkkel (`PRIMARY KEY`). Jeg har lagt til `AUTO_INCREMENT` for automatisk generering av
ID-er.

Relasjonene er implementert med fremmednøkler (`FOREIGN KEY`):

- `pets.owner_id` refererer til `owners.owner_id`.
- `stays.pet_id` refererer til `pets.pet_id`.
- `stays.room_id` refererer til `rooms.room_id`.

Alle tre relasjonene er én-til-mange-relasjoner (1:N). Fremmednøklene sikrer at refererte eiere, kjæledyr og rom finnes
i databasen.

### Datatyper og begrensninger

Datatypene følger ER-diagrammet:

- `INT` for primærnøkler og fremmednøkler.
- `VARCHAR` for tekstverdier og kontaktopplysninger.
- `DATE` for ankomst- og avreisedato.
- `DECIMAL(8,2)` for pris per døgn.

Telefonnummer lagres som `VARCHAR` fordi det kan inneholde landskode og innledende nuller.

Alle kolonnene har `NOT NULL` i samsvar med ER-diagrammet. I tillegg til `AUTO_INCREMENT` har jeg lagt til `UNIQUE` på
`room_number` for å sikre at hvert rom har et unikt romnummer. Tabellstrukturen og relasjonene følger ellers
ER-diagrammet.

### Eksempeldata

SQL-scriptet inneholder følgende eksempeldata:

| Tabell     | Antall rader |
|------------|-------------:|
| `owners`   |            8 |
| `pets`     |           12 |
| `rooms`    |            8 |
| `stays`    |           15 |
| **Totalt** |       **43** |

Eksempeldataene viser at en eier kan ha flere kjæledyr, at et kjæledyr kan ha flere opphold, og at et rom kan brukes i
ulike perioder. Eksempeloppholdene overlapper ikke for samme rom. Databasen har foreløpig ingen egen kontroll av
overlappende opphold eller ugyldig rekkefølge på datoene.

### Kjøring av SQL-scriptet

Åpne `database.sql` i DataGrip eller en annen MySQL-klient, koble til MySQL-serveren og kjør hele scriptet.

Scriptet oppretter databasen, tabellene og eksempeldataene. Tabellene opprettes i riktig rekkefølge med hensyn til
fremmednøklene. Ved hjelp av `DROP DATABASE IF EXISTS` slettes den eksisterende databasen før den opprettes på nytt.
Scriptet er dermed laget for å kunne kjøres flere ganger uten manuell opprydding.

**Merk:** Alle eksisterende data i databasen `dyrepensjonat` slettes ved ny kjøring av hele scriptet.
