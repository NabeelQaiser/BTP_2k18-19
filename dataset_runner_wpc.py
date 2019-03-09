import os
import sys
from subprocess import call

datapath = "/home/mridul/Music/BTP-II/PLSQLBenchMarkCode/plSqlCode"     # data-folder-path hardcoded
specpath = "/home/mridul/Music/BTP-II/PLSQLBenchMarkCode/specification"     # spec-folder-path hardcoded

dataList = os.listdir(datapath)
specList = os.listdir(specpath)

counter = 0
print("Work in Progress...\n")
print(" Filename\t\t\tLinesOfCode\tExecutionTime\tNoOfVc\tSatisfiability\tViolatingInstance\n")
for dataFile in dataList:
    specFile = dataFile.split(".")[0].strip() + ".spec"
    if specFile in specList:
        # python3 simulator_wpc.py -datafilename <data-file-name> -data_spec_filepaths <data-file-path> <spec-file-path>
        gh = call(["python3", "simulator_wpc.py", "-datafilename", dataFile, "-data_spec_filepaths", datapath+"/"+dataFile, specpath+"/"+specFile])
        counter = counter + 1
print("\nTotal Files executed =", counter)
