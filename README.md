# Server for virtual microscope

There is no interface part, this is just about the backend. But you can interact with the server through the jsons requests

## Description of the application

Virtual microscope was commitioned by Mechanical Engineering and Technologies department of NSTU. Its main function is to simulate the work of the real microscope. Also it was meant to create the special environment for student to create the virtual lab, to change it and to send it to the tutor. The tutor, in his turn, may watch all the labs sent by students, and the evaluate them. My role in the project was to create the server, storing the data for all the sent and evaluated labs and to provide the access to this information and relevant actions, depending on the access level (tutor or student)

## Description of the server part

The server is intended to store the database and to manipulate with data - to push them to DB and pull them from it.
DB stores the following information: the information about the student (name, surname and studying group), the list of presaved labs with parametres, the list of saved labs with parametres and the final score, the list with the lab's descriptions

The server has the authorization mechanism which includes checking the entered username and password, generating of the unique token for each user every time they log in. Also there is a registration mechanism which includes adding a new user to the User table in DB.


## Server as a part of complex application

One of the versions of app beeng developed

![6L7t78Aw_AmkHvTMviIWlDOTCajlkU2fR55BO-G_S-btlKaXUa0byVLLprUW8cfBG0tAs4HqipET2Isl_rN1UFsr](https://user-images.githubusercontent.com/68100447/173136548-6ac63657-aefa-4876-b1e8-0788c4ba1c43.jpg)

## Project technologies

Server is written on python framework Django, uses the ajax technology to handle the jsons coming from JS, DB used^ SQLite3


## To learn more

Here you may see the prezentation (which includes demonstration) https://prezi.com/view/PU9BxluxFhGGzsnFznVv/
