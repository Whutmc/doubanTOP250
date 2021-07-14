# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DoubanPipeline:
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",
                            port=3306,
                            db="douban",

                            user="root",
                            passwd="123456",
                            charset="utf8")
        self.cursor=self.conn.cursor()
        create_sql = "create table if not exists TOP250(rank_1 int,title_1 varchar(20),score_1 varchar(10),comment_num_1 varchar(20),quote_1 varchar(50),img_path varchar(255))"
        self.cursor.execute(create_sql)
    def process_item(self, item, spider):
        insert_sql = "insert into TOP250(rank_1,title_1,score_1,comment_num_1,quote_1,img_path) values(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(insert_sql,[item['rank'],item['title'],item['score'],item['comment_num'],item['quote'],item['img_path']])
        self.conn.commit()
        return item
