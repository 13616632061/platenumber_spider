#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: @长泽雅美男友
@contact: 374454765@qq.com 
@file: plate_number.py
@time: 2018/2/3 15:37 
"""

import requests
from requests.exceptions import RequestException
import re
import os
from multiprocessing import Pool
import multiprocessing
from bs4 import BeautifulSoup

DIRECTION = '★精美图片\\'

class Fanhao():
    def __init__(self,type):
        self.session = requests.session()
        self.type = type
        self._url_dict_ = {
            '最新发行':'http://www.17fanhao.com/fanhao/index{}html',
            '最近入库':'http://www.17fanhao.com/fanhaoall/index{}html',
            '人气最多':'http://www.17fanhao.com/fanhaolook/index{}html',
            '评分最高':'http://www.17fanhao.com/fanhaoscore/index{}html',
            '步兵':'http://www.17fanhao.com/daquan01/index{}html',
            '字幕':'http://www.17fanhao.com/daquan02/index{}html',
            '单体':'http://www.17fanhao.com/daquan03/index{}html',
            '多名':'http://www.17fanhao.com/daquan04/index{}html',
            '人妻':'http://www.17fanhao.com/daquan05/index{}html',
            '户外':'http://www.17fanhao.com/daquan06/index{}html',
            '校园':'http://www.17fanhao.com/daquan07/index{}html',
            '警匪':'http://www.17fanhao.com/daquan08/index{}html',
            '奇幻':'http://www.17fanhao.com/daquan09/index{}html',

            # '最新出道':'http://www.17fanhao.com/nvyou/index{}html',
            # '最高人气':'http://www.17fanhao.com/nvyoulook/index{}html',
            # '最美':'http://www.17fanhao.com/nvyou01/index{}html',
            # '好看':'http://www.17fanhao.com/nvyou02/index{}html',
            # '萝莉':'http://www.17fanhao.com/nvyou04/index{}html',
            # '大胸':'http://www.17fanhao.com/nvyou05/index{}html',
            # '著名':'http://www.17fanhao.com/nvyou06/index{}html',
            # '90后':'http://www.17fanhao.com/nvyou07/index{}html',
            # '混血':'http://www.17fanhao.com/nvyou09/index{}html',
            # '名模':'http://www.17fanhao.com/nvyou10/index{}html'

        }

    def get_html(self,link):
        """获取网页源代码"""
        headers = {
            'Host':'www.17fanhao.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Referer':'http://www.17fanhao.com/daquan.html',
            'Cookie':'__qiqi__view_ads120164=%2C25071; uhclvlastsearchtime=1517643595; __qiqi__view_plan120164=%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026%2C4026; uv_cookie_120164=1; uv_cookie_120165=1; UBGLAI63GV=dcxzs.1517727907; fikker-g2Cr-JZL8=ujQjCZi6SI7jS8Wh1tkrmdeP1hMJgtO6; fikker-g2Cr-JZL8=ujQjCZi6SI7jS8Wh1tkrmdeP1hMJgtO6; Hm_lvt_b5b2644d738829072e8aa62e0d334290=1517655337,1517727908,1517728718,1517728911; Hm_lvt_6d5e86213b07ede18ec639f1da3bc86b=1517655337,1517727908,1517728718,1517728912; __dsje_cpv_r_15887_cpv_plan_ids=%7C1719%7C%7C1632%7C%7C1645%7C%7C1633%7C; Hm_lpvt_b5b2644d738829072e8aa62e0d334290=1517728914; Hm_lpvt_6d5e86213b07ede18ec639f1da3bc86b=1517728914'
        }
        try:
            response = self.session.get(link,headers = headers)
            if response.status_code == 200:
                response.encoding = 'gb1312'
                return response.text
            return None
        except RequestException:
            print("请求页面失败")
            return None

    def get_counts(self):
        try:
            url = self._url_dict_[self.type].format('.')
            html = self.get_html(url)
            soup = BeautifulSoup(html,'html5lib')
            cnt = soup.select('div.pageurl > a')
            for i in cnt:
               yield i.get('href')
        except:
            return None

    def return_cnt(self):
        try:
            if self.get_counts() == None:
                num = 1
            else:
                n = [x for x in self.get_counts()][-1]
                num = re.findall(r'index_(.*?).html',n)[-1]
            return num
        except IndexError:
            num = 1
            return num

    def input_cnt(self):
        if self.return_cnt() and self.type in self._url_dict_.keys():
            cnt = self.return_cnt()
            print('一共为您搜出{}页'.format(cnt))
            print('提 示 : 不 要 超 过 最 大 页 数 ' + '\n')
            start_cnt = input('请 输 入 爬 取 起 始 页 : ')
            start_cnt = start_cnt.strip(' ')
            start = int(start_cnt)
            end_cnt = input('请 输 入 爬 取 结 束 页 : ')
            end_cnt = end_cnt.strip(' ')
            end = int(end_cnt)
            if end < start:
                end = start
            if start >= 1 and end < int(cnt):
                return start,end
            else:
                return None
        else:
            return None

    def get_index_urls(self,start_index,end_index):
        """获得索引页url"""
        urls = []
        cnts = [cnt for cnt in range(start_index, end_index + 1, 1)]
        for i in cnts:
            if i == 1:
                cnt = '.'
                url = self._url_dict_[self.type].format(cnt)
                urls.append(url)

            if i > 1:
                cnt = '_{n}.' .format(n = str(i))
                url = self._url_dict_[self.type].format(cnt)
                urls.append(url)

        return urls

    def parse_index_html(self,html):
        soup = BeautifulSoup(html,'html5lib')
        href = soup.select('.movie_list > li > a')
        for i in href:
            yield i.get('href')

    def parse_page_html(self,html):
        soup = BeautifulSoup(html,'html5lib')

        item = soup.select('.list_itemm > div')[0]
        item = list(item.stripped_strings)
        actor = ' '.join(item)

        img_tag = soup.select('.intro_figure > img')[0]
        img = re.findall(r'src="(.*?)"/>',str(img_tag))[0]

        num_tag = soup.select('.title_inner > input')[0]
        num = re.findall(r'value="(.*?)"/>',str(num_tag))[0]

        score = soup.select('.mod_score')[0].get_text()

        self.download_img(img,actor,num,score)

    def download_img(self,img,actor,num,score):
        try:
            response = self.session.get(img)
            if response.status_code == 200:
                formats = img.split('.')[-1]  # 获取文件格式
                self.save_img(response.content,actor,num,score,formats)
                print('save the picture : ', actor, num, score + '分')
            return None
        except RequestException:
            print('请求图片失败')

    def save_img(self,content,actor,num,score,formats):
        global DIRECTION

        dir_name = DIRECTION + self.type
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)  # 如果不存在则新建文件夹
        img_name = actor + '  ' + num  + '  ' + score + '分' + '.{}'.format(formats)
        img_path = os.path.join(dir_name,img_name)
        if not os.path.exists(img_path):
            # print('Save the picture: ' + img_path)
            with open(img_path, 'wb') as f:
                f.write(content)
                f.close()

    # def parse_ny_page(self, html):
    #     soup = BeautifulSoup(html,'html5lib')
    #     pass

    def main(self,url):
        index_html = self.get_html(url)
        for i in self.parse_index_html(index_html):
            page_url = 'http://www.17fanhao.com' + i     #详情页链接
            # print(page_url)
            page_html = self.get_html(page_url)
            if page_html:
                self.parse_page_html(page_html)

if __name__ == '__main__':
    tips = """	
                    |============================================
                    |名    称 : 精美图片爬取      
                    |版    本 : 3.0      
                    |作    者 : F_H_X                
                    |邮    箱 : 374454765@qq.com     
                    |功    能 : 获取精美图片保存到本地   
                    |可选类型 :  最新发行 最近入库
                    |           人气最多 评分最高
                    |           步兵 字幕 单体  
                    |           多名 人妻 户外
                    |           校园 警匪 奇幻
                    |* 若失败 请过一段时间重试,或联系作者~
                    |============================================
             """
    print(tips)

    while 1:
        multiprocessing.freeze_support()
        type = input('\n' + '请 输 入 类 型 : ')
        type = type.strip(' ')
        try:
            run = Fanhao(type)
            start,end = run.input_cnt()
            urls = run.get_index_urls(start,end)
            p = Pool()  # 进程池
            p.map_async(run.main, urls)
            p.close()
            p.join()
        except:
            print('失 败 请 重 新 输 入' + '\n')


