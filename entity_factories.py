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
    fighter=Fighter(hp=30, base_defense=1, base_power=1),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)

)


orc = Actor(

    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),

)

troll = Actor(

    char="T",
    color=(0, 165, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),

)

confusion_scroll = Item(

    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),

)

fireball_scroll = Item(

    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),

)

health_potion = Item(

    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=8),

)

lightning_scroll = Item(

    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
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
    name="Dagger",
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
    name="Studded Leaether Armor",
    equippable=equippable.StuddedLeatherArmor(),

)