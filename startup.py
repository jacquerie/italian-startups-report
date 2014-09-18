#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import Counter
import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_15092014'

def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME, index_col=None, convert_float=False)

    data = [el for el in sheet['nat.giuridica']]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)
    print

    data = [el for el in sheet['classe di valore della produzione ultimo anno (1)'] if el in ['A', 'B', 'C', 'D', 'E']]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)
    print

    data = [el for el in sheet['classe di addetti ultimo anno (2)'] if el in ['A', 'B', 'C', 'D', 'E']]
    for k,v in Counter(data).most_common():
        print "%4d\t%s" % (v, k)


if __name__ == '__main__':
    main()
