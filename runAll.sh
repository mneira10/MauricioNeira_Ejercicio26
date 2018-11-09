#!/bin/bash

g++ cuenta.c -o cuenta.x

python partir.py

for value in {1,10,20,50,100};
do 
  START=$(($(date +%s%N)/1000000))

  cd "partition"$value

  for ((j = 1; j <= value; j++)); 
  do
    .././cuenta.x "Pi_"$j".dat" cuenta.txt tiempo.txt
  done

  cd ..

  END=$(($(date +%s%N)/1000000))
  dif=$(($END-$START))
  echo $value $dif >> results.dat

  rm -rf "partition"$value
done

rm cuenta.x

python graph.py