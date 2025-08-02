import json
import warnings
import re
import os
from nodejs_wheel import (
    node,
)
import subprocess
name = 'zhihu'
allowed_domains = ['www.zhihu.com']
question_id = '532925796'
last_cursor = ""

# with requests

def xzse96(path: str, d_c0: str):
    completed_process = node(
        [os.path.join(__file__, "..", "xzse96.js"), path, d_c0],
        return_completed_process=True,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return completed_process.stdout

# start_url = f'https://www.zhihu.com/api/v4/questions/{question_id}/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&ws_qiangzhisafe=0&platform=desktop'
         #    "https://www.zhihu.com/api/v4/questions/506530422/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=0&limit=10&order=default&ws_qiangzhisafe=0&platform=deskto"
start_url = "https://www.zhihu.com/api/v4/questions/418687587/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=0&limit=10&order=default&ws_qiangzhisafe=0&platform=desktop"
# start_url = "https://www.zhihu.com/api/v4/questions/418687587/feeds?cursor=db048d1e5e78bd2323ca2ba494dd2a97&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=10&offset=88&order=default&platform=desktop&session_id=1753803439888605989&ws_qiangzhisafe=0"
cookies = {
    "_xsrf": "uQhu8B0cafVRbOgmQu7QTQsjxUg09erC",
    "_zap": "9761813b-2515-45b6-805a-453c020ee01a",
    "HMACCOUNT": "B6D9B64D9BFF55FC",
    "d_c0": "AEASBUGEiRmPTh-3834HysAopbfXmrXBLjg=|1731505313",
    "__snaker__id": "sNyET9dE7c33g4me",
    "o_act": "login",
    "expire_in": "15552000",
    "q_c1": "acaa31de18c043d6ad58f597ed93a245|1731505336000|1731505336000",
    "edu_user_uuid": "edu-v1|aa7d5547-4986-4a72-99ab-d35f8a5504f3",
    "SESSIONID": "MLPolvwEe4xWTzofBA19OpatSCckIVf4UEbj3AJcfXu",
    "JOID": "W1wVAUo6GhxTQG3bDTEvhxMA4lcdelJOPyQWqEpXI2AGFx-5b3OHZTBFZN0Mq9T3b4eNtZLCBOiZZ-Hh-1J2-I0=",
    "osd": "VlARCk43FhhYRGDXCTorih8E6VMQdlZFOykarEFTLmwCHBu0Y3eMYT1JYNYIptjzZIOAuZbJAOWVY-rl9l5y84k=",
    "__zse_ck": "004_W1R2EewRHOadOmQ=b6zlXejhBnmZBQOQtjx/wcF5tU7fLSLNFUN0r=GZ7SMtwLiX3B23PRFTh79tuZOkd48J8uHG968P9WzGdRwgYYC4cM9bYRtKa/Li83EYmwIM2tC1-FhhN2EsIm+12dnHgBORbFJhQcb8Il08YRznTcMDSuA7jhNvp1eVoRRk76+yJkVFABrXJ6XgZQ93f3TdWckT3QURpGu7yf1jIcw9xKx/w5u4dBTUZL8Q6pjyh3MUQ0f8b",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1754112420",
    "captcha_session_v2": "2|1:0|10:1754114190|18:captcha_session_v2|88:emRpVU1GRFhxemkyVE9NaWlzUEFDY0phM2IyTE9HVVp3YkIzNnBwaUdCUWRaZVROcTMwNGNYZ1NUdWpDaFNQRQ==|6c8efa68608cecd23d0d817b732db005be03bf9ea928685615a604ba8ec7c25f",
    "DATE": "1754114191506",
    "cmci9xde": "U2FsdGVkX19oKxRObY3FNt9iSfY8KecbSF7etpQpuDHtO8PsHylJ6kcKD+1DHgEVkyeGxefl4tufCkoe7UFW6w==",
    "pmck9xge": "U2FsdGVkX1+vxpIwOI/8i+5r4ZKVu6zXgUws/pwKMPY=",
    "assva6": "U2FsdGVkX1+YsrWtTRYULp79n5lfFC+ANfLtg4VTR9E=",
    "assva5": "U2FsdGVkX1+3m7sSlvVWHV2Q+7vqKO1ETmwyrx5eVZCiGew1/HExNrLgx1v6F/Z6x/k9k/FaB0DG5mdZv3DJDw==",
    "crystal": "U2FsdGVkX1/GF2skOFJCXPs0AAOl6+PloghZlvhU3eITlZfhrJiAkJh5In7V7ocJx1ktrGroH+5qAqHVN66IRoFwN4MLZqdBQs4+W21PBMBo6U/zgFFly3rK6Vt0jWzhy9hHM3nmvJcq8AdTiW3bVEo5pvQiNSTx1z2CNCg6/rqV+3CrJ8qg3Y95VcVH+Y40scagTTSDpfVK6F9asijviNE4eYP/FPQBqufCOCd+RvCpV6kV9/xtjFf6YggBZf+F",
    "vmce9xdq": "U2FsdGVkX19sHvUySsGnwz/1onPVFLmNfUKtQj+hURO7/1whs0qJX7IuS2mXWCeF8AnSa1ZHxHAA89gDoT97KkedGYGgYuLelebGZTsHrpo6xtLzxoYbz2nHRvucgipO9B6B+sQxQgZvJxu3+t6Ok97lADINmpsUbLXVLmlWXRw=",
    "gdxidpyhxdE": "OMEzEOY2yBjPRRIIxlPTDhOx%2F0%2Fi%2B38eKZ9Yh%5CV36f8xlmh5YHGkLJjDI3zB%5CZ%2Bpk%2FbK%2FAkRSEJ3244m%2FfRAdEX8RWvjyIuIwGYtTBRlO%2FMZuNm%5CCspN20qULUkG0g2ROyCLHSKZVtZW8ERIQenvjNa0R3lva23X5z7Aci%2B9p07zoUb9%3A1754115093529",
    "ref_source": "undefined",
    "z_c0": "2|1:0|10:1754114221|4:z_c0|92:Mi4xaGpxckFBQUFBQUFBUUJJRlFZU0pHUmNBQUFCZ0FsVk5yZlo2YVFCNTdVVEpQakw1LUpLTzJ5TEJBbW5MUE16TWpR|dca6151f460690953c44e2c4939112189084366ea909bad64098fa1ba85b0fe5",
    "tst": "r",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1754114224",
    "BEC": "4589376d83fd47c9203681b16177ae43",
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

params = {
            # 'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
            # 'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].author.follower_count,vip_info,kvip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
            'limit': 5,  # 每次请求返回的评论数量
            'offset': 0,  # 初始偏移量
            'order': 'updated',  # 排序方式
            'platform': 'desktop',  # 平台
            'session_id': '',  # 会话 ID
            'cursor': '',  # 初始 cursor 为空
        }

# get content for start_url without using scrapy instead using requests

import requests
response = requests.get(start_url, headers=headers, cookies=cookies)
if response.status_code == 200:
    # print(response.json()['data'][0]['target'])
    print(response.json()['data'])
else:
    print(f"Failed to fetch start URL content: {response.status_code}")
    #return None 
