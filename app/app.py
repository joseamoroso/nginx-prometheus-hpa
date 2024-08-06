from bottle import Bottle, response
from prometheus_client import Counter, start_http_server

c = Counter('heavywork_requests_total', 'Number of heavywork requests')
app = Bottle()

@app.post('/heavywork')
def heavywork():
    response.status = 202
    c.inc()
    return {"message": "Heavy work started"}

@app.post('/lightwork')
def lightwork():
    return {"message": "Light work done"}

@app.get('/up')
def lightwork():
    return {"message": "App running"}

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=8080)
