#!/bin/bash
# script for extract an audio channel from an audio file

echo "insert the wav file name without extension"
read file
for (( ; ; ))
do
   echo "insert the number of the channel you want to extract"
   echo "or exit with ctrl+c if you have done"
   read channel
   sudo sox $file.wav $file-$channel.wav remix $channel
done
