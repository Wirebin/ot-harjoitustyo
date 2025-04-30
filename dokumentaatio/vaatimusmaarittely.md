# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on pelattava ristinollapeli. Sitä voi pelata kahden henkilön kesken. Perinteisen ristinollan sijaan pelissä pelataan yhdeksän eri 3x3 ristinollapeliä, joiden tulokset muodostavat yhden ison 3x3 ristinollapelin.

## Perusversion toiminnallisuudet
### Aloitusruutu
- Näytöllä on "Aloita" nappi, jota painamalla peli alkaa. **(Tehty)**

### Pelinäkymä
- Näytöllä on yhdeksän 3x3 pelilautaa, jotka ovat erillisiä ristinolla pelejä. **(Tehty)**
- Ensimmäinen pelaaja aloittaa valitsemalla jonkin pelilaudoista ja laittamalla rastin johonkin sen 3x3 ruutuun. **(Tehty)**
- Toinen pelaaja joutuu tämän jälkeen pelaamaan siinä pelilaudassa, joka vastaa ensimmäisen pelaajan asettaman ristin sijaintia. 
- Kun pelaaja voittaa yhden yhdeksästä pelistä, se merkitään hänelle. Jos tapahtuu tasapeli, kyseinen pelilauta otetaan pois lopullisesta pelistä. **(Tehty)**
- Jos pelaaja valitsee ruudun, jossa ei voi enää pelata (esim. kun kyseisen ruudun peli on jo päättynyt), saa seuraava pelaaja valita vapaasti mihin pelilautaan hän pelaa.
- Peli jatkuu näin, kunnes toinen pelaajista voittaa pääpelin tai kun tulee tasapeli. **(Tehty)**

### Tulosruutu
- Näytöllä ilmoitetaan kuka voitti.
- Nappi, josta voi aloittaa pelin uudestaan. **(Tehty)**

## Jatkokehitysideoita
Perusversion jälkeen tehdyt lisäykset ajan salliessa:
- Peliohjeet alkuruutuun.
- Mahdollisuus pelata yksinpeliä bottia vastaan.
- Bottia vastaan pelaessa voi valita vaikeustason: helppo, keskitaso, vaikea.
