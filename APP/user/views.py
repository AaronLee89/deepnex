#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from . import user
from ..models import User
from .. import db
import os


@user.route('/reg/', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template("user/reg.html", title=u"账号注册")
    elif request.method == 'POST':
        _form = request.form
        username = _form['username']
        email = _form['email']
        password = _form['password']
        password2 = _form['password2']

        message_e, message_u, message_p = "", "", ""
        if User.query.filter_by(username=username).first():
            message_u = u'用户名已存在'
        if User.query.filter_by(email=email).first():
            message_e = u'邮箱已存在'
        if password != password2:
            message_p = u'两次输入密码不一致'

        data = None
        if message_u or message_e or message_e:
            data = _form
        if message_u or message_p or message_e:
            return render_template("user/reg.html", form=_form,
                                   title=u'账号注册',
                                   message_u=message_u,
                                   message_p=message_p,
                                   message_e=message_e,
                                   data=data)
        else:
            reg_user = User()
            reg_user.email = email
            reg_user.password = password
            reg_user.username = username
            reg_user.avatar_url = 'none.jpg'
            db.session.add(reg_user)
            db.session.commit()
            return redirect(url_for('main.index'))


@user.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("user/login.html", title=u"用户登录")
    elif request.method == 'POST':
        _form = request.form
        u = User.query.filter_by(email=_form['email']).first()

        if u is None:
            message_e = u'邮箱不存在'
            return render_template('user/login.html',
                                   title=u"用户登录",
                                   data=_form,
                                   message_e=message_e)

        next_url = request.args.get('next')
        if u and u.verify_password(_form['password']):
            login_user(u)
            u.last_login = datetime.now()
            db.session.commit()
            return redirect(next_url or url_for('main.index'))
        else:
            message_p = u"密码错误"
            return render_template('user/login.html',
                                   title=u"用户登录",
                                   data=_form,
                                   message_p=message_p)


@user.route('/logout/', methods=['GET', 'POST'])
def logout():
    pass
