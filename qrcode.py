from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)


@app.route("/qr")
def colour():
    with open("input.txt","r") as f:
        color = f.read()

    return render_template("base.html",color=color)


@app.route("/house/<house>")
def write_colour(house):
    house_dict = {
        "scott":"c01928",
        "etheldreda":"f0c566",
        "franklin":"009640",
        "turing":"1374bf",
        "seacole":"7a348a"
    }
    
    with open("input.txt", "w") as f:
        f.write(house_dict[house])

    return f"Thank you for choosing the {house} house!" 


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()