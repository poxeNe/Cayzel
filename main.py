#!/usr/bin/env python3
# import copy
import traceback
import tcod
import color
# from engine import Engine
# import entity_factories
import exceptions
import input_handlers
# from procgen import generate_dungeon
import setup_game

import faulthandler; faulthandler.enable()

def main() -> None:

    screen_width = 80
    screen_height = 50
    # map_width = 80
    # map_height = 43
    # room_max_size = 10
    # room_min_size = 6
    # max_rooms = 30
    # max_monsters_per_room = 2
    # max_items_per_room = 2

    tileset = tcod.tileset.load_tilesheet(

        "./art/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD

    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    
    with tcod.context.new_terminal(

        screen_width,
        screen_height,
        tileset=tileset,
        title="Cayzel",
        vsync=True,

    ) as context:

        root_console = tcod.Console(screen_width, screen_height, order="F")

        # while True:

        #     root_console.clear()
        #     engine.event_handler.on_render(console=root_console)
        #     context.present(root_console)

        #     try:

        #         for event in tcod.event.wait():

        #             context.convert_event(event)
                    
        #             engine.event_handler.handle_events(event)

        #     except Exception: # Handle exceptions in game.

        #         traceback.print_exc() # Print error to stderr.
                
        #         # Then print the error to the message log.
        #         engine.message_log.add_message(traceback.format_exc(), color.error)
                
        #     # engine.event_handler.handle_events(context)
        try:

            while True:

                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:

                    for event in tcod.event.wait():
                        
                        context.convert_event(event)
                        handler = handler.handle_events(event)

                except Exception: # Handle exceptions in game.

                    traceback.print_exc() # Print error to stderr.
                    
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):

                        handler.engine.message_log.add_message(

                            traceback.format_exc(), color.error

                        )

        except exceptions.QuitWithoutSaving:

            raise

        except SystemExit: # Save and quit.
            
            # TODO: Add the save function here
            raise

        except BaseException: # Save on any other unexpected exceptuion.

            # TODO: Add the save function here
            raise
        
if __name__ == "__main__":

    main()