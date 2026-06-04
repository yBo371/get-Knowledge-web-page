import trafilatura

url = "https://blog.cloudflare.com"

html = trafilatura.fetch_url(url)

text = trafilatura.extract(
    html,
    output_format="markdown"
)

print(text[:2000])