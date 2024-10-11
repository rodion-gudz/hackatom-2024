# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from audioop import reverse

from flask import flash, redirect, url_for, render_template, render_template_string

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message

from flask_moment import _moment


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    try:
        with open("name_limit.txt") as file:
            name_limit = int(file.read())
    except:
        name_limit = 77
    if form.validate_on_submit():
        name = form.name.data
        if len(name) > name_limit:
            flash('Слишком длинное имя!', category="error")
            return redirect(url_for('index'))
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.asc()).all()
    for index, message in enumerate(messages):
        try:
            messages[index].name = render_template_string(message.name)
        except:
            continue

    return render_template('index.html', form=form, messages=list(reversed(messages)))
