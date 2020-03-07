from flask import Flask,request,redirect,render_template,session,Response
from flask_pymongo import PyMongo
from json import loads

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/catmouse"
mongo = PyMongo(app)

def save(payload,ip):
    count=len(payload)
    payload=[{'ip': ip, 'time': t, 'x': x, 'y': y, 'state': s} for t,x,y,s in payload]
    print(f'Saving {count} events from {ip}.')
    mongo.db.mouse_movements.insert_many(payload)
    total_counts=mongo.db.mouse_movements.count_documents({})
    print(f"Total events saved is {total_counts}")
    
@app.route('/add',methods=['POST'])
def adding():
    payload=loads(request.form.get('events','[]'))
    ip = request.remote_addr
    save(payload,ip)
    return 'cunt'

def run(port=str(3663),host='0.0.0.0',debug=True):
    app.run(host=host,port=port,debug=True)
if __name__=='__main__':
    run()

