from flask import Blueprint, blueprints, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("")
def page_one():
    return render_template("")

@views.route("")
def page_two():
    return render_template("")

@views.route("")
def page_three():
    return render_template("")

@views.route("")
def page_four():
    return render_template("")

@views.route("/admin")
def admin():
    return render_template("")

@views.route("/javascript")
def javascript_redirect():
    return redirect(url_for("views.home"))

@views.route("/js")
def javascript_redirect():
    return redirect(url_for("views.home"))

@views.route("/home")
def home_redirect():
    return redirect(url_for("views.home"))
