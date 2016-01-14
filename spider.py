#!/usr/bin/env python
import urllib2,re

def url_html(num):
    request = urllib2.Request('http://dig.chouti.com/all/hot/recent/%s' % num)
    response = urllib2.urlopen(request)
    html = response.read()

    p = re.compile(r'<div class="item">.*?<div class=.*?<a href="(.*?)" class=.*?>(.*?)</a>.*?<a class="time-a" href="(.*?)" target="_blank">',re.S)
    m = re.findall(p,html)
    
    for i in m:
        if i[0].split(':')[0] == 'http':
            print i[0].strip()
        else:
            print 'http://dig.chouti.com%s' % i[0].strip()
        if len(i[1].strip().split()) == 1:
            print '%s' % i[1].strip()
            print i[2].strip()
        else:
            if 'span' in i[1]:
                pp = re.compile(r'class="kind-name">(.*?)</span>',re.S)
                mm = re.findall(pp,i[1].split()[1])
                print mm[0] , (i[1].split())[2]
                print i[2].split()
            else:
                if len(i) == 2:
                    print ''.join(i[1:]).strip()
                else:
                    print ''.join(i[1:]).strip().split('\t')[0]
                    print ''.join(i[1:]).strip().split('\t')[-1]
        print ''
    
if __name__=='__main__':
    for i in xrange(1,2):
        url_html(i)
