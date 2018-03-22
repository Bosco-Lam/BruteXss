#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author: Bosco Lam

import sys

from colorama import Style, Fore


def word_list_import(txt_file, lst):
    try:
        with open(txt_file, 'r') as f:  # Importing Payloads from specified wordlist.
            for line in f:
                final = str(line.replace("\n", ""))
                lst.append(final)
    except IOError:
        print("[!] Wordlist not found!")
        sys.exit(2)


def bg(p, status):
    try:
        b = ""
        la = ""
        lostatus = ""
        num = []
        s = len(max(p, key=len))  # list
        if s < 10:
            s = 10
        for i in range(len(p)):
            num.append(i)
        maxval = str(len(num))  # number
        for i in range(s):
            b = b + "-"
        for i in range(len(maxval)):
            la = la + "-"
        statuslen = len(max(status, key=len))
        for i in range(statuslen):
            lostatus = lostatus + "-"
        if len(b) < 10 :
            b = "----------"
        if len(lostatus) < 14:
            lostatus = "--------------"
        if len(la) < 2:
            la = "--"
        los = statuslen
        if los < 14:
            los = 14
        lenb = len(str(len(b)))
        if lenb < 14:
            lenb = 10
        else:
            lenb = 20
        upb = ("+-%s-+-%s-+-%s-+")%(la,b,lostatus)
        print(upb)
        st0 = "Parameters"
        st1 = "Status"
        print("| Id | "+st0.center(s, " ")+" | "+st1.center(los, " ")+" |")
        print(upb)
        for n, i, d in zip(num, p, status):
            string = (" %s | %s " % (str(n), str(i)))
            lofnum = str(n).center(int(len(la)), " ")
            lofstr = i.center(s, " ")
            lofst = d.center(los, " ")
            if "Not Vulnerable" in lofst:
                lofst = Fore.GREEN+d.center(los, " ")+Style.RESET_ALL
            else:
                lofst = Fore.RED+d.center(los, " ")+Style.RESET_ALL
            print("| "+lofnum+" | "+lofstr+" | "+lofst+" |")
            print(upb)
        return ""
    except ValueError:
        print("Uh oh! No parameters in URL!")


def complete(p, r, c, d):
    print("Bruteforce Completed.")
    if c == 0:
        print("Given parameters are not vulnerable to XSS.")
    elif c == 1:
        print("%s Parameter is vulnerable to XSS." % c)
    else:
        print("%s Parameters are vulnerable to XSS." % c)
    print("Scan Result for %s:" % d)
    print bg(p, r)
    sys.exit(0)
