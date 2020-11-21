from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home(): 
    print("user is going to /")
    return render_template('home.html')


@app.route('/about')
def about():
    print("user is goint to /about")
    return render_template('about_me.html')

# Testing
app.run(host='localhost', port=8080, debug=True)
    
    
