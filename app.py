from flask import Flask, render_template, request, redirect #imports peices from Flask lib
#Flask: creates a web app
#render_template: loads the html files in the directory
#request: gets data when forms are submitted
#redirect: brings user back to home page
import resend
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__) # starts a new webpage app, __name__ tells Flask where files are located
# __name__ is a built in var for py, which gets a value depending on how the file is being used
# this uses flask and tells it to use this file to run it, rather than another one

resend.api_key = os.getenv("RESEND_API_KEY")
bookings = [] # creates list for things user wants

@app.route('/') # when someone visits the homepage '/', run the home funct
# '/' is http://127,0.0.5000
def home(): # runs when someone visits the homepage
    return gallery()

@app.route('/about') # when someone visits the homepage '/', run the home funct
def about(): # runs when someone visits the homepage
    return render_template('about.html')
# displays about.html

@app.route('/contact', methods=['GET', 'POST']) # when someone visits the booking page, runs the book funct
# creates another webpage off of http://127,0.0.5000 -> http://127,0.0.5000/book
# GET is for if a form hasn't been submitted
# POST is for if a form has been submitted
    # request.method = 'GET' until the form is submitted, then it = 'POST'
def contact(): # runs when someone visits /book
    if request.method == 'POST': # when http://127.0.0.1:5000/book is entered into browser, browser sends GET /book
        # the index.html sets method to POST when it gets submitted (<form method="POST">), so this funct will save the data when that happens
        # if form has been submitted...
        firstName = request.form['firstName'] # this gets the info from the form because html file uses name
        lastName = request.form['lastName'] # this gets the info from the form because html file uses name
        email = request.form['emailAdress']
        telephoneNumber = request.form['telephoneNumber']
        state = request.form['state']
        notes = request.form['notes']
        bookings.append({ # append the values given to the array using a dictionary (each booking stored in a dict)
            'name': firstName + " " + lastName,
            'email': email,
            'telephoneNumber': telephoneNumber,
            'state': state,
            'notes': notes 
            })
        recentBooking = f"CONTACT REQUEST,\nName: {bookings[-1]['name']},\nEmail: {bookings[-1]['email']},\nPhone Number: {bookings[-1]['telephoneNumber']},\nExtra: {bookings[-1]['notes']}\n"
        # saveBookingsFile = open('photoBookings.txt', 'w')
        # saveBookingsFile.write("CONTACT REQUEST\n")
        # saveBookingsFile.write(f"Name: {bookings[-1]['name']}\n")
        # saveBookingsFile.write(f"Email: {bookings[-1]['email']}\n")
        # saveBookingsFile.write(f"Phone Number: {bookings[-1]['telephoneNumber']}\n")
        # saveBookingsFile.write(f"Extra: {bookings[-1]['notes']}\n")
        # saveBookingsFile.close()
        # saveBookingsFile = open('photoBookings.txt', 'r')
        # txtContents=saveBookingsFile.read()
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "cstoltphotos@gmail.com",
        "subject": "New Client Request!",
        "html": f"<p>{recentBooking}</p>"
        })

        

        return redirect('/') # go back to homepage
    
    return render_template('contact.html') # if form not submitted, go back to booking page


@app.route('/thankYou')
def thankYou():
    return render_template('thankYouPage.html') # if form not submitted, go back to booking page


@app.route('/petBooking', methods=['GET', 'POST']) # when someone visits the booking page, runs the book funct
def petBook(): # runs when someone visits /book
    if request.method == 'POST': # when http://127.0.0.1:5000/book is entered into browser, browser sends GET /book
        # the index.html sets method to POST when it gets submitted (<form method="POST">), so this funct will save the data when that happens
        # if form has been submitted...
        firstName = request.form['firstName'] # this gets the info from the form because html file uses name
        lastName = request.form['lastName'] # this gets the info from the form because html file uses name
        email = request.form['emailAdress']
        telephoneNumber = request.form['telephoneNumber']
        state = request.form['state']
        petName = request.form['petName']
        petSpecies = request.form['petSpecies']
        petBreed = request.form['petBreed']
        notes = request.form['notes']
        bookings.append({ # append the values given to the array using a dictionary (each booking stored in a dict)
            'name': firstName + " " + lastName,
            'email': email,
            'telephoneNumber': telephoneNumber,
            'state': state,
            'petName': petName,
            'petSpecies': petSpecies,
            'petBreed': petBreed,
            'notes': notes 
            })
        recentBooking = f"PET REQUEST,\nName: {bookings[-1]['name']},\nEmail: {bookings[-1]['email']},\nPhone Number: {bookings[-1]['telephoneNumber']},\n State: {bookings[-1]['state']}, Pet Name: {bookings[-1]['petName']} \n, Pet Species: {bookings[-1]['petSpecies']} \n, Pet Breed: {bookings[-1]['petBreed']} \n,  Extra: {bookings[-1]['notes']}\n"
        # saveBookingsFile = open('photoBookings.txt', 'a')
        # saveBookingsFile.write("PET BOOKING REQUEST\n")
        # saveBookingsFile.write(f"Name: {bookings[-1]['name']}\n")
        # saveBookingsFile.write(f"Email: {bookings[-1]['email']}\n")
        # saveBookingsFile.write(f"Phone Number: {bookings[-1]['telephoneNumber']}\n")
        # saveBookingsFile.write(f"Pet Name: {bookings[-1]['petName']}\n")
        # saveBookingsFile.write(f"Pet Species: {bookings[-1]['petSpecies']}\n")
        # saveBookingsFile.write(f"Pet Breed: {bookings[-1]['petBreed']}\n")
        # saveBookingsFile.write(f"Extra: {bookings[-1]['notes']}\n")
        # saveBookingsFile.close()
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "cstoltphotos@gmail.com",
        "subject": "New Client Request!",
        "html": f"<p>{recentBooking}</p>"
        })

        return redirect('/thankYou') # go back to homepage
    
    return render_template('petBooking.html') # if form not submitted, go back to booking page

@app.route('/equineBooking', methods=['GET', 'POST']) # when someone visits the booking page, runs the book funct
def equestrianBook(): # runs when someone visits /book
    if request.method == 'POST': # when http://127.0.0.1:5000/book is entered into browser, browser sends GET /book
        # the index.html sets method to POST when it gets submitted (<form method="POST">), so this funct will save the data when that happens
        # if form has been submitted...
        firstName = request.form['firstName'] # this gets the info from the form because html file uses name
        lastName = request.form['lastName'] # this gets the info from the form because html file uses name
        email = request.form['emailAdress']
        telephoneNumber = request.form['telephoneNumber']
        state = request.form['state']
        petName = request.form['petName']
        petBreed = request.form['petBreed']
        event = request.form['event']
        notes = request.form['notes']
        bookings.append({ # append the values given to the array using a dictionary (each booking stored in a dict)
            'name': firstName + " " + lastName,
            'email': email,
            'telephoneNumber': telephoneNumber,
            'state': state,
            'petName': petName,
            'petBreed': petBreed,
            'event': event,
            'notes': notes 
            })
        recentBooking = f"HORSE REQUEST,\nName: {bookings[-1]['name']},\nEmail: {bookings[-1]['email']},\nPhone Number: {bookings[-1]['telephoneNumber']},\n State: {bookings[-1]['state']}, Horse Name: {bookings[-1]['petName']} \n, Horse Breed: {bookings[-1]['petBreed']} \n, Event: {bookings[-1]['event']}  Extra: {bookings[-1]['notes']}\n"

        # saveBookingsFile = open('photoBookings.txt', 'a')
        # saveBookingsFile.write("EQUINE BOOKING REQUEST\n")
        # saveBookingsFile.write(f"Name: {bookings[-1]['name']}\n")
        # saveBookingsFile.write(f"Email: {bookings[-1]['email']}\n")
        # saveBookingsFile.write(f"Phone Number: {bookings[-1]['telephoneNumber']}\n")
        # saveBookingsFile.write(f"Pet Name: {bookings[-1]['petName']}\n")
        # saveBookingsFile.write(f"Pet Breed: {bookings[-1]['petBreed']}\n")
        # saveBookingsFile.write(f"Event: {bookings[-1]['event']}\n")
        # saveBookingsFile.write(f"Extra: {bookings[-1]['notes']}\n")
        # saveBookingsFile.close()
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "cstoltphotos@gmail.com",
        "subject": "New Client Request!",
        "html": f"<p>{recentBooking}</p>"
        })
        return redirect('/thankYou') # go back to homepage
    
    return render_template('equineBooking.html') # if form not submitted, go back to booking page


@app.route('/peopleBooking', methods=['GET', 'POST']) # when someone visits the booking page, runs the book funct
def peopleBook(): # runs when someone visits /book
    if request.method == 'POST': # when http://127.0.0.1:5000/book is entered into browser, browser sends GET /book
        # the index.html sets method to POST when it gets submitted (<form method="POST">), so this funct will save the data when that happens
        # if form has been submitted...
        firstName = request.form['firstName'] # this gets the info from the form because html file uses name
        lastName = request.form['lastName'] # this gets the info from the form because html file uses name
        email = request.form['emailAdress']
        telephoneNumber = request.form['telephoneNumber']
        state = request.form['state']
        numberOfPeople = request.form['numberOfPeople']
        reasonForShoot = request.form['reasonForShoot']
        event = request.form['event']
        notes = request.form['notes']
        bookings.append({ # append the values given to the array using a dictionary (each booking stored in a dict)
            'name': firstName + " " + lastName,
            'email': email,
            'telephoneNumber': telephoneNumber,
            'state': state,
            'numberOfPeople': numberOfPeople,
            'reasonForShoot': reasonForShoot,
            'event': event,
            'notes': notes 
            })
        recentBooking = f"PEOPLE REQUEST,\nName: {bookings[-1]['name']},\nEmail: {bookings[-1]['email']},\nPhone Number: {bookings[-1]['telephoneNumber']},\n State: {bookings[-1]['state']}, Number of People: {bookings[-1]['numberOfPeople']} \n, Reason For Shoot: {bookings[-1]['reasonForShoot']} \n, Event: {bookings[-1]['event']}  Extra: {bookings[-1]['notes']}\n"

        # saveBookingsFile = open('photoBookings.txt', 'a')
        # saveBookingsFile.write("PEOPLE BOOKING REQUEST\n")
        # saveBookingsFile.write(f"Name: {bookings[-1]['name']}\n")
        # saveBookingsFile.write(f"Email: {bookings[-1]['email']}\n")
        # saveBookingsFile.write(f"Phone Number: {bookings[-1]['telephoneNumber']}\n")
        # saveBookingsFile.write(f"Number of People: {bookings[-1]['numberOfPeople']}\n")
        # saveBookingsFile.write(f"Reason for Shoot: {bookings[-1]['reasonForShoot']}\n")
        # saveBookingsFile.write(f"Event: {bookings[-1]['event']}\n")
        # saveBookingsFile.write(f"Extra: {bookings[-1]['notes']}\n")
        # saveBookingsFile.close()
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "cstoltphotos@gmail.com",
        "subject": "New Client Request!",
        "html": f"<p>{recentBooking}</p>"
        })
        return redirect('/thankYou') # go back to homepage
    
    return render_template('peopleBooking.html') # if form not submitted, go back to booking page



@app.route('/gallery') # when gallery page is opened, run gallery function, which will get photos and run the html file
def gallery():
    photos = [
        # enter photos
        'Ziggy1.JPG',
        'Tom1.JPG',
        'Bowie1.JPG',
        'Joust1.JPG', 
        'Ziggy2.JPG',
        'Sarah1.JPG',
        'Theia1.JPG',
        'Ziggy3.JPG',
        'Winnie1.JPG'
    ]
    return render_template("gallery.html", photos=photos) # opens html file and sends photos

@app.route('/equestrianGallery')
def equestrianGallery():
    photos = [
        'Ziggy1.JPG',
        'Ziggy2.JPG',
        'Joust3.JPG',
        'Ziggy5.JPG',
        'Joust1.JPG',
        'Joust2.JPG',
        'Ziggy4.JPG',
        'Joust4.JPG',
        'Ziggy6.JPG'
    ]
    return render_template("equestrianGallery.html", photos=photos) # opens html file and sends photos

@app.route('/petGallery')
def petGallery():
    photos = [
       'Theia1.JPG',
       'Winnie1.JPG',
       'RenDog2.JPG',
       'RenDog1.JPG',
       'ZoCat1.JPG',
       'Bowie2.JPG'
    ]
    return render_template("petGallery.html", photos=photos) # opens html file and sends photos

@app.route('/peopleGallery')
def peopleGallery():
    photos = [
        'Tom3.JPG',
        'Tom1.JPG',
        'Carter1.JPG',
        'Sarah1.JPG',
        'Tom2.JPG',
    ]
    return render_template("peopleGallery.html", photos=photos) # opens html file and sends photos

@app.route('/skateGallery')
def skateGallery():
    photos = [
        'Skate1.JPG',
        'Skate2.JPG',
        'Skate6.JPG',
        'Skate3.JPG',
        'Skate5.JPG',
        'Skate4.JPG',

    ]
    return render_template("skateGallery.html", photos=photos) # opens html file and sends photos

if __name__ == '__main__': # if this file is the one running everything...
    app.run(debug=True) # run the app using this program
