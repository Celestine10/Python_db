from main import User,Session,engine
from sqlalchemy import asc, desc

local_session = Session(bind=engine)

#Ascending Order
users_asc=local_session.query(User).order_by(asc(User.userName)).all()

for user in users_asc:
    print(f"User {user.userName}")
    
print()
#Descending Order
users_dsc=local_session.query(User).order_by(desc(User.userName)).all()

for user in users_dsc:
    print(f"User {user.userName}")
        