import requests as web
import time 
f = open("res.txt","w+")

# 7390
try:
    for i in range(739):
        page_num = str((i*10)+1)
        res = web.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyALJZaTRZBbQzwBI21da1d9qgSVpim28sQ&cx=6de800d51f748f99f&start={}&q=tigergraph+site%3Amedium.com".format(page_num)).json()
        print(str(i))
        for item in res["items"]:
            print(item["title"])
            print(item["link"])
            try:
                dec = item["pagemap"]["metatags"][0]["og:description"]
            except:
                dec = ""
            f.write('"{}";"{}";"{}"\n'.format(item["title"],item["link"],dec))

        time.sleep(1)
except Exception as e:
    print(e)
    print(res)
    f.close()

f.close()