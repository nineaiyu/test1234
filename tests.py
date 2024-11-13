#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xadmin-server
# filename : tests
# author : ly_13
# date : 12/23/2023
import os

#
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

# for a in Menu.objects.filter(menu_type=2,name__startswith='import:'):
#     a.name = a.name.replace('import:','importData:')
#     a.save(update_fields=['name'])
#
# for a in Menu.objects.filter(menu_type=2,name__startswith='export:'):
#     a.name = a.name.replace('export:','exportData:')
#     a.save(update_fields=['name'])

# for a in Menu.objects.filter(menu_type=2,name__startswith='detail:'):
#     a.name = a.name.replace('detail:','retrieve:')
#     a.save(update_fields=['name'])
# for a in Menu.objects.filter(menu_type=2,name__startswith='delete:'):
#     a.name = a.name.replace('delete:','destroy:')
#     a.save(update_fields=['name'])
#
# for a in Menu.objects.filter(menu_type=2,name__startswith='batchDelete:'):
#     a.name = a.name.replace('batchDelete:','batchDestroy:')
#     a.save(update_fields=['name'])
# Menu.objects.filter(menu_type=2,name__startswith='partialUpdate:').delete()
# for a in Menu.objects.filter(menu_type=2,name__startswith='update:'):
#     a.name = a.name.replace('update:','partialUpdate:')
#     a.method='PATCH'
#     a.save(update_fields=['name','method'])


exit()

for i in apis:
    if 'BookViewSet' in i.get('view'):
        print(i)
print(111111111)

router = SimpleRouter(False)
router1 = NoDetailRouter(False)

x = router.get_routes(BookViewSet)
for i in x:
    print(i)
print(11111111111111)
x = router1.get_routes(BookViewSet)
for i in x:
    print(i)

exit()

ServerPerformanceCheckUtil().check_and_publish()

from system.models import *
from system.utils.auth import check_different_city_login_if_need
from settings.utils.security import LoginIpBlockUtil

for i in range(1, 100):
    for j in range(10):
        LoginIpBlockUtil(f'103.91.179.{i}').set_block_if_need()

user = UserInfo.objects.get(username='isummer')
check_different_city_login_if_need(user, '103.91.179.186')

exit()

#
# from demo.utils.serializer import BookSerializer
# from django.http import QueryDict
# from rest_framework.utils.html import parse_html_dict
#
# data = QueryDict('', mutable=True)
# data.update({
#     'meta.ddadf.edsafs':1,
#     'meta.ddadf.edsafs2':2,
# })
# print(parse_html_dict(data,'meta'))
for i in range(1, 56):
    LoginIpBlockUtil(f'10.33.22.{i}').set_block_if_need()
    LoginIpBlockUtil(f'10.33.22.{i}').set_block_if_need()

import struct


def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]


import socket


def int_to_ip(int_ip):
    return socket.inet_ntoa(struct.pack("!I", int_ip))


ip_address = "192.168.1.1"
integer_ip = ip_to_int(ip_address)
print(f"The integer representation of {ip_address} is: {integer_ip}")

integer_address = 3232235777  # 192.168.1.1的整数表示
ip_from_int = int_to_ip(integer_address)
print(f"The IP address of the integer {integer_address} is: {ip_from_int}")

exit()

# a = UserInfo.objects.create_user(username=2342344, password='1234234', email='nineven@qq.com')

import re

x = "rgba(135, 101, 92, 0.25)"
print(re.findall(r"\d+\.?\d*", x))
# tuple([int(x) for x in re.findall(r"\d+", x)])
print(x)

exit()

import base64

import requests

headers = {
    'Authorization': 'Basic ' + base64.b64encode(b'admin:admin').decode()
}
req = requests.get('http://localhost:8896/api/system/dashboard/user-total', headers=headers)
print(req.text)
