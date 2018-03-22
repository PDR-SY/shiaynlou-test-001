from flask import Flask,render_template,abort
import os
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
filelist = os.listdir('/home/shiyanlou/files/')
newsList = {}
titles = []
names = []
@app.route('/')
def index():
	if len(titles)==0:
		for filepath in filelist:
			filepath = '/home/shiyanlou/files/'+filepath
			key = filepath.replace('/home/shiyanlou/files/','').replace('.json','')
			with open(filepath,'r') as file:
				newsList[key] = json.loads(file.read())
			names.append(key)
			print(newsList)
		for key,value in newsList.items():
			print(value)
			titles.append(value['title'])	
	
	return render_template('index.html',titles = titles)


@app.route('/files/<filename>')
def file(filename):
	print(filename)
	if os.path.exists('/home/shiyanlou/files/'+filename+'.json'):
		print(filename in newsList)
		if filename in newsList:
			value = newsList[filename]
			print(value)
			return render_template('file.html',value = newsList[filename]) 
		else:
			abort(404)
	else:
		abort(404)


@app.errorhandler(404)
def not_found(eooro):
	return render_template('404.html'),404
