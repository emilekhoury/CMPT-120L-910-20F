from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home(): 
    app.logger.info("User connected to home route")
    return render_template('home.html')gi

@app.route('/about')
def about():
    app.logger.info("User connected to about route")
    return render_template('about_me.html')

@app.errorhandler(404)
def error_page(e):
    app.logger.info("User connected to 404")
    return render_template("404.html"), 404

# Testing
app.run(host='localhost', port=8080, debug=True)
    
    
