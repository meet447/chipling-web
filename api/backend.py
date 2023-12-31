import json
from service.chat import load_chats
from service.character import search_character
from llm.rika import Rika
from llm.Rikav2 import Rikav2
from llm.rikadel import rikadel
from llm.rikagpt import rika_chat_gpt

def homepage_api():
    
    data = load_chats
    return data

def search_api(search):
    
    data = search_character(search)
    return data

def rikav1_api(query):
    
    data = Rika(query=query)
    
    return data

def rikav2_api(query):
    
    data = Rikav2(query)
    return data

def rikadel_api(query):
    
    data = rikadel(query)
    
    return data

def rika_gpt(query):
    
    data = rika_chat_gpt(query)
    
    return data