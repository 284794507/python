#!/usr/bin/python
# -*- coding:utf8 -*-    
#coding:utf-8

#import regex
import re

def test_search():
    #re = regex.compile()
    result = re.findall('fs','fs ffs fss')
    if result is not None:
        print(result)
        for item in result:
            print(item)

def get_num_from_str(val:str):
    re = regex.compile()
    result = re.search('fs','fs ffs fss')
    if result is not None:
        print(result)
        
if __name__ == "__main__":
    test_search()
    