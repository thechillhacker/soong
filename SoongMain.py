#!/usr/bin/python2.7 -u
import os, sys
import random
import numpy
import wx, math
import Brain
from wx.glcanvas import GLCanvas
from OpenGL.GL import *
from OpenGL.GLU import *

class BrainSlider(wx.Panel):
	def __init__(self, parent, text, minVal, maxVal, curVal):
		wx.Panel.__init__(self, parent, size=(500, 80))
		self.value = curVal
		self.minVal = minVal
		self.maxVal = maxVal

class BrainDisplayCanvas(GLCanvas):
	def __init__(self, parent):
		GLCanvas.__init__(self, parent, -1, attribList=[wx.glcanvas.WX_GL_DOUBLEBUFFER], size=(500,300))
		wx.EVT_PAINT(self, self.OnDraw)
		#wx.EVT_SIZE(self, self.OnSize)
		#wx.EVT_MOTION(self, self.OnMouseMotion)
		#ex.EVT_WINDOW_DESTROY(self, self.OnDestroy)
		self.init = True

	def OnDraw(self,event):
		self.SetCurrent()

		if not self.init:
		    self.InitGL()
		    self.init = False

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()

		glEnableClientState(GL_VERTEX_ARRAY)


		glFlush()
		self.SwapBuffers()
		return

	def InitGL(self):
		'''
		Initialize GL
		'''
		return
		# set viewing projection
#		glClearDepth(1.0)

#		glMatrixMode(GL_PROJECTION)
#		glLoadIdentity()
#		gluPerspective(40.0, 1.0, 1.0, 30.0)

#		glMatrixMode(GL_MODELVIEW)
#		glLoadIdentity()
#		gluLookAt(0.0, 0.0, 10.0,
#		          0.0, 0.0, 0.0,
#		          0.0, 1.0, 0.0)

	def OnSize(self, event):
		try:
		    width, height = event.GetSize()
		except:
		    width = event.GetSize().width
		    height = event.GetSize().height
		self.Refresh()
		self.Update()

	def OnMouseMotion(self, event):
		x = event.GetX()
		y = event.GetY()

	def OnDestroy(self, event):
		print "Destroying Window"



class SoongMainFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(500,700), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		#self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.brainPanel = wx.Panel(self, -1, size=(500, 300), style=wx.BORDER_RAISED)
		self.brainCanvas = BrainDisplayCanvas(self.brainPanel)
		#self.sizer.Add(brainPanel)
		#self.SetSizer(self.sizer)
		self.Show(True)

app = wx.App(True)
frame = SoongMainFrame(None, "Soong Neural Network Status")

#frame.Show(True)
app.MainLoop()
