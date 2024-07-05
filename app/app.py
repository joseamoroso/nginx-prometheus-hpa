from bottle import Bottle, request, response

app = Bottle()

@app.post('/heavywork')
def heavywork():
    response.status = 202
    return {"message": "Heavy work started"}


@app.post('/lightwork')
def lightwork():
    return {"message": "Light work done"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
