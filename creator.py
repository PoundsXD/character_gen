"""Create RPG character."""

classes = {
    "warrior": {
        "health": 10,
        "mana": 2,
        "inteligence": 4,
        "strength": 15,
        "agility": 6,
        "stamina": 8,
        "luck": 1
    }
}


class Character(object):
    """Create a character object."""

    def __init__(self, gender, race, char_class):
        """Statistic for a character object."""
        self.gender = gender
        self.race = race
        self.char_class = char_class
        self.level = 1
        self.health = 0
        self.mana = 0
        self.inteligence = 0
        self.strength = 0
        self.agility = 0
        self.stamina = 0
        self.luck = 0

    def health(self, level, char_class):
        """Set health stat for character based on level and class."""
        self.health = ((level + 2) + classes[char_class]['health'])

    def mana(self, level, char_class):
        """Set mana stat for character based on level and class."""
        self.mana = ((level + 2) + classes[char_class]['mana'])

    def inteligence(self, level, char_class):
        """Set inteligence stat for character based on level and class."""
        self.inteligence = ((level + 2) + classes[char_class]['inteligence'])

    def strength(self, level, char_class):
        """Set strength stat for character based on level and class."""
        self.strength = ((level + 2) + classes[char_class]['strength'])

    def agility(self, level, char_class):
        """Set agility stat for character based on level and class."""
        self.agility = ((level + 2) + classes[char_class]['agility'])

    def luck(self, level, char_class):
        """Set luck stat for character based on level and class."""
        self.luck = ((level + 1) + classes[char_class]['luck'])

    def stamina(self, level, char_class):
        """Set stamina stat for character based on level and class."""
        self.stamina = ((level + 2) + classes[char_class]['stamina'])
