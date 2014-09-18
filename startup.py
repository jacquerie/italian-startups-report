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

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    data = [el for el in sheet[BUSINESS_TYPE]]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)
    print

    data = [el for el in sheet[REVENUE_CLASS] if el in CLASSES]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)
    print

    data = [el for el in sheet[EMPLOYEE_CLASS] if el in CLASSES]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)


if __name__ == '__main__':
    main()
