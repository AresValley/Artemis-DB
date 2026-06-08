import json
import requests

API_URL = "https://www.sigidwiki.com/api.php"
PAGE_TITLE = "Low Rate Picture Transmission (LRPT)"


params_testo = {
    "action": "query",
    "prop": "revisions",
    "titles": PAGE_TITLE,
    "rvprop": "content",
    "format": "json",
}

print("2. Estrazione e pulizia del testo originale della pagina...")
res_testo = requests.get(API_URL, params=params_testo)

data_testo = res_testo.json()
pages = data_testo["query"]["pages"]
page_id = list(pages.keys())[0]

wikitext_grezzo = pages[page_id]["revisions"][0]["*"]

print(wikitext_grezzo)