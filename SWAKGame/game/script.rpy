# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jonah = Character("Jonah")
define lyria = Character("Lyria")

# The game starts here.

label start:
    stop music fadeout 2.0
    # TODO: ADD MUSIC
    # TODO: ADD CITY BACKGROUND
    "The year was 1848. Just a few years after the dawn of the Magitek Revolution."
    "Long gone were the days of manual, pedestrian dungeoneering."
    "With the ancient resources of the world nearly depleted, a great breakthrough was necessary, and a great breakthrough took place."
    "With the discovery of extradimensional portals, any location could be turned into a dungeon site, producing a seemingly endless supply of relics, magical materials and valuable monsters."
    "Those manmade dungeon sites quickly turned into advances Dungeon Industries, where new machines would sort the valuables and crush the monsters originating from portals like well oiled machines."
    "Of course, no profitable process is ever simple and neither were portals."
    "Despite their innovative design, the earliest auto grinders lacked the capacity of culling every monster, leaving those for the manual work of specialized forces."
    "Such work would provide jobs for some of the old adventurers, continuing their labor as defense staff against the deadliest encounters."
    "Yes, the Magitek Revolution was an era of splendor… But not every bright period shines the same below its surface."
    "This is the story of such places in history, where the light didn’t seem to shine. No matter how hard one would look for it."
    jump scene_1_start
