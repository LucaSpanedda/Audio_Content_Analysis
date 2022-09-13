#!/bin/bash

echo "this is the main script!"

echo "plotting the X wav Samples..."
sudo python3 Xwav2txt.py
echo "done!"
echo "plotting the Y wav Samples..."
sudo python3 Ywav2txt.py
echo "done!"
echo "plotting the Z wav Samples..."
sudo python3 Zwav2txt.py
echo "done!"

echo "plotting the X waveform..."
sudo python3 Xtxt2waveform.py
echo "done!"
echo "plotting the Y waveform..."
sudo python3 Ytxt2waveform.py
echo "done!"
echo "plotting the Z waveform..."
sudo python3 Ztxt2waveform.py
echo "done!"

echo "plotting the phase space..."
sudo python3 XYZtxt2phasespace.py
echo "done!"

echo "all done!"