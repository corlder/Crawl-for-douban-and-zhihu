import scrapy
from douban_zhihu.items import DoubanZhihuItem
import json
import warnings
from urllib.parse import urlparse, parse_qs
from scrapy.exceptions import ScrapyDeprecationWarning
import re
import os
import subprocess
import requests
from nodejs_wheel import (
    node,
)

warnings.filterwarnings('ignore', category=ScrapyDeprecationWarning)

def xzse96(path: str, d_c0: str):
    completed_process = node(
        [os.path.join(__file__, "..", "xzse96.js"), path, d_c0],
        return_completed_process=True,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return completed_process.stdout

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    question_id = '418687587'
    last_cursor = ""
    offset = 0

    start_url = f'https://www.zhihu.com/api/v4/questions/{question_id}/feeds'
    cookies = {
        '__snaker__id': 'sNyET9dE7c33g4me',
        'q_c1': 'acaa31de18c043d6ad58f597ed93a245|1731505336000|1731505336000',
        '_xsrf': 'uQhu8B0cafVRbOgmQu7QTQsjxUg09erC',
        'z_c0': '2|1:0|10:1751443481|4:z_c0|80:MS4xaGpxckFBQUFBQUFtQUFBQVlBSlZUZG1pVDJsU3BueEpVelJaM1VBZUk2S2JsWUY0bWlnUnlRPT0=|319481d06a9fe58f843a80b4736b4ae0d20272ceafc7720145baf80bf05f8eb3',
        '__zse_ck': '004_zq=ink1XmtUu8Odkaz8lEqWUsilx8mYpdNS9X=OdcrLVZcd53gB7cfG2BiIrGMVjZeIi3gAWQlUd8VGGKaHK1jwObQ0f41axXL=7mumLlrwJC95rBc4NQeazeJ2BxgNl-Q5XrYa8Oi5siKp3sKf4h/lC37w1HYtfPxpk5cm9i3InEJU93R/BWGdCWHQdPdN4DJRprBQCaH08yJ7V5GeSaouspWNvAcDt94we9r2yHEjU2SogHwm5uiKMIkW5MQt16',
        'tst': 'r',
        'SESSIONID': 'MLPolvwEe4xWTzofBA19OpatSCckIVf4UEbj3AJcfXu',
        'JOID': 'W1wVAUo6GhxTQG3bDTEvhxMA4lcdelJOPyQWqEpXI2AGFx-5b3OHZTBFZN0Mq9T3b4eNtZLCBOiZZ-Hh-1J2-I0=',
        'osd': 'VlARCk43FhhYRGDXCTorih8E6VMQdlZFOykarEFTLmwCHBu0Y3eMYT1JYNYIptjzZIOAuZbJAOWVY-rl9l5y84k=',
        '_zap': '9761813b-2515-45b6-805a-453c020ee01a',
        'd_c0': 'AEASBUGEiRmPTh-3834HysAopbfXmrXBLjg=|1731505313',
        'BEC': '5ee33e0856ed13c879689106c041a08d',
        # 'HMACCOUNT': 'B6D9B64D9BFF55FC',
        # 'o_act': 'login',
        # 'ref_source': 'other_https://www.zhihu.com/signin?next=/follow',
        # 'expire_in': '15552000',
        # 'edu_user_uuid': 'edu-v1|aa7d5547-4986-4a72-99ab-d35f8a5504f3',
        # 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1751472426',
        # 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1753549646',
        
    }
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'Referer': f'https://www.zhihu.com/question/{question_id}',
                'x-zse-93': '101_3_3.0',  
                "x-zse-96": xzse96(start_url[len("https://www.zhihu.com") :], d_c0=cookies['d_c0']),
                # 'x-zse-96': '2.0_5QHNSQrdPY/RgWwvDOyMH1YPPV8ubW+87jAm7aNggf/w2XMbwSPkzd9Wv8IBAetu', 
                'Host': 'www.zhihu.com',
                
            }
    # https://www.zhihu.com/question/8045672950/answer/98576789837
    def start_requests(self):
        # 初始请求参数
        params = {
            'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
            'limit': 10,  # 每次请求返回的评论数量
            'offset': 0,  # 初始偏移量
            'order': 'default',  # 排序方式
            'platform': 'desktop',  # 平台
            'session_id': '',  # 会话 ID
            'cursor': '',  # 初始 cursor 为空
        }

        # 
        full_url = f'{self.start_url}?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset={self.offset}&limit=10&order=default&ws_qiangzhisafe=0&platform=desktop'
        
        # 发送初始请求
        # full_url = "https://www.zhihu.com/api/v4/questions/506530422/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset={self.offset}&limit=10&order=default&ws_qiangzhisafe=0&platform=desktop"
        new_headers = self.headers.copy()
        new_headers['x-zse-96'] = xzse96(full_url[len("https://www.zhihu.com") :], d_c0=self.cookies['d_c0'])
        self.headers = new_headers
        
        # yield self.parse_comments(requests.get(full_url, headers=new_headers, cookies=self.cookies))
        yield scrapy.Request(
            url=full_url,
            method='GET',
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse_comments,
        )
        # yield scrapy.Request(
        #     # url=self.start_url,
        #     url=full_url,
        #     method='GET',
        #     headers=self.headers,
        #     cookies=self.cookies,
        #     callback=self.parse_comments,
        #     meta={'params': params, 'count': 0}  # 添加计数器
        # )


    def parse_comments(self, response):
        # 解析返回的 JSON 数据
        # data = json.loads(response.text)
        
        # if response.status_code != 200:
        #     print(f'!!!!!!!!Failed to fetch comments: {response.status_code}, URL: {response.url}')
        #     return
        # print(response.json())
        data = response.json()
        # print(data)
        print(f'Fetched {len(data["data"])} comments')

        # 提取评论数据
        for comment in data['data']:
            target = comment.get('target', {})
            if not target:
                print("Target is empty, skipping...")
                continue

            # 抓取完整评论内容
            answer_id = target.get('id')
            if answer_id:
                print(f'Processing answer_id: {answer_id}')
                # 使用正确的 API URL
                # full_content_url = f'https://www.zhihu.com/api/v4/answers/{answer_id}?include=content'
                # new_headers = self.headers.copy()
                # new_headers['x-zse-96'] = xzse96(full_content_url[len("https://www.zhihu.com") :], d_c0=self.cookies['d_c0'])
                # # 打印完整内容 URL
                # print(f"Full content URL: {full_content_url}")
                # # local_params = {
                # #     'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
                # # }
                # yield scrapy.Request(
                #     url=full_content_url,
                #     method='GET',
                #     headers=new_headers,
                #     cookies=self.cookies,
                #     callback=self.parse_full_content,
                #     # meta = {'params': local_params}  # 传递计数器
                # )
                yield self.parse_full_content(target)
            else:
                print("No answer_id found in target")
        # print(data)
        # 获取下一个 cursor
        paging = data.get('paging', {})
        next_url = paging.get('next')  # 获取下一页的 URL
        
        if next_url:  # 限制抓取 250 条数据
            # 从 URL 中提取 cursor
            parsed_url = urlparse(next_url)
            query_params = parse_qs(parsed_url.query)
            next_cursor = query_params.get('cursor', [''])[0]  # 提取 cursor 参数
            print(f'Next cursor: {next_cursor}')
            print(f'self.last_cursor: {self.last_cursor}')
            # 如果 next_cursor 与 last_cursor 相同，则停止抓取
            if next_cursor == self.last_cursor:
                print("No new cursor found, stopping...")
                return
            self.last_cursor = next_cursor  # 更新 last_cursor

            # 更新请求参数
            # params = response.meta['params']
            # params['cursor'] = next_cursor
            # params['offset'] += params['limit']
            # self.offset += 1

            # 更新计数器
            # count = response.meta['count'] + len(data['data'])
            new_headers = self.headers.copy()
            print(next_url)
            # 发送下一个请求
            # next_full_url = f'{next_url}&include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset={self.offset}&limit=10&order=default&ws_qiangzhisafe=0&platform=desktop'
            new_headers = self.headers.copy()
            new_headers['x-zse-96'] = xzse96(next_url[len("https://www.zhihu.com") :], d_c0=self.cookies['d_c0'])
            print("hahahahah")
            # yield self.parse_comments(requests.get(next_url, headers=new_headers, cookies=self.cookies))
            yield scrapy.Request(   
                url=next_url,  # 直接使用 next_url
                method='GET',
                headers=new_headers,
                cookies=self.cookies,
                callback=self.parse_comments,
            )
            # yield scrapy.Request(
            #     # url=next_url,  # 直接使用 next_url
            #     url = next_full_url,
            #     method='GET',
            #     headers=new_headers,
            #     cookies=self.cookies,
            #     callback=self.parse_comments,
            #     meta={'params': params, 'count': count}
            # )
    def parse_full_content(self, data):
        # if response.status != 200:
        #     print(f'Failed to fetch full content: {response.status}, URL: {response.url}')
        #     return
        # print(response.json())
        # data = response.json()
        item = DoubanZhihuItem()
        item['question_id'] = data.get('question', {}).get('id', 'Unknown')
        item['answer_id'] = data.get('id', 'Unknown')
        content = data.get('content', '')
        # content = '\n'.join(content)   
        item['content'] = content
        # print(content)
        item['author_name'] = data.get('author', {}).get('name', 'Unknown')
        created_time = data.get('created_time', '')
        item['created_time'] = created_time
        
        item['voteup_count'] = data.get('voteup_count', '0')

        #matrix_tips: "2 赞同 · 3 评论" or "2 赞同"
        # item['reply_count'] = data.get('matrix_tips', '').split('·')[1].strip() if '·' in data.get('matrix_tips', '') else '0'
        #matrix_tips: "2 赞同 · 3 评论" or "2 赞同"
        # extract reply_count in "109 赞同 · 58 收藏 · 25 评论" 
        matrix_tips = data.get('matrix_tips', '')
        if '评论' in matrix_tips:
            reply_count = re.search(r'(\d+)\s*评论', matrix_tips)
            if reply_count:
                item['reply_count'] = reply_count.group(1)
            else:
                item['reply_count'] = '0'
        else:
            item['reply_count'] = '0'   
            
        return item
        # count = response.meta['count']
        # # 打印抓取进度
        # print(f'Fetched {count+1} comments')