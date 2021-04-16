#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:59:33 2021

@author: gam
"""
#import itertools # import combinations
import os
from multiprocessing import Process
import time
import random 
from itertools import combinations

    
def doWork(all_perms, cpu_id, per_process_element_size):
    v = random.randint(2, 5)
    perm = all_perms[cpu_id * per_process_element_size: (cpu_id+1) * per_process_element_size]
    print(f"workk {perm} id {cpu_id} per_process {per_process} {v} sec {os.getpid()}\n")
    time.sleep(v)
    print(f"dowork done id {cpu_id}", os.getpid())
        

if __name__=="__main__":
    
   all_perms = list(combinations(range(7), 5))
   process_list = []
   # per_process_element
   per_process_element_size = len(all_perms) // (os.cpu_count() - 1)
   print("per process", per_process)
   for i in range(os.cpu_count()-1):
       p = Process(target=doWork, args=(all_perms, i, per_process))
       process_list.append(p)
       p.start()

   # do other work here while doWork processes run
   for p in process_list:
        p.join()
   # waits until all processes join
   print("We're done")
