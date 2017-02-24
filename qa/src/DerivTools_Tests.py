#!/usr/bin/env python

'''
DerivTools_Tests.py
  Defines unit tests for derivTools.
'''

#############
#  IMPORTS  #
#############
# standard python packages
import os, sys, unittest

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../../../src" )
sys.path.append( packagePath )

from derivTools import *
# ------------------------------------------------------ #


######################
#  DERIVTOOLS TESTS  #
######################
class DerivTools_Tests( unittest.TestCase ) :

  def test__derivTools( self ) :
    return None

 
#########################
#  THREAD OF EXECUTION  #
#########################
# use this main if running this script exclusively.
if __name__ == "__main__" :
  unittest.main( verbosity=2 )


#########
#  EOF  #
#########