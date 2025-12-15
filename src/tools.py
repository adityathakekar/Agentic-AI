
from duckduckgo_search import DDGS

def search_web(query: str, max_results=3):
    print(f"   🔎 [TOOL] Searching: '{query}'...")
    try:
        results = DDGS().text(query, max_results=max_results)
        if not results: return "No results found."
        return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Search Error: {e}"
