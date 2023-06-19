from sprites.scroll import Scroll
from paths.get_path import get_full_path
import paths
from sprites.room import Room
from sprites.sprite import Sprite
from sprites.dialogs import Dialogs
from sprites.text import Text

scroll = Scroll(
    x=1025,
    y=10,
    width=150,
    height=50,
    image_path=get_full_path(path=r"resources/images/level_1/scroll.png")
)

full_scroll = Scroll(
    x=200,
    y=100,
    width=800,
    height=600,
    image_path=get_full_path(path=r"resources/images/level_1/scroll_unlocked.png")
)

canteen = Room(
    x=830,
    y=565,
    width=240,
    height=180,
    image_path=get_full_path(path=r"resources/images/level_1/canteen.jpg")
)


hero_room = Room(
    x=330,
    y=41,
    width=100,
    height=168,
    image_path=paths.hero_room_path
)
fire_exit = Room(
    x = 330,
    y = 573,
    width = 100,
    height = 168,
    image_path=paths.fire_exit_path       
)


meat = Sprite(
    x=400,
    y=500,
    width=50,
    height=50,
    image_path=paths.kotlet,
)

storeroom = Room(
    x=100,
    y=300,
    width=100,
    height=168,
    image_path=get_full_path(path="resources/images/level_1/storeroom.jpg")
)

basement = Room(
    x=100,
    y=555,
    width=100,
    height=168,
    image_path=get_full_path(path="resources/images/basment/basement.jpg")
)

# basement_full = Room(
#     x=100,
#     y=555,
#     width=100,
#     height=168,
#     image_path=get_full_path(path="resources/images/basment/basement.jpg")
# )

basement_cut = Room(
    x=100,
    y=555,
    width=100,
    height=168,
    image_path=get_full_path(path="resources/images/basment/basement2.jpg")
)

key_from_basement = Sprite(
    x=430,
    y=120,
    width=50,
    height=50,
    image_path=get_full_path(path="resources/images/storeroom/key_basement.png")
)

key_from_escape = Sprite(
    x=710,
    y=140,
    width=50,
    height=50,
    image_path=paths.key2
)

shovel = Sprite(
    x=1070,
    y=370,
    width=80,
    height=285,
    image_path=paths.lopatas
)

scissors = Sprite(
    x=50,
    y=490,
    width=75,
    height=75,
    image_path=paths.scissors1
)

rope = Sprite(
    x=834,
    y=105,
    width=100,
    height=80,
    image_path=paths.verevka2)
# basement
object1 = Sprite(
    x=100,
    y=50,
    width=50,
    height=50,
    image_path=paths.vint1
)

object2 = Sprite(
    x=1070,
    y=50,
    width=50,
    height=50,
    image_path=paths.vint2
)

object3 = Sprite(
    x=100,
    y=700,
    width=50,
    height=50,
    image_path=paths.vint3
)

object4 = Sprite(
    x=1070,
    y=700,
    width=50,
    height=50,
    image_path=paths.vint4
)
shield = Sprite(
    x=100,
    y=50,
    width=1020,
    height=700,
    image_path=paths.shield
)

# fire exit

block1 = Sprite(
    x=432,
    y=595,
    width=150,
    height=60,
    image_path=paths.bloks1
)

block2 = Sprite(
    x=432,
    y=660,
    width=150,
    height=55,
    image_path=paths.bloks2
)

block3 = Sprite(
    x=432,
    y=720,
    width=150,
    height=50,
    image_path=paths.bloks3
)

block4 = Sprite(
    x=297,
    y=600,
    width=130,
    height=50,
    image_path=paths.bloks4
    # 130
)

block5 = Sprite(
    x=297,
    y=660,
    width=130,
    height=55,
    image_path=paths.bloks5
)

block6 = Sprite(
    x=297,
    y=720,
    width=130,
    height=50,
    image_path=paths.bloks6
)

dig = Sprite(
              x = 297,
              y = 280,
              width=280,
              height=500,
              color=(255,0,0)
              )


exclamation_mark1 = Sprite(
    x=795,
    y=15,
    width=70,
    height=50,
    image_path=get_full_path(path="resources/images/level_1/exclamation_mark.png")
)

exclamation_mark2 = Sprite(
    x=1045,
    y=15,
    width=70,
    height=50,
    image_path=get_full_path(path="resources/images/level_1/exclamation_mark.png")
)

exclamation_mark3 = Sprite(
    x=810,
    y=282,
    width=70,
    height=50,
    image_path=get_full_path(path="resources/images/level_1/exclamation_mark.png")
)

dialog1 = Dialogs(
    x = 780,
    y = 41,
    width = 110,
    height = 168,
    image_path=paths.dialog
)
dialog2 = Dialogs(
    x = 1015,
    y = 41,
    width = 110,
    height = 168,
    image_path=paths.dialog
)

dialog2_1 = Dialogs(
    x = 1015,
    y = 41,
    width = 110,
    height = 168,
    image_path=paths.dialog
)

dialog3 = Dialogs(
    x = 780,
    y = 300,
    width = 110,
    height = 168,
    image_path=paths.dialog
)

dialog3_1 = Dialogs(
    x = 780,
    y = 300,
    width = 110,
    height = 168,
    image_path=paths.dialog
)

dialog4 = Dialogs(
    x = 780,
    y = 41,
    width = 110,
    height = 168,
    image_path=paths.dialog
)

arrow_down2 = Sprite(
    x=1045,
    y=15,
    width=70,
    height=50,
    image_path=get_full_path(path="resources/images/level_1/arrow_down.png")
)

arrow_down3 = Sprite(
    x=805,
    y=282,
    width=70,
    height=50,
    image_path=get_full_path(path="resources/images/level_1/arrow_down.png")
)


