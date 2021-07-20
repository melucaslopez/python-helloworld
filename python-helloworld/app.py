from flask import Flask, json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def stats_api():
    health = {
        "result": "OK - healthy"
    }
    response = app.response_class(
        response=json.dumps(health),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("status endpoint looks good")
    return response

@app.route("/metrics")
def metrics_api():
    counts = {
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }
    response = app.response_class(
        response=json.dumps(counts),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("metrics endpoint looks good")
    return response

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        filename='app.log',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')
    app.run(host='0.0.0.0')
