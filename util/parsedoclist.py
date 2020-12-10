#!/usr/bin/env python

import json

codeDocList = {}

def load_doclist(doclist_name):
    with open(doclist_name, 'r') as f:
        data = json.load(f)
        return data

def doc_of_the_code(code_name):
    value = codeDocList.get(code_name)
    if value:
        return value
    else:
        return 'OMGNoDocFound'

# The following code is for test
codeDocList = load_doclist("doclist.json")
#print(codeDocList)
#
#print(doc_of_the_code('hello.c'))
#print(doc_of_the_code('world.c'))
#print(doc_of_the_code('test.c'))
#print(doc_of_the_code('bye.c'))
