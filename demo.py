from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
	return "Index!"

@app.route("/categories")
def categories():
	return render_template('categories.html')

@app.route("/onboarding/<string:name>/")
def members(name):
    return render_template(
        'test.html',name=name)

@app.route("/refinedlist")
def refinedlist():
	return render_template('refinedlist.html')


if __name__ == "__main__":
	app.run()