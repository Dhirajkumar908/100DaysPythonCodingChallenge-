from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/portfolio">portfolio</a></p>
  <p><a href = "/linktree">linktree</a></p>
  </body>
  </html>"""
  return page

@app.route('/portfolio') 
def portfolio(): 
  today=datetime.date.today()
  page = f"""
  <html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
    <h2>{today}</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="static/image/om.jpeg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
  
</html>
  
  """
  
  return page

@app.route('/linktree')
def linktree():
  app=f"""<html><body>
  <h1>link Tree Page</h1>
  </body>
  </html>"""
  return app

app.run(host='0.0.0.0', port=81)