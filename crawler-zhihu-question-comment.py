import requests
import time
from datetime import datetime
import pandas as pd
import os
import subprocess
from nodejs_wheel import (
    node,
)

def xzse96(path: str, d_c0: str):
    completed_process = node(
        [os.path.join(__file__, "..", "xzse96.js"), path, d_c0],
        return_completed_process=True,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return completed_process.stdout


def get_zhihu_question_comments(question_id, limit=20,next_url=None):
    """
    获取知乎问题下的评论
    :param question_id: 问题ID
    :param limit: 每次请求获取的评论数量(默认20)
    :param offset: 偏移量(从第几条开始)
    :return: 评论列表
    """
    cookies = {
        "_xsrf": "uQhu8B0cafVRbOgmQu7QTQsjxUg09erC",
        "_zap": "9761813b-2515-45b6-805a-453c020ee01a",
        # "HMACCOUNT": "B6D9B64D9BFF55FC",
        "d_c0": "AEASBUGEiRmPTh-3834HysAopbfXmrXBLjg=|1731505313",
        "__snaker__id": "sNyET9dE7c33g4me",
        # "o_act": "login",
        # "expire_in": "15552000",
        "q_c1": "acaa31de18c043d6ad58f597ed93a245|1731505336000|1731505336000",
        # "edu_user_uuid": "edu-v1|aa7d5547-4986-4a72-99ab-d35f8a5504f3",
        "SESSIONID": "MLPolvwEe4xWTzofBA19OpatSCckIVf4UEbj3AJcfXu",
        "JOID": "W1wVAUo6GhxTQG3bDTEvhxMA4lcdelJOPyQWqEpXI2AGFx-5b3OHZTBFZN0Mq9T3b4eNtZLCBOiZZ-Hh-1J2-I0=",
        "osd": "VlARCk43FhhYRGDXCTorih8E6VMQdlZFOykarEFTLmwCHBu0Y3eMYT1JYNYIptjzZIOAuZbJAOWVY-rl9l5y84k=",
        "__zse_ck": "004_W1R2EewRHOadOmQ=b6zlXejhBnmZBQOQtjx/wcF5tU7fLSLNFUN0r=GZ7SMtwLiX3B23PRFTh79tuZOkd48J8uHG968P9WzGdRwgYYC4cM9bYRtKa/Li83EYmwIM2tC1-FhhN2EsIm+12dnHgBORbFJhQcb8Il08YRznTcMDSuA7jhNvp1eVoRRk76+yJkVFABrXJ6XgZQ93f3TdWckT3QURpGu7yf1jIcw9xKx/w5u4dBTUZL8Q6pjyh3MUQ0f8b",
        # "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1754112420",
        # "captcha_session_v2": "2|1:0|10:1754114190|18:captcha_session_v2|88:emRpVU1GRFhxemkyVE9NaWlzUEFDY0phM2IyTE9HVVp3YkIzNnBwaUdCUWRaZVROcTMwNGNYZ1NUdWpDaFNQRQ==|6c8efa68608cecd23d0d817b732db005be03bf9ea928685615a604ba8ec7c25f",
        "ref_source": "undefined",
        "z_c0": "2|1:0|10:1754114221|4:z_c0|92:Mi4xaGpxckFBQUFBQUFBUUJJRlFZU0pHUmNBQUFCZ0FsVk5yZlo2YVFCNTdVVEpQakw1LUpLTzJ5TEJBbW5MUE16TWpR|dca6151f460690953c44e2c4939112189084366ea909bad64098fa1ba85b0fe5",
        "tst": "r",
        "BEC": "4589376d83fd47c9203681b16177ae43",
        }
    url = f"https://www.zhihu.com/api/v4/comment_v5/questions/{question_id}/root_comment?order_by=score&limit={limit}&offset="
    # url = "https://www.zhihu.com/api/v4/comment_v5/questions/418687587/root_comment?order_by=score&limit=20&offset="
    # params = {
    #     "order": "score",
    #     "limit": limit,
    # }
    if next_url:
        # 如果提供了 next_url，则使用它
        url = next_url
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"https://www.zhihu.com/question/{question_id}",
        'x-zse-93': '101_3_3.0',  
        "x-zse-96": xzse96(url[len("https://www.zhihu.com") :], d_c0=cookies['d_c0']),
        'Host': 'www.zhihu.com',
    }
    try:
        response = requests.get(url, headers=headers,cookies=cookies, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    
def get_zhihu_question_child_comments(root_comment_id, limit=20, next_url=None):
    """
    获取知乎问题下的子评论
    :param comment_id: 评论ID
    :param limit: 每次请求获取的子评论数量(默认20)
    :param offset: 偏移量(从第几条开始)
    :return: 子评论列表
    """
    # https://www.zhihu.com/api/v4/comment_v5/comment/10993283923/child_comment?limit=20&offset=1726478685_10993289770_1&order_by=ts
    url = f"https://www.zhihu.com/api/v4/comment_v5/comment/{root_comment_id}/child_comment"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"https://www.zhihu.com/comment/{root_comment_id}",
    }

    params = {
        "limit": limit,
        "order_by": "ts",
    }
    if next_url:
        # 如果提供了 next_url，则使用它
        url = next_url  
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None


def parse_comments(comment_data, question_id):
    """
    解析评论数据
    :param comment_data: 原始评论数据
    :return: 解析后的评论列表
    """
    comments = []

    if not comment_data or "data" not in comment_data:
        return comments
    # print(len(comment_data["data"]))
    for item in comment_data["data"]:
        try:
            # 获取用户省份信息
            # province = item.get("address_text", {})

            root_comment = {
                "question_id": question_id,  # 问题ID
                "comment_id": item.get("id", ""),  # 评论ID
                "reply_comment_id": item.get("reply_comment_id", ""),  # 回复的评论ID
                "reply_root_comment_id": item.get("reply_root_comment_id", ""),  # 回复的根评论ID
                "content": item.get("content", ""),  # 评论内容
                "created_time": datetime.fromtimestamp(item.get("created_time", 0)).strftime('%Y-%m-%d %H:%M:%S'),
                "like_count": item.get("like_count", 0),  # 点赞数
                "child_comment_count": item.get("child_comment_count", 0),  # 子评论数
            }
            comments.append(root_comment)
            # 获取子评论
            if item.get("child_comment_count", 0) > 0:
                child_comments_data = get_zhihu_question_child_comments(item["id"])
                while True:
                    if child_comments_data and "data" in child_comments_data:
                        for child_item in child_comments_data["data"]:
                            child_comment = {   
                                "question_id": question_id,  # 回答ID
                                "comment_id": child_item.get("id", ""),  # 子评论ID
                                "reply_comment_id": child_item.get("reply_comment_id", ""),  # 回复的评论ID
                                "reply_root_comment_id": child_item.get("reply_root_comment_id", ""),  # 回复的根评论ID
                                "content": child_item.get("content", ""),  # 子评论内容
                                "created_time": datetime.fromtimestamp(child_item.get("created_time", 0)).strftime('%Y-%m-%d %H:%M:%S'),
                                "like_count": child_item.get("like_count", 0),  # 点赞数
                                "child_comment_count": child_item.get("child_comment_count", 0),  # 子评论数
                            }
                            comments.append(child_comment)
                    else:
                        print("没有更多子评论或获取失败")
                        break
                    next_url = child_comments_data.get("paging", {}).get("next", "")
                    is_end = child_comments_data.get("paging", {}).get("is_end", True)
                    if is_end or not next_url:
                        # print("已到达最后一页子评论")
                        break
                    child_comments_data = get_zhihu_question_child_comments(item["id"], next_url=next_url)
                    time.sleep(20)  # 防止请求过于频繁
        except TypeError as e:
            print(f"解析评论时类型错误: {e}, 原始数据: {item}")
            continue
        except KeyError as e:
            print(f"解析评论时缺少键: {e}, 原始数据: {item}")
            continue
        # except Exception as e:
        #     print(f"解析评论出错: {e}, 原始数据: {item}")
        #     continue

    return comments


def get_all_comments(answer_id):
    """
    获取所有评论
    :param answer_id: 回答ID
    :param max_count: 最大获取数量
    :return: 所有评论列表
    """
    all_comments = []

    limit = 20  # 每次请求获取20条
    data = get_zhihu_question_comments(answer_id, limit, "")
    # print(data)
    while True:
        # print(f"正在获取第 {offset // limit + 1} 页评论...")    

        if not data or "data" not in data:
            print("没有更多评论或获取失败")
            break
        # print(data)
        comments = parse_comments(data, answer_id)
        all_comments.extend(comments)
        # print(comments)
        # 检查是否还有更多评论或达到最大数量
        # print(data.get("paging", {}))
        # print(len(comments))
        if data.get("paging", {}).get("is_end", True) and len(comments) == 0:
        # if data.get("paging", {}).get("is_end", True) or len(comments) == 0:
            # print("已到达最后一页")
            break
        
        next_url = data.get("paging", {}).get("next", "")
        if not next_url:
            print("没有更多评论")
            break   
        data = get_zhihu_question_comments("", limit,next_url=next_url)

        time.sleep(20)  # 防止请求过于频繁

    return all_comments


def save_to_file(comments, question_id, filename="zhihu_comments"):
    """
    将评论保存到文件
    :param comments: 评论列表
    :param filename: 文件名
    """
    try:
        o_file = '{}_{}_question_comments.csv'.format(filename, question_id)
        df = pd.DataFrame(comments)
        if os.path.exists(o_file):
            # 如果文件已存在，则追加数据
            df.to_csv(o_file, mode='a', header=False, index=False, encoding='utf-8')
        else:
            df.to_csv(o_file, index=False, encoding='utf-8')
            # json.dump(comments, f, ensure_ascii=False, indent=2)
        print(f"评论已保存到 {o_file}")
    except Exception as e:
        print(f"保存文件失败: {e}")


if __name__ == "__main__":
    # 示例：替换为你想要爬取的知乎回答ID
    # answer_ids = ['81964408445','82586149604','82493740255','81348057992','81748398040','81531639383'] #
    
    file_list = [
        # 'zhihu_data/question/zhihu_data_506530422.xlsx',
        'zhihu_data/question/zhihu_data_52685561.xlsx',
        # 'zhihu_data/question/zhihu_data_344845648.xlsx',
        # 'zhihu_data/question/zhihu_data_414875849.xlsx',
        # 'zhihu_data/question/zhihu_data_418687587.xlsx',
        # 'zhihu_data/question/zhihu_data_506530422.xlsx',
        # 'zhihu_data/question/zhihu_data_516428687.xlsx'
    ]
    question_id_list = [
        '52685561',     
        '344845648',
        '414875849',
        '418687587',        
        '506530422',    
        '516428687'
    ]
    import pandas as pd 
    from tqdm import tqdm
    for question_id in question_id_list:
        print(f"问题ID: {question_id}")
    
        # df = pd.read_excel(file)  # 读取Excel文件
        # answer_ids = df['answer_id'].tolist()  # 获取所有回答ID
        # question_id = '506530422'  # 替换为实际问题ID
        # question_id = file.split('_')[-1].split('.')[0]
        # print(f"问题ID: {question_id}")
        
        # for answer_id in tqdm(answer_ids):
        print(f"开始爬取问题 {question_id} 的评论...")
        comments = get_all_comments(question_id)  # 最多获取100条评论

        if comments:
            print(f"共获取到 {len(comments)} 条评论")
            save_to_file(comments, question_id)
            # append to file if exists
        else:
            print("没有获取到任何评论")
        time.sleep(10)  # 防止请求过于频繁