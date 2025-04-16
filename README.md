# Ultimate ristinolla

Sovelluksena toimii peli nimeltä "Ultimate ristinolla".
Peli on toiminnaltaan samankaltainen kuin tavallinen ristinolla, mutta normaalista poiketen siinä pelataan yhdeksää eri ristinollapeliä joiden lopputulos muodostaa yhden ison pelin. Peli on tällä hetkellä suunniteltu pelattavaksi kahden ihmisen kesken.

## Dokumentaatio
[- Laskarit](laskarit/)\
[- Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)\
[- Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)\
[- Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)\
[- Changelog](dokumentaatio/changelog.md)

## Asennus
1. Kopioi projekti itsellesi komennolla:
```bash
git clone https://github.com/Wirebin/ot-harjoitustyo.git
```

2. Asenna projektin riippuvuudet päähakemiston sisällä:
```bash
poetry install --no-root
```

3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suoritus
Ohjelman pystyy suorittamaan komennolla:
```bash
poetry run invoke start
```

### Testaus 
Suorita testit komennolla:
```bash
poetry run invoke test
```

### Testikattavuus
Luo testikattavuusraportti komennolla:
```bash
poetry run invoke coverage
```

### Pylint
Suorita pylint komennolla:
```bash
poetry run invoke lint
```
