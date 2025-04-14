Tech Stack: Python, Flask, Twilio API, Open Notify API, OpenWeatherMap API, Harry Potter API 

Project Overview:
This project is a Flask-based web application that sends a custom SMS message using the Twilio API. The SMS content is dynamically generated using real-time data from three external APIs:

•	Current number of people in space

•	Weather update for a selected city

•	A random character quote or fact from the Harry Potter API

The app demonstrates not just messaging capabilities, but how to aggregate and personalize data from multiple sources into one seamless output.

Features & Functionality:
Displays the homepage with a simple interface.
/sms

Triggers the send_message() function, which:

1.	Pulls the number of people currently in space via Open Notify API

2.	Fetches the current weather in Sudbury via OpenWeatherMap API

3.	Gets a random Harry Potter character via a third-party API

4.	Combines all this into a message and sends it via Twilio SMS

Data Flow & Logic
User ➜ Web App ➜ Aggregated APIs ➜ Twilio ➜ SMS to Mobile

Message Example:
"There are 10 people in space.
The temperature in Sudbury is 4°C.
"Your random Harry Potter character is – Albus Dumbledore"

 Key Functions
 
•	people_space() – from space.py: Queries the Open Notify API for current astronauts.

•	get_weather(city) – from weather.py: Gets the temperature for a given city.
•	get_char() – from hp.py: Returns a random Harry Potter character.
•	send_message() – from twi.py: Assembles data and sends SMS via Twilio client.

Twilio credentials are securely managed using environment variables for best practices.
