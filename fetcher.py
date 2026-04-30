import trafilatura

def fetch_url(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    if not text:
        raise ValueError("Could not extract text from URL")
    return text