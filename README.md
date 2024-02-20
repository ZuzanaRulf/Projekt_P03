# Election Scraper

Tento skript slouží k scrapování výsledků voleb z roku 2017 z webové stránky [volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Jak používat skript

1. **Nainstalujte knihovny**: Nejprve si nainstalujte všechny potřebné knihovny ze souboru `requirements.txt` pomocí následujícího příkazu:

    ```bash
    python -m pip install -r requirements.txt
    ```

2. **Spusťte skript**: Skript lze spustit z příkazového řádku pomocí následujícího příkazu:

    ```bash
    python election_scraper.py <url> <output_file>
    ```

    Kde `<url>` představuje odkaz na územní celek, který chcete scrapovat, a `<output_file>` je jméno výstupního csv souboru, do kterého se budou výsledky ukládat.

## Formát výsledného souboru

Výsledný csv soubor obsahuje data oddělená čárkou a je kódován pomocí utf-8. Sloupce obsahují:

- **kód obce**
- **název obce**
- **voliči v seznamu**
- **vydané obálky**
- **platné hlasy**
- **kandidující strany** (každá strana má sloupec s počtem hlasů)


## Ukázka projektu

Pro ilustraci, zde je příklad spuštění skriptu pro [územní celek Prostějov](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103):

1. argument: [https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103)
2. argument: vysledky_prostejov.csv

#### Spuštění programu:

```bash
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"
```

#### Průběh programu:

```bash
STAHUJI DATA Z VYBRANEHO URL:  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLADAM DO SOUBORU:  vysledky_prostejov.csv
UKONCUJI election_scraper.py
```

#### Částečný výstup:

```bash
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,...
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
589284,Biskupice,238,132,131,14,0,0,9,0,5,24,2,1,1,0,0,10,2,0,34,0,0,10,0,0,0,0,19,0
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0
589306,Bousín,107,67,67,5,0,0,4,0,3,14,0,2,0,0,0,7,0,2,10,0,0,9,0,0,0,0,11,0
589314,Brodek u Konice,695,460,460,25,0,0,32,0,20,47,3,4,5,0,0,38,1,5,144,0,0,60,1,0,1,0,72,2
589322,Brodek u Prostějova,1 224,655,655,54,0,0,42,0,21,61,5,4,11,1,2,57,0,22,202,0,1,53,2,1,3,4,107,2
589331,Březsko,178,111,111,9,1,0,9,0,6,3,0,3,1,0,0,10,1,2,36,0,0,17,0,0,0,0,13,0
...
```
