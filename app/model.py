import bson

from datetime import datetime
from app import db #, admin
from flask_mongoengine.wtf import model_form
from wtforms import Form, StringField, SelectField
from flask_admin.contrib.mongoengine import ModelView
from flask_admin.actions import action

class Culto(db.Document):
    dt_culto = db.DateField(default=datetime.now())
    ativo = db.BooleanField(default=True)
    limite = db.IntField(default=80)
    vagas = db.IntField(default=80)
    periodo = db.StringField(default='noite')

    # def __repr__(self):
    #     return f'Culto: {self.dt_culto}({self.get_vagas_reais()}/{self.limite})'

    # def get_vagas_reais(self):
    #     return self.limite - len(Presenca.objects.filter(culto=self.id, precisa_assento=True))

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.dt_culto)
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
    nome = db.StringField(required=True, max_length=25)
    precisa_assento = db.BooleanField(default=True)
    data_criacao = db.DateTimeField(default=datetime.now())
    culto = db.ObjectIdField(required=True) #, default=get_last_culto())

    def __repr__(self):
        return f'Inscrição de {self.nome} {self.precisa_assento}'

    @property
    def data_culto(self):
        return Culto.objects.get(id=self.culto).dt_culto.strftime("%d/%m/%Y")

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.nome)
        culto = Culto.objects.get(id=document.culto)
        culto.vagas -= 1
        culto.save()


class RegForm(model_form(Presenca)):
    model = Presenca

    culto = SelectField('Culto', coerce=bson.objectid.ObjectId)

class BuscaForm(Form):
    busca = StringField()

# db.signals.post_save.connect(Presenca.post_save, sender=Presenca)
# db.signals.post_save.connect(Culto.post_save, sender=Culto)


class PresencaView(ModelView):
    @action('validate', 'Validar', 'Tem certeza que deseja validar estas inscrições?')
    def action_approve(self, ids):
        try:
            count = Presenca.objects(id__in=(ids)).update(precisa_assento=True)

            # flash(ngettext('Inscrição validada.',
            #                '%(count)s inscrições validades com sucesso.',
            #                count,
            #                count=count))
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
    column_filters = ['nome', 'precisa_assento']
    column_list = ['nome', 'precisa_assento', 'data_culto']
    column_export_list = ['nome', 'precisa_assento', 'data_culto']
    form = RegForm

            # flash(gettext('Falha ao validar incrições. %(error)s', error=str(ex)), 'error')

# admin.add_view(ModelView(Culto))
# admin.add_view(PresencaView(Presenca))
