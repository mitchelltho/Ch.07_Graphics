# 7.0 Jedi Training (20pts)  Name:________________

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Ch. 7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()
for i in range(0,500,20):
    arcade.draw_line(i, 0, i, 400, arcade.color.BLACK)

for i in range(0,500,20):
    arcade.draw_line(0, i, 500, i, arcade.color.BLACK)


arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
arcade.draw_ellipse_filled(250, 200, 80, 80, arcade.color.WISTERIA)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 45, -45, 0, 2)

arcade.finish_render()
arcade.run()

'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''



