#!/bin/bash
#PBS -l nodes=1:ppn=1,mem=1gb,walltime=00:10:00
#PBS -M m.neira10@uniandes.edu.co
#PBS -m abe
#PBS -N mneira10_testSubmission
#PBS -j oe


module load gcc/4.9.4
module load anaconda/python3
cd /hpcfs/home/fisi4028/m.neira10/MauricioNeira_Ejercicio26
./runAll.sh 1
