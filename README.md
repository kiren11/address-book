Goal: to create an interactive web app using Django and Python to create an address book, where contacts can be viewed, edited, deleted and searched for.

Instructions to run:
- Git clone repo through command line or GitHub GUI
- Run "python manage.py runserver" through terminal
- Open browser, go to "http://127.0.0.1:8000/login/"
- Had some difficulty with authentication, so a temporary username and pass are provided
      - Username: admin
      - Password: Pass


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
I have implemented this address book design using rows. Each rectangle can be clicked to access further details about the person. New contacts can be added through the "+ New Contact" button at the top right on the home page. To search for contacts, type in part of a name, or full name into the search bar and click the button to search. To delete a contact, click on the details of that person and click the button to delete. 

This was my first time coding with Django and I had a lot of fun! Unfortunately, I had difficulties getting the registration portion up and running, however the rest of the assignment is complete. I researched authentication, tried to implement different methods, but ultimately ran out of time.

------------------------------------------------------------------------------------------------------------------------------------------------------------
(Edge Cases Considered)
If no contacts present:
- Display message to user

Search:
- Search should be able to search for parts of a word, and still show result
	- example: search is "Gre", so "Greg Johnson" should still show up
- If I search for someone that is not in the contacts, contact list should be empty
- If two people have same string in their name, and it is searched, both contacts should show up
	- example: search is "Jo", both "John Doe" and "John Davidson" should show up

Inputs: 
- error thrown if form inputs are not of the right type
    -for example: only numbers can be entered for the phone category, up to 10 digits, otherwise an error is thrown

Deletion:
- offering prompt so that user has to click Delete twice
-------------------------------------------------------------------------------------------------------------------------------------------
With futher time, I'd explore:
- More form validation, checking inputs (no characters in phone number inputs, making sure emails have an "@" symbol")
    - Providing error messages in text rather than error being thrown
- Dynamic searching
- Complete authentication

Thank you!
Kiren Kaur
