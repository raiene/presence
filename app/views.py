from datetime import datetime
from flask import Flask, request, render_template
from app.model import CultoForm, RegForm, Culto, Presenca
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from app import app


# app = Flask(__name__)
# app.config.from_object("config")
# db = MongoEngine(app)
# Bootstrap(app)
# db.connect()

@app.route('/', methods=['GET', 'POST'])
def registration():
    send = False
    msg = ''
    form = RegForm(request.form)
    last_culto = Culto.objects.get(ativo=True)
    if request.method == 'POST' and form.validate_on_submit():
        print('Passou, de algum jeito')
        print(last_culto)
        # form.culto = last_culto.id
        del form.csrf_token
        # print(form.culto)
        last_culto = Culto.objects.get(ativo=True)
        if last_culto.vagas > 0:
            form.save()
            msg = 'Presença confirmada!'
            send = True
        else:
            msg = 'Não há mais vagas :('
    return render_template('index.html', form=form, sended=send, msg=msg, culto=last_culto)

@app.route('/addreunion', methods=['GET', 'POST'])
def cultos():
    form = CultoForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(dir(form))
            print(form._fields)
            print('Passou, de algum jeito')
            del form.csrf_token
            form.save()
        else:
            print(form)
            return(f'NAO VALIDOU, acho {form.validate()}: {form}')

    return render_template('culto.html', form=form)

@app.route('/terradonunca', methods=['GET'])
def lista_presentes():
    culto = Culto.objects.get(ativo=True)
    presencas = Presenca.objects.filter(culto=culto.id)
    return render_template('list.html', culto=culto, presences=presencas)

