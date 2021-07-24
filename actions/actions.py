from os import close, sep
from rasa_sdk.events import SlotSet
import csv
import numpy as np
from io import StringIO
import io
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import EventType
from rasa_sdk import Action
import re
import datetime
import string

class ValidateRestaurantForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_orientation_form"

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_nom(
        self,
        
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate nom value."""
        names=tracker.get_slot("nom")
        nom_expression=r'\d'
        valid=re.search(nom_expression, names)
        if len(slot_value)<3 or slot_value==" ":
            dispatcher.utter_message(text="entrer un nom correcte")
            return {"nom": None }
        elif valid:
            dispatcher.utter_message(text="entrer un nom correcte")
            return {"nom": None }
        else:
            return {"nom": slot_value}

    def validate_prenom(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate prenom value."""
        surname=tracker.get_slot("prenom")
        prenom_expression=r'\d'
        valid=re.search(prenom_expression, surname)
        if len(slot_value)<3 or slot_value==" ":
            dispatcher.utter_message(text="entrer un prénom correcte")
            return {"prenom": None }
        elif valid:
            dispatcher.utter_message(text="entrer un prénom correcte")
            return {"prenom": None }
        else:
            return {"prenom": slot_value}

    
    def validate_telephone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate telephone value."""
        phone = r"^[0-9][0-9]{7}$"
        match = re.match(phone, slot_value)
        if len(slot_value) == 8 and match:
            
            return {"telephone": slot_value}
        else:        
            return {"telephone": None}


    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""
        adresse = r"[^@]+@[^@]+\.[^@]+"
        match= re.match(adresse, slot_value)
        if slot_value and match:
            
            return {"email": slot_value}
        else:        
            return {"email": None}

    def validate_date_naissance(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate telephone value."""
        dates=r"[\d]{1,2}/[\d]{1,2}/[\d]{4}"
        match= re.match(dates, slot_value)
        if slot_value and match:
            
            return {"date_naissance": slot_value}
        else:        
            return {"date_naissance": None}

    def validate_dernier_diplome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate telephone value."""

        if tracker.get_slot("dernier_diplome"):
            
            return {"dernier_diplome": slot_value}
        else:        
            return {"dernier_diplome": None}

    def validate_specialite(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate specialite value."""

        if tracker.get_slot("specialite"):
            
            return {"specialite": slot_value}
        else:        
            return {"specialite": None}

    def validate_obtention(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate obtention value."""
        date_diplome = r"[289]"
        match = re.match(date_diplome, slot_value)
        if len(slot_value)==4 and match:
            
            return {"obtention": slot_value}
        else:        
            return {"obtention": None}

    def validate_mention(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate mention value."""

        if tracker.get_slot("mention"):
            
            return {"mention": slot_value}
        else:        
            return {"mention": None}

    def validate_centre_interet(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate centre_interet value."""

        if tracker.get_slot("centre_interet"):
            
            return {"centre_interet": slot_value}
        else:        
            return {"centre_interet": None}



class ActionCsv(Action):
    
    def name(self) -> Text:
        return "action_csv"
    
    def  run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nom= tracker.get_slot("nom")
        prenom= tracker.get_slot("prenom")
        telephone= tracker.get_slot("telephone")
        email= tracker.get_slot("email")
        naissance= tracker.get_slot("date_naissance")
        diplome= tracker.get_slot("dernier_diplome")
        specialite= tracker.get_slot("specialite")
        dateDiplome = tracker.get_slot("obtention")
        mention = tracker.get_slot("mention")
        interet = tracker.get_slot("centre_interet")
        
        if diplome=="bac":
            if specialite=="informatique":
                if mention=="bien" or mention=="assez-bien":
                    if interet=="informatique":
                        dispatcher.utter_message(text="prépa_ie")
       
                    return []
        elif diplome=="bac":
            if specialite=="informatique":
                if mention=="passable":
                    if interet=="informatique":
                        dispatcher.utter_message(text="licence_ie")
                    return[]

        elif diplome=="bac":
            if specialite=="math":
                if mention=="passable" or mention=="bien" or mention=="assez-bien" :
                    if interet=="probleme" or interet=="bricolage":
                        dispatcher.utter_message(text="Cycle Préparatoire Intégré Mécanique, Matériaux et Microtechniques")
                    return[]

        elif diplome=="licence":
            if specialite=="Électromécanique" or specialite=="automatique" or specialite=="logistique":
                if mention=="passable" or mention=="assez-bien" or mention=="bien":
                    if interet=="informatique" or interet=="bricolage":
                        dispatcher.utter_message(text="Ingénieur Génie Industriel")
                    return[]

        elif diplome=="licence":
            if specialite=="Mécanique" or specialite=="Mécatronique" :
                if mention=="passable" or mention=="assez-bien" or mention=="bien":
                    if interet=="informatique" or interet=="bricolage":
                        dispatcher.utter_message(text="Ingénieur en Mécatronique")
                    return[]
        
        elif diplome=="licence":
            if specialite=="tech-sup":
                if mention=="passable" or mention=="assez-bien" or mention=="bien":
                    if interet=="informatique" or interet=="bricolage":
                        dispatcher.utter_message(text="INGÉNIERIE ARCHITECTURE ET INTÉGRATION DES SYSTÈMES ET DES LOGICIELS (CNAM PARIS)")
                    return[]

        elif diplome=="licence":
            if specialite=="informatique":
                if mention=="passable" or mention=="assez-bien" or mention=="bien":
                    if interet=="reseaux" or interet=="mutlimédia":
                        dispatcher.utter_message(text="INGÉNIEUR INFORMATIQUE, RÉSEAUX ET MULTIMÉDIA")
                    return[]
                
        elif diplome=="licence":
            if specialite=="informatique":
                if mention=="passable" or mention=="assez-bien" or mention=="bien":
                    if interet=="jeux-vidéos":
                        dispatcher.utter_message(text="MASTER CANADIEN EN DÉVELOPPEMENT JEU VIDÉO")
                    return[]

        
        else:
             dispatcher.utter_message(text="désolé")



      

   




