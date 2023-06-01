from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587                             # TLSは587、SSLなら465
app.config['MAIL_USERNAME'] = 'testttttt886@gmail.com'
app.config['MAIL_PASSWORD'] = '@testmynaviapp'        # GmailのApp用のmパスワード設定をしておく必要あり
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'testttttt886@gmail.com'    # これがあるとsender設定が不要になる
mail = Mail(app)


@app.route('/')
def index():
    return """
    <p><a href="/send_mail">Send Mail</a></p>
    """


@app.route("/send_mail")
def send_mail():
    msg = Message('Test Mail', recipients=['ryuya00617@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == ('__main__'):
    app.run(debug=True)