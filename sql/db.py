# 创建session对象:

from sqlalchemy.orm import sessionmaker
from sql.user import User
import sql.coon as db

DBSession = sessionmaker(bind=db.coon_mysql())
session = DBSession()


# 添加元祖
def mysql_add(id, name):
    # 创建新User对象:
    new_user = User(id=id, name=name)
    print(new_user)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


# 查询数据库
def mysql_query_all():
    datas = session.query(User).all()
    return datas


def mysql_query(id):
    """" 使用id去查询数据集 """
    # session = coon.CoonMySql()
    datas = session.query(User).filter(User.id == id).one()
    session.close()

    # users = session.query(Users).filter_by(id=1).all()
    # for item in users:
    #     print(item.name)
    return datas


# 更新数据库  或者 修改数据库
def mysql_updata(id, name):
    """ 直接条件修改数据 """
    try:
        session.query(User).filter_by(id=id).update({'name': name})
        session.commit()
        session.close()
    except Exception as e:
        return e


def mysql_updata2(name1, name2):
    """ name1是查询的的name name2是要修改的name """
    # session = coon.CoonMySql()
    try:
        datas = session.query(User).filter_by(name=name1).first()
        datas.name = name2
        # session.add(User)
        session.commit()
        session.close()
    except Exception as e:
        return e


# 删除数据
def mysql_delete(name):
    delete_users = session.query(User).filter_by(name=name).first()
    if delete_users:
        session.delete(delete_users)
        session.commit()


def mysql_delete_id(id):
    delete_users = session.query(User).filter(User.name == id).first()
    if delete_users:
        session.delete(delete_users)
        session.commit()


def mysql_delete2(name):
    session.query(User).filter(User.name == name).delete()
    session.commit()
    session.close()


def mysql_delete2_id(id):
    session.query(User).filter(User.id == id).delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    # print([[i.id,i.name] for i in mysql_query_all()])
    print(mysql_updata2('哈哈', '666'))
