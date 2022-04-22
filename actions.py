from __future__ import annotations
from html.entities import entitydefs

from typing import Optional, Tuple, TYPE_CHECKING
# from typing import TYPE_CHECKING

if TYPE_CHECKING:

   from engine import Engine
   from entity import Entity

class Action:

    def __init__(self, entity: Entity) -> None:

        super().__init__()

        self.entity = entity

    @property

    def engine(self) -> Engine:
        """Return the engine this action belongs to."""

        return self.entity.gamemap.engine

    def perform(self) -> None:

    # def perform(self, engine: Engine, entity: Entity) -> None:
       """Perform this action with the objects needed to determine its scope.

        'self.engine' is the scope this action is being performed in.

        `self.entity` is the object performing the action.

        This method must be overridden by Action subclasses.
       """

       raise NotImplementedError()


class EscapeAction(Action):
    
    def perform(self) -> None:

    # There are 2 perform functions in different classes? Classes confuse me.
    # def perform(self, engine: Engine, entity: Entity) -> None:

       raise SystemExit()

class WaitAction(Action):

    def perform(self) -> None:

        pass

class ActionWithDirection(Action):

    def __init__(self, entity: Entity, dx: int, dy: int):

        super().__init__(entity)

    # def __init__(self, dx: int, dy: int):

    #     super().__init__()

        self.dx = dx
        self.dy = dy

    @property

    def dest_xy(self) -> Tuple[int, int]:
        """Returns this action's destination."""

        return self.entity.x + self.dx, self.entity.y + self.dy

    @property

    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this action's destination."""

        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    def perform(self) -> None:

    # def perform(self, engine: Engine, entity: Entity) -> None:

        raise NotImplementedError()

class MeleeAction(ActionWithDirection):

    # def perform(self, engine: Engine, entity: Entity) -> None:

        # dest_x = entity.x + self.dx
        # dest_y = entity.y + self.dy
        # target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)

    def perform(self) -> None:

        target = self.blocking_entity
        
        if not target:
            return # No entity to attack.

        print(f"You kick the {target.name}, much to its annoyance!")


# class MovementAction(Action):
class MovementAction(ActionWithDirection):

    # def __init__(self, dx: int, dy: int):

    #     super().__init__()

    #     self.dx = dx
    #     self.dy = dy

    # def perform(self, engine: Engine, entity: Entity) -> None:

    #     dest_x = entity.x + self.dx
    #     dest_y = entity.y + self.dy

    #     if not engine.game_map.in_bounds(dest_x, dest_y):

    def perform(self) -> None:

        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):

           return  # Destination is out of bounds.

        # if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:

           return  # Destination is blocked by a tile.

        # if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y): 
            
            return # Destination is blocked by an entity.

        # entity.move(self.dx, self.dy)
        self.entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    
    # def perform(self, engine: Engine, entity: Entity) -> None:

    #     dest_x = entity.x + self.dx
    #     dest_y = entity.y + self.dy

    #     if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):

    #         return MeleeAction(self.dx, self.dy).perform(engine, entity)

    def perform(self) -> None:

        if self.blocking_entity:

            return MeleeAction(self.entity, self.dx, self.dy).perform()

        else:

            # return MovementAction(self.dx, self.dy).perform(engine, entity)
            return MovementAction(self.entity, self.dx, self.dy).perform()