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

```bash
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"

## Ukázka výstupního souboru

Níže je ukázka obsahu výstupního csv souboru:

```csv
Code,Location,Registered,Envelopes,Valis,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
589284,Biskupice,238,132,131,14,0,0,9,0,5,24,2,1,1,0,0,10,2,0,34,0,0,10,0,0,0,0,19,0
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0
589306,Bousín,107,67,67,5,0,0,4,0,3,14,0,2,0,0,0,7,0,2,10,0,0,9,0,0,0,0,11,0
589314,Brodek u Konice,695,460,460,25,0,0,32,0,20,47,3,4,5,0,0,38,1,5,144,0,0,60,1,0,1,0,72,2
589322,Brodek u Prostějova,1 224,655,655,54,0,0,42,0,21,61,5,4,11,1,2,57,0,22,202,0,1,53,2,1,3,4,107,2
589331,Březsko,178,111,111,9,1,0,9,0,6,3,0,3,1,0,0,10,1,2,36,0,0,17,0,0,0,0,13,0
589349,Budětsko,331,208,206,6,0,0,24,0,6,22,1,3,2,0,0,7,1,3,58,0,1,32,0,1,2,0,35,2
589357,Buková,264,170,169,16,0,0,19,0,3,33,2,0,3,0,0,14,0,2,35,1,0,25,0,1,0,0,15,0
589365,Čehovice,426,281,280,16,0,0,27,0,8,42,5,7,5,0,0,18,0,10,80,0,1,13,0,0,1,3,44,0
589381,Čechy pod Kosířem,814,512,512,25,1,0,66,1,20,79,7,7,6,0,0,31,2,7,140,0,0,47,0,0,0,3,70,0
589390,Čelčice,437,272,272,21,0,0,23,1,10,46,5,0,3,0,1,18,0,2,74,0,1,15,0,0,1,1,49,1
589403,Čelechovice na Hané,1 063,649,642,49,0,1,45,0,63,76,2,3,0,1,0,43,0,15,198,0,2,32,0,1,0,6,103,2
589420,Dětkovice,427,283,281,19,0,0,12,0,6,47,2,4,4,1,0,38,0,2,82,0,0,36,0,2,0,1,25,0
589438,Dobrochov,270,172,170,13,0,0,14,1,7,13,5,2,3,0,0,13,0,5,51,0,1,17,0,0,0,0,25,0
589446,Dobromilice,629,308,308,9,0,4,22,0,14,42,1,0,1,0,0,10,0,0,95,1,1,36,2,0,0,0,68,2
589454,Doloplazy,459,244,244,24,1,0,20,0,5,37,2,0,3,0,0,12,0,0,71,0,0,8,1,1,2,1,56,0
589462,Drahany,443,290,287,11,0,0,29,0,28,44,2,6,6,0,0,9,0,9,70,0,2,17,0,1,1,1,51,0
558419,Držovice,1 139,748,742,78,1,0,42,3,40,45,4,6,5,0,9,60,0,15,275,0,2,38,0,4,1,5,102,7
