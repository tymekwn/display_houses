from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)

import sys

if sys.platform == "win32":
    working_dir = "."
else:
    working_dir = "/tmp"

@app.route("/qr")
def colour():
    try:
        open(f"{working_dir}/input.txt","r")
    except FileNotFoundError:
        with open(f"{working_dir}/input.txt","w") as f:
            f.write("white\nblank")
    with open(f"{working_dir}/input.txt","r") as f:
        color = f.readline()
        house = f.readline()
    print(house, color)
    try:
        with open(f"{working_dir}/{house}_counter.txt","r") as f:
            counter = f.read()
    except FileNotFoundError:
        counter = "0"
        with open(f"{working_dir}/{house}_counter.txt","w") as f:
            f.write(counter)


    
    return render_template("base.html",color=color,house=house,counter=counter)


@app.route("/house/<house>")
def write_colour(house):
    house_dict = {
        "etheldreda":"f0c566",
        "franklin":"009640",
        "seacole":"7a348a",
        "scott":"c01928",
        "turing":"1374bf"}
    current_house_counter = 1
    try:
        with open(f"{working_dir}/{house}_counter.txt","r") as f:
            current_house_counter = int(f.read()) + 1
    except FileNotFoundError:
        with open(f"{working_dir}/{house}_counter.txt","w") as f:
            f.write(str(current_house_counter))

    with open(f"{working_dir}/{house}_counter.txt","w") as f:
        f.write(str(current_house_counter))

    with open(f"{working_dir}/input.txt", "w") as f:
        f.write(f"{house_dict[house]}\n{house}")

    return f"Thank you for choosing the {house} house!" 

@app.route("/reset")
def reset():
    houselist = ["etheldreda","turing","franklin","scott","seacole"]
    for i in range(0,4):
        house = houselist[i]
        with open(f"{house}_counter.txt","w") as f:
            f.write(0)

    with open(f"{working_dir}/input.txt", "w") as f:
        f.write("white")

    return "Reset Complete."


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()