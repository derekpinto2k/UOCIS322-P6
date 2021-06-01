# Streaming Service

from flask import Flask, request
from flask_restful import Resource, Api
import csv
import os

from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevetsdb

app = Flask(__name__)
api = Api(app)


def csv_form(topk, d):
    times = json_form(topk, d)
    csv_times = []
    csv_times.append(",".join(list(times[0].keys())))

    for item in times:
        csv_times.append(",".join(list(item.values())))

    return csv_times

def json_form(topk, d):
    app.logger.debug("Pulling JSON form")
    times = []
    for item in db.vals.find({},{ "_id": 0}):
        times.append(item)

    if d:
        for item in times:
            del item[d]

    if topk > 0:
        return times[:topk]

    return times

class ListAll(Resource):
    def get(self):
        d=''
        topk=-1
        return json_form(topk, d)

class ListAll_Type(Resource):
    def get(self, dtype):
        d=''
        k = request.args.get('top', type=int, default=-1)
        if dtype == 'csv':
            return csv_form(k, d)

        return json_form(k, d)

class ListOpenOnly(Resource):
    def get(self):
        d='close'
        topk=-1
        return json_form(topk, d)

class ListOpenOnly_Type(Resource):
    def get(self, dtype):
        d='close'
        k = request.args.get('top', type=int, default=-1)
        if dtype == 'csv':
            return csv_form(k, d)

        return json_form(k, d)


class ListCloseOnly(Resource):
    def get(self):
        d='open'
        topk=-1
        return json_form(topk, d)

class ListCloseOnly_Type(Resource):
    def get(self, dtype):
        d='open'
        k = request.args.get('top', type=int, default=-1)
        if dtype == 'csv':
            return csv_form(k, d)

        return json_form(k, d)

#resources
api.add_resource(ListAll, '/ListAll')
api.add_resource(ListAll_Type, '/ListAll/<string:dtype>')
#api.add_resource(ListAll_Type_topk, '/ListAll/<string:dtype>?<int:top>')

api.add_resource(ListOpenOnly, '/ListOpenOnly')
api.add_resource(ListOpenOnly_Type, '/ListOpenOnly/<string:dtype>')

api.add_resource(ListCloseOnly, '/ListCloseOnly')
api.add_resource(ListCloseOnly_Type, '/ListCloseOnly/<string:dtype>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
