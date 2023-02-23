
# http://ip:port/_async/AsyncResponseService
#print(免责声明，本工具仅限学习使用，严禁用于违法犯罪，发生任何问题、违反任何法律都与发布者无关！)
# 221.120.187.201

import requests
import queue
from threading import Thread

def check_poc(q):
    # url = 'https://221.120.187.201'
    # url = 'https://www.baidu.com'
    poc = '/invoker/readonly'
    # poc = '/_async/AsyncResponseService'
    while not q.empty():
        url = q.get()
        target_url = url + poc
        # 忽略HTTPS的证书校验，取消安全提示
        try:
            requests.packages.urllib3.disable_warnings()
            ret = requests.get(target_url, verify=False)
            result = ret.content.decode()
            if 'HTTP Status 500' in result:
                print(f'{target_url}存在jboss反序列化漏洞漏洞!!!!!')
            # elif 'welcome to the' in result:
            #     print(f'{target_url}存在CVE-2017-10271weblogic反序列化漏洞')
            else:
                print(f'{target_url}不存在漏洞')
        except Exception:
            pass

q = queue.Queue()
for each_url in open(r'domains_HK.txt'):
    each_url = each_url.replace('\n', '')
    # check_poc(each_url)
    q.put(each_url)

for i in range(0,10):
    t = Thread(target=check_poc, args=(q, ))
    t.start()
























