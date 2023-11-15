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
arcade.draw_line(20, 0, 20, 400, arcade.color.BLACK)
arcade.draw_line(40, 0, 40, 400, arcade.color.BLACK)
arcade.draw_line(60, 0, 60, 400, arcade.color.BLACK)
arcade.draw_line(80, 0, 80, 400, arcade.color.BLACK)
arcade.draw_line(100, 0, 100, 400, arcade.color.BLACK)
arcade.draw_line(120, 0, 120, 400, arcade.color.BLACK)
arcade.draw_line(140, 0, 140, 400, arcade.color.BLACK)
arcade.draw_line(160, 0, 160, 400, arcade.color.BLACK)
arcade.draw_line(180, 0, 180, 400, arcade.color.BLACK)
arcade.draw_line(200, 0, 200, 400, arcade.color.BLACK)
arcade.draw_line(220, 0, 220, 400, arcade.color.BLACK)
arcade.draw_line(240, 0, 240, 400, arcade.color.BLACK)
arcade.draw_line(260, 0, 260, 400, arcade.color.BLACK)
arcade.draw_line(280, 0, 280, 400, arcade.color.BLACK)
arcade.draw_line(300, 0, 300, 400, arcade.color.BLACK)
arcade.draw_line(320, 0, 320, 400, arcade.color.BLACK)
arcade.draw_line(340, 0, 340, 400, arcade.color.BLACK)
arcade.draw_line(360, 0, 360, 400, arcade.color.BLACK)
arcade.draw_line(380, 0, 380, 400, arcade.color.BLACK)
arcade.draw_line(400, 0, 400, 400, arcade.color.BLACK)
arcade.draw_line(420, 0, 420, 400, arcade.color.BLACK)
arcade.draw_line(440, 0, 440, 400, arcade.color.BLACK)
arcade.draw_line(460, 0, 460, 400, arcade.color.BLACK)
arcade.draw_line(480, 0, 480, 400, arcade.color.BLACK)
arcade.draw_line(500, 0, 500, 400, arcade.color.BLACK)
arcade.draw_line(0, 20, 500, 20, arcade.color.BLACK)
arcade.draw_line(0, 40, 500, 40, arcade.color.BLACK)
arcade.draw_line(0, 60, 500, 60, arcade.color.BLACK)
arcade.draw_line(0, 80, 500, 80, arcade.color.BLACK)
arcade.draw_line(0, 100, 500, 100, arcade.color.BLACK)
arcade.draw_line(0, 120, 500, 120, arcade.color.BLACK)
arcade.draw_line(0, 140, 500, 140, arcade.color.BLACK)
arcade.draw_line(0, 160, 500, 160, arcade.color.BLACK)
arcade.draw_line(0, 180, 500, 180, arcade.color.BLACK)
arcade.draw_line(0, 200, 500, 200, arcade.color.BLACK)
arcade.draw_line(0, 220, 500, 220, arcade.color.BLACK)
arcade.draw_line(0, 240, 500, 240, arcade.color.BLACK)
arcade.draw_line(0, 260, 500, 260, arcade.color.BLACK)
arcade.draw_line(0, 280, 500, 280, arcade.color.BLACK)
arcade.draw_line(0, 300, 500, 300, arcade.color.BLACK)
arcade.draw_line(0, 320, 500, 320, arcade.color.BLACK)
arcade.draw_line(0, 340, 500, 340, arcade.color.BLACK)
arcade.draw_line(0, 360, 500, 360, arcade.color.BLACK)
arcade.draw_line(0, 380, 500, 380, arcade.color.BLACK)
arcade.draw_line(0, 400, 500, 400, arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
arcade.draw_ellipse_filled(250, 200, 80, 80, arcade.color.WISTERIA)
arcade.draw_arc_filled()

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



