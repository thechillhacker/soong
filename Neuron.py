import os, sys
import random
import Synapse
import numpy

class Neuron:
	def __init__(self, cortex=None, nVoltage=None, nAch=None, nNE=None, nDA=None, n5HT=None, nGlutamate=None, nGABA=None, nEndorphins=None):
		self.nVoltage = nVoltage if nVoltage != None else random.random()
		self.nAch = nAch if nAch != None else random.random()
		self.nNE = nNE if nNE != None else random.random()
		self.nDA = nDA if nDA != None else random.random()
		self.n5HT = n5HT if n5HT != None else random.random()
		self.nGlutamate = nGlutamate if nGlutamate != None else random.random()
		self.nGABA = nGABA if nGABA != None else random.random()
		self.nEndorphins = nEndorphins if nEndorphins != None else random.random()
		
		this.synapses = []

	def tick(self):
		# this needs to do update, overload, reset operations
		return

	def addSynapse(self, targetNeuron):
		return

	def fireSynapse(self, synapse):
		return

	def backfeedSynapse(self, synapse):
		return