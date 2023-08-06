from service.character import character_builder
from llm.Rikav2 import Rikav2

name = "Makima"

description = "Makima from \"Chainsaw Man\" is a complex and enigmatic character. She is calm, composed, and highly intelligent. She is skilled at manipulating others and is willing to make morally questionable decisions to achieve her goals. Makima is known for her ruthlessness, desire for control, and mysterious motivations.."

scenario = "Her office, in the Public Safety building. . . <Start> \n"

chat = "{{char}}: *you enter her office, she looks at you*\n\n\"Who are you?\"\n{{user}}:"

prompt = character_builder(name=name,description=description, scenario=scenario, chat=chat)



while True:
    query = input("enter:")
    
    final = "\n{{char}}:"

    response = Rikav2(query=prompt + query + final)
    
    print(response)