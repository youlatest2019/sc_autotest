#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/9/13 9:34
# @Author   : yangshukun
# @File     : getfiledir.py

import os

dir = os.path.dirname(os.path.dirname(__file__))

CONFDIR = os.path.join(dir, 'Config')

BASEFACTORYDIR = os.path.join(dir, 'BaseOperations')

RESULTDIR = os.path.join(dir, 'result')

LOGDIR = os.path.join(RESULTDIR, 'logs')

REPORTDIR = os.path.join(RESULTDIR, 'report')

SCREENSHOTDIR = os.path.join(RESULTDIR, 'screenshosts')


print(SCREENSHOTDIR)

