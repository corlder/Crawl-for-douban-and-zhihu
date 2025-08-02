## 代码简要介绍
1. 豆瓣爬取 -> `crawler_douban.ipynb`
2. 知乎爬取：
    - 问题评论：`crawler-zhihu-question-comment.py` header需x-zse-96
    - 回答：`./douban_zhihu/spiders/zhihu.py` 需借助scrapy框架以及header需cookie及x-zse-96
    - 问题评论：`crawler-zhihu-answer-comment.py`
## 数据格式简要说明
### 豆瓣
#### 文件路径
`douban/{书名}/{版本ID}.csv`，csv文件可用pandas解析处理，也可直接用Excel或者WPS打开阅览
#### 数据统计
| 书名       | ID       | 评论数量 |
| -------- | -------- | ---- |
| 班主任      | 5348123  | 454  |
| 从森林里来的孩子 | 3640513  | 17   |
| 将军吟      | -        | 391  |
|          | 26354971 | 27   |
|          | 1545838  | 5    |
|          | 1084075  | 202  |
|          | 1685345  | 11   |
|          | 25981450 | 11   |
|          | 31793467 | 115  |
|          | 3533433  | 20   |
| 灵与肉      | -        | 529  |
|          | 11586912 | 83   |
|          | 24714648 | 84   |
|          | 11441802 | 36   |
|          | 1921338  | 326  |
| 铺花的歧路    | 19966306 | 26   |
| 伤痕       | 3013597  | 312  |
| 许茂和他的女儿们 | -        | 883  |
|          | 25981438 | 39   |
|          | 31743822 | 241  |
|          | 1200841  | 427  |
|          | 1029871  | 30   |
|          | 34820949 | 16   |
|          | 26360952 | 56   |
|          | 4144399  | 74   |
#### 字段说明
| 点赞数           | 评论者   | 评论时间 | 评论位置                | 评论内容 | 评论类型                       |
| ------------- | ----- | ---- | ------------------- | ---- | -------------------------- |
| 网页端**”有用“**数值 | 评论者名称 | 略    | 评论时的IP地址所在省份（不一定都有） | 略    | P是**读过**，N是**在读**，F是**想读** |
### 知乎
#### 文件路径
每个问题的评论、答案、以及答案的评论分别保存在`zhihu_data/question-comments/{question_id}.csv`、`zhihu_data/answers/{question_id}.csv`、`zhihu_data/answer-comments/{question_id}.csv`
#### 数据统计
| question_id | 问题                   | 问题的评论数 | 答案数 | 答案的评论总数 |
| ----------- | -------------------- | ------ | --- | ------- |
| 506530422   | 伤痕文学是什么？             | 1      | 52  | 465     |
| 52685561    | 如何看待伤痕文学对于青少年的消极影响?  | 39     | 534 | 2734    |
| 516428687   | 为什么知乎上有那么多人憎恨伤痕文学？   | 52     | 879 | 12669   |
| 344845648   | 为什么知乎很多人反感伤痕文学？      | 42     | 880 | 8232    |
| 414875849   | 什么是伤痕文学？             | 0      | 104 | 615     |
| 418687587   | 为何现在的年轻人对伤痕文学无感甚至反感？ | 173    | 872 | 27188   |
#### 字段说明
##### 问题的评论
`zhihu_data/question-comments/{question_id}.csv`
```
question_id: 问题ID
comment_id: 评论ID
reply_comment_id: 回复的评论ID
reply_root_comment_id: 回复的根评论ID（类似于这楼的楼主的评论，一簇评论的父评论）
content: 评论内容
created_time: 评论创建时间
like_count: 点赞数
child_comment_count: 子评论数
```
##### 答案
`zhihu_data/answers/{question_id}.csv`
```
question_id: 问题ID
answer_id: 回答ID
content: 回答的内容
author_name: 回答者的用户名
created_time: 回答创建的时间
voteup_count: 回答的点赞数
reply_count: 回答的回复数 
```
回答可直接用浏览器访问`https://www.zhihu.com/question/{question_id}/answer/{answer_id}`查看，注意将花括号连同内容替换成问题及回答ID即可。
##### 答案的评论
`zhihu_data/answer-comments/{question_id}.csv`
```
question_id: 问题ID
comment_id: 评论ID
reply_comment_id: 回复的评论ID
reply_root_comment_id: 回复的根评论ID（类似于这楼的楼主的评论，一簇评论的父评论）
content: 评论内容
created_time: 评论创建时间
like_count: 点赞数（点赞数不一定准确）
child_comment_count: 子评论数
```
#### 其他说明
- 本项目爬虫基于网页端知乎开发，但知乎网页端似乎对可访问到的回答数量有限制，像「[为何现在的年轻人对伤痕文学无感甚至反感？](https://www.zhihu.com/question/418687587)」理应有4224条回复，但网页端爬虫只爬取到了872条就报无更多数据。不过，爬取顺序是按默认排序（猜测是综合回复和点赞量给出降序），872条这样的数量基本把话题度高的（评论多）的答案给覆盖到了。
