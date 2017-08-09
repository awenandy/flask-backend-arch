from main.models.user import User
from main.database import db

def new_user():
    username = 'flask'
    password = 'ssan'
    query_all = db.session.query(User).filter(User.username == username).all()
    if not query_all:
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
    return True
