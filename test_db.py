import pymysql
# 建立连接
conn = pymysql.connect(host='localhost',user='root',password='root',database='bootcamp')
# 创建游标
cursor = conn.cursor()
# 执行SQL语句
sql = 'select word,freq from words order by freq desc limit 10'
cursor.execute(sql)

# 获取并打印结果
result = cursor.fetchall()
for row in result:
    print(row)
# 关闭游标和连接
cursor.close()
conn.close()