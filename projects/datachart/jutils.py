#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
import requests,io,json

def jdump(obj):
    return json.dumps(obj, indent=4, ensure_ascii=False, encoding='utf8')

def jload(json_path):
    fp = open(json_path, 'r')
    return json.load(fp, encoding='utf8')

def jwrite(filename, obj):
    jdumpStr = jdump(obj)
    with io.open(filename, 'w', encoding='utf8') as fr:
        fr.write(jdumpStr)

def getHttpJson(url):
    r = requests.get(url)
    return r.json()
