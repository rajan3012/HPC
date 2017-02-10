#!/usr/bin/env jython

import sys

TAULIB = "{TAULIB}"

sys.path.append(TAULIB+"/perfexplorer.jar")
sys.path.append(TAULIB+"/perfdmf.jar")
sys.path.append(TAULIB+"/tau-common.jar")

from edu.uoregon.tau.perfexplorer.glue import *
from edu.uoregon.tau.perfdmf import Trial
from edu.uoregon.tau.perfexplorer.client import PerfExplorerModel

from java.util import HashSet
from java.util import ArrayList
from java.util.regex import Pattern
from java.util.regex import Matcher

def dump(result):
    threads = result.getThreads()
    events  = result.getEvents()
    metrics = result.getMetrics()

    #change this to event -> thread -> metric
    '''
        for thread in threads:
            for event in events:
                for metric in metrics:
                    data = result.getDataPoint(thread, event, metric, result.EXCLUSIVE)
                    print "%s : %s : %s : %s" % (thread, event, metric, data)
    '''

    #num_of_metrics = 0
    '''
    for metric in metrics:
        num_of_metrics = num_of_metrics +1
    '''
    #just considering FP_OPS
    per_thread_count = []
    max_metric_count = 0
    for event in events:
        for thread in threads:
            temp_count =result.getDataPoint(thread, event, metric, result.EXCLUSIVE)
            per_thread_count.append(temp_count)
            if temp_count > max_metric_count:
                max_metric_count = temp_count
            print "%s : %s : %s : %s" % (thread, event, metric, data)

    threshold = 1.2
    below_threshold = 0
    for single_count in per_thread_count:
        if (single_count/max_metric_count) < threshold:
            below_threshold = below_threshold + 1

    if below_threshold == len(per_thread_count) - 1:
        print "Not parallelized"
    elif below_threshold > 2:
        print "Imbalanced"


 
if __name__ == '__main__':
    #derived_metrics = {derived_metrics}
    #derived_metric = "PAPI_FP_OPS"
    result = DataSourceResult(DataSourceResult.PPK, ["{ppk}"], False)

    dump(result)
'''
    for name, metric in derived_metrics.items():
        d_result = DeriveMetricEquation(result, metric, name).processData()
        map(dump, d_result)
'''
