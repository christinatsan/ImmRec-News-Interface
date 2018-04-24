from flask import Flask, flash, redirect, render_template, request, session, abort, Response, jsonify
import json
#from flask.ext.session import Session
from forms import LoginForm

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'you-will-never-guess'

chosenTags1 = []
chosenTags2 = []
chosenTags3 = []

@app.route("/",methods=['post','get'])
def index():
	return render_template('index.html')

@app.route("/categories")
def categories():
	categoryList = [
				{
					'tag': 'Tag 1',
					'title': 'News 1',
					'description':'news 1',
					'author':'author 1'
					

				},
				{
					'tag': 'Tag 2',
					'title':'News 2',
					'description': 'news 2',
					'author':'author 2'

				}
			]

	return render_template('categories.html',categories = categoryList)

@app.route("/categories2")
def categories2():

	global chosenTags1

	# TODO: get categories/tags based on chosenTags1

	categoryList = [
				{
					'tag': 'Tag 3',
					'title': 'News 3',
					'description':'news 3',
					'author':'author 3'
					

				},
				{
					'tag': 'Tag 4',
					'title':'News 4',
					'description': 'news 4',
					'author':'author 4'

				}
			]

	return render_template('categories2.html',categories = categoryList)


@app.route("/categories3")
def categories3():

	global chosenTags2

	# TODO: get categories/tags based on chosenTags2


	categoryList = [
				{
					'tag': 'Tag 5',
					'title': 'News 5',
					'description':'news 5',
					'author':'author 5'
					

				},
				{
					'tag': 'Tag 6',
					'title':'News 6',
					'description': 'news 6',
					'author':'author 6'

				}
			]

	return render_template('categories3.html',categories = categoryList)

@app.route("/recommendations")
def recommendations():

	global chosenTags3

	print(chosenTags3)

	#given tags get articles

	articleList = [
				{
					'tag': 'Tag 1',
					'title': 'News 1',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 2',
					'title':'News 2',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},
				{
					'tag': 'Tag 3',
					'title': 'News 3',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 3',
					'title':'News 4',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 4',
					'title': 'News 5',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 5',
					'title':'News 6',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 6',
					'title':'News 7',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},										
			]	

	return render_template('recommendations.html',articles = articleList)

@app.route('/postmethod2', methods = ['POST'])
def get_post_javascript_data2():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global chosenTags2

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	chosenTags2.append(tag)

    return jsonify(jsonData)

@app.route('/postmethod1', methods = ['POST'])
def get_post_javascript_data1():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global chosenTags1

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	chosenTags1.append(tag)
    	
    return jsonify(jsonData)

@app.route('/postmethod3', methods = ['POST'])
def get_post_javascript_data3():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global chosenTags3

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	chosenTags3.append(tag)
    	
    return jsonify(jsonData)


@app.route("/preferences/<category>")
def preferences(category):
	catTitle = "[" + category + "]"
	jsonTitle = json.loads(catTitle)
	print(jsonTitle["title"])
	#print(catTitle['title'])
	return render_template('refinedlist.html',category = category)

@app.route("/onboarding/")
def onboarding():
	form = LoginForm()
	return render_template('onboarding.html', title='Sign In', form=form)
# @app.route("/onboarding/<string:name>/")
# def members(name):
#     return render_template('test.html',name=name)


# @app.route("/refinedlist")
# def refinedlist():
	# return render_template('refinedlist.html')


if __name__ == "__main__":
	app.run()