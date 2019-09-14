# Filename: read_musicxml_files_for_ml_dataset_py3.py.py
# Function: study structure of musicxml files in music21 and create ML dataset
#           
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
import music21 as m

scorePath = "~/Documents/sources/python/python3/python3_music21/ml_music21_scores/input_files"
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

# Combine multiple parts to one part by chordifying
chrdfStream = curStream.chordify()
#chrdfStream.show()
chrdfStream.show("text")

# For ML dataset[absolute_time_t, KeySignature, TimeSignature, tempo, Dynamic,  TimeSignature, chord_at_t]
# Because of size of all files use numpy array on disk (.save())
# x =  x[absolute_time_t, KeySignature, TimeSignature, tempo, Dynamic,  TimeSignature]
# y = y[chord_at_t]
 