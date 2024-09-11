from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/announcements.html")
def announcements():
    return render_template("announcements.html")


@app.route("/president.html")
def president():
    return render_template("president.html")


@app.route("/secretary.html")
def secretary():
    return render_template("secretary.html")


@app.route("/organizer.html")
def organizer():
    return render_template("organizer.html")


@app.route("/treasurer.html")
def treasurer():
    return render_template("treasurer.html")


@app.route("/media.html")
def media():
    return render_template("media.html")


@app.route("/message.html")
def message():
    return render_template("message.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
