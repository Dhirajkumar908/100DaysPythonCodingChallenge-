from flask import Flask, redirect

app=Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    
    page=""
    f=open("template/index.html", "r")
    page=f.read()
    f.close()

    return page

@app.route('/blog1')
def blog1():
    name='Dhiraj'
    title="Day76 python coding challenge"
    text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
    image = "om.jpeg"
    link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"
    page=""
    f=open("template/portfolio.html", "r")
    page=f.read()
    f.close()
    page=page.replace("{name}", name)
    page=page.replace("{title}", title)
    page=page.replace("{text}", text)
    page=page.replace("{image}", image)
    page=page.replace("{link}", link)

    return page
@app.route('/blog2')
def blog2():
    name='Ram'
    title="Day99 python coding challenge"
    text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
    image = "om.jpeg"
    link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"
    page=""
    f=open("template/portfolio.html", "r")
    page=f.read()
    f.close()
    page=page.replace("{name}", name)
    page=page.replace("{title}", title)
    page=page.replace("{text}", text)
    page=page.replace("{image}", image)
    page=page.replace("{link}", link)

    return page

@app.route('/77')
def linktree():
    return redirect("https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")


app.run(host='0.0.0.0', port=81)