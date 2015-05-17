"""Generate fake data for testing purposes."""

from faker import Faker
from random import randint
from GoPlayer import Player
from pprint import pprint

fake = Faker()

names = [fake.name() for x in range(49)]
ids = [x for x in range(49)]
ranks = [randint(-30, 7) for x in range(49)]

player_info = list(zip(names, ids, ranks))

player_list = []

for rec in player_info:
    player_list.append(Player(name=rec[0], aga_id=rec[1],
                              aga_rating=rec[2]))

