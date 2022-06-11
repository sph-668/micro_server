# Server for virtual microscope

There is no interface part, this is just about the backend. But you can interact with the server through the jsons requests

## Description of the application

Virtual microscope was commitioned by Mechanical Engineering and Technologies department of NSTU. Its main function is to simulate the work of the real microscope. Also it was meant to create the special environment for student to create the virtual lab, to change it and to send it to the tutor. The tutor, in his turn, may watch all the labs sent by students, and the evaluate them. My role in the project was to create the server, storing the data for all the sent and evaluated labs and to provide the access to this information and relevant actions, depending on the access level (tutor or student)

## Description of the server part

The server is intended to store the database and to manipulate with data - to push them to DB and pull them from it.
DB stores the following information: the information about the student (name, surname and studying group), the list of presaved labs with parametres, the list of saved labs with parametres and the final score, the list with the lab's descriptions

The server has the authorization mechanism which includes checking the entered username and password, generating of the unique token for each user every time they log in. Also there is a registration mechanism which includes adding a new user to the User table in DB.


## Server as a part of complex application

One of the versions of app

![image](https://user-images.githubusercontent.com/68100447/173196556-8cd14b74-85d1-4151-b4c5-16291fa16f6b.png)

![image](https://user-images.githubusercontent.com/68100447/173196615-24629224-edee-4085-a327-c2c330103a18.png)



## Project technologies

Server is written on python framework Django, uses the ajax technology to handle the jsons coming from JS, DB used^ SQLite3


## To learn more

Here you may see the prezentation (which includes demonstration) https://prezi.com/view/PU9BxluxFhGGzsnFznVv/

## To learn how that works

You have to clone the code and run the server by

`python manage.py runserver 0.0.0.0:8000`

Then you have to go to 127.0.0.1:8000

If you get the page with 'status: ok',you may pass the json of the following format to check if server is all right:

`let response = await (await fetch('signin/', {
method: 'POST',
body: JSON.stringify({username: 'Попов Игорь', password: '1ww3ee', group: 'ПМИ-90'})
})).json();`

You'll get the unique token for the session. Also you may sign up in the 'application', using the json like 

`let response = await (await fetch('signup/', {
method: 'POST',
body: JSON.stringify({username: 'your_name', password: 'your_password', group: 'your_studing_group'})
})).json();`

The required fields for the json body of the other requests are in the code comments
