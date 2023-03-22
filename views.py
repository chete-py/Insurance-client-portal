from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template('home')

@views.route("/products")
def products():
    return render_template('products')

@views.route("/claims")
def claims():
    return render_template('claims')


@views.route("/Login")
def Login():
    return render_template('Login')


@views.route("/contact")
def contact():
    return render_template('contact')








