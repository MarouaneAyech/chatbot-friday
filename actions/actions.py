from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateetudiantForm(FormValidationAction):
   

    def name(self) -> Text:
        return "validate_etudiant_form"

    @staticmethod
    def formation_db() -> List[Text]:
        """base des cycles de formations à polytech."""

        return 
        [
            "licence",
            "cycle preparatoire",
            "architecture",
            "cycle ingégnieure",
            "master professionels",
            "formations pour les professionels",
            "academy de dévéloppement de compétences",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        

        try:
            int(string)
            return True
        except ValueError:
            return False

   

    def validate_diplome(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        

        if value.lower() in self.formation_db():

            if value.lower()=="licence":
                dispatcher.utter_message(response="utter_licence")

            elif value.lower()=="cycle preparatoire":
                dispatcher.utter_message(response="utter_cycle_preparatoire")

            elif value.lower()=="master professionnels":
                dispatcher.utter_message(response="utter_master_pro")

            elif value.lower()=="cycle ingégnieure":
                dispatcher.utter_message(response="utter_ingégnieur")
            
            return {"diplome": value}

        
        else:
            dispatcher.utter_message(response="utter_wrong_diplome")
           
            return {"diplome": None}

   
    
  