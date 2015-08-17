from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId
import pymongo
 
app = Flask(__name__)
 
mongoClient = pymongo.MongoClient('localhost', 27017)
db = mongoClient['wattpad']
def toJson(data):
    return json.dumps(data, default=json_util.default)
 
@app.route('/contents/', methods=['GET'])
 
def findcontents():
    if request.method == 'GET':
        results = db['contents'].find()
        json_results= []
        for result in results:
            json_results.append(result)
        return toJson(json_results)
 
if __name__ == '__main__':
    app.run(debug=True)