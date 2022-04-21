#!/usr/bin/env python3
import copy

import tcod

from engine import Engine
# from entity import Entity
import entity_factories
# from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:

    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    
    # player_x = int(screen_width / 2)
    # player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(

        "./art/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD

    )

    event_handler = EventHandler()

    # player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    player = copy.deepcopy(entity_factories.player)
    # npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    # entities = {npc, player}

    # game_map = GameMap(map_width, map_height)
    # game_map = generate_dungeon(map_width, map_height)
    game_map = generate_dungeon(

        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player

    )

    # engine = Engine(entities=entities, event_handler=event_handler, player=player)
    # engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(

        screen_width,
        screen_height,
        tileset=tileset,
        title="Cayzel",
        vsync=True,

    ) as context:

        root_console = tcod.Console(screen_width, screen_height, order="F")

        while True:

            # root_console.print(x=player_x, y=player_y, string="@")
            # root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            engine.render(console=root_console, context=context)

            # context.present(root_console)
            events = tcod.event.wait()
            
            engine.handle_events(events)
            # root_console.clear()

            # for event in tcod.event.wait():

            #     # if event.type == "QUIT":

            #     #     raise SystemExit()
            #     action = event_handler.dispatch(event)

            #     if action is None:
            #         continue
                
            #     if isinstance(action, MovementAction):
            #         # player_x += action.dx
            #         # player_y += action.dy
            #         player.move(dx=action.dx, dy=action.dy)

            #     elif isinstance(action, EscapeAction):
            #         raise SystemExit()


if __name__ == "__main__":

    main()