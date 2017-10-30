#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json

BASE_URL = 'http://10.127.48.18:8080/'
LOGIN_DATA = '{"username":"guoguixin","password":"guoguixin"}'


class ApiClient:
    def __init__(self, base_url=BASE_URL, login_cookie=None, login_data=LOGIN_DATA):
        self.base_url = base_url
        self.login_cookie = login_cookie
        self.login_data = login_data

    def login(self):
        """
        用户登录，返回值为是否成功（布尔型）
        """
        login_url = self.base_url + 'auth'
        r = requests.post(login_url, data=LOGIN_DATA)
        if r.status_code == 200:
            self.login_cookie = dict(kubernetes_token=r.cookies['kubernetes_token'])
            print 'login success'
            return True
        else:
            print 'login failed:' + r.text
            return False

    def open(self, url, data=None, method=None):
        """ 
        收发请求的底层函数，执行此函数前需要手动登录。
        将接收的字典格式数据data封装进请求，根据url参数发送到对应的api接口的地址，
        并对返回的数据进行处理以及保存。
        返回值为一个字典，即api接口返回的数据。
        """
        url = self.base_url + url
        if method == 'POST' or method == 'post':
            r = requests.post(url, data=data, cookies=self.login_cookie)
            return r.json()
        elif method == 'GET' or method == 'get':
            r = requests.get(url, params=data, cookies=self.login_cookie)
            return r.json()
        elif method == 'DELETE' or method == 'delete':
            r = requests.delete(url, data=data, cookies=self.login_cookie)
            return r.json()
        else:
            return dict(message='method is invalid')

    def get_user(self):
        """
        获取用户列表
        """
        return self.open('user', method='get')

    def create_spark(self, name, nodes, cpu, memory):
        """
        创建一个spark实例 
        """
        instancename = name
        aid = 1
        param = "{\"nodes\":%d,\"cpu\":%d,\"memory\":%d}" % (nodes, cpu*1000, memory)
        data = json.dumps(dict(instancename=instancename, aid=aid, param=param))
        return self.open('instance', method='post', data=data)

    def delete_instance(self, iid):
        """
        删除一个实例
        """
        data = '{"iid":%s}' % iid
        return self.open('instance', method='delete', data=data)

    def get_instances_list(self):
        """
        获取实例列表,参数kind为必须(all、single、proxy)
        """
        data = dict(kind='all')
        return self.open('instance', method='get', data=data)

    def get_instance_detail(self, iid):
        """
        获取某个实例的详细信息，包括配置参数
        """
        data = dict(kind='single', iid=iid)
        return self.open('instance', method='get', data=data)

    def get_instance_proxy(self, iid):
        """
        获取某个实例的proxy代理链接
        """
        data = dict(kind='proxy', iid=iid)
        return self.open('instance', method='get', data=data)


if __name__ == '__main__':
    api_client = ApiClient()
    api_client.login()

