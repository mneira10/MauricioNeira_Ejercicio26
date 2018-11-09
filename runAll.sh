#!/bin/bash

g++ cuenta.c -o cuenta.x -std=c++11

python partir.py

for value in {1,10,20,50,100};
do 

  cd "partition"$value

  for ((j = 1; j <= value; j++)); 
  do
    .././cuenta.x "Pi_"$j".dat" cuenta.txt tiempo.txt &
  done

  cd ..

  sleep 2
  echo "copying time values to tiempoPart"$value"proc"$1".txt"
  cat ./"partition"$value/tiempo.txt >> ./"tiempoPart"$value"proc"$1".txt"

  rm -rf "partition"$value
done

rm cuenta.x

python graph.py
