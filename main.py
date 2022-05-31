from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')

engine = create_engine(connection_string,echo=True)

Session = sessionmaker()

Base = declarative_base()
""""
class User
    id int
    username str
    email str
    date_created datetime
        
"""
  
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True)
    userName = Column(String(20), nullable=False,unique=True)
    email = Column(String(), unique=True, nullable = False)
    date_created = Column(DateTime(),default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User userName={self.userName} email={self.email}>"
    
new_user = User(id=1, userName="Alfred",email="alfred@gmail.com")
print(new_user)
    
    