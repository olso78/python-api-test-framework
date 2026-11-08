import pymysql,json
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'bootcamp')
cursor = conn.cursor()
# 1. 建表
cursor.execute(
    "CREATE TABLE IF NOT EXISTS dictionary (word VARCHAR(50) PRIMARY KEY, meaning VARCHAR(100) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP) DEFAULT CHARSET=utf8mb4")
with open('words.json',encoding='utf-8') as f:
    data = json.load(f)
# 2.准备数据列表（列表中装元组）
data_list = []
for word, meaning in data.items():
    data_list.append((word, meaning))

sql='INSERT INTO dictionary (word, meaning) VALUES (%s, %s) AS new ON DUPLICATE KEY UPDATE meaning = new.meaning'
cursor.executemany(sql,data_list)
conn.commit()
cursor.close()
conn.close()