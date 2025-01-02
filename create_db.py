from ayupharma import app, db
from ayupharma.models import User,Disease
from flask_login import login_user,current_user,logout_user,login_required
import queue
import spacy
nlp = spacy.load("en_core_web_lg")
# nlp = spacy.load("en_core_med7_lg")
with app.app_context(): 
    user = User.query.filter_by(id=1).first()
search_list = user.search.split(',')
search = search_list[-1]
print(search)
f1 = 0.7
f2 = 0.3
d = {}
e = {}
f = {}
pq = queue.PriorityQueue()
with app.app_context():
    all_symptoms= Disease.query.with_entities(Disease.symptoms).all()
    all_diseases= Disease.query.with_entities(Disease.disease).all() 
    all_questions = Disease.query.with_entities(Disease.questions).all()
    print(all_symptoms)
    print(all_diseases)
    print(all_questions)
    for symptom, disease in zip(all_symptoms, all_diseases):
        elements_list = symptom[0].split(',')
        b = []
        maxy = 0
        mean = 0
        sumy = 0
        for x in elements_list:
            doc1 = nlp(search)
            doc2 = nlp(x)
            doc3 = nlp(disease)
            alpha = doc1.similarity(doc2)
            beta = doc1.similarity(doc3)
            print(disease)
            l = [x,alpha]
            maxy = max(alpha,maxy)
            sumy = sumy+alpha
            b.append(l)
        mean = sumy / len(b)
        po = beta
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
    print(item)
    i+=1

weights = []

questions_list = {}
with app.app_context():
    disease_list = Disease.query.filter(Disease.disease.in_(y)).all()
    for disease in disease_list:
        que = disease.questions.split('\n')
        que = [s.replace(',', '') for s in que]
        que = [s.replace(',', '').strip() for s in que]
        questions_list[disease.disease] = que 

print(questions_list)