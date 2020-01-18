@echo off
rem Builds the Visual C x86 import libraries.
rem Requires gendef (see MakeDefs.bat) and vcvars32.bat on
rem the executable search path.

CALL vcvars32.bat
CALL MakeDefs.bat
CALL MakeLibs.bat
