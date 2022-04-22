from __future__ import annotations

from typing import TYPE_CHECKING

# from typing import Set, Iterable, Any
# from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

# from actions import EscapeAction, MovementAction
# from entity import Entity
# from game_map import GameMap
from input_handlers import EventHandler

if TYPE_CHECKING:
    
    from entity import Entity
    from game_map import GameMap

class Engine:

    game_map: GameMap

    # def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
    # def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
    # def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):

    #     # self.entities = entities
    #     self.event_handler = event_handler
    #     self.game_map = game_map
    #     self.player = player
    #     self.update_fov()

    def __init__(self, player: Entity):

        self.event_handler: EventHandler = EventHandler(self)
        self.player = player

    def handle_enemy_turns(self) -> None:

        for entity in set(self.game_map.actors) - {self.player}:

            if entity.ai:

                entity.ai.perform()
            
        # for entity in self.game_map.entities - {self.player}:

            # print(f'The {entity.name} wonders when it will get to take a real turn')

    # def handle_events(self, events: Iterable[Any]) -> None:

    #     for event in events:

    #         action = self.event_handler.dispatch(event)

    #         if action is None:

    #             continue

    #         action.perform(self, self.player)

    #         self.handle_enemy_turns()

    #         self.update_fov() # Update the FOC before the player's next action.
            
    def update_fov(self) -> None:

        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(

            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,

        )

        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

            # if isinstance(action, MovementAction):

            #     # self.player.move(dx=action.dx, dy=action.dy)
            #     if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
            #         self.player.move(dx=action.dx, dy=action.dy)

            # elif isinstance(action, EscapeAction):

            #     raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        
        self.game_map.render(console)

        # for entity in self.entities:

        #     # console.print(entity.x, entity.y, entity.char, fg=entity.color)
        #     # Only print entities that are in the FOV.
        #     if self.game_map.visible[entity.x, entity.y]:
        #         console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()