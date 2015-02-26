Sun Feb 15 15:55:20 CST 2015

```
$ cd projects/datachart/
$ python build-org-term.py
$ cd ../websites && rsync -av root/ USERNAME@console.tw:/home/USERNAME/console.tw
```

Tue Feb 10 18:52:45 CST 2015

```
~/git/console-tw$ cd projects/datachart/
~/git/console-tw/projects/datachart$ python build-org-term.py
mv ../websites/root/data/org-name-taxonomy-term.json ../websites/root/data/org-name-taxonomy-term-150206.json
mv org-name-taxonomy-term.json ../websites/root/data/
```


Thu Feb  5 10:45:25 CST 2015

```
~/git/console-tw/projects/datachart$ nosetests
F.
======================================================================
FAIL: test_meta_count (test_list_json.TestApp150205)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/lin/git/console-tw/projects/datachart/test/test_list_json.py", line 23, in test_meta_count
    self.assertEqual(self.rdict['meta']['count'],4245)
AssertionError: 3533 != 4245
-------------------- >> begin captured logging << --------------------
requests.packages.urllib3.connectionpool: INFO: Starting new HTTP connection (1): file.data.gov.tw
requests.packages.urllib3.connectionpool: DEBUG: "GET /event/%E6%94%BF%E5%BA%9C%E8%B3%87%E6%96%99%E9%96%8B%E6%94%BE%E5%B9%B3%E8%87%BA%E8%B3%87%E6%96%99%E9%9B%86%E6%B8%85%E5%96%AE.json HTTP/1.1" 200 3180504
--------------------- >> end captured logging << ---------------------

----------------------------------------------------------------------
Ran 2 tests in 4.373s

FAILED (failures=1)
```
