# Server for virtual microscope

There is no interface part, this is just about the backend. But you can interact with the server through the jsons requests

## Description

The server is intended to store the database and to manipulate with data - to push them to DB and pull them from it.
DB stores the following information: the information about the student (name, surname and studying group), the list of presaved labs with parametres, the list of saved labs with parametres and the final score

The server has the authorization mechanism which includes checking the entered username and password, generation ofthe unique token for each user every time they log in. Also there is a registration mechanism which includes adding a new user to the User table in DB.

The server ia also validationg the entering data

## Server as a part of complex application

One of the versions of app beeng developed

![6L7t78Aw_AmkHvTMviIWlDOTCajlkU2fR55BO-G_S-btlKaXUa0byVLLprUW8cfBG0tAs4HqipET2Isl_rN1UFsr](https://user-images.githubusercontent.com/68100447/173136548-6ac63657-aefa-4876-b1e8-0788c4ba1c43.jpg)


## To learn more

Here you may see the prezentation (which includes demonstration) https://prezi.com/view/PU9BxluxFhGGzsnFznVv/
