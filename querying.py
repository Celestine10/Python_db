import imp
from main import User,Session,engine

local_session = Session(bind=engine)

#return all objects
#users = local_session.query(User).all()[:3]

#for user in users:
 #   print(user.userName)
 
#queryfor one user
jane = local_session.query(User).filter(User.userName=="Janezeen").first()
print(jane)
 