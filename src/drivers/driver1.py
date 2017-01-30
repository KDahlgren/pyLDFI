#!/usr/bin/env python

'''
driver1.py
  A driver exemplifying the orchestration of the
  implemented LDFI workflow.
'''

# **************************************** #

#############
#  IMPORTS  #
#############
# standard python packages
import os, sys

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../.." )
sys.path.append( packagePath )

from dedt       import dedt, dedalusParser
from derivation import provTree
from utils      import parseCommandLineInput
from evaluators import c4_evaluator

# **************************************** #

DRIVER_DEBUG = True
DEV_HACK     = True

################
#  PARSE ARGS  #
################
# parse arguments from the command line
def parseArgs( ) :
  argDict = {}   # empty dict

  argDict = parseCommandLineInput.parseCommandLineInput( )  # get dictionary of arguments.

  return argDict

####################
#  PASS TO SOLVER  #
####################
# pass dedalus programs and arguments to solver
def passToSolver() :
  print " ... In passToSolver ..."
  #

####################
#  OUTPUT RESULTS  #
####################
# output results =]
def outputResults() :
  print " ... In outputResults ..."
  #

############
#  DRIVER  #
############
def driver() :
  # get list of command line args, except prog name
  argList = sys.argv[1:]

  # print help if no args provided
  if( len(argList) < 1 ) :
    thisFilename = os.path.basename(__file__)     # name of this file
    print "No arguments provided. Please run 'python " + sys.argv[0] + " -h' for assistance."
    sys.exit()

  # ----------------------------------------------- #

  # pass list to parse args, get dict of args
  argDict = parseArgs( )
  print argDict

  # ----------------------------------------------- #

  # translate all input dedalus files into a single datalog program
  outputs         = dedt.translateDedalus( argDict )
  tableListPath   = outputs[0] # string of table names
  datalogProgPath = outputs[1] # path to datalog program
  irCursor        = outputs[2] # ir db cursor
  saveDB          = outputs[3] # ir db save file

  if DRIVER_DEBUG :
    print "outputs              = " + str( outputs )
    print "table   list    path = " + tableListPath
    print "datalog program path = " + datalogProgPath

  # ----------------------------------------------- #

  # run through evaluator
  resultsPath = None
  #resultsPath = c4_evaluator.runC4_directly( datalogProgPath, tableListPath )
  #c4_evaluator.runC4_wrapper( datalogProgPath, tableListPath )

  # ----------------------------------------------- #

  # if buggy => output results
  # else => ...

  # ----------------------------------------------- #
  # get provenance trees

  if DEV_HACK :
    resultsPath = "/Users/KsComp/projects/pyldfi/src/derivation/testData.txt"
    print "driver1.py DEV_HACK True : resultsPath = " + resultsPath

  if resultsPath :
    parsedResults = provTree.getEvalResults_file( resultsPath )

    provTreeComplete = []
    for seedRecord in parsedResults[ "post" ] :
      if DRIVER_DEBUG :
        print "seedRecord = " + str( seedRecord )
      newProvTree = provTree.generateProvTree( seedRecord, parsedResults, irCursor )
      provTreeComplete.append( newProvTree )

    # -------------------------------------------- #
    # cleanUp saved db stuff
    dedt.cleanUp( irCursor, saveDB )

    # -------------------------------------------- #
    # sanity check
    print "PROGRAM EXITED SUCCESSFULLY"

  else :
    sys.exit( "SHIT GOT BUGGY" ) # sanity check


#########################
#  THREAD OF EXECUTION  #
#########################
driver()


#########
#  EOF  #
#########
