import requests
from config.config import SERP_API_KEY

def search_web(query):
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
    response = requests.get(url)
    data = response.json()
    results = data.get("organic_results", [])
    return "\n".join([res["title"] + ": " + res["link"] for res in results[:3]])
