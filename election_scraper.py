"""

projekt_3.py: třetí projekt do Engeto Online Python Akademie

Elections Scraper

author: Zuzana Rulfová

email: rulfova.zuzana@gmail.com

discord: zuzana576

"""

import sys
import bs4
import requests
from bs4 import BeautifulSoup
import csv


def zpracuj_odpoved_serveru(url: str) -> BeautifulSoup:
    "Načte stránku a převede ji na BS"

    response = requests.get(url)
    if response.status_code != 200:
        print("Nepodařilo se načíst stránku. Zkontrolujte zadanou URL.")
    return BeautifulSoup(response.text, "html.parser")


def najdi_info_o_obci(soup: BeautifulSoup) -> list[dict]:
    "Pro každou obec dohledá a zapíše kod obce, jméno a odkaz na další výsledky voleb"

    tabulky = soup.find_all("table", {"class": "table"})
    vysledky = []
    for tabulka in tabulky:
        vsechny_td = tabulka.find_all("td",  {"class": "overflow_name"})
        vsechny_tr = [td.find_parent("tr") for td in vsechny_td]  # Najdeme příslušné řádky
        # Projdeme všechny relevantní řádky tabulky
        for tr in vsechny_tr: 
            radek = tr.find_all("td")
            # Najdeme kód obce
            kod_obce = radek[0].text.strip()
            # Najdeme jméno obce
            jmeno_obce = radek[1].text.strip()
            # Najdeme odkaz na další výsledky
            odkaz = radek[0].find("a")["href"]
            # Přidáme výsledek do seznamu
            vysledky.append({
                "kod_obce": kod_obce,
                "jmeno_obce": jmeno_obce,
                "odkaz": odkaz
            })
    return vysledky

def vysledky_stran(soup: BeautifulSoup) -> list[dict]:
    "Získání tabulky s výsledky pro jednotlivé politické strany"

    # Nalezení všech tabulek s třídou "table"
    tabulky = soup.find_all("table", {"class": "table"})
    vysledky = []
    for tabulka in tabulky:
        vsechny_td = tabulka.find_all("td",  {"class": "overflow_name"})
        vsechny_tr = [td.find_parent("tr") for td in vsechny_td]  # Najdeme příslušné řádky
        # Projdeme všechny relevantní řádky tabulky
        for tr in vsechny_tr: 
            radek = tr.find_all("td")
            # Najdeme kód obce
            nazev_strany = radek[1].text.strip()
            # Najdeme jméno obce
            vysledky_strany = radek[2].text.strip()

            # Přidáme výsledek do seznamu
            vysledky.append({
                "nazev_strany": nazev_strany,
                "vysledky_strany": vysledky_strany
            })
    return vysledky

def uloz_vysledky_do_csv(vysledky_voleb):
    "Zapíše tabulku s vásledky do csv souboru"
    print("UKLADAM DO SOUBORU: ",output_file)
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        klice = vysledky_voleb[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=klice)
        writer.writeheader()
        writer.writerows(vysledky_voleb)


def prochazeni_stranek_obci(informace: list[dict]) -> list[dict]:
    "Prochází výsledky voleb pro obce a zapisuje výsledky do výsledné tabulky"
    odkazy = [info["odkaz"] for info in informace]
    kody = [info["kod_obce"] for info in informace]
    jmena = [info["jmeno_obce"] for info in informace]
    vysledky = []

     # Nalezení odkazů na jednotlivé obce
    index = 0
    for link in odkazy:        
        obec_url = "https://volby.cz/pls/ps2017nss/" + link
        # Pro každou obec získáme výsledky hlasování
        obec_soup = zpracuj_odpoved_serveru(obec_url)
 
        # Získání kódu obce
        obec_kod = kody[index]
    
        # Získání názvu obce
        obec_nazev = jmena[index]
        
        # Získání počtu voličů v seznamu
        volici_v_seznamu = obec_soup.find_all("td", {"class": "cislo"})[3].text.strip()

        # Získání počtu vydaných obálek
        vydane_obalky = obec_soup.find_all("td", {"class": "cislo"})[6].text.strip()

        # Získání počtu platných hlasů
        platne_hlasy = obec_soup.find_all("td", {"class": "cislo"})[7].text.strip()

        # Získání názvů stran a výsledků
        hlasovani = vysledky_stran(obec_soup)
        jmena_stran = [hlas["nazev_strany"] for hlas in hlasovani]
        hlasy_stran = [hlas["vysledky_strany"] for hlas in hlasovani]

        vysledky.append({
            "Code": obec_kod,
            "Location": obec_nazev,
            "Registered": volici_v_seznamu,
            "Envelopes": vydane_obalky,
            "Valid": platne_hlasy,
            **{strana: hlasy for strana, hlasy in zip(jmena_stran, hlasy_stran)}
        })
        index += 1
    return vysledky
            
    

def main(url, output_file):
    zakladni_url = "https://volby.cz/pls/ps2017nss/"

    # Kontrola vložené url adresy
    if zakladni_url not in url:
        print("Chybný formát URL adresy. Zadejte platnou URL adresu územního celku.")
        sys.exit(1)
    else:
        print("STAHUJI DATA Z VYBRANEHO URL: ",url)

    soup = zpracuj_odpoved_serveru(url)
    informace = najdi_info_o_obci(soup)
    vysledky_voleb = prochazeni_stranek_obci(informace)
    uloz_vysledky_do_csv(vysledky_voleb)
    print("UKONCUJI election_scraper.py")
    


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python election_scraper.py <url> <output_file>")
        sys.exit(1)
    url = sys.argv[1]
    output_file = sys.argv[2]

    main(url, output_file)
