from sqlalchemy import create_engine, text
from sql.coon import coon_mysql

"""
    sql原生写法 实现增删改查
"""

engine = coon_mysql().connect()


# table_name = 'hi'


# 查询全部数据
def select_all(table_name='hi'):
    sql = 'select * from %s' % table_name
    results = engine.execute(text(sql))
    engine.closs()
    return results


def select_name(name, table_name='hi'):
    sql = 'select * from %s where name = %s' % (table_name, name)
    results = engine.execute(text(sql))
    engine.closs()
    return results


def select_id(id, table_name='hi'):
    sql = 'select * from %s where id = %d' % (table_name, id)
    results = engine.execute(text(sql))
    engine.closs()
    return results


# 增加数据
def insert_mysql(id, name, table_name='hi'):
    try:
        sql = 'insert into %s values(%d,"%s")' % (table_name, id, name)
        engine.execute(text(sql))
        engine.commit()
        engine.closs()
    except Exception as e:
        return e


# 删除
def delete_mysql_name(name, table_name='hi'):
    try:
        # sql = """delete from %s where name = "%s" """ % (table_name, name)
        sql = 'delete from %s where name = "%s"' % (table_name, name)
        engine.execute(text(sql))
        engine.commit()
        engine.closs()
        return "cucceed"
    except Exception as e:
        return e


def delete_mysql_id(id, table_name='hi'):
    try:
        # sql = """delete from %s where name = "%s" """ % (table_name, name)
        sql = 'delete from %s where id = %d' % (table_name, id)
        engine.execute(text(sql))
        engine.commit()
        engine.closs()
        return "cucceed"
    except Exception as e:
        return e


# 更新
def updata_mysql_name(name, new_name, table_name='hi'):
    try:
        sql = 'updata %s set name = "%s" where name = "%s"' % (table_name, new_name, name)
        engine.execute(text(sql))
        engine.commit()
        engine.closs()
        return "cucceed"
    except Exception as e:
        return e


def updata_mysql_id(id, name, table_name='hi'):
    try:
        sql = 'updata %s set name = "%s" where id = %d' % (table_name, name, id)
        engine.execute(text(sql))
        engine.commit()
        engine.closs()
        return "cucceed"
    except Exception as e:
        return e


# if __name__ == '__main__':
#     # insert_mysql(6,'hello')
#     print(delete_mysql_id(5))
