#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter
import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_22092014'

BUSINESS_TYPE = 'nat.giuridica'
REVENUE_CLASS = 'classe di valore della produzione ultimo anno (1)'
EMPLOYEE_CLASS = 'classe di addetti ultimo anno (2)'
CLASSES = ['A', 'B', 'C', 'D', 'E']

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    print sheet[BUSINESS_TYPE].value_counts()
    print
    print sheet[sheet[REVENUE_CLASS].isin(CLASSES)][REVENUE_CLASS].value_counts()
    print
    print sheet[sheet[EMPLOYEE_CLASS].isin(CLASSES)][EMPLOYEE_CLASS].value_counts()
    print

    data = sheet.as_matrix()

    good = filter(lambda el: el[-5] in CLASSES and el[-4] in CLASSES and el[-5] < el[-4], data)
    for el in map(lambda el: el[0], good):
        print el
    print

    good = filter(lambda el: el[-5] in CLASSES and el[-4] in CLASSES, data)
    for k, v in Counter(map(lambda el: "%c%c" % (el[-5], el[-4]), good)).most_common():
        print "%4d\t%s" % (v, k)
    print

    min_total = 0
    max_total = 0
    good = [el for el in sheet[REVENUE_CLASS] if el in CLASSES]
    for el in good:
        if el == 'A':
            max_total += 110
        elif el == 'B':
            min_total += 110
            max_total += 500
        elif el == 'C':
            min_total += 500
            max_total += 1000
        elif el == 'D':
            min_total += 1000
            max_total += 2000
        elif el == 'E':
            min_total += 2000
            max_total += 5000
    print "Min total: %d000" % min_total
    print "Max total: %d000" % max_total
    print

if __name__ == '__main__':
    main()
