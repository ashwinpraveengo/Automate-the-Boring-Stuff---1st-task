import re

def is_strong_password(pw):
    if len(pw) < 8: return False
    if not re.search(r'[A-Z]', pw): 
        return False
    if not re.search(r'[a-z]', pw): 
        return False
    if not re.search(r'\d', pw): 
        return False
    return True

print(is_strong_password('Str0ngPass')) 
print(is_strong_password('weakpass'))  
