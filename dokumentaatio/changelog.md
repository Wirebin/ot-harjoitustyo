# Changelog

## Viikko 3
- Lisätty 'Component'-luokka, joka luo jokaiselle komponentille draw ja update metodit.
- Lisätty 'Button'-luokka, jonka avulla peliin voi luoda painettavia nappuloita.
- Lisätty yleinen 'game.py' tiedosto, joka vastaa pelin suorittamisesta.
- Testattu, että 'Button'-luokka toimii oikein.

## Viikko 4
- Lisätty 'Tile'-luokka, joka on yksittäinen pelinlautan laatta.
- Lisätty 'Sub_board' ja 'Main_board'-luokat, jotka mahdollistavat pelin päätoimivuuden.
- Lisätty mahdollisuus näyttää tekstiä 'Button'-luokkaan.
- Lisätty 'States' ja 'State_Manager'-luokat, jotka vastaavat pelin eri tilojen hallinnasta.
- Testattu 'State_Manager'-luokan toimivuus.

## Viikko 5
- Koodin refaktorointi.
- Lisätty 'Shapes'-tiedosto, jossa kaksi funktiota kuvioiden tekemiseen.
- Lisätty mahdollisuus asettaa omalla vuorolla pelinappula ruudukkoon.
- Lisätty testejä 'Main_board', 'Sub_board' ja 'Tile'-luokille

## Viikko 6
- Koodin refaktorointi ja tiedostojen tarkempi jako kansioihin.
- Lisätty 'OnePressInput'-luokka, joka hoitaa pelin käyttämät hiiren syötöt.
- Lisätty mahdollisuus voittaa peli.
- Lisätty pelin lopetusruutu, jossa näkyy pelin voittaja ja mahdollisuus pelata uudestaan.

## Viikko 7
- Lisätty 'TurnManager'-luokka, joka huolehtii pelitilanteen ylläpitämisestä.
- Lisätty 'Text'-luokka helppoa tekstintekoa varten.
- Siirretty vakiomuuttujat erilliseen 'constant.py' tiedostoon.
- Ominaisuus, jossa pelinappula pitää laittaa edellisen liikkeen vastaavalle pelilaudalle.
- Viimeisten testien lisäys.
- Käyttöohjeiden teko.
- Testidokumentin teko.
- Arkkitehtuuridokumentin teko.
