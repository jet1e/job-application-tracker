from flask import Flask, request, jsonify, render_template
import os
from datetime import date, time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def dashboard():
    count_in_progress = 31
    count_accepted = 0
    count_rejected = 9
    user_name = "Jet"
    
    return render_template('dashboard.html',
                            user_name=user_name,
                            date=_get_formatted_date(),
                            count_in_progress=count_in_progress,
                            count_accepted=count_accepted,
                            count_rejected=count_rejected)

@app.route('/add_application', methods=['POST'])
def add_application():
    # Save to database
    return jsonify({"success": True})

def _get_formatted_date():
    today = date.today()
    day = today.day
    month = today.strftime("%B")
    year = today.year
    suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return f"{month} {day}{suffix}, {year}"

def _get_intro_quote(): #TODO
    return None

# main driver function
if __name__ == '__main__':
    app.run(debug=True)