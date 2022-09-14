from pony import orm
from datetime import datetime
from pony.orm import *


db = orm.Database()
# MySQL
db.bind(provider='mysql', host='localhost', user='wafi', passwd='djamel2013', db='Telegram')




class Fixed_usd_amount(db.Entity):
    number = orm.Required(str)
    amount_trade = orm.Set('Amount_trade')

class Percentage(db.Entity):
    number = orm.Required(str)
    amount_trade = orm.Set('Amount_trade')
  
class First_entry_grace_percentage(db.Entity):
    number = orm.Required(str)
    strategy_user = orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    
class Entry_strategy(db.Entity):
    number = orm.Required(str)
    strategy_user = orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    # owners = orm.Set("Owner", reverse='entry_strategys')

class Take_profit_strategy(db.Entity):
    number = orm.Required(str)
    strategy_user = orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    
class Close_trade_on_take_profit(db.Entity):
    number = orm.Required(str)

class Blacklist_symbols(db.Entity):
    number = orm.Required(str)


class Max_trades(db.Entity):
    number = orm.Required(str)

class Stop_loss_timeout(db.Entity):
    number = orm.Required(str)

class Default_stop_loss(db.Entity):
    number = orm.Required(str)
    
    
class Amount_trade(db.Entity):
    percentage = orm.Optional(Percentage)
    fixed_usd_amount = orm.Optional(Fixed_usd_amount)
    


class Binance(db.Entity):
    api_key = orm.Required(str)
    api_secret = orm.Required(str)
    symbol = orm.Optional(str)
    total_last_day = orm.Optional(str)
    total_last_month = orm.Optional(str)
    users = orm.Optional('User')
    


class User(db.Entity):
    channel_id = orm.Required(str)
    first_name = orm.Required(str)
    last_name = orm.Required(str)
    auto_trading = orm.Optional(bool, default=False)
    # strategy_id = Column(Integer, ForeignKey('strategy_user.id'), nullable=False)
    binance = orm.Set(Binance)
    owner =  orm.Required('Owner')
    strategy = orm.Set('Strategy_user')




class Owner(db.Entity):

    channel_id = orm.Required(str)
    bot_token =  orm.Required(str)
    auto_trading = orm.Optional(str)
    expire_time = orm.Required(datetime)
    entry_date = orm.Required(datetime)
    # strategy_id = Column(Integer, ForeignKey('strategy_owner.id'), nullable=False)
    is_warn = orm.Optional(bool, default=False)
    user = orm.Optional(User)
    auto_trading = orm.Optional(bool, default=False)
    strategy = orm.Set('Strategy_owner')


class Strategy_user(db.Entity):
    name = orm.Required(str)
    take_profit = orm.Optional(Take_profit_strategy)
    first_entry_grace = orm.Optional(First_entry_grace_percentage)
    entry_strategy = orm.Optional(Entry_strategy)
    user = orm.Required(User)

class Strategy_owner(db.Entity):
    name = orm.Required(str)
    take_profit = orm.Optional(Take_profit_strategy)
    first_entry_grace = orm.Optional(First_entry_grace_percentage)
    entry_strategy = orm.Optional(Entry_strategy)
    owner = orm.Required(Owner)
    

db.generate_mapping(create_tables=True)
# with orm.db_session:
#     # owner = Owner(channel_id='1233', bot_token='bot_token', entry_date= '2018-12-19 09:26:03.478039', expire_time='2018-12-19 09:26:03.478039',  auto_trading=0)
#     # user = User(channel_id='12342', first_name='Wafi', last_name='mameri', auto_trading=0, owner=2)
#     # binance = Binance(api_key='api_key', api_secret='api_secret', symbol='Dinars', total_last_day= '1234', total_last_month= '1234', users=3)
#         per_10 = Percentage(number='None',)
#         per_1 = Percentage(number='1',)
#         per_2 = Percentage(number='2',)
#         per_3 = Percentage(number='5',)
#         per_4 = Percentage(number='10',)
#         per_5 = Percentage(number='15',)
#         per_6 = Percentage(number='20',)
#         per_7 = Percentage(number='25',)
#         per_8 = Percentage(number='30',)
#         per_9 = Percentage(number='40',)
        
#         dsl1 = Default_stop_loss(number='Without')
#         dsl2 = Default_stop_loss(number='1')
#         dsl3 = Default_stop_loss(number='2')
#         dsl4 = Default_stop_loss(number='3')
#         dsl5 = Default_stop_loss(number='4')
#         dsl6 = Default_stop_loss(number='5')
#         dsl7 = Default_stop_loss(number='6')
#         dsl8 = Default_stop_loss(number='7.5')
#         dsl9 = Default_stop_loss(number='10')
#         dsl10 = Default_stop_loss(number='15')
        
#         es1 = Entry_strategy(number='Disable')
#         es2 = Entry_strategy(number='One Target')
#         es3 = Entry_strategy(number='Two Targets')
#         es4 = Entry_strategy(number='Three Targets')
#         es5 = Entry_strategy(number='Fifty On First Traget')
#         es6 = Entry_strategy(number='Skip First')
        
         
#         tps1 = Take_profit_strategy(number='Disable')
#         tps2 = Take_profit_strategy(number='One Target')
#         tps3 = Take_profit_strategy(number='Two Targets')
#         tps4 = Take_profit_strategy(number='Three Targets')
#         tps5 = Take_profit_strategy(number='Fifty On First Traget')
#         tps6 = Take_profit_strategy(number='Skip First')
        
#         fegp1 = First_entry_grace_percentage(number='Disable')
#         fegp2 = First_entry_grace_percentage(number='0.4')
#         fegp3 = First_entry_grace_percentage(number='0.8')
#         fegp4 = First_entry_grace_percentage(number='1.2')
#         fegp5 = First_entry_grace_percentage(number='1.6')
#         fegp6 = First_entry_grace_percentage(number='2.0')
#         fegp7 = First_entry_grace_percentage(number='2.4')
#         fegp8 = First_entry_grace_percentage(number='2.8')
#         fegp9 = First_entry_grace_percentage(number='3.2')
#         fegp10 = First_entry_grace_percentage(number='3.6')
#         fegp11 = First_entry_grace_percentage(number='4.0')
        
#         fua1 = Fixed_usd_amount(number='None')
#         fua2 = Fixed_usd_amount(number='20')
#         fua3 = Fixed_usd_amount(number='50')
#         fua4 = Fixed_usd_amount(number='100')
#         fua5 = Fixed_usd_amount(number='500')
#         fua6 = Fixed_usd_amount(number='1000')
#         fua7 = Fixed_usd_amount(number='2000')
#         fua8 = Fixed_usd_amount(number='5000')
#         fua9 = Fixed_usd_amount(number='10000')
#         slt1 = Stop_loss_timeout(number='Without')
#         slt2 = Stop_loss_timeout(number='1 minute')
#         slt3 = Stop_loss_timeout(number='5 minute')
#         slt4 = Stop_loss_timeout(number='1 hour')
# 
# slt5 = Stop_loss_timeout(number='4 hours')
@db_session
def return_auto_trading(id, change=None):
    toto = orm.select(p for p in User if p.id==id).first()
    if change=='True':
        toto.set(auto_trading=1)
        return 'On'
    elif change == 'False':
        toto.set(auto_trading=0)
        return 'Off'
    return(toto.auto_trading)

@db_session
def check_user(id, owner_id):
    # owner = orm.select(p for p in Owner if p.id==owner_id ).first()
    user = orm.select(p for p in User if (p.id == id and p.owner.id==owner_id) ).first()
    # print(user.auto_trading, type(user.auto_trading))
    status = 'Off'
    if user.auto_trading==True:
        status = 'On'
    return(user.first_name, status)


@db_session
def return_table_value(table):
    result = list(orm.select(p.number for p in table))
    return result

@db_session
def return_owner_strat(stat_name, owner_id, user_id):
    result = orm.select(p for p in Strategy_owner if p.name==stat_name).first()
    return {
        'name': result.name,
        'take_profit': result.take_profit.number,
        'first_entry_grace': result.first_entry_grace.number,
        'entry_strategy': result.entry_strategy.number,
    }
    
@db_session  
def return_owner_strat_id(stat_name, owner_id, user_id):
    result = orm.select(p for p in Strategy_owner if p.name==stat_name).first()
    return {
        'name': (result.name, result.name),
        'take_profit': (result.take_profit.id, result.take_profit.number),
        'first_entry_grace': (result.first_entry_grace.id, result.first_entry_grace.number),
        'entry_strategy': (result.entry_strategy.id, result.entry_strategy.number),
    }

@db_session
def list_owner_strat(table, user_id, owner_id):
    return list(orm.select(p.name for p in table))

@db_session
def copy_strategy(name,
                  take_profit,
                  first_entry_grace,
                  entry_strategy,
                  user_id,
                  ):
    
    strategy =  Strategy_user(
        name=name,
        take_profit=take_profit,
        first_entry_grace=first_entry_grace,
        entry_strategy=entry_strategy,
        user=user_id,
        )

if __name__=='__main__':  
    print(return_owner_strat_id('owner_strategy1', 3, 2))