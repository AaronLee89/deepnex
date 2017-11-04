#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user
from datetime import datetime
from ..models import User, News
from ..util.authorize import admin_login
from . import admin
from .. import db


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/admin_login.html', title=u'管理员登录')
    elif request.method == 'POST':
        _form = request.form
        u = User.query.filter_by(email=_form['email']).first()

        if u is None:
            message_e = u'邮箱不存在'
            return render_template('admin/admin_login.html',
                                   title=u"管理员登录",
                                   data=_form,
                                   message_e=message_e)

        if u and u.verify_password(_form['password']) and u.permissions == 0:
            login_user(u)
            u.last_login = datetime.now()
            db.session.commit()
            return redirect(url_for('admin.index'))
        else:
            message_p = u"密码错误,或该用户未注册为管理员"
            return render_template('admin/admin_login.html',
                                   title=u"管理员登录",
                                   data=_form,
                                   message_p=message_p)


@admin.route('/')
@admin_login
def index():
    return render_template('admin/index.html', title=u'主控制台')


@admin.route('/user', methods=['GET', 'POST'])
@admin_login
def user():
    """管理员查看用户列表"""
    users = User.query.all()
    return render_template('admin/user/index.html',
                           users=users,
                           title=u'用户管理')


@admin.route('/user/auth/<int:uid>', methods=['GET', 'POST'])
@admin_login
def user_auth(uid):
    """管理员审核通过普通用户的认证"""
    u = User.query.filter_by(id=uid).first_or_404()
    u.is_auth = 1
    db.session.commit()
    return redirect(url_for('admin.user'))


@admin.route('/instance', methods=['GET', 'POST'])
@admin_login
def instance():
    return redirect(url_for('instance.index'))


@admin.route('/application', methods=['GET', 'POST'])
@admin_login
def application():
    return redirect(url_for('application.index'))


@admin.route('/news')
@admin_login
def news():
    """管理员查看资讯列表"""
    news_list = News.query.all()
    return render_template('admin/article/news.html',
                           title=u'新闻资讯管理',
                           news_list=news_list)


@admin.route('/news/create', methods=['GET', 'POST'])
@admin_login
def news_create():
    """管理员创建资讯"""
    if request.method == 'GET':
        return render_template('admin/article/news_create.html', title=u'创建新闻资讯')
    elif request.method == 'POST':
        _form = request.form
        title = _form['title']
        poster = _form['poster']
        content = _form['content'].replace("\n", "")
        new_news = News(title=title, poster=poster, content=content)
        db.session.add(new_news)
        db.session.commit()
        return redirect(url_for('admin.news'))


@admin.route('/news/edit/<int:nid>', methods=['GET', 'POST'])
@admin_login
def news_edit(nid):
    """管理员编辑资讯"""
    if request.method == 'GET':
        cur_news = News.query.filter_by(id=nid).first_or_404()
        return render_template('admin/article/news_edit.html', title=u'编辑新闻资讯', news=cur_news)
    elif request.method == 'POST':
        _form = request.form
        cur_news = News.query.filter_by(id=nid).first_or_404()
        cur_news.title = _form['title']
        cur_news.poster = _form['poster']
        cur_news.content = _form['content']
        db.session.commit()
        return redirect(url_for('admin.news'))


@admin.route('/news/delete', methods=['POST'])
@admin_login
def news_delete():
    """管理员删除资讯"""
    nid = request.form['nid']
    cur_news = News.query.filter_by(id=nid).first_or_404()
    db.session.delete(cur_news)
    db.session.commit()
    return jsonify(status="success")


@admin.route('/notice', methods=['GET', 'POST'])
@admin_login
def notice():
    pass


@admin.route('/help', methods=['GET', 'POST'])
@admin_login
def help():
    pass
