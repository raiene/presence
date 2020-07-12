from datetime import datetime
from app import db
from flask_mongoengine.wtf import model_form
from wtforms import Form, StringField

class Culto(db.Document):
    data = db.DateField()
    ativo = db.BooleanField(default=True)
    limite = db.IntField(default=80)
    vagas = db.IntField(default=80)

    def __repr__(self):
        return f'Culto: {self.data}({self.get_vagas_reais()}/{self.limite})'

    def get_vagas_reais(self):
        return len(Presenca.objects.filter(culto=self.id, precisa_assento=True))

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.data)
        if 'created' in kwargs:
            culto = Culto.objects.filter(ativo=True, id__ne=document.id).update(ativo=False)


CultoForm = model_form(Culto)


def get_last_culto():
    import app
    try:
        return Culto.objects.get(ativo=True).id
    except db.DoesNotExist:
        return None


class Presenca(db.Document):
    nome = db.StringField(required=True)
    precisa_assento = db.BooleanField(default=True)
    data_criacao = db.DateTimeField(default=datetime.now())
    culto = db.ObjectIdField(required=True, default=get_last_culto())

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.nome)
        culto = Culto.objects.get(id=document.culto)
        culto.vagas -= 1
        culto.save()


RegForm = model_form(Presenca)

class BuscaForm(Form):
    busca = StringField()

db.signals.post_save.connect(Presenca.post_save, sender=Presenca)
db.signals.post_save.connect(Culto.post_save, sender=Culto)
