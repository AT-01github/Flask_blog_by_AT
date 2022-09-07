from flask import Flask, render_template,request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import json
import os
from datetime import datetime
from flask_mail import Mail
import math


with open('config.json', 'r') as c:
    params= json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key= 'super secret key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI']=params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI']=params['prod_uri']
db = SQLAlchemy(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
    mail=Mail(app)
)


class Contacts(db.Model):
    '''name , email,Serial,date,phone_num, message'''
    name = db.Column(db.String(120),unique=False, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    Serial = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12),nullable=True)
    phone_num = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    Title= db.Column(db.String(120), unique=False, nullable=False)
    Serial = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=True)
    slug= db.Column(db.String(21), nullable=False)
    content= db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    img_file=db.Column(db.String(20), nullable=True)


@app.route("/")
def home():
    posts = Posts.query.filter_by().all()#[0:params['no_of_posts']]
    last=math.ceil(len(posts)/int(params['no_of_posts']))
    page=request.args.get('page')
    if (not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    if page==1:
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif page==last:
        prev= "/?page=" + str(page - 1)
        next="#"
    else:
        prev= "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@app.route("/edit/<string:Serial>", methods=['GET', 'POST'])
def edit(Serial):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method=='POST':
            box_title=request.form.get('Title')
            tagline=request.form.get('tagline')
            slug=request.form.get('slug')
            date=datetime.now()
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            if Serial == '0':
                post = Posts(Title=box_title, slug=slug, content=content, tagline=tagline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(Serial=Serial).first()
                post.Title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tagline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/' + Serial)
        post = Posts.query.filter_by(Serial=Serial).first()
        return render_template('edit.html', params=params, post=post, Serial=Serial)

@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop('user')
    return redirect("/dashboard")

@app.route("/delete/<string:Serial>", methods=['GET','POST'])
def delete(Serial):
    if ('user' in session and session['user'] == params['admin_user']):
        post=Posts.query.filter_by(Serial=Serial).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')




@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if(request.method=='POST'):
        f=request.files['file1']
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method=='POST':
                f=request.files['file1']
                f.save((app.config['UPLOAD_FOLDER'])+'\\'+ secure_filename(f.filename))
                return "uploaded successfully"




@app.route("/contact", methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        '''Add entry to database'''
        names=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone_num')
        message=request.form.get('message')
        entry = Contacts(Serial=0, name=names, phone_num=phone, email=email, date=datetime.now(), message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params=params, post=post)


@app.route("/post")
def post_page():
    return render_template('post.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if('user' in session and session['user']==params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if(username==params['admin_user'] and userpass==params['admin_password']):
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
    else:

        return render_template('login.html', params=params)





app.run(debug=True)