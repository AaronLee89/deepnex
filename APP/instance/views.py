#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from ..util.API_manage import ApiClient
from . import instance
from .. import db
import json


@instance.route('/', methods=['GET', 'POST'])
@login_required
def index():
    api_client = ApiClient()
    api_client.login()
    data = api_client.get_instances_list()
    return render_template("instance/index.html",
                           instances=data['instances'],
                           title=u"我的实例")


@instance.route('/<int:iid>', methods=['GET', 'POST'])
@login_required
def detail(iid):
    api_client = ApiClient()
    api_client.login()
    i_data = api_client.get_instance_detail(iid=iid)
    instance = i_data['instance']
    config = i_data['config'][0]
    param = json.loads(i_data['config'][0]['param'])

    proxy = api_client.get_instance_proxy(iid=iid)
    return render_template("instance/detail.html",
                           instance=instance,
                           config=config,
                           param=param,
                           proxys=proxy['Services'],
                           title=u"实例详情")


@instance.route('/create', methods=['POST'])
@login_required
def create():
    _form = request.form
    name = _form['name']
    nodes = int(_form['nodes'])
    cpu = int(_form['cpu'])
    memory = int(_form['memory'])

    api_client = ApiClient()
    api_client.login()
    api_client.create_spark(name, nodes, cpu, memory)
    return redirect(url_for('instance.index', message='created'))


@instance.route('/delete/<int:iid>')
@login_required
def delete(iid):
    api_client = ApiClient()
    api_client.login()
    api_client.delete_instance(iid)
    return redirect(url_for('instance.index', message='deleted'))
