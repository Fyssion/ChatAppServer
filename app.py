from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "0f0a2448bd028146bfa8f615ff308525"


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", category="success")
        return redirect(url_for("index"))
    return render_template("signup.html", title="Signup", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@chatapp.com" and form.password.data == "password":
            flash("You have been logged in!", category="success")
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Please check username and password." , "danger")
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)