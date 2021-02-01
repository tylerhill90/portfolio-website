#!/usr/bin/env python3

"""A website to house my coding portfolio."""

from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='./assets')
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='tylerhill90@gmail.com',
    MAIL_PASSWORD='gicifxpxnbsdmezf'
)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject')
        sent_by = request.form.get('email')
        msg = Message(subject, sender=sent_by, recipients=[
            'tylerhill90@gmail.com'])
        msg.body = f'{request.form.get("message")}\n\nFrom: {sent_by}'
        mail.send(msg)

    return render_template('index.html')

@app.route('/alignment-algorithms', methods=['GET', 'POST'])
def align_algs():
    return render_template('seq-align.html')


if __name__ == '__main__':
    app.run(debug=False)
