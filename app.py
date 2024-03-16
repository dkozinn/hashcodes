# pylint: disable=C0111,C0112,C0113,C0114,C0115,C0116

from flask import Flask, redirect, render_template, request, url_for

from hashcodes import calc_hash  # Assuming hashcodes.py is in the same directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    input_string = request.form["callsign"]
    callsign, hash_list, storage = calc_hash(input_string)

    return render_template(
        "result.html",
        callsign=callsign,
        hash_list=hash_list,
        storage=storage,
    )


@app.route("/calculate_again")
def calculate_again():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)
