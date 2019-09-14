# Filename: read_musicxml_files_for_ml_dataset_py3.py.py
# Function: study structure of musicxml files in music21 and create ML dataset
#           
#           
# Comment: Use Python 3.6.8 64 bit instead of anaconda python
#          Have to solve how to use music21 with anaconda

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
 