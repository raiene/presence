from datetime import datetime
from app import db
from flask_mongoengine.wtf import model_form

class Culto(db.Document):
    data = db.DateField()
    ativo = db.BooleanField(default=True)
    limite = db.IntField(default=80)

    def __repr__(self):
        return f'Culto: {self.data}/{self.limite}'

CultoForm = model_form(Culto)


class Presenca(db.Document):
    nome = db.StringField(required=True)
    precisa_assento = db.BooleanField(default=True)
    data_criacao = db.DateTimeField(default=datetime.now())
    culto = db.ObjectIdField(required=True, default=Culto.objects.get(ativo=True).id)

RegForm = model_form(Presenca)
