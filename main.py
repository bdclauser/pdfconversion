from flask import Flask
app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def response():
    #Retrive the namve from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}


@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)