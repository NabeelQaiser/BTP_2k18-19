import os
import sys
from subprocess import call

datapath = "/home/mridul/Music/BTP-II/dataSetForMC/PLSQLBenchMarkCode/plSqlCode"     # data-folder-path hardcoded
specpath = "/home/mridul/Music/BTP-II/dataSetForMC/PLSQLBenchMarkCode/specification"     # spec-folder-path hardcoded

dataList = os.listdir(datapath)
specList = os.listdir(specpath)

counter = 0
print("Work in Progress for WPC...\n")
# print(" Filename\t\t\tLinesOfCode\tExecutionTime\tNoOfVc\tSatisfiability\tViolatingInstance\n")
for dataFile in dataList:
    specFile = dataFile.split(".")[0].strip() + ".spec"
    if specFile in specList:
        # python3 simulator_mc.py <data-file-name> <spec-file-name> -data_spec_filepaths <data-file-path> <spec-file-path>
        # call(["python3", "simulator_mc.py", dataFile, specFile, "-data_spec_filepaths", datapath+"/"+dataFile, specpath+"/"+specFile])
        command = "python3 simulator_mc.py " + dataFile + " " + specFile + " -data_spec_filepaths " + datapath+"/"+dataFile + " " + specpath+"/"+specFile
        os.system(command)
        counter = counter + 1
print("\nTotal Files executed =", counter)
