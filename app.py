from flask import Flask, request, render_template
from model import RegForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def registration():
    send = False
    msg = ''
    form = RegForm(request.form)
    print(form.nome, form.precisa_assento)
    print(form.is_submitted(), form.validate())
    if request.method == 'POST' and form.validate_on_submit():
        print('Passou, de algum jeito')
        msg = 'Presença confirmada!'
        send = True
    return render_template('index.html', form=form, sended=send, msg=msg)
if __name__ == '__main__':
    app.run()
