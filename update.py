#coding=utf-8
import datetime
import urllib2,os
import pycurl
import hashlib

def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        m = f.read()
    sha1obj = hashlib.sha1()
    sha1obj.update(m)
    hash = sha1obj.hexdigest()
    return hash

def curl_msg(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    head = response.headers
    html = response.read()
    msg = [head,html]
    return msg

def play():
    token = 'df41d979799281a40aa309eda9c0fda5a9bd8990'
    today = datetime.datetime.now().strftime('%Y%m%d')
    day = curl_msg('http://user.ipip.net/download.php?a=version&token=%s' % token)
    if day[1] == today:
        dat = curl_msg('http://user.ipip.net/download.php?token=%s' % token)
        size = str(dat[0]).split()[10]
        sha1 = str(dat[0]).split()[17].split('-')[1]
        print size,sha1
        with open('/salt/rio/mydata4vipday2.dat','wb+') as f:
            f.write(dat[1])
        f_sha1 = CalcSha1('/salt/rio/mydata4vipday2.dat')
        if f_sha1 == sha1:
            os.system('salt megatron* state.sls rio.ipip -v')
        else:
            print 'sha1 is diff,please download again!!!!'
    else:
        print "did'not update"

def get_md5(path):
    m = md5()
    a_file = open(path,'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()


if __name__=='__main__':
    play()