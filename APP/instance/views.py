#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from . import instance
from .. import db


@instance.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("instance/instance.html",
                           title=u"我的实例")

