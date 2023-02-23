import base64
import requests
from lxml import etree
# "weblogic" && country="JP"
# https://fofa.info/result?qbase64=
#print(免责声明，本工具仅限学习使用，严禁用于违法犯罪，发生任何问题、违反任何法律都与发布者无关！)
def host_c():
    # search_kw = '"weblogic" && country="HK"'
    kw = 'CN'
    search_kw = f'"jboss" && country="{kw}"'
    search_url = 'https://fofa.info/result?qbase64='

    # &page=5&page_size=10
    # url拼接部分
    search_kw_encode = search_kw.encode()
    search_kw_base64 = base64.b64encode(search_kw_encode).decode()

    zuihou_url = search_url + search_kw_base64 + '&page=5&page_size=10'

    for page_num in range(1, 7):
        zuihou_url = search_url + search_kw_base64 + f'&page={page_num}&page_size=10'
        # print(zuihou_url)

        headers = {
            'Cookie': '_ga=GA1.1.1727528502.1669190434; __fcd=d2qC3zwUxnHBPcq24TUyKSW4; is_flag_login=0; isRedirect=1; Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1676258628,1676293078,1677119276; befor_router=%2F; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MjQ3MTA0LCJtaWQiOjEwMDE0MDk1MCwidXNlcm5hbWUiOiJzZG40MjIwMTYzIiwiZXhwIjoxNjc3Mzc4NDc4fQ.0lVL0PDET_9oCv-pMIZ4815sGr6THH2Oe2JOyU1u9KCVUVWhbaZnMoRcTxSdMJAEbVS9YY0DCBc9AYqvqHffQQ; user=%7B%22id%22%3A247104%2C%22mid%22%3A100140950%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22sdn4220163%22%2C%22nickname%22%3A%22sdn4220163%22%2C%22email%22%3A%22411631703%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%2296d46c25654b46604ac76233bf476875%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22sdn4220163%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A0%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D; baseShowChange=false; viewOneHundredData=false; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1677120701; _ga_9GWBD260K9=GS1.1.1677119275.7.1.1677120889.0.0.0',

        }

        # print(zuihou_url)

        ret = requests.get(zuihou_url, headers=headers)
        result = ret.content.decode()
        # print(result)
        et = etree.HTML(result)
        addrs = et.xpath('//div/span[@class="hsxa-host"]/a/@href')
        with open(f'domains_{kw}.txt', 'a') as f:
            for each_url in addrs:
                f.write(f'{each_url}\n')

        # print(addrs)  # ['url1', 'url2'...]

host_c()

