# **_WalletTracker_**

Sovelluksella käyttäjä pystyy seuraamaan omaa rahankulutustaan ja luomaan budjetteja eri aikarajojen mukaan. Käyttäjä pystyy luomaan oman käyttäjätunnuksen ja salasanan ja kirjautumalla sisään hän pystyy syöttämään tuloja ja menoja. Sovellus seuraa käyttäjän rahankulutusta ja budjettien ylittämistä 

## Python-versio

Sovelluksen toimintaa on testattu Python-versiolla `3.8`.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Release 1](https://github.com/Honkajo/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/Honkajo/ot-harjoitustyo/releases/tag/viikko6)
- [Lopullinen palautus](https://github.com/Honkajo/ot-harjoitustyo/releases/tag/final_release)

## Komentorivitoiminnot

Ohjelman pystyy suorittaa komennolla:

```bash
poetry run invoke start
```
Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```
Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```
Pylint-tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
