#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --job-name=qmc_trial_prod_test
#SBATCH --mem=8G
#SBATCH --output=qmc_trial_prod_test-%J.out
#SBATCH --account=def-rgmelko

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod.sh
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta -0.364386792453 --radius 1.05 --beta 0.5 --measurements 100000 --batches 10 --restart

echo 'qmc program completed'

# L = 5
# Omega = 1.0 (default)
# delta = -0.364386792453 = -1.545/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)

# June 1 3.50 pm
# 6911828
