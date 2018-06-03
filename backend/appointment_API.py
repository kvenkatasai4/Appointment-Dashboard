import json
from flask_api import FlaskAPI
from flask import make_response
import http
from flask import request
from postgresCRUD import PostgreSQLCRUD

app = FlaskAPI(__name__)


@app.route("/get_all_records", methods=['GET'])
def get_all_records():
    try:
        if request.method == "GET":
            db = PostgreSQLCRUD()
            db.connect()
            records = db.read_all()
            db.close()
            response = make_response(json.dumps(records))
        else:
            raise Exception("Invalid method")
    except Exception as error:
        response = make_response(json.dumps({"ERROR": str(error)}), http.HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers['Content-Type'] = "application/json"
    return response


@app.route("/get_records/<value>", methods=['GET'])
def get_records(value):
    try:
        if request.method == "GET":
            db = PostgreSQLCRUD()
            db.connect()
            records = db.read_query(value)
            db.close()
            response = make_response(json.dumps(records))
        else:
            raise Exception("Invalid method")
    except Exception as error:
        response = make_response(json.dumps({"ERROR": str(error)}), http.HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers['Content-Type'] = "application/json"
    return response


@app.route("/add_record", methods=['POST'])
def add_record():
    try:
        if request.method == "POST":
            payload = request.get_json()
            db = PostgreSQLCRUD()
            db.connect()
            records = db.insert_record(description=payload['description'], date=payload['date'], time=payload['time'])
            db.close()
            response = make_response(json.dumps(records))
        else:
            raise Exception("Invalid method")
    except Exception as error:
        response = make_response(json.dumps({"ERROR": str(error)}), http.HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers['Content-Type'] = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True)