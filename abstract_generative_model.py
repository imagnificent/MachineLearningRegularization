from abc import ABCMeta, abstractmethod

class Trainable(object):  
   __metaclass__ = ABCMeta

   @abstractmethod
   def build_model(self):    
       pass
   
   def train(self):    
       pass
