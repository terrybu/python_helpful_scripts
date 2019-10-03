#!/usr/bin/python

"""
Provides support for Logging to files.
"""

from datetime import datetime
from enum import Enum
import os
import sys

class LogLevel(Enum):
    NONE = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    TRACE = 5

class LogFile:
    
    def __init__( self, fileName, logLevel ):
        self.logFile = None
        self.startTime = datetime.now()
        self.logFile = open( "Logs/" + fileName + "_" + self.startTime.strftime( "%Y-%m-%d-%H-%M-%S" ) + ".log", "w" )
        self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [INFO] - Log file opened.\n" )
        self.logFile.flush()
        self.logLevel = logLevel

    def errorLog( self, message ):
        print(message)
        if self.logLevel.value >= LogLevel.ERROR.value:
            self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [ERROR] - " + message + ".\n" )
            self.logFile.flush()

    def warningLog( self, message ):
        print(message)
        if self.logLevel.value >= LogLevel.WARNING.value:
            self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [WARN] - " + message + ".\n" )
            self.logFile.flush()

    def infoLog( self, message ):
        print(message)
        if self.logLevel.value >= LogLevel.INFO.value:
            self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [INFO] - " + message + ".\n" )
            self.logFile.flush()

    def debugLog( self, message ):
        print(message)
        if self.logLevel.value >= LogLevel.DEBUG.value:
            self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [DEBUG] - " + message + ".\n" )
            self.logFile.flush()

    def traceLog( self, message ):
        print(message)
        if self.logLevel.value >= LogLevel.TRACE.value:
            self.logFile.write( datetime.now().strftime( "%Y-%m-%d %H:%M:%S") + " - [TRACE] - " + message + ".\n" )
            self.logFile.flush()




