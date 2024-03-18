from flask import Flask

app=Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    page=''
    f=open("template/index.html", "r")
    page=f.read()
    f.close()

    return page


app.run(host='0.0.0.0', port=81)