# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
class ActionDisplayResults(Action):
    def name(self) -> Text:
        return "action_displayResults"    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            track=tracker.latest_message["entities"]
            mongoConn=MongoClient("mongodb+srv://Admin:Admin@cluster0-q4yrs.mongodb.net/FP?retryWrites=true&w=majority")
            myDb=mongoConn['ChatBot']
            print(track)
            search_value=str(track[0]['value'])
            description="Not Found"
            if myDb!=None:
                myCol=myDb['keywords']
                for i in list(myCol.find()):
                    if(i['keyword'].lower().find(search_value.lower())>=0):
                        description=i['description']
                        print(i)
            message="I am displaying result for the keyword "+ search_value+'\n'+ description
            dispatcher.utter_message(text=message)            
        except:
            message="Keyword Not Found Please Try Again"
            dispatcher.utter_message(text=message)
        return []
