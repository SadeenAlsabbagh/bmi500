#!/bin/bash

#SBATCH --job-name=pbmc10k
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --output=pbmc10k_output.txt

cd ~/bmi500
source bmi500/bin/activate

/usr/bin/time -v python scanpy_pbmc.py \
    --data-dir data \
    --data-set pbmc10k \
    --out-dir data \
    --num-threads 4
