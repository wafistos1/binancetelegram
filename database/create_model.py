from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import registry
from sqlalchemy import update
from sqlalchemy import insert


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


class FristEntryGracePercentage(Base):
    __tablename__ = 'first_entry_grace_percentage'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))


class EntryStrategy(Base):
    __tablename__ = 'entry_strategy'
    id = Column(Integer, primary_key=True)
    number = Column(String(30))

class TakeProfitStrategy(Base):
    __tablename__ = 'take_profit_strategry'
    id = Column(Integer, primary_key=True)
    number = Column(String(30))

class CloseTradeOnTakeProfit(Base):
    __tablename__ = 'close_trade_on_take_profit'
    id = Column(Integer, primary_key=True)
    onoff = Column(Boolean)

class BlacklistSymbols(Base):
    __tablename__ = 'blacklist_symbols'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))

class MaxTrades(Base):
    __tablename__ = 'max_trades'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))

class StopLossTimeout(Base):
    __tablename__ = 'stop_loss_timeout'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))

class DefaultStopLoss(Base):
    __tablename__ = 'default_stop_loss'
    id = Column(Integer, primary_key=True)
    number = Column(String(50))


# DATA with ForeignKey

class AmountTrade(Base):
    __tablename__= 'amount_per_trade'
    id = Column(Integer, primary_key=True)
    percentage_id = Column(Integer, ForeignKey('percentage.id'), nullable=False)
    fixed_usd_amount_id = Column(Integer, ForeignKey('fixed_usd_amount.id'), nullable=False)





   
class Owner(Base):
    __tablename__ = 'owner'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    bot_token =  Column(String(200))
    expire_time = Column(DateTime)
    auto_trading = Column(Boolean, default=False)
    entry_date = Column(DateTime, nullable=False)
    # strategy_id = Column(Integer, ForeignKey('strategy_owner.id'), nullable=False)
    is_warn = Column(Boolean, default=False)


# Class of final users
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(200))
    owner_id =  Column(Integer, ForeignKey("owner.id"), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    auto_trading = Column(Boolean, default=False)
    # strategy_id = Column(Integer, ForeignKey('strategy_user.id'), nullable=False)
    binance_id = Column(Integer, ForeignKey('binance.id'), nullable=False)
   

class StrategyUser(Base):
    __tablename__ = 'strategy_user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    take_profit = Column(Boolean)
    first_entry_grace_id = Column(Integer, ForeignKey('first_entry_grace_percentage.id'), nullable=False)
    entry_strategy_id = Column(Integer, ForeignKey('entry_strategy.id'), nullable=False)
    # number_target_id = Column(Integer, ForeignKey('number_target.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class StrategyOwner(Base):
    __tablename__ = 'strategy_owner'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    take_profit = Column(Boolean)
    first_entry_grace_id = Column(Integer, ForeignKey('first_entry_grace_percentage.id'), nullable=False)
    entry_strategy_id = Column(Integer, ForeignKey('entry_strategy.id'), nullable=False)
    # number_target_id = Column(Integer, ForeignKey('number_target.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)



# Class binance
class Binance(Base):
    __tablename__ = 'binance'
    
    id = Column(Integer, primary_key=True)
    api_key = Column(String(300))
    api_secrect = Column(String(300))
    symbol = Column(String(300))
    total_last_day = Column(String(50))
    total_last_month = Column(String(50))
    

# mapper_registry = registry()



# mapper_registry.map_imperatively(User, StrategyUser)
# mapper_registry.map_imperatively(Owner, StrategyOwner)

# # session = Session(engine)
# session.commit()
def main():
    Base.metadata.create_all(engine)
    # with Session(engine) as session:
    #     per_10 = Percentage(number='None',)
    #     per_1 = Percentage(number='1',)
    #     per_2 = Percentage(number='2',)
    #     per_3 = Percentage(number='5',)
    #     per_4 = Percentage(number='10',)
    #     per_5 = Percentage(number='15',)
    #     per_6 = Percentage(number='20',)
    #     per_7 = Percentage(number='25',)
    #     per_8 = Percentage(number='30',)
    #     per_9 = Percentage(number='40',)
        
    #     dsl1 = DefaultStopLoss(number='Without')
    #     dsl2 = DefaultStopLoss(number='1')
    #     dsl3 = DefaultStopLoss(number='2')
    #     dsl4 = DefaultStopLoss(number='3')
    #     dsl5 = DefaultStopLoss(number='4')
    #     dsl6 = DefaultStopLoss(number='5')
    #     dsl7 = DefaultStopLoss(number='6')
    #     dsl8 = DefaultStopLoss(number='7.5')
    #     dsl9 = DefaultStopLoss(number='10')
    #     dsl10 = DefaultStopLoss(number='15')
        
    #     es1 = EntryStrategy(number='Disable')
    #     es2 = EntryStrategy(number='One Target')
    #     es3 = EntryStrategy(number='Two Targets')
    #     es4 = EntryStrategy(number='Three Targets')
    #     es5 = EntryStrategy(number='Fifty On First Traget')
    #     es6 = EntryStrategy(number='Skip First')
        
         
    #     tps1 = TakeProfitStrategy(number='Disable')
    #     tps2 = TakeProfitStrategy(number='One Target')
    #     tps3 = TakeProfitStrategy(number='Two Targets')
    #     tps4 = TakeProfitStrategy(number='Three Targets')
    #     tps5 = TakeProfitStrategy(number='Fifty On First Traget')
    #     tps6 = TakeProfitStrategy(number='Skip First')
        
    #     fegp1 = FristEntryGracePercentage(number='Disable')
    #     fegp2 = FristEntryGracePercentage(number='0.4')
    #     fegp3 = FristEntryGracePercentage(number='0.8')
    #     fegp4 = FristEntryGracePercentage(number='1.2')
    #     fegp5 = FristEntryGracePercentage(number='1.6')
    #     fegp6 = FristEntryGracePercentage(number='2.0')
    #     fegp7 = FristEntryGracePercentage(number='2.4')
    #     fegp8 = FristEntryGracePercentage(number='2.8')
    #     fegp9 = FristEntryGracePercentage(number='3.2')
    #     fegp10 = FristEntryGracePercentage(number='3.6')
    #     fegp11 = FristEntryGracePercentage(number='4.0')
    #     fua1 = FixedUsdAmount(number='None')
    #     fua2 = FixedUsdAmount(number='20')
    #     fua3 = FixedUsdAmount(number='50')
    #     fua4 = FixedUsdAmount(number='100')
    #     fua5 = FixedUsdAmount(number='500')
    #     fua6 = FixedUsdAmount(number='1000')
    #     fua7 = FixedUsdAmount(number='2000')
    #     fua8 = FixedUsdAmount(number='5000')
    #     fua9 = FixedUsdAmount(number='10000')
    #     slt1 = StopLossTimeout(number='Without')
    #     slt2 = StopLossTimeout(number='1 minute')
    #     slt3 = StopLossTimeout(number='5 minute')
    #     slt4 = StopLossTimeout(number='1 hour')
    #     slt5 = StopLossTimeout(number='4 hours')

    #     session.add_all([
    #         per_10,
    #         per_1,
    #         per_2,
    #         per_3,
    #         per_4,
    #         per_5,
    #         per_6,
    #         per_7,
    #         per_8,
    #         per_9,
    #         dsl1,
    #         dsl2,
    #         dsl3,
    #         dsl4,
    #         dsl5,
    #         dsl6,
    #         dsl7,
    #         dsl8,
    #         dsl9,
    #         dsl10,
    #         es1,
    #         es2,
    #         es3,
    #         es4,
    #         es5,
    #         es6,
            
    #         fegp1,
    #         fegp2,
    #         fegp3,
    #         fegp4,
    #         fegp5,
    #         fegp6,
    #         fegp7,
    #         fegp8,
    #         fegp9,
    #         fegp10,
    #         fegp11,
    #         fua1,
    #         fua2,
    #         fua3,
    #         fua4,
    #         fua5,
    #         fua6,
    #         fua7,
    #         fua8,
    #         fua9,
    #         slt1,
    #         slt2,
    #         slt3,
    #         slt4,
    #         slt5,
    #         tps1,
    #         tps2,
    #         tps3,
    #         tps4,
    #         tps5,
    #         tps6,

    #         ])
    #     # session.add_all([owner])
    #     session.commit()
        
def select_table(tablename):
    session = Session(engine)
    search_table = select(tablename)
    return [owner.number for owner in session.scalars(search_table)]

def select_user(user_tablename, id):
    session = Session(engine)
    search_user = select([user_tablename.channel_id, user_tablename.id, user_tablename.bot_token]).where(user_tablename.channel_id==id)
    return [t for t in session.scalars(search_user)]
    
def select_status_auto_trading(user_tablename, id):
    session = Session(engine)
    search_user = select(user_tablename.auto_trading).where(user_tablename.channel_id==id)
    resultat = session.execute(search_user).first()
    # print('REsultat', resultat.auto_trading)
    return resultat.auto_trading

def update_auto_trading(user_tablename, value, id):
    session = Session(engine)
    x = session.query(user_tablename).get(id)
    # print('X: ', x.auto_trading)
    # session.query(user_tablename).filter(user_tablename.id = 2).update(user_tablename).where(user_tablename.id == 2).values(name=value)
    x.auto_trading = value
    session.commit()
        
if __name__ in '__main__':
    # main()
    user = select_status_auto_trading(Owner, '123' )
    print(user)
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
