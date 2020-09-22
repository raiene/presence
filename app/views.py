from datetime import datetime, date
from flask import Flask, request, render_template
from app.model import CultoForm, RegForm, Culto, Presenca, BuscaForm
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
    last_culto = None
    # try:
    #     last_culto = Culto.objects.get(ativo=True)
    # except Culto.DoesNotExist:
    #     last_culto = None
    if request.method == 'POST' and form.validate_on_submit():
        print('Passou, de algum jeito')
        print(last_culto)
        # form.culto = last_culto.id
        del form.csrf_token
        # print(form.culto)
        last_culto = Culto.objects.get(ativo=True)
        if last_culto.get_vagas_reais() > 0:
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
    # culto = Culto.objects.get(ativo=True)
    culto = Culto.objects.order_by('-dt_culto').first()
    presencas = Presenca.objects.filter(culto=culto.id)
    return render_template('list.html', culto=culto, presences=presencas)

@app.route('/seencontre', methods=['GET', 'POST'])
def seache():
    culto = Culto.objects.get(ativo=True)
    form = BuscaForm(request.form)
    if request.method == 'POST':
        print(dir(form.busca))
        print(form.busca.data)
        resultados = Presenca.objects.filter(culto=culto.id, nome__icontains=form.busca.data)
        print(resultados)
    return render_template('busca.html', culto=culto, form=form, resultados=resultados)