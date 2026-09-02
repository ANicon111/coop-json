import json
from urllib.request import Request, urlopen

headers = {"User-Agent": "Mozilla/5.0"}

chains_req = Request("https://api.coopdk.lobyco.net/store/mobile-app/v3/chains", headers=headers)
catalogs_req = Request("https://api.coopdk.lobyco.net/leaflets/v1/catalogs", headers=headers)

chains = json.loads(urlopen(chains_req).read().decode("utf-8"))
catalogs = json.loads(urlopen(catalogs_req).read().decode("utf-8"))

with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"chains": chains, "catalogs": catalogs}, f)

print("Saved to data.json")
