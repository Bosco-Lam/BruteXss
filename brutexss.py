# Based on  shawarkhanethicalhacker/BruteXSS, https://github.com/shawarkhanethicalhacker/BruteXSS.
# #!/usr/bin/env python
# -*- coding:utf-8 -*-
# BruteXSS
# Cross-Site Scripting Bruteforcer
# @Author: Bosco Lam

import getopt
import sys
from colorama import init

from check_method import get, post

init()
banner = """
  ____             _        __  ______ ____  
 | __ ) _ __ _   _| |_ ___  \ \/ / ___/ ___| 
 |  _ \| '__| | | | __/ _ \  \  /\___ \___ \ 
 | |_) | |  | |_| | ||  __/  /  \ ___) |__) |
 |____/|_|   \__,_|\__\___| /_/\_\____/____/ 

 BruteXSS - Cross-Site Scripting BruteForcer

 Sponsored & Supported by Netsparker Web Application Security Scanner 

 Note: Using incorrect payloads in the custom
 wordlist may give you false positives so its
 better to use the wordlist which is already
 provided for positive results.
"""


def brute_xss(argv):
    print(banner)
    method = ''
    url = ''
    txt = ''
    data = ''
    try:
        opts, args = getopt.getopt(argv, "hm:u:t:d:", ["mfile=", "ufile=", "tfile=", "dfile"])
    except getopt.GetoptError:
        print('test.py -m <method> -u <url> -t <payload txt>')
        sys.exit(2)
    print opts, args
    for opt, arg in opts:
        if opt == '-h':
            print("""
            -m    Method,support GET and POST
            -u    The url to test
            -t    Use the payload file""")
            sys.exit(2)
        elif opt in ("-m", "--mfile"):
            method = arg
        elif opt in ("-u", "--ufile"):
            url = arg
        elif opt in ("-t", "--tfile"):
            txt = arg
        elif opt in ("-d", "--dfile"):
            data = arg
    if method.lower()[0] == 'g':
        get(url, txt)
    elif method.lower()[0] == 'p':
        post(url, txt, data)
    else:
        print("Incorrect method")


if __name__ == "__main__":
    brute_xss(sys.argv[1:])
