import requests

url = "https://www.indiatoday.in/india/story/nation-knows-congress-already-naked-pm-modi-shreds-party-over-shirtless-protest-at-ai-summit-2872474-2026-02-22"
def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

fetchAndSaveToFile(url, "data/newz.html")