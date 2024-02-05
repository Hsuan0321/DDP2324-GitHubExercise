# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g
app = Flask("app")

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")
database_path="app.db"

# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
# THIS ROUTE IS TO PROVE THE FLASK SETUP WORKS.
        
@app.route('/')
def show_landingpage():
    return render_template('Homepage.html')


@app.route('/homepage')
def show_homepage():
    return render_template('Homepage.html')


@app.route('/restaurant')
def show_restaurant():
    return render_template('Restaurant.html')

@app.route('/contactus')
def show_cotactus():
    return render_template('Contact us.html')

@app.route('/dirtyduckdetail')
def show_dirtyduck():
    return render_template('DD details.html')

@app.route('/reservation', methods=['GET'])
def form():
    return render_template('reservation.html')


#Function of making reservation
@app.route('/reservation', methods=['POST'])
def form_post():
    reservation_name = request.form['name']
    reservation_date = request.form['date']
    reservation_time = request.form['time']
    number_of_people = request.form['number of people']
    Email = request.form['Email']
    phone_number = request.form['phone']

    # Insert data into the database
    conn=get_db_connection()
    cur = conn.cursor()
    cur.execute('''INSERT INTO reservations (reservation_name, reservation_date, reservation_time, number_of_people, email, phone_number) 
                   VALUES (?, ?, ?, ?, ?, ?)''', 
                (reservation_name, reservation_date, reservation_time, number_of_people, Email, phone_number))
    conn.commit()
    conn.close()

    return "Reservation Submitted Successfully"

if __name__ == '__main__':
    app.run(debug=True)

    
    #Function of Checking Database and sned Email
    
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_via_smtp(recipient_email, subject, body):
    sender_email = "warwickrestauranthub@outlook.com"  # Replace with your email address
    sender_password = "Warwick123!"  # Replace with your email password

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    try:
        # Log in to server using secure context and send email
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)  # Replace with your SMTP server and port
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/reservation', methods=['POST'])
def form_post():
    # Your form handling code here...
    Email = request.form.get('email')
    reservation_name = request.form.get('reservation_name')
    # Assuming the reservation was added to the database successfully
    email_subject = "Reservation Confirmation"
    email_body = f"Dear {reservation_name},\n\nYour reservation has been made successfully."
    send_email_via_smtp(Email, email_subject, email_body)

    return "Reservation Submitted Successfully"