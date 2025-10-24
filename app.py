from flask import Flask, request
from flask import render_template
import redis

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def login():
    name = request.form.get('name')
    new_data = name

    if name is not None :
        r = redis.Redis(
            host='redis-18405.c252.ap-southeast-1-1.ec2.redns.redis-cloud.com',
            port=18405,
            decode_responses=True,
            username="admin",
            password="Ehsanjaya18!",
        )
        new_data = new_data + ':' + str(r.get('data'))
        r.set('data', new_data)

    
    return render_template('main.html', person=name, data=new_data)
