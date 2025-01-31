#!/bin/bash
#SBATCH --array=0-26
#SBATCH --time=05:00:00
#SBATCH --job-name=L6_prod_test
#SBATCH --mem=2G
#SBATCH --output=L6_prod_test-%J.out
#SBATCH --account=rrg-rgmelko-ab

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod_arr2.sh
echo "Starting task $SLURM_ARRAY_TASK_ID (L = 6)"
RB_ID=$((SLURM_ARRAY_TASK_ID % 3 + 1))
BETA_ID=$((SLURM_ARRAY_TASK_ID / 3 + 1))

echo "RB_ID = $RB_ID"
echo "BETA_ID = $BETA_ID"
RB=$(sed -n "${RB_ID}p" rb_list)
echo "Radius $RB"
BETA=$(sed -n "${BETA_ID}p" beta_list)
echo "Beta $BETA"
echo " "

julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta -0.364386792453 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 1"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta -0.128537735849 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 2"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 0.932783018868 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 3"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 1.05070754717 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 4"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 1.16863207547 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 5"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 1.28655660377 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 6"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 1.52240566038 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 7"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 1.75825471698 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 8"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 2.9375 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 9"
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta 3.1733490566 --radius $RB --beta $BETA --measurements 100000 --batches 10
echo "L = 6 beta $BETA Rb $RB delta 10"

echo "qmc program L = 6 beta $BETA Rb $RB completed"


# Omega = 1.0 (default)
# delta = table value/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)
