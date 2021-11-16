from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import os


app = Flask(__name__)

gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if gunicorn:
    metrics = GunicornInternalPrometheusMetrics(app)
else:
    metrics = PrometheusMetrics(app, group_by='path')
    metrics.info("app_info", "Application Info", version="1.0.3")

@app.route('/')
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()