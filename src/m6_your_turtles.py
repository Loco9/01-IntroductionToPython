"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Logan Cody.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

davis = rg.SimpleTurtle('turtle')
davis.pen = rg.Pen('red', 5)
davis.speed = 8

marry = rg.SimpleTurtle()
marry.pen = rg.Pen('blue', 5)
marry.speed = 8

davis.go_to(rg.Point(100, 0))
marry.go_to(rg.Point(-100, 0))

for k in range(8):
    davis.forward(20)
    davis.left(50)
    davis.go_to(rg.Point(100, 0))

    marry.backward(20)
    marry.right(50)
    marry.go_to(rg.Point(-100, 0))

window.close_on_mouse_click()