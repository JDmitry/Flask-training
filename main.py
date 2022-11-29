from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def req():
    return "IP: {}\nother: {}".format(request.remote_addr, request.user_agent)

if __name__ == "__main__":
    app.run(debug=True)
    