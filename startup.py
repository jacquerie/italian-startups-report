#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pandas as pd

XLS_NAME = 'startup.xls'
SHEET_NAME = 'STARTUP_22092014'

BUSINESS_NAME = 'denominazione'
BUSINESS_TYPE = 'nat.giuridica'
REVENUE_CLASS = 'classe di valore della produzione ultimo anno (1)'
EMPLOYEE_CLASS = 'classe di addetti ultimo anno (2)'

CLASSES = ['A', 'B', 'C', 'D', 'E']


def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    # Business type counts.
    print sheet[BUSINESS_TYPE].value_counts()
    print

    # Revenue classes counts.
    print sheet[
        sheet[REVENUE_CLASS].isin(CLASSES)
    ][REVENUE_CLASS].value_counts()
    print

    # Employee classes counts.
    print sheet[
        sheet[EMPLOYEE_CLASS].isin(CLASSES)
    ][EMPLOYEE_CLASS].value_counts()
    print

    # Classes mixing revenue class and employee class, and their counts.
    print sheet[
        (sheet[REVENUE_CLASS].isin(CLASSES)) &
        (sheet[EMPLOYEE_CLASS].isin(CLASSES))
    ].T.apply(
        lambda el: el[REVENUE_CLASS] + el[EMPLOYEE_CLASS]
    ).value_counts()
    print

    # Startups whose revenue class is smaller than their employee class.
    print sheet.loc[
        (sheet[REVENUE_CLASS].isin(CLASSES)) &
        (sheet[EMPLOYEE_CLASS].isin(CLASSES)) &
        (sheet[REVENUE_CLASS] < sheet[EMPLOYEE_CLASS]), BUSINESS_NAME]
    print

    # Startups whose revenue class is much bigger than their employee class.
    print sheet.loc[
        sheet.index[sheet[
            (sheet[REVENUE_CLASS].isin(CLASSES)) &
            (sheet[EMPLOYEE_CLASS].isin(CLASSES))
        ].T.apply(
            lambda el: ord(el[REVENUE_CLASS]) > ord(el[EMPLOYEE_CLASS]) + 1).T
        ], BUSINESS_NAME]
    print


if __name__ == '__main__':
    main()
