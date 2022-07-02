## INS

`https://city-index-api.herokuapp.com/api/ins/json/<matrix_name>/?query=Localitati:<option1>,<option2>;Judete:<option1>,<option2>,<option3>`Ad

### Exemplu 
`https://city-index-api.herokuapp.com/api/ins/json/POP107D/?query=Sexe:Masculin,Feminin;Judete:Alba;Localitati:1017%20MUNICIPIUL%20ALBA%20IULIA,2915%20ORAS%20BAIA%20DE%20ARIES;`


## CFR

`https://city-index-api.herokuapp.com/api/cfr/?city=<statie>&date=<data>` sau
`https://city-index-api.herokuapp.com/api/cfr/?city=<statie>` pentru date=azi

| Url                                                                               | Description                                                                   |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| https://city-index-api.herokuapp.com/api/cfr/?city=Bucuresti-Nord                 | trenurile care pleaca sau vin din statia `Bucuresti-Nord` in ziua de azi      |
| https://city-index-api.herokuapp.com/api/cfr/?city=Bucuresti-Nord&date=29.06.2022 | Trenurile care pleaca sau vin in statia `Bucuresti Nord` pe data `29.06.2022` |
