from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbfood


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def post_article():
    name_receive = request.form['name_give']
    date_receive = request.form['date_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    image_receive = request.form['image_give']
    type_receive = request.form['type_give']
    review_receive = request.form['review_give']
    point_receive = request.form['point_give']

    print(request.form)
    doc = {
        'name': name_receive,
        'date': date_receive,
        'address': address_receive,
        'phone': phone_receive,
        'image': image_receive,
        'type': type_receive,
        'review': review_receive,
        'point': point_receive
    }

    db.foodbox.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '저장완료!'})


@app.route('/show', methods=['GET'])
def read_articles():
    foodboxes  = list(db.foodbox.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!', 'foodboxes': foodboxes })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)