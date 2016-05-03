"""
MCGWidget is defined in this module, see its documentation.
"""

import time
import Queue
import math

import wx

from vector import Vector
from my_mcg import *
import misc.dumpqueue as dumpqueue
from misc.fromresourcefolder import from_resource_folder


class MCGWidget(wx.Panel):
    """
    A wxPython widget to display the MCG screen and all the drawings that
    it made.
    """
    def __init__(self,parent,mcg_queue,*args,**kwargs):
        wx.Panel.__init__(self,parent,style=wx.SUNKEN_BORDER,*args,**kwargs)

        self.BACKGROUND_COLOR = wx.Colour(212,208,200)

        self.mcg = MCG()
        self.bitmap = wx.EmptyBitmap(*BITMAP_SIZE)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE,self.on_size)
        self.Bind(wx.EVT_IDLE,self.on_idle)
        self.mcg_queue = mcg_queue
        self.idle_block = False
        self.Origin = origin
        self.Scale = 1
        self.Brush = wx.Brush("black", wx.TRANSPARENT)
        self.Pen = wx.Pen("red", 1, wx.SOLID)
        
    def on_paint(self,e=None):
        """
        Paint event handler. Reads the mcg reports and draws graphics
        accordingly.
        """
        mcg_reports=dumpqueue.dump_queue(self.mcg_queue)
        dc=wx.GCDC(wx.MemoryDC(self.bitmap))
        dc.SetDeviceOrigin(self.Origin[0],self.Origin[1])
        dc.SetUserScale(self.Scale,-self.Scale)
        dc.SetBrush(self.Brush)
        dc.SetPen(self.Pen)
        #dc.ComputeScaleAndOrigin()
        for mcg_report in mcg_reports:
            #time.sleep(.01)
            if mcg_report.comando == "clear":
                dc.SetDeviceOrigin(0,0)
                dc.SetUserScale(1,1)
                #dc.ComputeScaleAndOrigin()
                brush=wx.Brush("black", wx.SOLID)
                dc.SetBackground(brush)
                dc.Clear()
                dc.SetDeviceOrigin(self.Origin[0],self.Origin[1])
                dc.SetUserScale(self.Scale,-self.Scale)
                #dc.ComputeScaleAndOrigin()
            elif mcg_report.comando == "SetPen":
                self.Pen = mcg_report.give_pen()
                dc.SetPen(self.Pen)
            elif mcg_report.comando == "SetBrush":
                self.Brush = mcg_report.give_brush()
                dc.SetBrush(self.Brush)
            elif mcg_report.comando == "SetDeviceOrigin":
                self.Origin=(mcg_report.arg[0],mcg_report.arg[1])
            elif mcg_report.comando == "SetUserScale":
                self.Scale = mcg_report.arg
            elif mcg_report.comando == "DrawRotatedText":
                dc.SetPen(mcg_report.give_pen())
                dc.SetFont(mcg_report.give_font())
                dc.DrawRotatedText(mcg_report.arg[0],mcg_report.arg[1],mcg_report.arg[2],mcg_report.arg[3])
            elif mcg_report.comando == "DrawText":
                dc.SetPen(mcg_report.give_pen())
                dc.SetFont(mcg_report.give_font())
                dc.DrawText(mcg_report.arg[0],mcg_report.arg[1],mcg_report.arg[2])
            elif mcg_report.comando == "DrawEllipse":
                dc.DrawEllipse(mcg_report.arg[0],mcg_report.arg[1],mcg_report.arg[2],mcg_report.arg[3])
            elif mcg_report.comando == "DrawEllipseList":
                dc.DrawEllipseList(mcg_report.arg,mcg_report.give_pen(),mcg_report.give_brush())
            elif mcg_report.comando == "DrawArcPoint":
                dc.DrawArcPoint(mcg_report.arg[0],mcg_report.arg[1],mcg_report.arg[2])
            elif mcg_report.comando == "DrawPointList":
                dc.SetPen(mcg_report.give_pen())
                dc.DrawPointList(mcg_report.arg)
            elif mcg_report.comando == "DrawCirclePoint":
                dc.SetPen(mcg_report.give_pen())
                dc.SetBrush(mcg_report.give_brush())
                dc.DrawCirclePoint(mcg_report.arg[0],mcg_report.arg[1])
            elif mcg_report.comando == "DrawPolygon":
                dc.DrawPolygon(mcg_report.arg)
            elif mcg_report.comando == "DrawPolygonList":
                dc.DrawPolygonList(mcg_report.arg,mcg_report.give_pen(),mcg_report.give_brush())
            elif mcg_report.comando == "DrawPolygonListC":
                dc.SetBrush(wx.Brush("red",wx.TRANSPARENT))
                for face in mcg_report.arg:
                    dc.SetPen(wx.Pen(face[0],1,wx.SOLID))
                    dc.DrawPolygon(face[1])
            elif mcg_report.comando == "DrawPolygonListB":
                for face in mcg_report.arg:
                    dc.SetBrush(wx.Brush(face[0],wx.SOLID))
                    dc.DrawPolygon(face[1])
            elif mcg_report.comando == "DrawLineList":
                dc.DrawLineList(mcg_report.arg)
            elif mcg_report.comando == "DrawLinePoint":
                dc.SetPen(mcg_report.give_pen())
                dc.DrawLinePoint(mcg_report.arg[0],mcg_report.arg[1])
            elif mcg_report.comando == "DrawPointPoint":
                dc.DrawPointPoint(mcg_report.arg)
            elif mcg_report.comando == "DrawSpline":
                dc.DrawSpline(mcg_report.arg)
            self.mcg = mcg_report

        del dc
        if len(mcg_reports) > 0:
            self.Refresh()


        dc=wx.PaintDC(self)
        widget_size = Vector(self.GetSize())
        top_left_corner =(-BITMAP_SIZE+widget_size)/2.0
        # Draw the bitmap:
        dc.DrawBitmap(self.bitmap, *top_left_corner)

        dc.Destroy()



    def on_idle(self,e=None):
        """
        Idle event handler. Checks whether there are any
        pending MCG reports, and if there are tells the widget
        to process them.
        """
        if self.idle_block==True: return

        if self.mcg_queue.qsize()>0: self.Refresh()

        wx.CallLater(10,self._clear_idle_block_and_do) # Should make the delay customizable?
        self.idle_block=True


    def _clear_idle_block_and_do(self):
        self.idle_block=False
        event=wx.PyEvent()
        event.SetEventType(wx.wxEVT_IDLE)
        wx.PostEvent(self,event)

    def on_size(self,e=None):
        self.Refresh()

