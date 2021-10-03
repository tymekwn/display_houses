from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)

@app.route("/qr")
def colour():
    with open("input.txt","r") as f:
        color = f.readline()
        house = f.readline()
    print(house, color)

    with open(f"{house}_counter.txt","r") as f:
        counter = f.read()
    
    return render_template("base.html",color=color,house=house,counter=counter)


@app.route("/house/<house>")
def write_colour(house):
    house_dict = {
        "etheldreda":"f0c566",
        "franklin":"009640",
        "seacole":"7a348a",
        "scott":"c01928",
        "turing":"1374bf"}

    with open(f"{house}_counter.txt","r") as f:
        current_house_counter = int(f.read())
        current_house_counter += 1
    with open(f"{house}_counter.txt","w") as f:
        f.write(str(current_house_counter))

    with open("input.txt", "w") as f:
        f.write(f"{house_dict[house]}\n{house}")

    return f"Thank you for choosing the {house} house!" 


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()