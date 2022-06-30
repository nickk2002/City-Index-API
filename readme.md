##INS

`https://city-index-api.herokuapp.com/api/ins/json/<matrix_name>/<localitate>`

| Url                                                                                        | Description                                                                                                |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| https://city-index-api.herokuapp.com/api/ins/json/POP308A/1017%20MUNICIPIUL%20ALBA%20IULIA | Ia indicatorul pentru aceasta matrice si localitate                                                        |
| https://city-index-api.herokuapp.com/api/ins/json/POP308A/all                              | Toate localitatile si le afizeaza. Nu o sa functioneze pentru ca ia mai mult de 30 de secunde requestul-ul |


## CFR

`https://city-index-api.herokuapp.com/api/cfr/?city=<statie>&date=<data>` sau
`https://city-index-api.herokuapp.com/api/cfr/?city=<statie>` pentru date=azi

| Url                                                                               | Description                                                                   |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| https://city-index-api.herokuapp.com/api/cfr/?city=Bucuresti-Nord                 | trenurile care pleaca sau vin din statia `Bucuresti-Nord` in ziua de azi      |
| https://city-index-api.herokuapp.com/api/cfr/?city=Bucuresti-Nord&date=29.06.2022 | Trenurile care pleaca sau vin in statia `Bucuresti Nord` pe data `29.06.2022` |
