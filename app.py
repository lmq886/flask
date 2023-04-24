from flask import Flask, request
from flask_cors import CORS,cross_origin
from sql import resql, db

app = Flask(__name__)
cors=CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# 查询所有数据
@app.route('/gethi')
def get_hi():
    datas = db.mysql_query_all()
    list_data = {}
    for i in datas:
        list_data[i.id] = i.name
    print(list_data)
    return list_data


# 原生sql
@app.route('/getsqlhi')
def get_sql_hi():
    datas = resql.select_all()
    data = dict([i for i in datas])  # 返回类型必须是 字典 字符 元祖
    return data


# 增加数据
@app.route('/addsql', methods=['post'])
def add_sql():
    type_str = request.content_type[:16]
    print(type(request.content_type))
    if (type_str == 'application/json'):
        id = request.get_json()["id"]
        name = request.get_json()["name"]
        # print('26' + id, name)
        db.mysql_add(id, name)
        return 'ok'

    elif (type_str in ['application/x-ww', 'multipart/form-d']):
        res = request.form
        name = res.get("name")
        id = res.get("id")
        # print(id, name)
        db.mysql_add(id, name)
        return 'ok'
    else:
        return 'error'


# 修改数据
@app.route('/insert', methods=['post', 'update'])
def insert_id():
    type_str = request.content_type[:16]
    if type_str == 'application/json':
        """
        id 指定修改的id name修改后的name  name1 修改前的name
        接口样式  下同
        {
            "name": "哈哈",
            "id": 10,
            "name1": null
        }
        """

        id = request.get_json()["id"]
        name = request.get_json()["name"]
        name1 = request.get_json()["name1"]
        # name2 = request.get_json()["name2"]
        if id is not None:
            db.mysql_updata(id, name)
        elif name1 is not None:
            db.mysql_updata2(name1, name)
        else:
            return 0
        return 'ok'
    elif type_str in ['application/x-ww', 'multipart/form-d']:
        res = request.form
        id = res.get('id')
        name = res.get("name")
        name1 = res.get("name1")
        if id is not None:
            db.mysql_updata(id, name)
        elif name1 is not None:
            db.mysql_updata2(name1, name)
        else:
            return 0
        return 'ok'
    else:
        return "error"


# 删除数据
@app.route('/delete', methods=['post', 'delete'])
def delete_hi():
    """
    接口样式
            {
            "name":"hello",
            "id":null
        }
    :return:
    """
    type_str = request.content_type[:16]
    print(type(request.content_type))
    if type_str == 'application/json':
        id = request.get_json()["id"]
        name = request.get_json()["name"]
        if name is not None:
            db.mysql_delete(name)
        elif id is not None:
            db.mysql_delete_id(id)
        return 'ok'

    elif type_str in ['application/x-ww', 'multipart/form-d']:
        res = request.form
        name = res.get("name")
        id = res.get("id")
        # print(id, name)
        db.mysql_add(id, name)
        return 'ok'
    else:
        return 'error'


if __name__ == '__main__':
    app.run(debug=True)
