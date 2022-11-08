from flask import Flask, render_template, jsonify, request, redirect, url_for

from models import User, ModelUser
from settings import Connect

app = Flask(__name__, static_url_path='/')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getUsers", methods=["POST", "GET"])
def getUsers():
    if request.method == "POST":
        db = Connect()
        conn = db.getConnect()
        results = ModelUser.getUsers(conn)
        
        return jsonify({"data": results})
    else:
        return redirect( url_for('home') )

@app.route("/getUser", methods=["POST", "GET"])
def getUser():
    if request.method == "POST":
        id = request.form['id']
        db = Connect()
        conn = db.getConnect()
        results = ModelUser.getUser(conn, id)
        return jsonify({"data": results})
    else:
        return redirect( url_for('home') )
   
    
@app.route("/add", methods=["POST", "GET"])
def addUser():
    if request.method == "POST":
        user = User(request.form['username'], request.form['fullname'])
        db = Connect()
        conn = db.getConnect()
        
        result = ModelUser.addUser(conn,user)
        
        return jsonify({"message": "okey", "insertedRow":result})
    else:
        return redirect( url_for('home') )


@app.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method == "POST":
        id = request.form['id']
        db = Connect()
        conn = db.getConnect()
        result = ModelUser.deleteUser(conn, id)
    
        return jsonify({"message": "okey", "deleted":result})
    else:
        return redirect( url_for('home') )

if __name__ == "__main__":
    app.run(debug=True)