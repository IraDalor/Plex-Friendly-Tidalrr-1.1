#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/10/25
@Author  :   Jacob Roy
@Contributor: Ethan Paffe
@Version :   1.1
@Contact :   lejacobroy@gmail.com
@Desc    :   
'''
from multiprocessing import Process
from runWebServer import webServer
from runSchedule import mainSchedule

def main():
    print("Starting tidalrr app", flush=True)
    processes = []

    process1 = Process(target=webServer, args=(False,))
    process2 = Process(target=mainSchedule)
    #process2 = Process(target=mainScansSchedule)
    #process3 = Process(target=mainDownloadsSchedule)

    processes.extend([process1, process2])

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()