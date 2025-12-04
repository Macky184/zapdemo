from flask import Flask, render_template, request, redirect, session, url_for, render_template_string

app = Flask(__name__)
app.secret_key = "zap-demo-secret"  

USERS = {
    "user": {"password": "userpass", "admin": False},
    "admin": {"password": "adminpass", "admin": True},
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = USERS.get(username)
        if user and user["password"] == password:
            session["username"] = username
            session["admin"] = user["admin"]
            return redirect("/index")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/index")
def index():
    if "username" not in session:
        return redirect("/login")
    msg = request.args.get("msg", "")
    try:
        evaluated = render_template_string(msg)
    except Exception as e:
        evaluated = f"Error: {e}"
    return render_template("index.html", username=session["username"], msg=evaluated)

@app.route("/admin")
def admin():
    if "username" not in session:
        return redirect("/login")
    if not session.get("admin"):
        return "403 Forbidden", 403
    return render_template("admin.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
