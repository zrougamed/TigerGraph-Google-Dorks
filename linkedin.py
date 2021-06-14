import requests as web
import time 

f = open("res.txt","a")

CX_ID = "6de800d51f748f99f"
API_KEY = "AIzaSyALJZaTRZBbQzwBI21da1d9qgSVpim28sQ"
STR_SEARCH = '"Dentist"++"%40outlook.com"+-intitle:"profiles"+-inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'

url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&start={}&q={}"


def getPage(index):
    try:
        print(url.format(API_KEY,CX_ID,index,STR_SEARCH))
        res = web.get(url.format(API_KEY,CX_ID,index,STR_SEARCH)).json()
        for item in res["items"]:
            print(item["title"])
            print(item["link"])
            try:
                dec = item["pagemap"]["metatags"][0]["og:description"]
            except:
                dec = ""
            f.write('"{}";"{}";"{}"\n'.format(item["title"],item["link"],dec))
        try:
            if res["queries"]["nextPage"][0]["startIndex"] != None:
                print("############################### NEXT ####################")
                getPage(str(res["queries"]["nextPage"][0]["startIndex"]))
            else:
                return True
        except Exception as e:
            print(e)
            return True
        time.sleep(1)
    except Exception as e:
        print(e)
        print(res)
        f.close()



getPage("1")
f.close()


# {'error': {'code': 429, 'message': "Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'customsearch.googleapis.com' for consumer 'project_number:385042346764'.", 'errors': [{'message': "Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'customsearch.googleapis.com' for consumer 'project_number:385042346764'.", 'domain': 'global', 'reason': 'rateLimitExceeded'}], 'status': 'RESOURCE_EXHAUSTED'}}
