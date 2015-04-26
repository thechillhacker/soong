#!/usr/bin/python2.7
import os, sys
import random
import numpy
import wx, math
import Brain

try:
    from wx import glcanvas
    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    # The Python OpenGL package can be found at
    # http://PyOpenGL.sourceforge.net/
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    haveOpenGL = False

#----------------------------------------------------------------------


class BrainSlider(wx.Panel):
	def __init__(self, parent, inText, ctrlVar):
		wx.Panel.__init__(self, parent, size=(500, 50))
		self.minVal = 0.00
		self.maxVal = 1.00
		self.ctrlVar = ctrlVar
		self.grid = wx.GridSizer(rows=2, cols=2, hgap=5, vgap=5)
		self.label = wx.StaticText(self, wx.ID_ANY, label=inText, style=wx.ALIGN_LEFT)
		self.grid.Add(self.label, 0, 0)
		self.spinCtrl = wx.SpinCtrlDouble(self, value=str(self.ctrlVar), inc=0.001, min=self.minVal, max=self.maxVal)
		self.spinCtrl.SetDigits(4)

		self.grid.Add(self.spinCtrl, 0, 0)

		self.SetSizer(self.grid)
		#self.Show(True)

class BrainDisplayCanvas(glcanvas.GLCanvas):
	def __init__(self, parent):
		self.init = None
		glcanvas.GLCanvas.__init__(self, parent, -1, attribList=[wx.glcanvas.WX_GL_DOUBLEBUFFER], size=(500,300))
		self.context = glcanvas.GLContext(self)
		wx.EVT_PAINT(self, self.OnDraw)
		wx.EVT_SIZE(self, self.OnSize)
		wx.EVT_MOTION(self, self.OnMouseMotion)
		wx.EVT_WINDOW_DESTROY(self, self.OnDestroy)
		self.init = True

	def OnDraw(self,event):
		self.SetCurrent(self.context)

		if not self.init:
		    self.InitGL()
		    self.init = False

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()

		radius = 1.0
		x = radius*math.sin(0)
		y = radius*math.cos(0)
		glColor(0.0, 1.0, 0.0)
		glBegin(GL_LINE_STRIP)
		for deg in xrange(1000):
			glVertex(x, y, 0.0)
			rad = math.radians(deg)
			radius -= 0.001
			x = radius*math.sin(rad)
			y = radius*math.cos(rad)
		glEnd()

		glEnableClientState(GL_VERTEX_ARRAY)

		spiral_array = []

		# Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
		radius = 0.8
		x = radius*math.sin(0)
		y = radius*math.cos(0)
		glColor(1.0, 0.0, 0.0)
		for deg in xrange(820):
			spiral_array.append([x,y])
			rad = math.radians(deg)
			radius -= 0.001
			x = radius*math.sin(rad)
			y = radius*math.cos(rad)

		glVertexPointerf(spiral_array)
		glDrawArrays(GL_LINE_STRIP, 0, len(spiral_array))


		glFlush()
		self.SwapBuffers()

	def InitGL(self):
		'''
		Initialize GL
		'''
		#return
		# set viewing projection
		glClearDepth(1.0)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(40.0, 1.0, 1.0, 30.0)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(0.0, 0.0, 10.0,
		          0.0, 0.0, 0.0,
		          0.0, 1.0, 0.0)

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

class WindowUpdateTimer():

class SoongMainFrame(wx.Frame):
	def __init__(self, parent, title):
		self.brain = Brain.Brain()
		wx.Frame.__init__(self, parent, title=title, size=(500,800), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.brainPanel = wx.Panel(self, -1, size=(500, 300), style=wx.BORDER_RAISED)
		self.brainCanvas = BrainDisplayCanvas(self.brainPanel)
		self.sizer.Add(self.brainPanel)
		
		control_data = [['Sys. Voltage', self.brain.systemVoltage],
			['Sys. Acetylcholine (Ach)', self.brain.systemAch],
			['Sys. Norepinephrine (NE)', self.brain.systemNE],
			['Sys. Dopamine (DA)', self.brain.systemDA],
			['Sys. Serotonin (5HT)', self.brain.system5HT],
			['Sys. Glutamate', self.brain.systemGlutamate],
			['Sys. Gamma-aminobutyric acid (GABA)', self.brain.systemGABA],
			['Sys. Endorphins', self.brain.systemEndorphins]]
		self.sliderControls = {}
		for akey, acontrol in control_data:
			w = BrainSlider(parent=self, inText=akey, ctrlVar=acontrol)
			self.sliderControls[akey] = w
			self.sizer.Add(self.sliderControls[akey])
		self.SetSizer(self.sizer)
		self.Show(True)

app = wx.App(True)
frame = SoongMainFrame(None, "Soong Neural Network Status")

#frame.Show(True)
app.MainLoop()
