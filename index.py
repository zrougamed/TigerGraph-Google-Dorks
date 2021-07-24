from flask import Flask,render_template,request, session, redirect, url_for, escape
import requests as web



app = Flask(__name__)

app.secret_key = 'qs:dklkqsopicjlaazealmzdiopqsuiouqsiojejoqsd'


@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      if request.form['username'] == "inerp" and request.form['password'] == "inerp":
         session['username'] = request.form['username']
         return redirect(url_for('index'))
      else:
         return '''
            
   <form action="" method="post">
      <p><input type="text" name="username" /></p>
      <p><input type="text" name="password" /></p>
      <p><input type="submit" value="Login" /></p>
   </form>		
         '''      
   return '''
	
   <form action="" method="post">
      <p><input type="text" name="username" /></p>
      <p><input type="text" name="password" /></p>
      <p><input type="submit" value="Login" /></p>
   </form>	
'''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))





START = 0
def dorker(keySearch,keyMail,keySites):
   
   CX_ID = "CX_ID"
   API_KEY = "API_KEY"

   STR_SEARCH = '{}++"{}"'.format(keySearch,keyMail[0])
   LINKED_IN = '+-intitle:"profiles"+-inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'
   if 'lin' in keySites:
      STR_SEARCH += LINKED_IN
   
   url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&start={}&q={}"
   print(url.format(API_KEY,CX_ID,START,STR_SEARCH))
   res = web.get(url.format(API_KEY,CX_ID,START,STR_SEARCH)).json()
   return res 



@app.route("/",methods=["GET","POST"])
def index():
   if 'username' in session:
      if session["username"] != "inerp":
         return redirect(url_for('login'))
   else:
      return redirect(url_for('login'))
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
