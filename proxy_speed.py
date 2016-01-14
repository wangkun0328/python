import urllib2,sys,re,time
import xml.dom.minidom
import logging
from multiprocessing import Process, Manager


logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='myapp.log',
    filemode='a+')


def curl_msg(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request,timeout=5)
    #head = response.headers
    html = response.read()
    return html


def xml_msg(xml_str):
    speed_list = []
    dom = xml.dom.minidom.parseString(xml_str)
    root = dom.documentElement
    itemlist = root.getElementsByTagName('PROXY')
    for n in range(len(itemlist)):
        item = itemlist[n]
        speed = item.getAttribute("PROXY_SPEED")
        speed_list.append(speed)
    return speed_list

def speed_msg(i):
#    error_list = []
    global error_list
    limit = 40

    try:
        xml_s = curl_msg('http://%s:8888/speed' % i)
        speed_list = xml_msg(xml_s)
    except:
        speed_list = [0.000]
#    return speed_list

    print i , speed_list

    logging.debug({i:speed_list})
    num = 0
    for s in speed_list:
        if int(str(s).split('.')[0]) >= limit:
            num += 1
        elif float(re.findall('\d+.\d+',str(s))[0]) == 0:
            num += 1
        else:
            pass
    if num == len(speed_list):
        error_list.append(i)
    #print error_list


def limit():
    global error_list
    error_list = []
#    limit = 40
    ip_list = ['8.8.8.8','1.1.1.1']
    threads = []
    for a in ip_list:
        t = Process(target=speed_msg, args=(a,))
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

#        try:
#            xml_s = curl_msg('http://%s:8888/speed' % i)
#            speed_list = xml_msg(xml_s)
#        except:
#            speed_list = [0.000]
        
#        print i , speed_list
#
#        logging.debug({i:speed_list})
#        num = 0
#        for s in speed_list:
#            if int(str(s).split('.')[0]) >= limit:
#                num += 1
#            elif float(re.findall('\d+.\d+',str(s))[0]) == 0:
#                num += 1
#            else:
#                pass
#        if num == len(speed_list):
#            error_list.append(i)
    return error_list

def play():
    main_dic = {}
    while True:
        error_list = limit()
        for ip in error_list:
            if ip in main_dic:
                if main_dic[ip][2] == 0:
                    main_dic[ip][1] += 1
                else:
                    main_dic[ip][2] = 0
                    main_dic[ip][1] += 1
                    main_dic[ip][0] = main_dic[ip][1] - 1
            else:
                main_dic[ip] = [-1,0,0]
        for ip_renew in main_dic.keys():
            main_dic[ip_renew][0] += 1
            main_dic[ip_renew][2] = main_dic[ip_renew][0] - main_dic[ip_renew][1]

        for m in main_dic.keys():
            if main_dic[m][1] == 5:
                print 'error'
                logging.info('%s is error' % m)
            elif main_dic[m][2] == 10:
                if main_dic[m][1] >= 5:
                    del main_dic[m]
                    print 'renew'
                    logging.info('%s is renew' % m)
                else:
                    del main_dic[m]
            else:
                pass
        print main_dic
        logging.debug(main_dic)
        
        time.sleep(10)


if __name__=='__main__':
    try:
        play()
    #xml_s = curl_msg('http://219.146.243.186:8888/speed')
    #xml_msg(xml_s)
    except KeyboardInterrupt:
        print 'ctrl-c'
        sys.exit()
