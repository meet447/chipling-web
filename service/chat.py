import json
import uuid

def create_chat(user, name, short_desc, long_desc, alias, origin):
    
    uui = uuid.uuid1()
    
    id = uui.hex
    
    with open("data.json", "a") as file:  # Use "a" mode to append to the file
        post = {
            'user': user,
            'name': name,
            'short_desc': short_desc,
            'long_desc': long_desc,
            'alias': alias,
            'origin': origin,
            'id': id
        }
        
        json.dump(post, file)
        file.write('\n')

create_chat(user="ee", name="ss", short_desc="clear", long_desc="eeeee", alias="ee", origin="ee")

def load_chats():
    posts = []
    with open('data.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
            
        return posts            
         