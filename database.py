users = set()

def add_user(user_id):
    users.add(user_id)

def get_users():
    return list(users)
