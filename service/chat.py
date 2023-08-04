import json
import uuid

def create_chat(user, name, short_desc, long_desc, alias, origin, id):
    
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

def load_chats():
    posts = []
    with open('data.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
            
        return posts            
    

def get_chat(id):
    
    results = []
    
    data = load_chats()
    for post in data:
        if post['id'] == id:
             results.append(post)
             
    return results