import pymysql


# connect database
def connect():
    db = pymysql.connect("localhost", "root", "yjw715901", "PROJECT")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMOTION")

    # 使用预处理语句创建表
    sql = """CREATE TABLE EMOTION (
             `id` INT( 5 ) UNSIGNED NOT NULL AUTO_INCREMENT ,`LIST` INT NOT NULL , PRIMARY KEY ( `id` )
              )"""

    cursor.execute(sql)

    # 关闭数据库连接
    db.close()


def insert(id, data):
    db = pymysql.connect("localhost", "root", "yjw715901", "PROJECT")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO EMOTION(id, LIST) VALUES('%s','%s')" % (id, data)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        print('insert error')
        db.rollback()
    finally:
        db.close()
