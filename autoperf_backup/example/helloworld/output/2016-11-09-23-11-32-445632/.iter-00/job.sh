#!/bin/sh
export PATH=/home/rsawhney/Desktop/HPC/tau-2.25.1/x86_64/bin:$PATH

# mark the job as running
echo -n "helloworld 2016-11-09-23-11-32-445632 serial:$$ Running" >2016-11-09-23-11-32-445632/.iter-00/.job.stat

# setup the environment for the experiment
# Generic environment variables
export OMP_NUM_THREADS=1
# TAU environment variables
export TAU_VERBOSE=1
export TAU_METRICS=PAPI_TOT_INS:PAPI_TOT_CYC
export PROFILEDIR=2016-11-09-23-11-32-445632/.iter-00/profiles


# run the experiment
tau_exec -T papi,pdt,serial -ebs -ebs_period=10000 -ebs_source=TIME ../helloworld 2>&1 | tee 2016-11-09-23-11-32-445632/.iter-00/job.log

# mark the job as finished
echo -n "helloworld 2016-11-09-23-11-32-445632 serial:$$ Finished" >2016-11-09-23-11-32-445632/.iter-00/.job.stat
