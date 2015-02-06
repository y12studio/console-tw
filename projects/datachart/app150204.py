#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import requests,io,json,hashlib,jutils

class ConvertList150204:

    def __init__(self):
        self.url = "http://file.data.gov.tw/event/政府資料開放平臺資料集清單.json"

    def buildDict(self):
        jr = jutils.getHttpJson(self.url)
        rdict = {}
        records = {}
        meta={}
        for item in jr['Records']:
            rid = hashlib.sha256(item[u'資料集名稱'].encode('utf-8')).hexdigest()
            v = {}
            v['name'] = item[u'資料集名稱']
            v['url'] = item[u'下載連結']
            v['format'] = item[u'檔案格式']
            records[rid] = v
        meta['count']=len(jr['Records'])
        rdict['records'] = records
        rdict['meta'] = meta
        return rdict

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

if __name__ == '__main__':
    # 150204 parse 政府資料開放平臺資料集清單.json {'count': 3533} but data.gov.tw show 4135?
    #build('raw150204.json')
    app = ConvertList150204()
    #rdict = app.buildDict()
    #jutils.jwrite('raw150204_1.json',rdict)
    print('hello')
