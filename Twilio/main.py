from flask import Flask, render_template
from twi import send_message

app = Flask('app')


@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/sms')
def send_sms():
  #this is where you connect to the APIs and send the sms
  msg = f"The following message has been sent: {send_message()}"
  return render_template("sms.html", msg=msg)


app.run(host='0.0.0.0', port=8080)
