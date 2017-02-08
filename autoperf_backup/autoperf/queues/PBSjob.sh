#!/bin/bash
#
#PBS -N autoperf.cn110.22073
#PBS -o 2017-02-01-13-37-44-617802/pbs.log
#PBS -e 2017-02-01-13-37-44-617802/pbs.log
#PBS -j oe


export PATH=/home16/rsawhney/tau/tau-2.26/x86_64/bin:$PATH

cd $PBS_O_WORKDIR
NP=$(wc -l $PBS_NODEFILE | awk '{print $1}')

echo cwd: `pwd`
echo NP : $NP
echo PBS_NP: $PBS_NP

# mark the job as running
echo -n "pi 2017-02-01-13-37-44-617802 PBS:$PBS_JOBID Running" >2017-02-01-13-37-44-617802/.iter-00/.job.stat

# setup the environment for the experiment
# Generic environment variables
export OMP_NUM_THREADS=1
# TAU environment variables
export TAU_VERBOSE=1
export TAU_METRICS=PAPI_FP_INS:PAPI_L3_TCM:PAPI_TOT_CYC:PAPI_L1_DCM:PAPI_TOT_INS
export PROFILEDIR=2017-02-01-13-37-44-617802/.iter-00/profiles


# run the experiment
tau_exec -T papi,pdt,mpi -ebs -ebs_period=10000 -ebs_source=TIME ../pi 10000000 2>&1 | tee 2017-02-01-13-37-44-617802/.iter-00/job.log

# mark the job as finished
echo -n "pi 2017-02-01-13-37-44-617802 PBS:$PBS_JOBID Finished" >2017-02-01-13-37-44-617802/.iter-00/.job.stat

# notify autoperf that we are done
# ssh cn110 kill -SIGUSR1 22073
