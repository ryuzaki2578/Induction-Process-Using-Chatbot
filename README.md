# Induction Process Using Chatbot

To digitalize Induction Process

## Getting Started

	-For running the chatbot local machine do the following
		-Be in project directory
		-Start action server by using the command
			-rasa run actions
		-Run the chatbot in debug mode by using the following command
			-rasa shell --debug
		-For adding search keywords in lookup file(i.e. documents & video titles etc) update the lookup.txt file ./data/lookup
		-Schema of the mongodb Document:
		{
			"_id": { "bsonType": BSON.ObjectId() }
			"keyword": {"bsonType": "string"},
			"description":{"bsonType": "string"}
		}
		-Adding a document: 
		{
			"_id":{"$oid":"5f37ef25bb3dfbd192cc2d45"},
			"keyword":"Search Keyword you want to add i.e. video/document title",
			"description":"That video link"
		}
		-For adding Western Union Description update utter_displayAbouWU text in Domain.yml file
		
### Prerequisites
	-For the project we need
		-python 3.7
		-Rasa Framework install by the following command
			-pip install rasa
		-MongoDB for Database
### Installing
	-To run the command line app follow the instructions
	-Be in project directory
	-Start action server by using the command
		-rasa run actions
	-Run the chatbot in debug mode by using the following command
		-rasa shell --debug
	-Start the Rasa Chatbot Server By running the following command
		-rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml(specify port where you want to run rasa server)
	-Run Chatbot.py

## Built With

* [Rasa](https://rasa.com/docs/) - The Chatbot Framework
* [MongoDB](https://api.mongodb.com/python/current/tutorial.html) - For Database
