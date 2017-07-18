from main.models.user import User
from main.database import db

def new_user():
    user = User(username='flask')
    user.hash_password('ssan')
    db.session.add(user)
    db.session.commit()
    return True
