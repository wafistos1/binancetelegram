from xmlrpc.client import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('mysql+pymysql://wafi:djamel2013@localhost:3306/Telegram')#, echo=True)

# engine = create_engine("sqlite://", echo=True, future=True)
#Class of final users
class FixedUsdAmount(Base):
    __tablename__= 'fixed_usd_amount'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))


class Percentage(Base):
    __tablename__= 'percentage'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))


class AmountTrade(Base):
    __tablename__= 'amount_per_trade'
    id = Column(Integer, primary_key=True)
    percentage_id = Column(Integer, ForeignKey('percentage.id'), nullable=False)
    fixed_usd_amount_id = Column(Integer, ForeignKey('fixed_usd_amount.id'))


class FristEntry(Base):
    __tablename__ = 'first_entry_grace_percentage'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)


class EntryStrategy(Base):
    __tablename__ = 'entry_strategy'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

class TakeProfitStrategy(Base):
    __tablename__ = 'take_profit_strategry'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

class CloseTradeOnTakeProfit(Base):
    __tablename__ = 'close_trade_on_take_profit'
    id = Column(Integer, primary_key=True)
    onoff = Column(Boolean)

class BlacklistSymbols(Base):
    __tablename__ = 'blacklist_symbols'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

class MaxTrades(Base):
    __tablename__ = 'max_trades'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

class StopLossTimeout(Base):
    __tablename__ = 'stop_loss_timeout'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

class DefaultStopLoss(Base):
    __tablename__ = 'default_stop_loss'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    
class Owner(Base):
    __tablename__ = 'owner'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    bot_token =  Column(String(200))


# Class of final users
class Users(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    owner_id =  Column(Integer, ForeignKey("owner.id"), nullable=False)


# Class binance
class Binance(Base):
    __tablename__ = 'binance'
    
    id = Column(Integer, primary_key=True)
    api_key = Column(String(300))
    api_secrect = Column(String(300))
    symbol = Column(String(300))
    total_last_day = Column(String(50))
    total_last_month = Column(String(50))
    

class Strategy_user(Base):
    __tablename__ = 'strategy_user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    take_profit = Column(Boolean)
    first_entry_grace_id = Column(Integer, ForeignKey('first_entry_grace_percentage.id'), nullable=False)
    entry_strategy_id = Column(Integer, ForeignKey('entry_strategy.id'), nullable=False)
    number_target_id = Column(Integer, ForeignKey('number_target.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)


class Strategy_owner(Base):
    __tablename__ = 'strategy_owner'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    take_profit = Column(Boolean)
    first_entry_grace_id = Column(Integer, ForeignKey('first_entry_grace_percentage.id'), nullable=False)
    entry_strategy_id = Column(Integer, ForeignKey('entry_strategy.id'), nullable=False)
    number_target_id = Column(Integer, ForeignKey('number_target.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

# # session = Session(engine)
# session.commit()
def main():
    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     # percentage_1 = Percentage(number='1',)
    #     # percentage_2 = Percentage(number='2',)
    #     # percentage_3 = Percentage(number='5',)
    #     # percentage_4 = Percentage(number='10',)
    #     # percentage_5 = Percentage(number='15',)
    #     # percentage_6 = Percentage(number='20',)
    #     # percentage_7 = Percentage(number='25',)
    #     # percentage_8 = Percentage(number='30',)
    #     # percentage_9 = Percentage(number='40',)
        
    #     percentage_1 = FixedUsdAmount(number='20',)
    #     percentage_2 = FixedUsdAmount(number='50',)
    #     percentage_3 = FixedUsdAmount(number='100',)
    #     percentage_4 = FixedUsdAmount(number='500',)
    #     percentage_5 = FixedUsdAmount(number='1000',)
    #     percentage_6 = FixedUsdAmount(number='2000',)
    #     percentage_7 = FixedUsdAmount(number='5000',)
    #     percentage_8 = FixedUsdAmount(number='10000',)
        
    #     session.add_all([
    #         percentage_1,
    #         percentage_2,
    #         percentage_3,
    #         percentage_4,
    #         percentage_5,
    #         percentage_6,
    #         percentage_7,
    #         percentage_8,
    #         ])
    #     # session.add_all([owner])
    #     session.commit()
        
def select_table(tablename):
    session = Session(engine)
    search_owner = select(tablename)
    try:
        return [owner.number for owner in session.scalars(search_owner)]
    except:
        return [owner.name for owner in session.scalars(search_owner)]
        
    
if __name__ in '__main__':
    main()
    # toto = select_table(FixedUsdAmount)
    # print(toto)
# class User(Base):
#     __tablename__ = "user_account"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     fullname = Column(String(200))
#     addresses = relationship(
#         "Address", back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self):
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
# class Address(Base):
#     __tablename__ = "address"
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String(200), nullable=False)
#     user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
#     user = relationship("User", back_populates="addresses")
#     def __repr__(self):
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
# Base.metadata.create_all(engine)
# from sqlalchemy.orm import Session

# with Session(engine) as session:
#     spongebob = User(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#     )
#     sandy = User(
#         name="sandy",
#         fullname="Sandy Cheeks",
#         addresses=[
#             Address(email_address="sandy@sqlalchemy.org"),
#             Address(email_address="sandy@squirrelpower.org"),
#         ],
#     )
#     patrick = User(name="patrick", fullname="Patrick Star")
#     session.add_all([spongebob, sandy, patrick])
#     session.commit()
