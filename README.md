# AirBnB_clone
## Description
   This project is the first step towards building an online marketspace HBNB: the AirBnB clone. On this level, is handled a part from the backend.
## AirBnB console usage
This console allow us to be able to manage the objects of our project:
#
	* Create a new object (ex: a new User or a new Place)
	* Retrieve an object from a file, a database etc
	* Do operations on objects (count, compute stats, etc)
	* Update attributes of an object
	* Destroy an object
## Classes
#
	* BaseModel
	* FileStorage
	* User
	* State
	* City
	* Amenity
	* Place
	* Review
## Commands
#
	* EOF: quit the console by end of file properly
	* quit: quit console
	* all: show all objects
	* help: list of available commands
	* create: create a new class instance
	* destroy: removes objects from storage
	* update: updates instances in storage
## Command Usage
EOF
#
	EOF
Quit
#
	quit
All
#
	all <class name>
Help
#
	help <command>
Create
#
	create <class name>
Destroy
#
	destroy <class name> <object id>
Update
#
	update <class name> <id> <attribute name>
# AUTHOR
Fares Sassi - fares.sassi2015@gmail.com