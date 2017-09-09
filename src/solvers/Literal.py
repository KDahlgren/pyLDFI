#!/usr/bin/env python

'''
Literal.py
  definition of boolean formula consisting only of a single literal
  borrows elements from https://github.com/palvaro/ldfi-py
'''

# **************************************** #

#############
#  IMPORTS  #
#############
# standard python packages
import inspect, os, sys

from BooleanFormula import BooleanFormula

# ------------------------------------------------------ #
# import sibling packages HERE!!!
if not os.path.abspath( __file__ + "/../.." ) in sys.path :
  sys.path.append( os.path.abspath( __file__ + "/../.." ) )

from utilities import tools

# **************************************** #

DEBUG = tools.getConfig( "SOLVERS", "LITERAL_DEBUG", bool )

class Literal( BooleanFormula ) :

  #################
  #  CONSTRUCTOR  #
  #################
  def __init__( self, value ) :

    # BOOLEAN FORMULA CONSTRUCTOR left, right, value
    BooleanFormula.__init__( self, None, None, value )

    if DEBUG :
      print "instantiated Literal with self.value = " + self.value


#########
#  EOF  #
#########
