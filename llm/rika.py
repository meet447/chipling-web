import os, time
from hugchat_api import HuggingChat
from config import hf_key, token, email

EMAIL = email

# create ThreadPool

cookies = {"hf-chat": hf_key, "token": token}

def Rika(query):
        
    print(query)
    
    HUG = HuggingChat(max_thread=1) 
    
    print('1')      

    bot = HUG.getBot(email=EMAIL, cookies=cookies)
    
    print('2')

    conversation_id = bot.createConversation()
    
    print('3')

    conversations = bot.getConversations()
    
    print('4')

    conv_id = list(conversations.keys())[0]
    
    print(conversations)

    message = bot.chat(
        text=query,
        conversation_id=conversation_id,
        web_search=False,
        max_tries=2,
    )
    # wait the full text or...
    while not message.web_search_done:
        time.sleep(0.1)
    print("webstep done!")
    while not message.isDone():
        time.sleep(0.1)
    respone = message.getFinalText()

    bot.removeConversation(conversation_id=conv_id)

    print("conversation removed")
    
    return respone

###### rikav1  hugging face base mdoel requires hf#######################