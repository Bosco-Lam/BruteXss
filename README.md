#BruteXSS

BruteXSS - Cross-Site Scripting BruteForcer

Author: Bosco Lam

**The BruteXSS project is sponsored and supported by [Netsparker Web Application Security Scanner](https://www.netsparker.com/?utm_source=github.com&utm_medium=referral&utm_content=brand+name&utm_campaign=generic+advert)**

Disclaimer: I am not responsible for any damage done using this tool. This tool should only be used for educational purposes and for penetration testing.


###Compatibility: 
* Windows , Linux or any device running python 2.7

###Requirements: 

* Python 2.7

* Wordlist included(wordlist.txt)

* Modules required: Colorama, Mechanize


###Modules Required:

* Colorama:  https://pypi.python.org/pypi/colorama/

* Mechanize: https://pypi.python.org/pypi/mechanize/


###Description:
**BruteXSS** is a very powerful and fast Cross-Site Scripting Brutforcer which is used for bruteforcing a parameters. The BruteXSS injects multiple payloads loaded from a specified wordlist and fires them at the specified parameters and scans if any of the parameter is vulnerable to XSS vulnerability. BruteXSS is very accurate at doing its task and there is no chance of false positive as the scanning is much powerful. BruteXSS supports POST and GET requests which makes it compatible with the modern web applications.

###Features:

* XSS Bruteforcing

* XSS Scanning

* Supports GET/POST requests

* Custom wordlist can be included

* One command can do all the things

###Usage:

```
COMMAND:  python brutexss.py -m <METHOD> -u <URL> -t <WORDLIST> -d <DATA>
METHOD:   (G)ET & (P)OST
URL:      http://www.site.com/?parameter=value
WORDLIST: wordlist.txt
POST DATA: parameter=value&parameter1=value1
```

###Output:

```
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
Checking if site.com is available...
site.com is available! Good!
Bruteforce start:
Testing 'parameter' parameter...
2 / 25 payloads injected...
Bruteforce Completed.
'parameter1' parameter not vulnerable.
1 Parameter is vulnerable to XSS.
Scan Result for site.com
+----+--------------+----------------+
| Id | Parameters   |     Status     |
+----+--------------+----------------+
| 0  |  parameter   |  Vulnerable    |
+----+--------------+----------------+
| 1  |   parameter1 | Not Vulnerable |
+----+--------------+----------------+

```
