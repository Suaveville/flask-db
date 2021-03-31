from flask import Flask, render_template, jsonify
import aws_controller



application = Flask(__name__)

# Index
@application.route('/')
def index():
    return render_template('home.html')

@application.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())

# About
@application.route('/about')
def about():
    return render_template('about.html')

# Articles
@application.route('/articles')
def articles():
    return render_template('articles.html')


# Articles
#@app.route('/articles')
#def articles():

# Con esto debugeamos
if __name__ == '__main__':
    
    application.run(debug=True)
