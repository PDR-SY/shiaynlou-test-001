from flask import Flask,render_template,abort
import os
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

@app.route('/')
def index():
	titles = File.query.all()
	return render_template('index.html',titles = titles)


@app.route('/file/<file_id>')
def file(file_id):
	file_click =  File.query.filter_by(id=file_id).first()
	if file_click is not None:
			return render_template('file.html',file = file_click) 
	else:
		abort(404)


@app.errorhandler(404)
def not_found(eooro):
	return render_template('404.html'),404


class File(db.Model):


	"""docstring for File"""
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	content = db.Column(db.Text)
	category = db.relationship('Category',backref='file')

	def __init__(self,title,category,content,created_time=None):
		self.title = title
		self.created_time = created_time
		self.content = content
		if created_time is None:
			self.created_time = datetime.utcnow()
		self.created_time = created_time
		self.category = category
	def __repr__(self):
		return '<File %r>' % self.title
			

		
class Category(db.Model):

	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(80))
	child = db.relationship('File')
	"""docstring for Category"""
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return '<Category %r>' % self.name