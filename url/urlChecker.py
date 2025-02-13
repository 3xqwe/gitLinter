import requests 

def urlChecker(url):
    import requests

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'}

    response = requests.get(url, headers=headers)

    if (response.status_code == 200) and (response.headers["Server"] == "GitHub.com"):
        return True
    else:
        return False


