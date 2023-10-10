
###########################################
#autoBeauty.py
#Version 1.0.0
#Last updated October 05 2020
#This module allow to import multi passes render from the render engine Cycle
#and Redshift, let the user choose some setup and finally reconstruct
#automaticly the beauty.
###########################################


import nuke, autoBeauty_v1_3_02


nuke.menu("Nuke").addCommand("Utilities/AutoBeauty", "autoBeauty_v1_3_02.user_choices()")
