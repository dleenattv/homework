from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework2


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    recv_name = request.form['send_name']
    recv_count = request.form['send_count']
    recv_addr = request.form['send_addr']
    recv_tel = request.form['send_tel']

    send_info = {
        'orderName': recv_name,
        'orderCount': recv_count,
        'orderAddr': recv_addr,
        'orderTel': recv_tel
    }
    db.dbhomework2.insert_one(send_info)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.dbhomework2.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
