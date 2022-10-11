from flask import Flask, redirect, render_template,request,session,url_for

app = Flask(__name__)
app.config["SECRET_KEY"]="eaf266f88f72894c90"
#另一種密鑰寫法 app.secret_key="eaf266f88f72894c90"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signin", methods=["POST"])
def signIn():
    name=request.form["name"]
    password=request.form["password"]
   
    #存進session
    session["username"]=name

    if name=="test" and password=="test":
        return redirect(url_for("member")) 
    elif name=="" or password=="":  
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error"),message="帳號、或密碼輸入錯誤")


@app.route("/member")
def member():
    name=session["username"]
    if name=="": return redirect(url_for("index"))
    print("if you log in, and session is ",dict(session))
    
    return render_template("signin.html", name=name)

@app.route("/signout")
def signOut():
    if 'username' in session:
        session["username"]=""
        # session.pop("password",None)
        print("if you log out, and session is ",dict(session))
        return redirect(url_for("index"))


@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("signin.html",message=message)
        
    # return render_template("signin.html",name=name,password=password,message=message)





@app.route("/square")
def square():
    number=request.values.get("num","")
    # number=request.form["num"]
    number=int(number)
    result=number**2
    
    
    return render_template("square.html",number=number, result=result)


@app.route("/square/<num>")
def squareOutside(num):
    num=int(num)
    result=num**2
    return render_template("square.html",number=num, result=result)







if __name__ == "__main__":
    app.run(port=3000,debug=True)