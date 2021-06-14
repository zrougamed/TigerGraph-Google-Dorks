from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
   if request.method == "POST":
      print(request.form)

   return render_template("index.html")


app.run(host="0.0.0.0",port=1988,debug=True)
