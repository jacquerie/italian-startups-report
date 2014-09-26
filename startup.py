#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter
import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_15092014'

BUSINESS_TYPE = 'nat.giuridica'
REVENUE_CLASS = 'classe di valore della produzione ultimo anno (1)'
EMPLOYEE_CLASS = 'classe di addetti ultimo anno (2)'
CLASSES = ['A', 'B', 'C', 'D', 'E']

def print_report(sheet, column, values=None):
    data = [el for el in sheet[column]]
    if values:
        data = filter(lambda el: el in values, data)

    for k, v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)
    print

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    print_report(sheet, BUSINESS_TYPE)
    print_report(sheet, REVENUE_CLASS, CLASSES)
    print_report(sheet, EMPLOYEE_CLASS, CLASSES)

    data = sheet.as_matrix()
    good = filter(lambda el: el[-5] in CLASSES and el[-4] in CLASSES and el[-5] < el[-4], data)
    for el in map(lambda el: el[0], good):
        print el

if __name__ == '__main__':
    main()
