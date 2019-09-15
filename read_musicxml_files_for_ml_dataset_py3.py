# Filename: read_musicxml_files_for_ml_dataset_py3.py.py
# Function: study structure of musicxml files in music21 and create ML dataset
#           
# Comment: When using anaconda python use following installation steps to installa music21 library in anaconda python
#          See: https://stackoverflow.com/questions/36164986/how-to-install-package-in-anaconda
#               https://pypi.org/project/music21/
#               @ 20190609 5.7.0 latest version
#               Installation steps music21 in anaconda:
#               1. download latest tar.gz file for music21 libaray
#               2. unzip tar.gz
#               3. cd to unzip directory
#               4. in uzip directory execute command:
#                  python setup.py install
#               
import types
import music21 as m

scorePath = "~/Documents/sources/python/python3/python3_ml_music21_scores/input_files"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "TestScore.musicxml"

outputFormat = 'musicxml'
outputFileDFLT = scorePath+'/output.'+outputFormat

# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/usr/bin/musescore3'

curStream = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')
#curStream.show("text")

def getOffsets (stream):
    offsetsList = []
    for e in stream.recurse():
        offsetsList.append(e.offset)
    return(offsetsList)
# getOffsets

def getOffsetsAndElements(stream):
    offsetsList = []
    for e in stream.recurse():
        l = [e.offset, e]
        offsetsList.append(l)
    return(offsetsList)
# getOffsetsAndElements

def getOffsetsAndChords(stream):
    offsetsList = []
    for e in stream.recurse():
        # Pick only ChordObjects
        if type(e) is m.chord.Chord:
           l = [e.offset, e, e.fullName, e.pitchedCommonName, e.commonName]
           offsetsList.append(l)
    return(offsetsList)
# getOffsetsAndChords


def getMeasureObjects (stream):
    return(list(stream.iter.getElementsByClass("Measure")))
# getMeasureObjects

def getOffsetsAndMeasures(stream):
    offsetsList = []
    for e in chrdfStream.recurse():
        # Pick only MeasureObjects
        if type(e) is m.stream.Measure:
           l = [e.offset, "M"+str(e.number)]
           offsetsList.append(l)
    return(offsetsList)
# getOffsetsAndMeasures

### ToDo ###
### ???  create function for timeSignature
### ???  create function for KeySignature # be aware KeySignature change in a Measures
###      of a Score, so create [[offset,KeySignature ], ..]



# Combine multiple parts to one part by chordifying
chrdfStream = curStream.chordify()

print("aantal elementen in chrdfStream len(chrdfStream)", len(chrdfStream))
print("")
print("offsets(chrdfStream): ", getOffsets(chrdfStream))
print("")
print("getOffsetsAndElements(chrdfStream): ", getOffsetsAndElements(chrdfStream))
print("")

print("getMeasureObjects(chrdfStream)", getMeasureObjects(chrdfStream))
print("")
print("getOffsetsAndMeasures(chrdfStream)", getOffsetsAndMeasures(chrdfStream))
print("")
print("getOffsetsAndChords(chrdfStream)", getOffsetsAndChords(chrdfStream))
print("")

#chrdfStream.show()
chrdfStream.show("text")

# For ML dataset[absolute_time_t, KeySignature, TimeSignature, tempo, Dynamic,  TimeSignature, chord_at_t]
# Because of size of all files use numpy array on disk (.save())
# x =  x[absolute_time_t, KeySignature, TimeSignature, tempo, Dynamic,  TimeSignature]
# y = y[chord_at_t]
 