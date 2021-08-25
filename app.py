from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') 
def index(): 
	return render_template("index.html")

@app.route("/about") 
def about(): 
	return render_template("about.html") 

@app.route("/millengine") 
def millengine(): 
	return render_template("millengine.html") 

@app.route("/QueenAnne") 
def QueenAnne(): 
	return render_template("QueenAnne.html")

@app.route("/shakertable") 
def shakertable(): 
	return render_template("shakertable.html") 

@app.route("/aerospike") 
def aerospike(): 
	return render_template("aerospike.html") 

@app.route("/turbofan") 
def turbofan(): 
	return render_template("turbofan.html")

@app.route("/steamengine") 
def steamengine(): 
	return render_template("steamengine.html")

@app.route("/entu") 
def entu(): 
	return render_template("entu.html")