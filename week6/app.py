import mysql.connector 
from flask import Flask, redirect, render_template,request,session,url_for

app = Flask(__name__)
app.config["SECRET_KEY"]="eaf266f88f72894c90"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:thu982305@localhost/website"

mydb = mysql.connector.connect(user='root', password='需要時再打Q_Q',host='127.0.0.1',database='website')

mycursor = mydb.cursor(buffered=True)




@app.route("/")
def index():


    return render_template('index.html')

@app.route("/signup", methods=["POST"])
def register():
    
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    try:
        mycursor.execute("insert into member(name,username,password)  values(%(name)s,%(username)s,%(password)s)", {"name":name, "username":username, "password":password})
        mydb.commit()
        
        return redirect(url_for("index"))
    except:
        return redirect(url_for("error",message="帳號已經被註冊"))

@app.route("/signin", methods=["POST"])
def signIn(): 
    name=request.form["username"]
    password=request.form["password"]
    
 
    try:
        mycursor.execute("select username, password  from member  where username=%(name)s and password=%(password)s", {"name":name, "password":password}) 
      #存進session
        mydb.commit()
        for (name, password) in mycursor:
            print(f"your name is {name} and password is {password}")
            session["username"]=name
            return redirect(url_for("member")) 
    except: return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

    return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))



@app.route("/member")
def member():
    if "username" in session:        
        username=session["username"]
        mycursor.execute("select name, content from member inner join  message on member.id=message.member_id order by message.time" ) 
        mydb.commit()
        contents=[]
        for (name,content) in mycursor:
            contents.append({"name":name,"content":content}) 

        return render_template("signin.html", username=username, contents=contents)
    else:  return redirect(url_for("index"))

@app.route("/signout")
def signOut():
    if 'username' in session:
        session.pop("username",None)
        return redirect(url_for("index"))



@app.route("/message",methods=["POST"])
def message():

    id=session["id"] 
    message=request.form["message"]
    mycursor.execute("insert into message(member_id,content) values(%(id)s, %(message)s)", {"id":id, "message":message})
    mydb.commit()
    return redirect(url_for("member"))



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