#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mon Apr 25 17:03:04 BST 2016
import sys

IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'


def my_logo():
    return """
    submission for test for <redacted>
    Chris T. Cheyne
    christopercheyne@gmail.com

    """

class Infinitum:
    """ return sum[i = 1..N, n] """
    def __init__(self):
        self.T = 3
        self.N = 1
        self.m = 1
        self.a = {}     # poor mans hashtable
        self.b = {}     # final column output

    def compute_data(self):
        """ read the data from STDIN (really should be a text file) """
        """ and we would use 'with open FILENAME as f:' """
        """ no error checking to decrease verbosity """
        #print "INPUT T, number of test cases :"
        self.T = int(raw_input())
        for k in xrange(0, self.T):
            # for T = 5, we have range [0..4]
            #print "INPUT n, M line " + str(k+1) + " :"
            self.a[k] = map(int, raw_input().split())
            self.N, self.m, res = (self.a[k][0], self.a[k][1], 0)
            # sum the operators in modulo
            for a in xrange(1, self.N+1):
                res += (a % self.m)
            self.b[k] = res


    def print_data(self):
        """ print the results, array a """
        """ should use dict.values() """
        for k in xrange(0,len(self.b)):
            print self.b[k]


if __name__ == '__main__':
    # print my_logo()
    I = Infinitum()
    I.compute_data()
    I.print_data()

