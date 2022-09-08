from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine

Base = declarative_base()

# engine ='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
#     user='wafi',
#     password='123',
#     server='localhost',
#     database='Telegram'
#     )

engine = create_engine("sqlite://", echo=True, future=True)
# Class of final users
class Owner(Base):
    __tablename__ = 'owner_telegram'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    bot_token =  Column(String(200))

# Class of final users
class Users(Base):
    __tablename__ = 'user_telegram'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    owner_id =  Column(Integer, ForeignKey("owner_telegram.id"), nullable=False)

# engine ='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
#     user='wafi',
#     password='123',
#     server='localhost',
#     database='Telegram'
#     )
# # session = Session(engine)
# session.commit()
Base.metadata.create_all(engine)