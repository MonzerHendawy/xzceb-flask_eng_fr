import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
# apikey is saved in .env file
# url is saved in .env file
# apikey and url are passed as arguments,
# to create an instance of ibm watson translator

authenticator = IAMAuthenticator(apikey) 
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def englishToFrench (englishText):
    """
    translate englishText to frenchText
    """
    try:
        #condition to make sure the text is NOT null or empty
        if  englishText and englishText.strip():
            # obtain the translation object from ibm_watson api
            translationObject = language_translator.translate(text=englishText,
            model_id="en-fr").get_result()
            #retrieve the english translation from the translation object
            frenchText = translationObject["translations"] [0] ["translation"]
            # return the clean data
            return frenchText
        else:
            #in case the text is null or empty
            return "please enter a valid text to translate"
    #catch any exception and print the exception message
    except ApiException as ex:
        print(ex.message)

def frenchToEnglish(frenchText):
    """
    translate frenchText to englishText
    """
    try:
        #condition to make sure the text is NOT  null or empty
        if  frenchText and frenchText.strip():
            # obtain the translation object from ibm_watson api
            translationObject = language_translator.translate(text=frenchText,
            model_id="fr-en").get_result()
            #retrieve the english translation from the translation object
            englishText = translationObject["translations"] [0] ["translation"]
            # return the clean data
            return englishText
        else:
            #in case the text was null or empty
            return "please enter a valid text to translate"
    #catch any exception and print the exception message
    except ApiException as ex:
        print(ex.message)