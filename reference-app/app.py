#Reference source :https://github.com/rycus86/prometheus_flask_exporter#prometheus-flask-exporter


from flask import Flask, render_template, request, jsonify
import os
from flask_pymongo import PyMongo
from jaeger_client import Config
from flask_opentracing import FlaskTracing
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
from os import getenv
JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')



trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'
mongo = PyMongo(app)

metrics = PrometheusMetrics(app, group_by='path')
metrics.info("app_info", "Application Info", version="1.0.3")


new_var = {'reporting_host': JAEGER_HOST}
config = Config(
    config={
        'sampler':
            {
                'type': 'const',
                'param': 1
            },
        'logging': True,
        'reporter_batch_size': 1,
        new_var },
    service_name="backend")

tracer = config.initialize_tracer()
tracing = FlaskTracing(tracer, True, app)

path_counter = metrics.counter(
    'path_counter', 'Request count by path',
    labels={'path': lambda: request.path}
)


@app.route('/')
@path_counter
def homepage():
    with tracer.start_span('hello') as span:
        res = "Hello World"
        span.set_tag('message',res)
    return "Hello World"


@app.route('/api')
@path_counter
def my_api():
    with tracer.start_span('api') as span:
        answer = "something"
        span.set_tag('message', answer)
    return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()
