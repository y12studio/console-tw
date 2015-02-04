#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
import requests,io,json,hashlib

url = "http://file.data.gov.tw/event/政府資料開放平臺資料集清單.json"
"""
 {
            "主要欄位說明": "港口代碼,船舶英文名稱,船舶中文名稱,預定進港日期及時間,實際進港日期及日時,預定出港日期及時間,實際出港日期及時間",
            "下載連結": "http://www.motcmpb.gov.tw/MOTCMPBWeb/wSite/public/Data/f1412753810074.zip",
            "授權方式": "政府資料開放平臺資料使用規範",
            "資料集提供機關": "交通部航港局",
            "資料集類型": "rawData",
            "檔案格式": "csv",
            "授權說明網址": "http://data.gov.tw/?q=principle",
            "資料集描述": "港口代碼,船舶英文名稱,船舶中文名稱,預定進港日期及時間,實際進港日期及日時,預定出港日期及時間,實際出港日期及時間",
            "計費方式": "免費",
            "備註": "",
            "資料集提供機關聯絡人": "劉小姐",
            "資料集提供機關聯絡人電話": "02-89786865",
            "編碼格式": "UTF-8",
            "更新頻率": "每月",
            "資料集名稱": "103年9月國際商港船舶進出港動態資料"
        }
"""

def jdump(obj):
    return json.dumps(obj, indent=4, ensure_ascii=False, encoding='utf8')

def jload(json_path):
    fp = open(json_path, 'r')
    return json.load(fp, encoding='utf8')

def jwrite(filename, jdump):
    with io.open(filename, 'w', encoding='utf8') as fr:
        fr.write(jdump)

def getRawJson():
    r = requests.get(url)
    return r.json()

def build(filename):
    jr = getRawJson()
    rdict = {}
    i = 0
    for item in jr['Records']:
        rid = hashlib.sha256(item[u'資料集名稱'].encode('utf-8')).hexdigest()
        v = {}
        v['name'] = item[u'資料集名稱']
        v['url'] = item[u'下載連結']
        v['format'] = item[u'檔案格式']
        # only save first 10 items
        i+=1
        if i < 10 :
            rdict[rid] = v
    meta={}
    meta['count']=len(jr['Records'])
    rdict['meta'] = meta
    jwrite(filename,jdump(rdict))
    print meta

if __name__ == '__main__':
    # 150204 parse 政府資料開放平臺資料集清單.json {'count': 3533} but data.gov.tw show 4135?
    build('raw150204.json')
