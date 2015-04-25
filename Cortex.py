import os, sys
import Neuron
import Synapse

class Cortex:
	def __init__(self, brain):
		self.brain = brain
		self.subCortexes = []

	def initNeuralStructure(self):
		return

	def addSubcortex(self, subcortex):
		self.subCortexes.append(subcortex)

class VisualCortex(Cortex):
	def __init__(self, brain):
		Cortex.__init__(brain)
		self.initVisualCortex()

	def initVisualCortex(self):
		return

class Neocortex(Cortex):
	def __init__(self, brain):
		Cortex.__init__(brain)
		this.visualCortex = VisualCortex(this.brain)
		self.addSubcortex(this.visualCortex)