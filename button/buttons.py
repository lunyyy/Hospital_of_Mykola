from button.class_button import Button
import button.settings as settings
from paths import play_button_path
from paths import continue_button_path
from paths import help_button_path
from paths import autors_button_path
from paths import exit_button_path
from paths.get_path import get_full_path

play = Button(x=860,
              y=200,
              width=settings.width,
              height=settings.height,
              image_path=play_button_path,
              )

continuee = Button(x=settings.x,
                  y=270,
                  width=settings.width,
                  height=settings.height,
                  image_path=continue_button_path
                  )

helpp = Button(x=settings.x,
               y=400,
               width=settings.width,
               height=settings.height,
               image_path=help_button_path
               )


exitt = Button(x=860,
               y=400,
               width=settings.width,
               height=settings.height,
               image_path=exit_button_path
               )

#Кнопки (Вверх, вниз)

down = Button(
              x = 510,
              y = 25,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
            )

down2 = Button(
              x = 510,
              y = 275,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
            )

down3 = Button(
              x = 685,
              y = 25,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
              )


up = Button(
              x =685,
              y = 275,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
            )

up2 = Button(
              x =510,
              y = 540,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
            )

up3 = Button(
              x = 685,
              y = 540,
              width = 20,
              height = 20,
              image_path=get_full_path(path="resources/images/level_1/button.png")
            )

#Прямоугольники зоны лесницы 

three = Button(
              x=505,
              y=100,
              width=205,
              height=100,
        
              )

two = Button(
              x=505,
              y=370,
              width=205,
              height=100,
        
              )

one = Button(
              x=505,
              y=640,
              width=205,
              height=100,

              )

# dig = Button(
#               x = 480,
#               y = 280,
#               width=500,
#               height=500
#               )


exit_from_lvl1 = Button(
                        x = 480,
                        y = 280,
                        width=50,
                        height=50,
                        image_path=play_button_path
                        )



exit_from_full_scroll = Button(
  x=950,
  y=100,
  width=50,
  height=50,
  image_path=get_full_path(path=r"resources/images/level_1/quit_button.jpg")
)

exit_from_kitchen = Button(
  x=0,
  y=0,
  width=100,
  height=50,
  image_path=get_full_path(path=r"resources/images/level_1/quit_button.jpg")
)

exit_from_button_help = Button(
                              x=1100,
                              y=0,
                              width=100,
                              height=50,
                              image_path=get_full_path(path=r"resources/images/level_1/quit_button.jpg")
)