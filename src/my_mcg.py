import wx

from vector import Vector
from misc.angles import deg_to_rad, rad_to_deg


# Size of the MCG canvas. We assume no user will have a screen
# so big that the canvas will be bigger than this.
BITMAP_SIZE = Vector((2000,1200))

# Center of the canvas.
origin = BITMAP_SIZE / 2.0


# 4 lambda functions for transforming between the reference frame
# that we prefer and the reference frame that wxPython prefers:

#to_my_angle = lambda angle: rad_to_deg(-angle)-180
#from_my_angle = lambda angle: deg_to_rad(-angle+180)

#from_my_pos = lambda pos: -pos+origin
#to_my_pos = lambda pos: -pos+origin

##############

class MCG(object):
    """
    A MCG object defines a view by its attributes, such as
    position, orientation, color, etc. See source of __init__ for
    a complete list.
    """
    def __init__(self):
        self.pen_color = "red"
        self.pen_width = 1
        self.pen_style = wx.SOLID
        self.brush_color = "red"
        self.brush_style = wx.TRANSPARENT
        self.font_pointSize = 15
        self.font_family= wx.FONTFAMILY_SWISS
        self.font_style= wx.FONTSTYLE_NORMAL
        self.font_weight = wx.FONTWEIGHT_NORMAL
        self.Scale = 1.0
        self.comando = ""
        self.arg = []
        self.SPEED=400.0 # Pixels per second
        self.ANGULAR_SPEED=360.0 # Degrees per second


    def give_pen(self):
        """
        Gives a wxPython pen that corresponds to the color, width,
        and style of the mcg instance.
        """
        return wx.Pen(self.pen_color,self.pen_width,self.pen_style)

    def give_brush(self):
        """
        Gives a wxPython brush that corresponds to the color, 
        and style of the mcg instance.
        """
        return wx.Brush(self.brush_color,self.brush_style)

    def give_font(self):
        """
        Gives a wxPython font that corresponds to the color, 
        and style of the mcg instance.
        """
        return wx.Font(self.font_pointSize, self.font_family, self.font_style, self.font_weight)

    def give_scale(self):
        """
        Gives a wxPython font that corresponds to the scale, 
        and style of the mcg instance.
        """
        return self.Scale
