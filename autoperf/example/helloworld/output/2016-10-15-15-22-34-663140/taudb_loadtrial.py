#!/usr/bin/env jython

TAUROOT  = "/home/rsawhney/Desktop/HPC/tau-2.25.1/x86_64"
TAUDB    = "demo"
FILETYPE = "packed"
APPNAME  = "helloworld"
EXPNAME  = "helloworld"
TRIAL    = "2016-10-15-15-22-34-663140"
SOURCE   = "data.ppk"

import os
import sys
import subprocess

from glob import glob

# import all necessary JARs
for jar in glob("%s/lib/*.jar" % TAUROOT):
    sys.path.append(jar)

# so that we can use them here
from edu.uoregon.tau.perfdmf.taudb import TAUdbDatabaseAPI

def is_exist(taudb, trial):
    """
    Check whether the `trial` exist in `taudb`

    Args:
      taudb (string): TAUdb config name
      trial (string): A trial name

    Returns:
      bool: whether `trial` exist in `taudb`
    """

    # connect to `taudb`
    cfg = os.path.expanduser("~/.ParaProf/perfdmf.cfg.%s" % taudb)
    db = TAUdbDatabaseAPI()
    db.initialize(cfg, False)

    # search for the `trial`
    for t in db.getTrialList(False):
        if t.getName() == trial:
            return True

    return False


if __name__ == "__main__":
    if is_exist(TAUDB, TRIAL):
        pass
    else:
        print "*** Loading trial %s to TAUdb ..." % TRIAL
        subprocess.call(["%s/bin/taudb_loadtrial" % TAUROOT,
                         "-f",
                         FILETYPE,
                         "-c",
                         TAUDB,
                         "-a",
                         APPNAME,
                         "-x",
                         EXPNAME,
                         "-n",
                         TRIAL,
                         "%s/%s" % (TRIAL, SOURCE)])
