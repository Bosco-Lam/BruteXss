#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author: Bosco Lam

import httplib
import mechanize
import socket
import urllib
import urlparse
from string import whitespace

from tools import *


def get(site, pl_file):
    try:
        if 'https://' in site or 'http://' in site:
            pass
        else:
            site = "http://" + site
        final_url = urlparse.urlparse(site)
        urldata = urlparse.parse_qsl(final_url.query)
        domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=final_url)
        domain = domain0.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
        print("Checking if " + domain + " is available...")
        connection = httplib.HTTPConnection(domain)
        connection.connect()
        print(domain + " is available! Good!")
        url = site
        paraname = []
        paravalue = []
        payloads = []
        word_list_import(pl_file, payloads)
        o = urlparse.urlparse(site)
        parameters = urlparse.parse_qs(o.query, keep_blank_values=True)
        path = urlparse.urlparse(site).scheme + "://" + urlparse.urlparse(site).netloc + urlparse.urlparse(site).path
        for para in parameters:  # Arranging parameters and values.
            for i in parameters[para]:
                paraname.append(para)
                paravalue.append(i)
        total = 0
        c = 0
        fpar = []
        fresult = []
        progress = 0
        print("Bruteforce start:")
        for pn, pv in zip(paraname, paravalue):  # Scanning the parameter.
            print("Testing '" + pn + "' parameter...")
            fpar.append(str(pn))
            for x in payloads:  #
                validate = x.translate(None, whitespace)
                if validate == "":
                    progress = progress + 1
                else:
                    sys.stdout.write("\r%i / %s payloads injected..." % (progress, len(payloads)))
                    sys.stdout.flush()
                    progress = progress + 1
                    enc = urllib.quote_plus(x)
                    data = path + "?" + pn + "=" + pv + enc
                    page = urllib.urlopen(data)
                    sourcecode = page.read()
                    if x in sourcecode:
                        print("XSS Vulnerability Found! \n" + "Parameter:\t%s\n" + "Payload:\t%s" % pn, x)
                        fresult.append("  Vulnerable  ")
                        c = 1
                        total = total + 1
                        progress = progress + 1
                        break
                    else:
                        c = 0
            if c == 0:
                print("'%s' parameter not vulnerable." % pn)
                fresult.append("Not Vulnerable")
                progress = progress + 1
                pass
            progress = 0
        complete(fpar, fresult, total, domain)
    except (httplib.HTTPResponse, socket.error) as Exit:
        print(site + "is offline")


def post(site, pl_file, data):
    try:
        try:
            br = mechanize.Browser()
            br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11')]
            br.set_handle_robots(False)
            br.set_handle_refresh(False)
            if 'https://' in site or 'http://' in site:
                pass
            else:
                site = "http://" + site
            finalurl = urlparse.urlparse(site)
            urldata = urlparse.parse_qsl(finalurl.query)
            domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=finalurl)
            domain = domain0.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
            print("Checking if " + domain + " is available...")
            connection = httplib.HTTPConnection(domain)
            connection.connect()
            print(domain + " is available! Good!")
            path = urlparse.urlparse(site).scheme + "://" + urlparse.urlparse(site).netloc + urlparse.urlparse(site).path
            param = str(data)
            payloads = []
            word_list_import(pl_file, payloads)
            lop = str(len(payloads))
            print("Bruteforce start:")
            params = "http://www.site.com/?" + param
            final_url = urlparse.urlparse(params)
            urldata = urlparse.parse_qsl(final_url.query)
            o = urlparse.urlparse(params)
            parameters = urlparse.parse_qs(o.query, keep_blank_values=True)
            paraname = []
            paravalue = []
            for para in parameters:  # Arranging parameters and values.
                for i in parameters[para]:
                    paraname.append(para)
                    paravalue.append(i)
            fpar = []
            fresult = []
            total = 0
            progress = 0
            pname1 = []  # parameter name
            payload1 = []
            for pn, pv in zip(paraname, paravalue):  # Scanning the parameter.
                print("Testing '" + pn + "' parameter...")
                fpar.append(str(pn))
                for i in payloads:
                    validate = i.translate(None, whitespace)
                    if validate == "":
                        progress = progress + 1
                    else:
                        progress = progress + 1
                        sys.stdout.write("\r%i / %s payloads injected..." % (progress, len(payloads)))
                        sys.stdout.flush()
                        pname1.append(pn)
                        payload1.append(str(i))
                        d4rk = 0
                        for m in range(len(paraname)):
                            d = paraname[d4rk]
                            d1 = paravalue[d4rk]
                            tst = "".join(pname1)
                            tst1 = "".join(d)
                            if pn in d:
                                d4rk = d4rk + 1
                            else:
                                d4rk = d4rk + 1
                                pname1.append(str(d))
                                payload1.append(str(d1))
                        data = urllib.urlencode(dict(zip(pname1, payload1)))
                        r = br.open(path, data)
                        sourcecode = r.read()
                        pname1 = []
                        payload1 = []
                        if i in sourcecode:
                            print(" XSS Vulnerability Found! \n" + " Parameter:\t%s\n" + " Payload:\t%s" % (pn, i))
                            fresult.append("  Vulnerable  ")
                            c = 1
                            total = total + 1
                            progress = progress + 1
                            break
                        else:
                            c = 0
                if c == 0:
                    print(" '%s' parameter not vulnerable." % pn)
                    fresult.append("Not Vulnerable")
                    progress = progress + 1
                    pass
                progress = 0
            complete(fpar, fresult, total, domain)
        except(httplib.HTTPResponse, socket.error) as Exit:
            print("Site " + site + " is offline!" + Style.RESET_ALL)
    except (mechanize.HTTPError, mechanize.URLError) as e:
        print("HTTP ERROR! %s %s" + Style.RESET_ALL) % (e.code, e.reason)
