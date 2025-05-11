# Testausdokumentti

Sovellusta on testattu automaattisesti ja manuaalisesti. Sovelluksen automaattisessa testauksessa on käytetty unittest-kirjastoa.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikkaa testataan useissa erillisissä tiedostoissa. Nämä tiedostot keskittyvät johonkin tiettyyn osaan sovelluslogiikasta. Ne sisältävät seke yksikkö- sekä integraatiotestauksia. Esimerkiksi `main_board_test.py` tiedostossa on yksittäisiä testejä liittyen `MainBoard` luokkaan, mutta myös testejä kuten `test_sub_board_list_size()`, joka vaatii myös `SubBoard` luokan.

### Manuaalitestaus

Sovellus on testattu toimivaksi Linux käyttöjärjestelmässä. Sen lisäksi monia sovelluksen ominaisuuksia on testattu normaalin käytön kautta sovelluskehityksen edetessä.

### Testauskattavuus 
![](/dokumentaatio/assets/coverage.png)

Testauskattavuus on kokonaisuudessaan 84%. Testauksesta on jätetty pois `main.py` ja `shapes.py` tiedostot, sillä ne hoitavat pelin piirtämistä ja konfigurointia. Testattavista tiedostoista on myös ohitettu kaikki `draw()` funktiot, koska ne hoitavat myös vain käyttöliittymän piirtämistä eivätkä sisällä itsessään mitään logiikkaa.
