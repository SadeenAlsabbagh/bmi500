#!/bin/bash

#SBATCH --job-name=pbmc3k
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --output=pbmc3k_output.txt

cd ~/bmi500
source bmi500/bin/activate

/usr/bin/time -v python scanpy_pbmc.py \
    --data-dir data \
    --data-set pbmc3k \
    --out-dir data \
    --num-threads 4
