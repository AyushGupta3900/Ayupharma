import secrets
import os
from flask import render_template, url_for, flash, redirect,request
from ayupharma import app,bcrypt,db
from ayupharma.forms import RegistrationForm, SigninForm, SearchForm, UpdateAccountForm, DiseaseForm, ContactUsForm
from ayupharma.models import User,Message,Disease
from flask_login import login_user,current_user,logout_user,login_required
import queue
import spacy
import time
import asyncio

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',title='home')

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/action")
def action():
    return render_template('action.html',title='action')

@app.route("/contact",methods=['GET','POST'])
def contact():
    form = ContactUsForm()
    if form.validate_on_submit():
        message = Message(firstname=form.firstname.data,lastname=form.lastname.data,email=form.email.data,mobile_number=form.mobile_number.data,message=form.message.data)
        with app.app_context():
            db.session.add(message)
            db.session.commit()
        flash(f'Message Send Successfully!','success')
        return redirect(url_for('contact'))
    return render_template('contact.html',title='contact',form=form)

@app.route("/copy")
def copy():
    return render_template('copy.html',title='copy')

@app.route("/emergencies")
def emergencies():
    return render_template('emergencies.html',title='Immediate Action')
    
@app.route("/fulldetail")
def fulldetail():
    return render_template('fulldetail.html',title='fulldetail')

@app.route("/herb")
def herb():
    return render_template('herb.html',title='Herb Encyclopedia')

@app.route("/herbpage")
def herbpage():
    return render_template('herbpage.html',title='Herb Details')

@app.route("/services")
def services():
    return render_template('services.html',title='services')

@app.route("/yoga")
def yoga():
    return render_template('yoga.html',title='yoga')

@app.route("/yogadetails")
def yogadetails():
    return render_template('yogadetails.html',title='yogadetails')

@app.route("/register",methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
        return redirect(url_for('home'))
   form = RegistrationForm()
   if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
        user = User(username=form.username.data,email=form.email.data,password=hashed_password,mobile_number=form.mobile_number.data)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        flash(f'Account created Successfully! You can log in now','success')
        return redirect(url_for('signin'))
   return render_template('register.html',title='register', form=form)

@app.route("/signin",methods=['GET','POST'])
def signin():
   if current_user.is_authenticated:
       return redirect(url_for('home'))
   form = SigninForm()
   if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password,form.password.data):
        login_user(user,remember=form.remember.data)
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
   return render_template('signin.html',title='signin', form=form)

@app.route("/logout",methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    form1 = DiseaseForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            with app.app_context():
                current_user.image_file = picture_file
                db.session.commit()
        with app.app_context():
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('Your account has been updated','success')
            return redirect(url_for('account'))

    elif form1.validate_on_submit():
        with app.app_context():
            current_user.disease_1 = form1.disease_1.data
            current_user.disease_2 = form1.disease_2.data
            current_user.disease_3 = form1.disease_3.data
            db.session.commit()
            flash('Your diseases has been updated','info')
            return redirect(url_for('account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form1.disease_1.data = current_user.disease_1
        form1.disease_2.data = current_user.disease_2
        form1.disease_3.data = current_user.disease_3
    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',title='account',image_file=image_file,form=form,form1=form1)


async def generate_questions():
    # using cached model 
    nlp = get_nlp_model()
    # nlp = spacy.load("en_core_web_sm")
    # nlp = spacy.load("en_core_med7_lg")
    with app.app_context(): 
        user = User.query.filter_by(id=1).first()
    search_list = user.search.split(',')
    search = search_list[-1]

    f1 = 0.7
    f2 = 0.3
    f3 = 2
    d = {}
    e = {}
    f = {}
    pq = queue.PriorityQueue()
    with app.app_context():
        all_symptoms= Disease.query.with_entities(Disease.symptoms).all()
        all_diseases= Disease.query.with_entities(Disease.disease).all() 
        all_questions = Disease.query.with_entities(Disease.questions).all()

        for symptom, disease in zip(all_symptoms, all_diseases):
            elements_list = symptom[0].split(',')
            b = []
            maxy = 0
            mean = 0
            sumy = 0
            for x in elements_list:
                doc1 = nlp(search)
                doc2 = nlp(x)
                doc3 = nlp(disease[0])
                alpha = doc1.similarity(doc2)
                beta = doc1.similarity(doc3)
                l = [x,alpha]
                maxy = max(alpha,beta,maxy)
                sumy = sumy+alpha
                b.append(l)
            mean = sumy / len(b)
            po = mean*f1+maxy*f2+beta*f3
            mm = [maxy,mean,po]
            b.append(mm)
            d[disease]  = b
            temp = {}
            temp[disease] = b
            pq.put((-po, temp))

    y = []
    i = 0
    while i<4:
        item = pq.get()
        keys = item[1].keys()
        key_list = list(keys)
        y.append(key_list[0][0])
        i+=1
    questions_list = {}
    disease_list = []
    with app.app_context():
        for yo in y:
            xo = Disease.query.filter(Disease.disease == yo).all()
            disease_list.extend(xo)

        for disease in disease_list:
            # print(disease.questions)
            que = disease.questions.split('\n')
            que = [s.replace(',', '') for s in que]
            que = [s.replace(',', '').strip() for s in que]
            questions_list[disease.disease] = que 
    return questions_list

async def generate_options():
    options_list = []
    with app.app_context():
        all_symptoms= Disease.query.with_entities(Disease.symptoms).all()
        all_diseases= Disease.query.with_entities(Disease.disease).all()
        for symptom in all_symptoms:
            elements_list = symptom[0].split(',')
            for x in elements_list:
                options_list.append(x)
        for disease in all_diseases:
            disease_list = disease[0].split(',')
            for x in disease_list:
                options_list.append(x)

    return  options_list

@app.route("/prompt", methods=['GET', 'POST'])
@login_required
async def prompt():
    questions_dic = await generate_questions()
    
    questions = []
    for key, value in questions_dic.items():
        questions.extend(value)
    
    return render_template('prompt.html', title='prompt', questions=questions, questions_dic=questions_dic)


@app.route("/search",methods=['GET','POST'])
async def search():

    form = SearchForm()
    if form.validate_on_submit():
        flash(f'These are questions according to your symptom! {form.search.data}','success')
        with app.app_context():
            x = current_user.search
            if x != '':
                current_user.search = x+','+form.search.data
            else:
                current_user.search = form.search.data
            db.session.commit()
        return redirect(url_for('prompt'))
    options = await generate_options()
    return render_template('search.html',title='search',form=form,options=options)

@app.route('/output', methods=['GET', 'POST'])
@login_required
async def output():
    questions_dic = await generate_questions()
    answers = {}
    answerbool = []
    weights = {}
    for key, value in request.form.items():
        if key.startswith("question_"):
            question_number = key.replace("question_", "")
            answers[int(question_number)] = value
            if value == 'yes':
                answerbool.append('1')
            else:
                answerbool.append('0')
    maxwt = 0
    j= 0
    for key,value in questions_dic.items():
        wt = 0
        for i in range(0,len(value)):
            if (answerbool[i+j]=='1'):
                wt+=1
        j+=len(value)
        maxwt = max(wt,maxwt)
        weights[key]= str(wt)
    for key,value in weights.items():
        if maxwt == int(value):
            answer = key
    with app.app_context():
        curr_disease = Disease.query.filter_by(disease=answer).first()
        yogas = curr_disease.yoga_practices.split(',')
        herbs = curr_disease.ayurvedic_herbs.split(',')
    return render_template("output.html", answerbool=answerbool,answer=answer,yogas=yogas,herbs=herbs,title='output')



# Further optimisations
nlp = None

def get_nlp_model():
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_lg")  
    return nlp
