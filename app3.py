from flask import Flask

app=Flask(__name__, static_url_path='/static')

@app.route('/')
def index():

    page='''
        <h1><a href="74" >day74</a></h1>
        <h1><a href="75" >day75</a></h1>
        <h1><a href="76" >day76</a></h1>
        <h1><a href="77" >day77</a></h1>

        '''
    return page

@app.route('/74')
def day74():
   
    day='74'
    link='https://replit.com/@kumardhirajkuma/Day78100Days'
    text="Assigned the result of each replace operation back to the page variable."
    page=""
    f=open('template/reple.html', "r")
    page=f.read()
    f.close()

    page=page.replace("{day}", day)
    page=page.replace("{link}", link)
    page=page.replace("{text}", text)

    return page

@app.route('/75')
def day75():
   
    day='75'
    link='https://replit.com/@kumardhirajkuma/Day78100Days'
    text="Assigned the result of each replace operation back to the page variable."
    page=""
    f=open('template/reple.html', "r")
    page=f.read()
    f.close()

    page=page.replace("{day}", day)
    page=page.replace("{link}", link)
    page=page.replace("{text}", text)

    return page

app.run(host='0.0.0.0', port=81)