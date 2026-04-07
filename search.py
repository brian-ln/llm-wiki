import urllib.request
import urllib.parse
import re
import html

def search_ddg(query):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html_content = urllib.request.urlopen(req).read().decode('utf-8')
        links = re.findall(r'<a class="result__url" href="([^"]+)">([^<]+)</a>', html_content)
        for href, text in links[:5]:
            print(f"{html.unescape(text).strip()} - {urllib.parse.unquote(href)}")
    except Exception as e:
        print("Error:", e)

print("--- Mamba SSM ---")
search_ddg("Mamba State Space Model architecture arxiv")
print("\n--- Neural ISAs ---")
search_ddg("\"Software 2.0\" OR \"differentiable programming\" neural architecture \"instruction set\"")
