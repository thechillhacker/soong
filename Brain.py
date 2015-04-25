import os, sys
import Neuron
import Synapse
import Cortex
import random
import pysqlite2


class Brain:
	def __init__(self, brainMap=None, systemVoltage=None, systemAch=None, systemNE=None, systemDA=None, system5HT=None, systemGlutamate=None, systemGABA=None, systemEndorphins=None):
		self.NeuronCount = 0

		self.systemVoltage = systemVoltage if systemVoltage != None else random.random()
		self.systemAch = systemAch if systemAch != None else random.random()
		self.systemNE = systemNE if systemNE != None else random.random()
		self.systemDA = systemDA if systemDA != None else random.random()
		self.system5HT = system5HT if system5HT != None else random.random()
		self.systemGlutamate = systemGlutamate if systemGlutamate != None else random.random()
		self.systemGABA = systemGABA if systemGABA != None else random.random()
		self.systemEndorphins = systemEndorphins if systemEndorphins != None else random.random()

		self.Neocortex = Cortex.Neocortex(brain=this) # higher cognative array - higher order pattern matching, analysis and social, primary memory store
		self.LimbicCluster = Cortex.LimbicCluster(brain=this) # regulates system timing, electrical, and NT levels - regulates mood/emotion
		self.Cerebellum = Cortex.Cerebellum(brain=this) # primary io matrix - will handle direct sensory input, and motor/data output

		if brainMap == None:
			self.initNeuralStructure()
		else:
			loadBrainMap(brainMap=brainMap)

	# need methods to associate/export neural i/o pathways to/from the cortexes
	def initNeuralStructure(self):
		self.Neocortex.initNeuralStructure()
		self.LimbicCluster.initNeuralStructure()
		self.Cerebellum.initNeuralStructure()

	def loadBrainMap(self, brainMap):
		return

	def saveBrainMap(self):
		return

	def tick(self):
		return
