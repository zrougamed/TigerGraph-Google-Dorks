from flask import Flask,render_template,request
import requests as web

app = Flask(__name__)
START = 0
def dorker(keySearch,keyMail,keySites):
   
   CX_ID = "6de800d51f748f99f"
   API_KEY = "AIzaSyALJZaTRZBbQzwBI21da1d9qgSVpim28sQ"

   STR_SEARCH = '"{}"++"{}"'.format(keySearch,keyMail[0])
   LINKED_IN = '+-intitle:"profiles"+-inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'
   if 'lin' in keySites:
      STR_SEARCH += LINKED_IN
   print(STR_SEARCH)
   url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&start={}&q={}"
   res = web.get(url.format(API_KEY,CX_ID,START,STR_SEARCH)).json()
   return res 



@app.route("/",methods=["GET","POST"])
def index():
   if request.method == "POST":
      mailSource = request.form.getlist('mailSource')
      print(mailSource)

      searchSource = request.form.getlist('searchSource')
      print(searchSource)

      keysSource = request.form.get("keysSource")
      print(keysSource)
      res = dorker(keysSource,mailSource,searchSource)
      return res
   return render_template("index.html")


app.run(host="0.0.0.0",port=1988,debug=True)
