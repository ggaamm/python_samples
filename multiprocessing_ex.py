#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:59:33 2021

@author: gam
"""
import itertools # import combinations
import os
from multiprocessing import Process
import time
import random 


    
def doWork(perm):
    v = random.randint(2, 5)
    print(f"workk {v} sec {os.getpid()}\n")
    time.sleep(v)
    print("dowork done", os.getpid())
        

if __name__=="__main__":
    
   all_perms = itertools.combinations(range(7), 5)
   process_list = []
   print(os.cpu_count())
   for i in range(os.cpu_count()-2):
       p = Process(target=doWork, args=(all_perms,))
       process_list.append(p)
       p.start()

   # do other work here while doWork processes run
   for p in process_list:
        p.join()
   # waits until all processes join
   print("We're done")
