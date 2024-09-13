from flask import Flask, render_template, url_for, request
import smtplib
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/announcements")
def announcements():
    return render_template("announcements.html")


@app.route("/president")
def president():
    return render_template("president.html")


@app.route("/secretary")
def secretary():
    return render_template("secretary.html")


@app.route("/organizer")
def organizer():
    return render_template("organizer.html")


@app.route("/treasurer")
def treasurer():
    return render_template("treasurer.html")


@app.route("/media")
def media():
    return render_template("media.html")


@app.route("/message")
def message():
    return render_template("message.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        messages = request.form['message']

        my_email = "ghastu2014@gmail.com"
        password = "djbjxpeqecvgmwvn"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=email, to_addrs=my_email,
                                msg=f"Subject: New Message From Your Website!\n\nName: {name}\nEmail address: {email}\nPhone number: {phone}\nMessage: {messages}")
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
