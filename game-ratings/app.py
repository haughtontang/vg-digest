from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q")
    return render_template("home.html", query=query)

if __name__ == "__main__":
    app.run(debug=True)
