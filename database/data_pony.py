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
    strategy_Users= orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    
class Entry_strategy(db.Entity):
    number = orm.Required(str)
    strategy_Users= orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    # owners = orm.Set("Owner", reverse='entry_strategys')

class Take_profit_strategy(db.Entity):
    number = orm.Required(str)
    strategy_Users= orm.Set('Strategy_user')
    strategy_owner = orm.Set('Strategy_owner')
    
class Close_trade_on_take_profit(db.Entity):
    number = orm.Required(str)
    strategy_Users= orm.Set('Strategy_user')

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
    Memberships = orm.Set('Strategy_owner')
    Users= orm.Set('Strategy_user')
    


class Binance(db.Entity):
    api_key = orm.Required(str)
    api_secret = orm.Required(str)
    symbol = orm.Optional(str)
    total_last_day = orm.Optional(str)
    total_last_month = orm.Optional(str)
    users = orm.Optional('Users')
    


class Users(db.Entity):
    username = orm.Optional(str)
    first_name = orm.Optional(str)
    last_name = orm.Optional(str)
    bot_token = orm.Optional(str)
    auto_trading = orm.Optional(bool, default=False)
    # strategy_id = Column(Integer, ForeignKey('strategy_user.id'), nullable=False)
    binance = orm.Optional(Binance)
    # Memberships =  orm.Required('Memberships')
    strategy = orm.Set('Strategy_user')




class Memberships(db.Entity):
    user_id = orm.Optional(str)
    expire_time = orm.Required(datetime)
    bot_token =  orm.Required(str, unique=True)
    is_warn = orm.Optional(bool, default=False)
    username = orm.Optional(str)
    entry_date = orm.Required(datetime)
    channel_username = orm.Required(str)
    
    # users = orm.Set(Users)
    auto_trading = orm.Optional(bool, default=False)
    strategy = orm.Set('Strategy_owner')



class Strategy_user(db.Entity):
    name = orm.Required(str)
    take_profit = orm.Optional(Take_profit_strategy)
    first_entry_grace = orm.Optional(First_entry_grace_percentage)
    entry_strategy = orm.Optional(Entry_strategy)
    close_trade_on_take_profit =  orm.Optional(Close_trade_on_take_profit)
    amount_per_trade = orm.Optional(Amount_trade)
    users= orm.Required(Users)


class Strategy_owner(db.Entity):
    name = orm.Required(str)
    take_profit = orm.Optional(Take_profit_strategy)
    first_entry_grace = orm.Optional(First_entry_grace_percentage, default=1)
    entry_strategy = orm.Optional(Entry_strategy)
    amount_per_trade = orm.Optional(Amount_trade)
    Memberships = orm.Required(Memberships)
    
    

db.generate_mapping(create_tables=True)
# with orm.db_session:
#     owner = Memberships(
#         channel_username='Channel_test_bot_telegram_username',
#         bot_token='bot_token_channel1',
#         entry_date= '2018-12-19 09:26:03.478039',
#         expire_time='2018-12-19 09:26:03.478039',
#         is_warn=1,
#         auto_trading=0,
#         username='Owner1'
#         )
#     # # print(owner)
#     user= Users(
#         username='username_user',
#         first_name='Wafi',
#         last_name='mameri',
#         auto_trading=0,
#         bot_token=owner.bot_token,
#         )
#     binance = Binance(
#         api_key='api_key_binance_test',
#         api_secret='api_secret_binance_test',
#         symbol='Dinars',
#         total_last_day= '1234',
#         total_last_month= '1234',
#         users=user)


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
    
#     dsl1 = Default_stop_loss(number='Without')
#     dsl2 = Default_stop_loss(number='1')
#     dsl3 = Default_stop_loss(number='2')
#     dsl4 = Default_stop_loss(number='3')
#     dsl5 = Default_stop_loss(number='4')
#     dsl6 = Default_stop_loss(number='5')
#     dsl7 = Default_stop_loss(number='6')
#     dsl8 = Default_stop_loss(number='7.5')
#     dsl9 = Default_stop_loss(number='10')
#     dsl10 = Default_stop_loss(number='15')
    
#     es1 = Entry_strategy(number='Disable')
#     es2 = Entry_strategy(number='One Target')
#     es3 = Entry_strategy(number='Two Targets')
#     es4 = Entry_strategy(number='Three Targets')
#     es5 = Entry_strategy(number='Fifty On First Traget')
#     es6 = Entry_strategy(number='Skip First')
    
        
#     tps1 = Take_profit_strategy(number='Disable')
#     tps2 = Take_profit_strategy(number='One Target')
#     tps3 = Take_profit_strategy(number='Two Targets')
#     tps4 = Take_profit_strategy(number='Three Targets')
#     tps5 = Take_profit_strategy(number='Fifty On First Traget')
#     tps6 = Take_profit_strategy(number='Skip First')
    
#     fegp1 = First_entry_grace_percentage(number='Disable')
#     fegp2 = First_entry_grace_percentage(number='0.4')
#     fegp3 = First_entry_grace_percentage(number='0.8')
#     fegp4 = First_entry_grace_percentage(number='1.2')
#     fegp5 = First_entry_grace_percentage(number='1.6')
#     fegp6 = First_entry_grace_percentage(number='2.0')
#     fegp7 = First_entry_grace_percentage(number='2.4')
#     fegp8 = First_entry_grace_percentage(number='2.8')
#     fegp9 = First_entry_grace_percentage(number='3.2')
#     fegp10 = First_entry_grace_percentage(number='3.6')
#     fegp11 = First_entry_grace_percentage(number='4.0')
    
#     fua1 = Fixed_usd_amount(number='None')
#     fua2 = Fixed_usd_amount(number='20')
#     fua3 = Fixed_usd_amount(number='50')
#     fua4 = Fixed_usd_amount(number='100')
#     fua5 = Fixed_usd_amount(number='500')
#     fua6 = Fixed_usd_amount(number='1000')
#     fua7 = Fixed_usd_amount(number='2000')
#     fua8 = Fixed_usd_amount(number='5000')
#     fua9 = Fixed_usd_amount(number='10000')
#     slt1 = Stop_loss_timeout(number='Without')
#     slt2 = Stop_loss_timeout(number='1 minute')
#     slt3 = Stop_loss_timeout(number='5 minute')
#     slt4 = Stop_loss_timeout(number='1 hour')

#     ctotp1 = Close_trade_on_take_profit(number='On')
#     ctotp2 = Close_trade_on_take_profit(number='Off')

#     slt5 = Stop_loss_timeout(number='4 hours')
#     ampt = Amount_trade(percentage=per_4, fixed_usd_amount=fua3)
        
@db_session
def return_auto_trading(user_id, change=None):
    toto = orm.select(p for p in Users if p.id==user_id).first()
    if change=='True':
        toto.set(auto_trading=1)
        return 'On'
    elif change == 'False':
        toto.set(auto_trading=0)
        return 'Off'
    return(toto.auto_trading)


@db_session
def check_user(id, owner_id):
    owner = orm.select(p for p in Memberships if p.id==owner_id ).first()
    user= orm.select(p for p in Users if (p.id == id and p.bot_token == owner.bot_token)).first()
    
    # print(user.auto_trading, type(user.auto_trading))
    status = 'Off'
    try:
        if user.auto_trading==True:
            status = 'On'
        return(user.first_name, status)
    except:
        return '' , ''


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
    percentage = result.amount_per_trade.percentage
    fixed_usd_amount = result.amount_per_trade.fixed_usd_amount
    return {
        'name': (result.name, result.name),
        'take_profit': (result.take_profit.id, result.take_profit.number),
        'first_entry_grace': (result.first_entry_grace.id, result.first_entry_grace.number),
        'entry_strategy': (result.entry_strategy.id, result.entry_strategy.number),
        'percentage': (percentage.id, percentage.number),
        'fixed_usd_amount': (fixed_usd_amount.id, fixed_usd_amount.number),
        
    }

@db_session
def list_owner_strat(table, user_id, owner_id):
    return list(orm.select(p.name for p in table))

@db_session
def copy_strategy(name,
                  take_profit,
                  first_entry_grace,
                  entry_strategy,
                  percentage,
                  fixed_usd_amount,
                  user_id,
                  ):
    print('Percentage: ', percentage)
    print('fixed_usd_amount: ', fixed_usd_amount)
    amount = orm.select(p for p in Amount_trade if p.percentage.number==percentage and p.fixed_usd_amount.number==fixed_usd_amount).first()
    print(amount)
    strategy =  Strategy_user(
        name=name,
        take_profit=take_profit,
        first_entry_grace=first_entry_grace,
        entry_strategy=entry_strategy,
        amount_per_trade=amount.id,
        close_trade_on_take_profit=2,
        users=user_id,
        )

@db_session
def save_strategy(name,
                  take_profit_number,
                  first_entry_grace_number,
                  entry_strategy_number,
                  percentage_number,
                  fixed_usd_amount_number,
                  user_id,
                  ):
    take_profit = orm.select(p for p in Take_profit_strategy if p.number==take_profit_number).first()
    first_entry_grace = orm.select(p for p in First_entry_grace_percentage if p.number==first_entry_grace_number).first()
    entry_strategy = orm.select(p for p in Entry_strategy if p.number==entry_strategy_number).first()
    percentage = orm.select(p for p in Percentage if p.number==percentage_number).first()
    fix_usd = orm.select(p for p in Fixed_usd_amount if p.number==fixed_usd_amount_number).first()
    print('Percentage: ', percentage)
    print('fixed_usd_amount: ', fix_usd)
    create_amount = Amount_trade(
            percentage=percentage,
            fixed_usd_amount=fix_usd,
                                 
                                 )

    strategy =  Strategy_owner(
        name=name,
        take_profit=take_profit,
        first_entry_grace=first_entry_grace,
        entry_strategy=entry_strategy,
        # close_trade_on_take_profit=,
        amount_per_trade=create_amount,
        Memberships=user_id,
        )
if __name__=='__main__': 
    # pass
    print(save_strategy('owner_strat_3', 'One Target', '1.2', 'Off', '10', '50',1))