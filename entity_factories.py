from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(

    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=1, base_magic=1),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)

)

rat = Actor(

    char="r",
    color=(138, 72, 123),
    name="Rat",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=6, base_defense=0, base_power=3, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),

)

kobold = Actor(

    char="k",
    color=(255, 128, 0),
    name="Kobold",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=8, base_defense=0, base_power=3, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),

)

orc = Actor(

    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=1, base_power=4, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),

)

skeleton = Actor(

    char="S",
    color=(0, 213, 255),
    name="Skeleton",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=13, base_defense=2, base_power=5, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),

)

troll = Actor(

    char="T",
    color=(0, 165, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=3, base_power=6, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200),

)

zombie = Actor(

    char="z",
    color=(255, 222, 0),
    name="Zombie",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=14, base_defense=4, base_power=8, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=300),

)

harpy = Actor(

    char="h",
    color=(255, 0, 213),
    name="Harpy",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=12, base_defense=1, base_power=9, base_magic=0),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=350),

)

confusion_scroll = Item(

    char="~",
    color=(207, 63, 255),
    name="Scroll of Confusion",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),

)

fireball_scroll = Item(

    char="~",
    color=(255, 0, 0),
    name="Scroll of Fireball",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),

)

health_potion = Item(

    char="!",
    color=(255, 15, 25),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=6),

)

lightning_scroll = Item(

    char="~",
    color=(255, 255, 0),
    name="Scroll of Lightning",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),

)

dagger = Item(

    char="/",
    color=(0, 191, 255),
    name="Dagger",
    equippable=equippable.Dagger(),

)

shortsword = Item(

    char="/",
    color=(0, 191, 255),
    name="Shortsword",
    equippable=equippable.Shortsword(),

)

falchion = Item(

    char="/",
    color=(0, 191, 255),
    name="Falchion",
    equippable=equippable.Falchion(),

)

robe = Item(

    char="]",
    color=(139, 99, 189),
    name="Robe",
    equippable=equippable.Robe(),

)

quilted_armor = Item(

    char="[",
    color=(139, 69, 19),
    name="Quilted Armor",
    equippable=equippable.QuiltedArmor(),

)

leather_armor = Item(

    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),

)

studded_leather_armor = Item(

    char="[",
    color=(139, 69, 19),
    name="Studded Leather Armor",
    equippable=equippable.StuddedLeatherArmor(),

)