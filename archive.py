#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from constants import *
import shutil


def main():
    new_name = 'startup-' + DATE + '.xls'
    old_name = 'startup.xls'

    shutil.copy(old_name, new_name)


if __name__ == '__main__':
    main()
