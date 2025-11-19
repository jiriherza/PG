import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najde ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nacte url, ktere vrati jako seznam pomoci return
    """
    hrefs = []

    # stáhnout obsah URL
    response = requests.get(url)

    # ověření status kódu
    if response.status_code != 200:
        raise Exception(f"Chyba pri stahovani URL, status code = {response.status_code}")

    # získání obsahu stránky jako text
    html = response.content.decode('utf-8')

    # rozdělíme HTML na části obsahující <a
    parts = html.split('<a ')
    for part in parts[1:]:
        if 'href="' in part:
            start = part.find('href="') + 6
            end = part.find('"', start)
            if end > start:
                link = part[start:end]
                hrefs.append(link)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")