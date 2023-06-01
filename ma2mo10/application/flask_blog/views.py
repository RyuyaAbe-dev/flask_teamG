from flask_blog import app

@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def hello_world():
    return "Hello World"