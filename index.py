from flask import Flask,render_template


app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
   return render_template("index.html")


app.run(host="0.0.0.0",port=1988,debug=True)
