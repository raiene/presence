from datetime import datetime
from app import db
from flask_mongoengine.wtf import model_form

class Culto(db.Document):
    data = db.DateField()
    ativo = db.BooleanField(default=True)
    limite = db.IntField(default=80)
    vagas = db.IntField(default=80)

    def __repr__(self):
        return f'Culto: {self.data}({self.vagas}/{self.limite})'

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.data)
        if 'created' in kwargs:
            culto = Culto.objects.filter(ativo=True, id__ne=document.id).update(ativo=False)


CultoForm = model_form(Culto)


class Presenca(db.Document):
    nome = db.StringField(required=True)
    precisa_assento = db.BooleanField(default=True)
    data_criacao = db.DateTimeField(default=datetime.now())
    culto = db.ObjectIdField(required=True, default=Culto.objects.get(ativo=True).id)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.nome)
        culto = Culto.objects.get(id=document.culto)
        culto.vagas -= 1
        culto.save()


RegForm = model_form(Presenca)

db.signals.post_save.connect(Presenca.post_save, sender=Presenca)
db.signals.post_save.connect(Culto.post_save, sender=Culto)