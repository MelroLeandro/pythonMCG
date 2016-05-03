import sys
import multiprocessing
import copy
import math
import time

import smartsleep
import misc.angles as angles
import shelltoprocess
from my_mcg import *
from vector import Vector

import wx


def log(x):
    print(x)
    sys.stdout.flush()

class MCGProcess(multiprocessing.Process):
    """
    A MCGProcess is a subclass of multiprocessing.Process.
    It is the process from which the user of PythonMCG works;
    It defines all the MCG commands.
    Then it runs a shelltoprocess.Console which connects to the shell
    in the main application window, allowing the user to control
    this process.
    """
    def __init__(self,*args,**kwargs):
        multiprocessing.Process.__init__(self,*args,**kwargs)

        self.daemon=True


        self.mcg_queue=multiprocessing.Queue()
        self.queue_pack=shelltoprocess.make_queue_pack()

        """
        Constants:
        """
        #self.FPS=25
        #self.FRAME_TIME=1/float(self.FPS)



    def send_report(self):
        """
        Sends a "mcg report" to the MCGWidget.
        By sending MCG reports every time the sceen is update,
        the MCGWidget can always know where changes in the sceen
        and draw graphics accordingly.
        """
        self.mcg_queue.put(self.mcg)

    def run(self):

        TRANSPARENT = 106
        SOLID = 100
        DOT = 101
        DOT_DASH = 104
        LONG_DASH = 102
        SHORT_DASH = 103
        STIPPLE = 110
        CROSSDIAG_HATCH = 112
        FDIAGONAL_HATCH = 113
        CROSS_HATCH = 114


        self.mcg=MCG()


        def SetDeviceOrigin(x,y):
            """
            Sets the x and y axis orientation (i.e., the direction from lowest to highest values on the axis). The default orientation is the
            natural orientation, e.g. x axis from left to right and y axis from bottom up.
            """
            self.mcg.comando = "SetDeviceOrigin"
            self.mcg.arg = (x,y)
            self.send_report()
        
        def DrawArcPoint(pt1, pt2, center):
            """
            DrawArcPoint(self, pt1, pt2, center)
            Draws an arc of a circle, centred on the center point (xc, yc),
            from the first point to the second.
            """
            self.mcg.comando = "DrawArcPoint"
            self.mcg.arg = (pt1, pt2, center)
            self.send_report()
               
        def DrawCirclePoint(pt, radius):
            """
            DrawCirclePoint(self, pt, radius)
            Draws a circle with the given center point and radius.
            """
            self.mcg.comando = "DrawCirclePoint"
            self.mcg.arg = (pt, radius)
            self.send_report()
        
        def DrawEllipse(x, y, width, height):
            """
            DrawEllipse(self, x, y, width, height)
            Draws an ellipse contained in the specified rectangle.
            """
            self.mcg.comando = "DrawEllipse"
            self.mcg.arg = (x, y, width, height)
            self.send_report()

        def DrawEllipseList(ellipses):
            """
            DrawEllipseList(self, ellipses, pens, brushes)
            Draw a list of ellipses as quickly as possible.
            """
            self.mcg.comando = "DrawEllipseList"
            self.mcg.arg = ellipses
            self.send_report()

        def DrawLineList(points):
            """
            DrawLines(self, points, xoffset, yoffset)
            Draws lines using a sequence of wx.Point objects, adding the optional offset coordinate.
            """
            self.mcg.comando = "DrawLineList"
            self.mcg.arg = points
            self.send_report()
        
        def DrawLinePoint(pt1,pt2):
            """
            DrawLinePoint(self, list)
            Draws a line from the first point to the second.
            """
            self.mcg.comando = "DrawLinePoint"
            self.mcg.arg = [pt1,pt2]
            self.send_report()
        
        def DrawPointList(points):
            """
            DrawPointList(self, points, pens)
            Draw a list of points as quickly as possible.
            """
            self.mcg.comando = "DrawPointList"
            self.mcg.arg = points
            self.send_report()
        

        def DrawPointPoint(pt):
            """
            DrawPointPoint(self, pt)
            Draws a point using the current pen.
            """
            self.mcg.comando = "DrawPointPoint"
            self.mcg.arg = pt
            self.send_report()

        def DrawPolygon(points):
            """
            DrawPolygon(self, points, xoffset, yoffset, fillStyle)
            Draws a filled polygon using a sequence of wx.Point objects, adding the optional offset coordinate.
            """
            self.mcg.comando = "DrawPolygon"
            self.mcg.arg = points
            self.send_report()
        
        def DrawPolygonList(polygons):
            """
            DrawPolygonList(self, polygons, pens, brushes)
            Draw a list of polygons, each of which is a list of points.
            """
            self.mcg.comando = "DrawPolygonList"
            self.mcg.arg = polygons
            self.send_report()

        def DrawPolygonListC(polygons):
            """
            DrawPolygonList(self, polygons, pens, brushes)
            Draw a list of polygons, each of which is a list of points.
            """
            self.mcg.comando = "DrawPolygonListC"
            self.mcg.arg = polygons
            self.send_report()

        def DrawPolygonListB(polygons):
            """
            DrawPolygonList(self, polygons, pens, brushes)
            Draw a list of polygons, each of which is a list of points.
            """
            self.mcg.comando = "DrawPolygonListB"
            self.mcg.arg = polygons
            self.send_report()
        
        def DrawRotatedText(text, x,y, angle):        
            """
            DrawRotatedText(self, text, x, y, angle)
            Draws the text rotated by angle degrees, if supported by the platform.
            """
            self.mcg.comando = "DrawRotatedText"
            self.mcg.arg = [text, x,y, angle]
            self.send_report()
        
        
        def DrawSpline(points):
            """
            DrawSpline(self, points)
            Draws a spline between all given control points, (a list of wx.Point objects)
            using the current pen.
            """
            self.mcg.comando = "DrawSpline"
            self.mcg.arg = points
            self.send_report()

        def DrawText(text, x,y):
            """
            DrawText(self, text, x, y)
            Draws a text string at the specified point, using the current text font, and the current text foreground and background colours.
            """
            self.mcg.comando = "DrawText"
            self.mcg.arg = [text, x,y]
            self.send_report()

        def SetUserScale(s):
            """
            SetUserScale(self, x, y)
            Sets the user scaling factor, useful for applications which require 'zooming'.
            """
            self.mcg.Scale = s
            self.mcg.comando = "SetUserScale"
            self.mcg.arg = s
            self.send_report()
        
        def SetBrush(color, style):
            """
            SetBrush(self, brush)
            Sets the current brush for the DC.
            """
            self.mcg.brush_color = color
            self.mcg.brush_style = style
            self.mcg.comando = "SetBrush"
            self.send_report()

        def SetPen(color, width, style):
            """
            SetPen(self, pen)
            Sets the current pen for the DC.
            The style may be one of the following:
                wxSOLID  Solid style.  
                wxTRANSPARENT  No pen is used.  
                wxDOT  Dotted style.  
                wxLONG_DASH  Long dashed style.  
                wxSHORT_DASH  Short dashed style.  
                wxDOT_DASH  Dot and dash style.  
                wxSTIPPLE  Use the stipple bitmap.  
                wxUSER_DASH  Use the user dashes: see wxPen::SetDashes.  
                wxBDIAGONAL_HATCH  Backward diagonal hatch.  
                wxCROSSDIAG_HATCH  Cross-diagonal hatch.  
                wxFDIAGONAL_HATCH  Forward diagonal hatch.  
                wxCROSS_HATCH  Cross hatch.  
                wxHORIZONTAL_HATCH  Horizontal hatch.  
                wxVERTICAL_HATCH  Vertical hatch.
            Sets the color of the mcg's pen. Specify a color as a string.

            Examples:
            color("white")
            color("green")
            color("#00FFCC")
            """
            self.mcg.pen_color=color
            self.mcg.pen_width=width
            self.mcg.pen_style=style
            self.mcg.comando = "SetPen"
            self.send_report()

        def color(color):
            """
            Sets the color of the mcg's pen. Specify a color as a string.

            Examples:
            color("white")
            color("green")
            color("#00FFCC")
            """
            self.mcg.color=color
            self.send_report()

        def width(width):
            """
            Sets the width of the mcg's pen. Width must be a positive number.
            """
            self.mcg.width = width
            self.send_report()



        def clear():
            """
            Clears the screen, making it all black again.
            """
            self.mcg.comando = "clear"
            self.send_report()

        def reset():
            """
            Resets all the mcg's properties and clears the screen.
            """
            self.mcg = MCG()
            clear()

        locals_for_console={"color": color, "width": width, "clear": clear,
                            "reset": reset, 
                            "DrawPointList": DrawPointList, "DrawPointPoint": DrawPointPoint,
                            "DrawLineList": DrawLineList, "DrawLinePoint": DrawLinePoint,
                            "DrawPolygon": DrawPolygon, "SetPen": SetPen,
                            "DrawPolygonList": DrawPolygonList, "DrawRotatedText": DrawRotatedText,
                            "DrawText": DrawText, "SetBrush": SetBrush,
                            "DrawPolygonListC": DrawPolygonListC, "DrawPolygonListB": DrawPolygonListB,
                            "SetUserScale": SetUserScale, "DrawSpline":DrawSpline,
                            "SetDeviceOrigin": SetDeviceOrigin, "SetUserScale": SetUserScale,
                            "DrawEllipseList": DrawEllipseList, "DrawEllipse": DrawEllipse,
                            "DrawCirclePoint": DrawCirclePoint, "DrawArcPoint": DrawArcPoint,
                            "TRANSPARENT": TRANSPARENT, "SOLID": SOLID, "DOT": DOT,
                            "DOT_DASH": DOT_DASH, "LONG_DASH": LONG_DASH, "SHORT_DASH": SHORT_DASH,
                            "STIPPLE": STIPPLE, "CROSSDIAG_HATCH": "CROSSDIAG_HATCH",
                            "FDIAGONAL_HATCH": FDIAGONAL_HATCH, "CROSS_HATCH": CROSS_HATCH}

        self.console = \
            shelltoprocess.Console(queue_pack=self.queue_pack,locals=locals_for_console)

        #import cProfile; cProfile.runctx("console.interact()", globals(), locals())
        self.console.interact()
        sys.stdout.flush()
