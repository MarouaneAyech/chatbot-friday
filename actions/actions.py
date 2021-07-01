from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPrendreDiplome(Action):

    def name(self) -> Text:
        return "action_prendre_diplome"
    
    def  run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text =tracker.latest_message['text']
        
      
        return [SlotSet("specialite", text)]


class ActionDonnerOrientationBac(Action):

    def name(self) -> Text:
        return "action_donner_orientation_bac"
    
    def  run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bac = tracker.get_slot("specialite")
        if not bac:
            dispatcher.utter_message(text="ce genre de bac n'est pas pris à polytech")
        elif bac=="informatique":
            dispatcher.utter_message(response='utter_wrong_informatique')
        elif bac=="mathématique":
            dispatcher.utter_message(response='utter_wrong_science')
        return []



class ActionPrendreDiplomeAutre(Action):
    
    def name(self) -> Text:
        return "action_prendre_diplome_autre"
    
    def  run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
      
        return [SlotSet("diplome", text)]

class ActionPrendreSpecialiteAutre(Action):
    
    def name(self) -> Text:
        return "action_prendre_specialite"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["specialite"]
    
    def  run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        
      
        return [SlotSet("specialite", text)]


class ActionDonnerOrientationAutre(Action):

    def name(self) -> Text:
        return "action_donner_orientation_autre"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        diplome = tracker.get_slot("diplome")
        specialite=tracker.get_slot('specialite')
        if not diplome and not specialite:
            dispatcher.utter_message(text="ce genre de bac n'est pas pris à polytech")
        elif diplome=="licence" and specialite=='informatique':
            dispatcher.utter_message(response='utter_wrong_licence_info')
        elif diplome=="master" and specialite=='informatique':
            dispatcher.utter_message(response='utter_wrong_master_info')
        
        return []




