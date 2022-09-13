#!/bin/bash

echo "insert the 3 channel wav file in this folder now"
echo "then insert the wav file name without extension"
echo "...if there is an older directory with the file name will be deletted"
echo "so if you want to exit press ctrl+c now instead of the file name"
read file
sudo rm -r $file-plots

echo "making the plots directory..."
sudo mkdir $file-plots
sudo cp -R pyfiles/. $file-plots/
sudo cp $file.wav $file-plots/
cd $file-plots/

echo "exporting the 3 wav channels..."
sudo sox $file.wav x.wav remix 1
sudo sox $file.wav y.wav remix 2
sudo sox $file.wav z.wav remix 3

echo "launching the main script..."
sudo bash main-py.sh

echo "clearing the plots directory..."
sudo rm -r Xwav2txt.py
sudo rm -r Ywav2txt.py
sudo rm -r Zwav2txt.py
sudo rm -r Xtxt2waveform.py
sudo rm -r Ytxt2waveform.py
sudo rm -r Ztxt2waveform.py
sudo rm -r XYZtxt2phasespace.py
sudo rm -r main-py.sh

echo "all done!"
echo "end of the script"