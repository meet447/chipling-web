from service.chat import get_chat
from service.character import character_builder

def process_prompt(id):

    details = get_chat(id=id)
    
    name = details[0]["name"]
    desc = details[0]["long_desc"]
    scenario = details[0]["dialouge"]
    chat = details[0]["chat"]

    prompt = character_builder(name=name, description=desc, chat=chat, scenario=scenario)
        
    return prompt
    