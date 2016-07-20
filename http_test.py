# -*- coding: utf-8 -*-
#import urllib2

##eg1
#print urllib2.urlopen('http://www.baidu.com').read()


# import urllib2
# url = 'http://192.168.100.20/devices/test'
# user = 'admin'
# passwd = 'admin'
# psmg = urllib2.HTTPPasswordMgrWithDefaultRealm()
# psmg.add_password(None,url,user,passwd)
# hdlr = urllib2.HTTPBasicAuthHandler(psmg)
# opener = urllib2.build_opener(hdlr)
# urllib2.install_opener(opener)
# f = urllib2.urlopen(url)


import unirest

device_ip = "192.168.100.20"
prefix    = "/devices"

urlprefix = "http://" + device_ip + prefix
print urlprefix

auth_data = ("admin", "admin")
url = urlprefix + "/test"
response = unirest.get(url, auth=auth_data)
print response.body