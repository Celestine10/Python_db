from main import User,Session,engine

local_session = Session(bind=engine)

"""The followng lines below were used to populate the database"""
#user_to_update = local_session.query(User).filter(User.userName=="Alfred").first()
#user_to_update = local_session.query(User).filter(User.userName=="Jerry").first()
user_to_update = local_session.query(User).filter(User.userName=="Jordan").first()
#user_to_update = local_session.query(User).filter(User.userName=="joelington@yahoo.com").first()
#user_to_update = local_session.query(User).filter(User.userName=="Jesse").first()
#user_to_update = local_session.query(User).filter(User.userName=="Joan").first()
#user_to_update = local_session.query(User).filter(User.userName=="Jane Hause").first()
#user_to_update = local_session.query(User).filter(User.userName=="Jaden").first()
	
#user_to_update.userName = "Alfred Rewane"
#user_to_update.email ="alfredrewane@gmail.com"
#user_to_update.userName = "Martha Joelington"
#user_to_update.email = "joelington@yahoo.com"
#user_to_update.userName = "Jaden Sancho"
#user_to_update.email = "jaden@gmail.com"
#user_to_update.userName = "Jerry White"
#user_to_update.email = "jerry@gmail.com"
user_to_update.userName = "Jordan Hause"
user_to_update.email ="jordan@gmail.com" 

#user_to_update.userName = "Jesse Jaggs"
#user_to_update.email ="jesse@yahoo.com"
#user_to_update.userName = "Joan Laporta"
#user_to_update.email ="joan@hotmail.com"
#user_to_update.userName = "Jane Elozino"
#user_to_update.email ="janezeen@hotmail.com"


local_session.commit()
print("Updated")