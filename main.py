from flask import Flask

app = Flask(__name__)
# app.debug=True

@app.route('/')
def index():
    return "<h1>Python</h1>"

# app.add_url_rule('/', 'index', index)

@app.route("/about")
def about():
    return "<h2>About</h2>"

# app.add_url_rule("/about", "about", about)

@app.route('/feedback')
@app.route('/contact')
def feedback():
    return "Feedback"

# app.add_url_rule("/feedback", 'feed', feedback)
# app.add_url_rule("/contact", "con", feedback)

@app.route('/user/<int:id>/')
def user(id):
    return "User #{}".format(id)

if __name__ == "__main__":
    app.run(debug=True)
    