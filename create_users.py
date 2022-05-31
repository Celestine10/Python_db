import email
from locale import locale_alias
from main import User,Session,engine


"""{
        "userName": "Jerry Ole",
         "email": "jerry@gmail.com"
    },  {
        "userName": "Jordan Amavi",
         "email": "jordan@gmail.com"     
    },  {
        "userName": "Jaden Enke",
         "email": "jaden@gmail.com"
    },  {
         "userName": "Joel Jones",
         "email": "joel@gmail.com"
    },  {     
         "userName": "Jesse Marsch",
         "email": "jesse@yahoo.com"
    },  {     
         "userName": "Joan Onyi",
         "email": "joan@hotmail.com"
         
    },  {     
         "userName": "Janezeen Elozi",
         "email": "janezeen@hotmail.com"
         
    }, {     
         "userName": "Michael Donaldson",
         "email": "mdonaldson@hotmail.com"
         
     },  {     
         "userName": "Mikel Jose",
         "email": "josem@gmail.com"
         
    },  {     
         "userName": "Teresa Mendoza",
         "email": "teresa@outlook.com"
         
}
    """  
users = [   
         {     
         "userName": "Steve Naismith",
         "email": "steve@outlook.com"
         
},  {     
         "userName": "Olusola Falaye",
         "email": "folusola@gmail.com"
         
          },  {     
         "userName": "Audu Garba",
         "email": "audugarba@yahoo.com"
         
          },  {     
         "userName": "Chukwu Chinenye",
         "email": "chukwuc@gmail.com"
         
          },  {     
         "userName": "Uche Diokpa",
         "email": "ucdiokpa@ootlook.com"
         
          },  {     
         "userName": "Imeh Briggs",
         "email": "briggs@gmail.com"
}]

local_session = Session(bind=engine)

"""new_user=User(userName="Alfred",email="alfredrewane@gmail.com")

local_session.add(new_user)

local_session.commit()"""

for person in users:
    new_user=User(userName=person["userName"],email=person["email"])
    
    local_session.add(new_user)
    local_session.commit()
    print(f"Added {person['userName']}")