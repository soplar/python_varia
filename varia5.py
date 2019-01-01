def web_lookup(url, saved = {}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page



# @cache is actually just syntactic sugar for the following:
# web_lookup = cache(web_lookup)

@cache
def web_lookup(url):
    page = urlopen(url)
    try:        
        return page.read()
    finally:
        page.close()