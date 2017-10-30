#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from ..util.API_manage import ApiClient
from . import application
from .. import db


@application.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("application/index.html", title=u"应用模板")


