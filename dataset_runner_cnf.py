import os
import sys
from subprocess import call

# datapath = "/home/nabeel/PycharmProjects/PLSQLBenchMarkCode/PLSQLBenchMarkCode1/plSqlCode"     # data-folder-path hardcoded
# specpath = "/home/nabeel/PycharmProjects/PLSQLBenchMarkCode/PLSQLBenchMarkCode1/specification"     # spec-folder-path hardcoded
datapath = "/home/mridul/Music/BTP-II/nabeel_dataset/latest_dataset/plSqlCode"     # data-folder-path hardcoded
specpath = "/home/mridul/Music/BTP-II/nabeel_dataset/latest_dataset/specification"     # spec-folder-path hardcoded

dataList = os.listdir(datapath)
specList = os.listdir(specpath)

counter = 0
print("Work in Progress for CNF...\n")
print(" Filename\t\t\tLinesOfCode\tExecutionTime\tNoOfVc\tSatisfiability\tViolatingInstance\n")
for dataFile in dataList:
    specFile = dataFile.split(".")[0].strip() + ".spec"
    if specFile in specList:
        # python3 simulator_wpc.py -datafilename <data-file-name> -data_spec_filepaths <data-file-path> <spec-file-path>
        gh = call(["python3", "simulator_cnf.py", "-datafilename", dataFile, "-data_spec_filepaths", datapath+"/"+dataFile, specpath+"/"+specFile])
        counter = counter + 1
print("\nTotal Files executed =", counter)
