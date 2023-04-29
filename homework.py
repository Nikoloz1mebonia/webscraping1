import requests
from bs4 import BeautifulSoup
for page in range(1,3):
    url = f"https://biblusi.ge/products?category=291&page={page}"
    r = requests.get(url)
    print(r.status_code)
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    body = soup.find("body")
    nuxt = body.find("div",id="__nuxt")
    layout = nuxt.find("div",id="__layout")
    brand = layout.find("div")
    NUXT = brand.find("div",{"class":"books w-100 w-md-90 mx-auto NUXT"})
    w100 = NUXT.find("div",{"class":"w-90 w-md-100 mx-auto"})
    overlay = w100.find("div",{"class":"b-overlay-wrap position-relative mt-1_875rem"})
    row = overlay.find("div",{"class":"row"})
    mb = row.find("div",{"class":"mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6"})
    position = mb.find("div",{"class":"position-relative"})
    rounded = position.find("div",{"class":"rounded-0_375rem overflow-hidden"})
    bg = rounded.find("div")
    height = bg.find("div")
    print(height.text)
