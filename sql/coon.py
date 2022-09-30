import pymysql
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from user import User as hi


def coon_mysql():
    # 创建连接  '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/hello", echo=True, future=True)
    # create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
    # 并初始化DBSession：   创建键dbsessionmaker
    return engine
