from flask import Flask , request

app=Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    page=''
    f=open("template/index.html", "r")
    page=f.read()
    f.close()

    return page

@app.route('/process', methods=["POST"])
def process():
    form_data=request.form
    page=""

    if form_data["baldies"]=="david":
        page +=f"you are alright{form_data['username']}"
    else:
        page +=f"You have picked wrong {form_data['username']}"

    return page

@app.route('/loginPage')
def loginPage():
    page=""
    f=open("template/login.html", "r")
    page=f.read()
    f.close()
    return page

@app.route('/login', methods=["POST"])
def login():
    page=""
    userid=request.form.get("userid")
    password=request.form.get("password")
    print(password)
    if userid=="dhiraj" and password==123:
        page +=f"{userid} are loged in successfully"
    else:
        page +=f"{userid} is invalid"
    return page


app.run(host='0.0.0.0', port=81)