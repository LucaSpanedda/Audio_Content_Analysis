#!/bin/bash
# analisis and resynthesis of an audio file

echo insert the name of the audio file with extension
read audio
sudo -v
python3 FFT_range.py $audio 20 20000 19980
echo FFT done
echo insert the name of the list file with extension
read audiolist
python3 sort_amplitudes.py $audiolist
echo peak amplitudes sorted
python3 filter_frequencies.py $audiolist
echo peak frequencies extracted
python3 sort_frequencies.py $audiolist
echo frequencies ordered - sorted
python3 resynthesis.py $audiolist
echo resynthesis done 