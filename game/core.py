"""
The Game Requirements:

Location: name, description, exits
World: collection of locations
GameState: world, current location
Move function: move a charcter to a connected location
"""

from pyrsistent import PClass, pmap_field, field, pmap


class Location(PClass):
    """Fetches Location

    Args:
    Returns:
    Raises:
    """
    name = field(str)
    description = field(str)
    exits = pmap_field(str, str)  # direction name -> location name

home = Location(name="Home", description="Home is where the heart is",
                exits={'east': 'Street'})

street = Location(name="Street", description="The street next to your house",
                  exits={'west': 'Home'})


class GameState(PClass):
     """Fetches Game State

    Args: PClass
    Returns:
    Raises:
    """
    location = field(Location)
    world = pmap_field(str, Location)

# create initial world object
world = pmap({x.name: x for x in [home, street]})


def render(state):
    "Display name of the room, description, and exits"
    exits = '\n'.join('* {} to {}'.format(exit, location) for exit,
                      location in state.location.exits.items())
    return "* {name} *\n\n{description}\n\nExits:\n{exits}".format(
            name=state.location.name,
            description=state.location.description,
            exits=exits
    )


def move(state, exit_name):
    location_name = state.location.exits.get(exit_name)
    if location_name is None:
        return None
    target_location = state.world.get(location_name)
    return GameState(location=target_location, world=state.world)


home = Location(name="Home", description="Home is where the heart is!",
                exits={'east': 'Street'})
street = Location(name="Street", description="The street next to your house.",              exits={'west': 'Home'})
world = pmap({x.name: x for x in [home, street]})
initial_state = GameState(location=home, world=world)
