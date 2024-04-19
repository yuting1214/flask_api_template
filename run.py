import os
from dotenv import load_dotenv
from  sys import exit
from flask import render_template
from apps.config import config_dict
from apps import create_app
from api.models import Person


_ = load_dotenv('.env')

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('APP_DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))