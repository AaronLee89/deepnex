#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template, jsonify
from flask_login import login_required, current_user


@main.route('/')
@login_required
def index():
    return render_template("main/index.html",
                           title=u"我的主页")


@main.route('/test')
def test():
    d = dict()
    d['username'] = 'zzp'
    d['password'] = '123456'
    return jsonify(d)


@main.app_errorhandler(404)
def page_404(err):
    return render_template('404.html', title='404'), 404


@main.app_errorhandler(403)
def page_403(err):
    return render_template('403.html', title='403'), 403


@main.app_errorhandler(500)
def page_500(err):
    return render_template('500.html', title='500'), 500
