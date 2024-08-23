from __future__ import annotations
import atexit
from .animations import play_onload_animation
from .builtins_modifiers import (
    set_grumpy_input, 
    set_grumpy_print
)

@atexit.register
def goodbye_image() -> None:
    import webbrowser

    grumpy_cat = "https://www.google.com/search?sca_esv=ea2cb3181ae7dcdc&sxsrf=ADLYWIIuPDQV_8tVkBFfW2lielLsLYOztg:1724363947530&q=grumpy+cat&udm=2&fbs=AEQNm0CRjlOtE433-CvsDZEksQ8zUchZAntv9lLo-e4ZT42ratBCI50jVD5EdzCOdux47zeiB6ovlrZ7ln5v-PWVI1zt81JEK34kdeI12fKNSw-Ta55KkmZblEVqLhEijaNxPZB08LjelYFyHNrlZJ3GOjO2QgumXWzHais8y1oB0zpw6NqKAezlkI_ThEXL3JdqayJNru5aLsakJ_kQdseCylKf5kSgeA&sa=X&ved=2ahUKEwiQjbmkzImIAxX10wIHHfjHKEcQtKgLegQIEBAB&biw=2101&bih=1231&dpr=2"
    
    webbrowser.open_new(grumpy_cat)

def meow() -> None:
    play_onload_animation()
    set_grumpy_input()
    set_grumpy_print()