"""Implementation of the First Price Auction
The auction is characterized by a good that is been offered by a seller, that value the good at zero, and
N buyers, each having a private value for the good. The auction is a one step game where the player with 
highest bid receives the good and pay the bid made. The remainder of the players receive nothing and pays
nothing.
"""
from otree.api import *

class Constants(BaseConstants):

    NAME_IN_URL = 'first_price_auction'
    PLAYERS_PER_GROUP = None
    INSTRUCTIONS_TEMPLATE = 'first_price_auction/instructions.html'
    DISTRIBUTION = 'uniform'
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    
    highest_bid = models.CurrencyField()

class Player(BasePlayer):

    ai_group = models.BooleanField()
    private_value = models.CurrencyField(doc='private value for each player')





# FUNCTIONS


# PAGES

class MyPage(Page):
    pass

class Results(Page):
    pass
