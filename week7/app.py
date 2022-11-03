import mysql.connector 
from flask import Flask, redirect, render_template,request,session,url_for,Response,jsonify, flash,json,make_response
import re



app = Flask(__name__)
app.config["SECRET_KEY"]="eaf266f88f72894c90"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:thu982305@localhost/website"

mydb = mysql.connector.connect(user='root', password='thu982305',host='127.0.0.1',database='website')

mycursor = mydb.cursor(buffered=True)

regex=r"^\w[a-zA-Z@#0-9.]*$"



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=["POST"])
def register():
    
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    match_username = re.search(r'\S', username)
    match_name = re.search(r'\S', name)
    match_pw = re.search(r'\S', password)
    if match_username and match_name and match_pw:
        try:
            mycursor.execute("insert into member(name,username,password) values(%(name)s,%(username)s,%(password)s)", {"name":name, "username":username, "password":password})
            mydb.commit()
            flash('恭喜你註冊成功呀!!!')
            return redirect(url_for("index"))
        except : return redirect(url_for("error",message="帳號已經被註冊"))
    else:
        flash('請勿留白!!!!!!!!')
        return redirect(url_for("index"))

@app.route("/signin", methods=["POST"])
def signIn(): 
    name=request.form["username"]
    password=request.form["password"]
    try:
        mycursor.execute("select username, password,id  from member  where username=%(name)s and password=%(password)s", {"name":name, "password":password}) 
      #存進session
        mydb.commit()
        for (name, password,id) in mycursor:
            session["username"]=name
            session["id"] =id
            return redirect(url_for("member")) 
    except: return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

    return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))



@app.route("/member")
def member():
    if "username" in session:        
        username=session["username"]
        mycursor.execute("select name, content from member inner join  message on member.id=message.member_id order by message.time desc" ) 
        mydb.commit()
        contents=[]
        for (name,content) in mycursor:
            contents.append({"name":name,"content":content})        
        return render_template("signin.html", username=username,contents=contents)
    else:  return redirect(url_for("index"))

@app.route("/signout")
def signOut():
    if 'username' in session:
        session.pop("username",None)
        session.pop("id",None)
        return redirect(url_for("index"))



@app.route("/message",methods=["POST"])
def message():

    id=session["id"] 
    message=request.form["message"]
    match = re.search(r'\S', message)
    if match:
        mycursor.execute("insert into message(member_id,content) values(%(id)s, %(message)s)", {"id":id, "message":message})
        mydb.commit()
        return redirect(url_for("member"))
    else:
        flash('請勿輸入空白字串!!!!!')
        return redirect(url_for("member"))


@app.route("/api/member")
def searchMember():
    username=request.args.get("username")
    match_username = re.search(r'\S', username)
    result={}
    if match_username and "username" in session:
        mycursor.execute("select id,name from member where username=%(username)s",{"username":username})
        user = mycursor.fetchone()  
        if user != None:
            data={'id':user[0],'name':user[1],'username':username}
            result.update({"data": data}) 
            return result 
        else: 
            result.update({"data": None}) 
            return result
    else:
        result.update({"data": None}) 
        return result



@app.route("/api/member/<username>", methods=["PATCH"])
def updateMember(username):
    id=session["id"]
    newName = request.get_json()["name"]
    match = re.search(r'\S', newName)
    if "username" in session and match:
        try:
            mycursor.execute("update member set name=%(newName)s where id=%(id)s",{"newName":newName,"id":id})
            mydb.commit()
            res = make_response(jsonify({"ok":True}),200)
            return res
        except: 
            res= make_response(jsonify({"error":True}),400)
            return res
    else:
        res= make_response(jsonify({"error":True}),400)
        return res


@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("signin.html",message=message)

@app.errorhandler(404)
def page_not_found(e):
    errorMsg="Page Not Found"
    return render_template("error.html",errorMsg=errorMsg),404

@app.errorhandler(500)
def internal_server_error(e):
    errorMsg="Internal Server Error"
    return render_template("error.html",errorMsg=errorMsg),500

if __name__ == "__main__":
    app.run(port=3000,debug=True)