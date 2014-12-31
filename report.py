#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from constants import *
import itertools
import math
import pandas as pd


def estimate_total(sheet, column, values, limits):
    lower = 0
    upper = 0
    s = sheet[
        sheet[column].isin(values)
    ][column]
    for el in s:
        if el in limits:
            lower += limits[el]['lower']
            upper += limits[el]['upper']
        else:
            continue
    return [lower, upper]


def combine_and_count(sheet, fst_col, fst_val, snd_col, snd_val):
    return sheet[
        (sheet[fst_col].isin(fst_val)) &
        (sheet[snd_col].isin(snd_val))
    ].T.apply(
        lambda el: str(el[fst_col]) + str(el[snd_col])
    ).value_counts()


def intersect_and_project(sheet, fst_col, fst_val, snd_col, snd_val, res_col):
    return sheet.loc[
        (sheet[fst_col] == fst_val) &
        (sheet[snd_col] == snd_val), res_col]


def month_diff(d1, d2):
    return (365 * (d1.year - d2.year) + (d1.dayofyear - d2.dayofyear)) / 30


def main():
    xls = pd.ExcelFile(XLS_NAME)
    sheet = xls.parse(SHEET_NAME)

    print
    print 'First ten provinces ordered by number of startups'
    print '-------------------------------------------------'
    print sheet[BUSINESS_PROV].value_counts().head(10)
    print

    # XXX(jacquerie): This needs a refactoring.
    print
    print 'First ten provinces ordered by numer of startups, weighted by population'
    print '------------------------------------------------------------------------'
    d = {}
    s = sheet.groupby([BUSINESS_PROV]).size()
    for el in s.index:
        d[el] = s[el] / float(POPULATION[el])
    result = sorted(d.iteritems(), key=lambda x: -x[1])
    for el in map(lambda x: x[0], result[:10]):
        print "%s%7d" % (el, s[el])
    print

    print
    print 'Business types used by startups with counts'
    print '-------------------------------------------'
    print sheet[BUSINESS_TYPE].value_counts()
    print

    print
    print 'Lower and upper estimates of all revenue produced by startups'
    print '-------------------------------------------------------------'
    lower, upper = estimate_total(sheet,
                                  REVENUE_CLASS,
                                  REVENUE_CLASSES,
                                  REVENUE_LIMITS)
    print "Minimum total revenue: €%d" % lower
    print "Maximum total revenue: €%d" % upper
    print "N: %d" % sheet[
        sheet[REVENUE_CLASS].isin(REVENUE_CLASSES)
    ][REVENUE_CLASS].count()
    print

    print
    print 'Lower and upper estimates of the total number of employees in startups'
    print '----------------------------------------------------------------------'
    lower, upper = estimate_total(sheet,
                                  EMPLOYEE_CLASS,
                                  EMPLOYEE_CLASSES,
                                  EMPLOYEE_LIMITS)
    print "Minimum total employees: %d" % lower
    print "Maximum total employees: %d" % upper
    print "N: %d" % sheet[
        sheet[EMPLOYEE_CLASS].isin(EMPLOYEE_CLASSES)
    ][EMPLOYEE_CLASS].count()
    print

    print
    print 'Lower and upper estimates of the total capital of startups'
    print '----------------------------------------------------------'
    lower, upper = estimate_total(sheet,
                                  CAPITAL_CLASS,
                                  CAPITAL_CLASSES,
                                  CAPITAL_LIMITS)
    print "Minimum total capital: €%d" % lower
    print "Maximum total capital: €%d" % upper
    print "N: %d" % sheet[
        sheet[CAPITAL_CLASS].isin(CAPITAL_CLASSES)
    ][CAPITAL_CLASS].count()
    print

    print
    print 'Classes combining revenue and employee classes and their counts'
    print '---------------------------------------------------------------'
    print combine_and_count(sheet,
                            REVENUE_CLASS, REVENUE_CLASSES,
                            EMPLOYEE_CLASS, EMPLOYEE_CLASSES)
    print

    print
    print 'Startups whose revenue class is smaller than their employee class'
    print '-----------------------------------------------------------------'
    print sheet.loc[
        (sheet[REVENUE_CLASS].isin(REVENUE_CLASSES)) &
        (sheet[EMPLOYEE_CLASS].isin(EMPLOYEE_CLASSES)) &
        (sheet[REVENUE_CLASS] < sheet[EMPLOYEE_CLASS]), BUSINESS_NAME]
    print

    print
    print 'Startups whose revenue class is much bigger than their employee class'
    print '---------------------------------------------------------------------'
    for el in itertools.product(REVENUE_CLASSES, EMPLOYEE_CLASSES):
        if (ord(el[0]) > ord(el[1]) + 1):
            print intersect_and_project(sheet,
                                        REVENUE_CLASS, el[0],
                                        EMPLOYEE_CLASS, el[1],
                                        BUSINESS_NAME)
            print
    print

    print
    print 'Classes combining revenue class and capital class'
    print '-------------------------------------------------'
    print combine_and_count(sheet,
                            REVENUE_CLASS, REVENUE_CLASSES,
                            CAPITAL_CLASS, CAPITAL_CLASSES)
    print

    print
    print 'Classes combining employee class and capital class'
    print '-------------------------------------------------'
    print combine_and_count(sheet,
                            EMPLOYEE_CLASS, EMPLOYEE_CLASSES,
                            CAPITAL_CLASS, CAPITAL_CLASSES)
    print

    # XXX(jacquerie): This needs a refactoring.
    print
    print 'First ten startups by month-by-month growth estimate'
    print '----------------------------------------------------'
    d = {}
    s = pd.to_datetime(sheet[BEGIN_DATE], dayfirst=True)
    for el in s.index:
        if sheet.at[el, REVENUE_CLASS] in REVENUE_CLASSES and not pd.isnull(s[el]):
            n = month_diff(pd.to_datetime(DATE), s[el])
            if (n < 6):
                continue  # Discard startups active for less than 6 months.
            b = max(REVENUE_LIMITS[sheet.at[el, REVENUE_CLASS]]['lower'], 10000)
            d[el] = (math.log(b) - math.log(10000)) / n
    result = sorted(d.iteritems(), key=lambda x: -x[1])
    for el in map(lambda x: x[0], result[:10]):
        print sheet.at[el, BUSINESS_NAME]
    print

    # XXX(jacquerie): This needs a refactoring.
    print
    print 'Startups active for more than 48 months'
    print '---------------------------------------'
    d = {}
    s = pd.to_datetime(sheet[BEGIN_DATE], dayfirst=True)
    for el in s.index:
        if not pd.isnull(s[el]):
            n = month_diff(pd.to_datetime(DATE), s[el])
            if (n > 48):
                d[sheet.at[el, BUSINESS_NAME]] = n
    result = sorted(d.iteritems(), key=lambda x: x[1])
    for el in result:
        print "%d\t%s" % (el[1], el[0])
    print


if __name__ == '__main__':
    main()
