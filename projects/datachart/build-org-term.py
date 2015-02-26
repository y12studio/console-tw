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
import requests,io,json,hashlib,jutils,datetime,shutil
from BeautifulSoup import BeautifulSoup as soup

class ConvertTool:

    def buildDict(self, urlx):
        jr = jutils.getHttpJson(urlx)
        rdict = {}
        vmap = {}
        prefix = '/taxonomy/term/'
        countDataset = 0
        for item in jr:
            atag = soup(item[u'提供機關名稱']).a
            cd = int(item[u'資料集總數'])
            countDataset += cd
            vmap[atag['href'].replace(prefix,'')]={'name':atag.string,'dataset':cd}
        rdict['data'] = vmap
        rdict['meta'] = {'countTerm':len(jr),
        'countDataset':countDataset,
        'source':'http://data.gov.tw/data_usage/orgfullname/json',
          'host':'http://data.gov.tw',
          'build':'http://console.tw',
          'script':'https://github.com/y12studio/console-tw/tree/master/projects/datachart/build-org-term.py',
          'prefix':prefix,
          'time':datetime.datetime.utcnow().isoformat()}
        return rdict

"""
http://data.gov.tw/data_usage/orgfullname/json
 {
提供機關名稱: "<a href="/taxonomy/term/688">財政部關務署基隆關</a>",
資料集總數: "0",
瀏覽總人次: "0"
}
"""

if __name__ == '__main__':
    app = ConvertTool()
    url = 'http://data.gov.tw/data_usage/orgfullname/json'
    r = app.buildDict(url)
    filename = 'org-term'
    parentDir = '../websites/root/data/org-term/v1/'
    jutils.jwriteWithDateTag(parentDir, filename,r)
