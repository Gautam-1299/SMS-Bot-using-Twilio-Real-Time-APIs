import os
from twilio.rest import Client
from space import people_space
from weather import get_weather
from hp import get_char


def send_message():
  # Find your Account SID and Auth Token at twilio.com/console
  # and set the environment variables. See http://twil.io/secure
  account_sid = os.environ['TWILIO_ACCOUNT_SID'] # sid from your profile
  auth_token = os.environ['TWILIO_AUTH_TOKEN'] # authentication token
  client = Client(account_sid, auth_token)
  
  msg = f"{people_space()}. \nThe temprature in Sudbury is {get_weather('Sudbury')}. \n{get_char()}"
  message = client.messages.create(
      body=msg,
      from_="+15076657329", # twilio number
      to="+17056906249", #canadian number
    )
  
  return(message.body)