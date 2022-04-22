from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor
# from entity import Entity

player = Actor(

    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),

)

# player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Actor(

    char="o",
    color=(63, 127, 63),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),

)

troll = Actor(

    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),

)

# orc = Entity(char="o", color=(63, 127, 63), name="Orc", blocks_movement=True)
# troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True)