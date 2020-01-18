@echo off
rem Make .lib import libraries.
rem Requires Visual C++ Studio or Toolkit.
rem vcvars32.bat must be run first to use LINK.EXE.

LINK.EXE /LIB /NOLOGO /DEF:SDL.def /MACHINE:x86 /OUT:SDL.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_ttf.def /MACHINE:x86 /OUT:SDL_ttf.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_image.def /MACHINE:x86 /OUT:SDL_image.lib
LINK.EXE /LIB /NOLOGO /DEF:SDL_mixer.def /MACHINE:x86 /OUT:SDL_mixer.lib
LINK.EXE /LIB /NOLOGO /DEF:freetype.def /MACHINE:x86 /OUT:freetype.lib
LINK.EXE /LIB /NOLOGO /DEF:tiff.def /MACHINE:x86 /OUT:tiff.lib
LINK.EXE /LIB /NOLOGO /DEF:png.def /MACHINE:x86 /OUT:png.lib
LINK.EXE /LIB /NOLOGO /DEF:jpeg.def /MACHINE:x86 /OUT:jpeg.lib
LINK.EXE /LIB /NOLOGO /DEF:webp.def /MACHINE:x86 /OUT:webp.lib
LINK.EXE /LIB /NOLOGO /DEF:mpg123.def /MACHINE:x86 /OUT:mpg123.lib
LINK.EXE /LIB /NOLOGO /DEF:z.def /MACHINE:x86 /OUT:z.lib
LINK.EXE /LIB /NOLOGO /DEF:vorbisfile.def /MACHINE:x86 /OUT:vorbisfile.lib
LINK.EXE /LIB /NOLOGO /DEF:vorbis.def /MACHINE:x86 /OUT:vorbis.lib
LINK.EXE /LIB /NOLOGO /DEF:ogg.def /MACHINE:x86 /OUT:ogg.lib
LINK.EXE /LIB /NOLOGO /DEF:portmidi.def /MACHINE:x86 /OUT:portmidi.lib
rem LINK.EXE /LIB /NOLOGO /DEF:gcc.def /MACHINE:x86 /OUT:gcc.lib
rem LINK.EXE /LIB /NOLOGO /DEF:stdcxx.def /MACHINE:x86 /OUT:stdcxx.lib
