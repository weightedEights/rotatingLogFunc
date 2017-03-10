#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
Intro Text
"""

from datetime import datetime


def main():

    printHeader()


def printHeader():
    print("---------------------------------")
    print("   Rotating Log Test Script")
    print("   " + str(datetime.now()))
    print("---------------------------------")


if __name__ == '__main__':
    main()