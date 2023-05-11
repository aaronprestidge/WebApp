# Real Python Project - Web Applications
# Aaron Prestidge
# May 8, 2023

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congrats, it's a web app."

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

# if __name__ == "__main__":
#     celsius = input("Celsius: ")
#     print("Fahrenheit:", fahrenheit_from(celsius))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
