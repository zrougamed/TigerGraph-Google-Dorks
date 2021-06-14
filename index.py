from flask import Flask,render_template,request


app = Flask(__name__)
START = 0
def dorker(keySearch,keyMail,keySites):
   
   CX_ID = "6de800d51f748f99f"
   API_KEY = "AIzaSyALJZaTRZBbQzwBI21da1d9qgSVpim28sQ"

   STR_SEARCH = '"{}"++"{}"'.format(keySearch)
   LINKED_IN = '+-intitle:"profiles"+-inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'
   url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&start={}&q={}"



@app.route("/",methods=["GET","POST"])
def index():
   if request.method == "POST":
      print(request.form)
      for e in request.form:
         print(e)
      return request.form
   return render_template("index.html")


app.run(host="0.0.0.0",port=1988,debug=True)
