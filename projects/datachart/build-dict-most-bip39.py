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
import requests,io,json,hashlib,jutils,datetime,shutil,funcy
from collections import Counter
import itertools

MOST_LIMIT = 512
CHAR_MIN = 2
CHAR_MAX = 2

def jj(o):
    return jutils.jdump(o)

def buildDict(prefix,urlx):
    rd = jutils.getHttpCsv(urlx)
    rdict = {}
    wlist = []
    for row in rd:
        cols = row.split(',')
        if len(cols) > 5:
            wlist.append(cols[5])
    w2list = [i for i in wlist if len(i) >= CHAR_MIN and len(i) <= CHAR_MAX]
    #print jj(w2list[:50])
    #pr = partListToDict(w2list,keyFuncFirstChar)
    pr = funcy.group_by(lambda x : x[0], w2list)
    c = Counter([i[0] for i in w2list]).most_common(MOST_LIMIT)
    # print jj(c[:24])
    # print jj(pr[c[0][0]])
    fmck = [i[0] for i in c]
    fmcv = [i[1] for i in c]
    # 256*8=2048
    # 512*4=2048
    wordlist = funcy.flatten([pr[x][:4] for x in fmck])
    rdict['data'] = funcy.select_keys(lambda x:x in fmck, pr)
    rdict['meta'] = {
        'source':urlx,
        'wordlist':wordlist,
        'firstMostCommonKey': fmck,
        'firstMostCommonCount':fmcv,
          'host':'http://data.gov.tw',
          'build':'http://console.tw',
          'script':'https://github.com/y12studio/console-tw/tree/master/projects/datachart/',
          'prefix':prefix,
          'time':datetime.datetime.utcnow().isoformat()}
    return rdict

"""
稿件版本,稿件階段,稿件狀態,備注,字詞流水序,正體字形,簡化字形,音序,臺／陸特有詞,臺／陸特有音,臺灣音讀,臺灣漢拼..

upload to 
http://console.tw/data/dict-most-bip39/v1/dict-most-bip39.json
"""

if __name__ == '__main__':
    #url = 'https://github.com/g0v/moedict-data-csld/blob/master/兩岸詞典.csv'
    # 24MB, download to local server for test
    url = 'http://localhost:8080/dict.csv'
    prefix = 'dict-most-bip39'
    r = buildDict(prefix, url)
    parentDir = '../websites/root/data/'+prefix+'/v1/'
    jutils.jwriteWithDateTag(parentDir,prefix,r)
