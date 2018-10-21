import re
import requests


def get_region_list():
    url = 'https://bj.lianjia.com/ershoufang/'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'lianjia_uuid=8bab2c14-a665-44ca-b038-8eb50bde5ff4; _smt_uid=5bc740c8.1c1b882f; _ga=GA1.2.916036215.1539784907; _gid=GA1.2.561869791.1539874647; all-lj=3d8def84426f51ac8062bdea518a8717; TY_SESSION_ID=e4370781-048f-4b06-ad73-fca9aadac9b0; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1539874917,1539876161,1539955288,1540036146; select_city=110000; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1540043204',
    'Host': 'bj.lianjia.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.lianjia.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text
    region = re.findall('<div class="sub_nav section_sub_nav" >(.*?)</div>', html, re.S)[0]
    region_patch = re.findall('href="(/ershoufang/.*?)"', region)
    base_url = 'https://bj.lianjia.com'
    region_list = [base_url+i for i in region_patch]
    return region_list