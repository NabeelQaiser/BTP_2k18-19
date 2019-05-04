import os
import sys
import datetime
from SeAPI.TesterClassForSeApi import TesterClassForSeApi


def execute(dataFileName, specFileName):
    pwd = os.getcwd()
    pwd = pwd + "/"
    seApiObj = TesterClassForSeApi()

    # recording startTime1
    startTime1 = datetime.datetime.now()

    linesOfCode, noOfVc = seApiObj.execute(dataFileName, specFileName, pwd)

    # recording endTime1
    endTime1 = datetime.datetime.now()

    print("////// Execution completed for file :", dataFileName)
    print("No. of VCs =", noOfVc)
    print("Time Taken =", (endTime1-startTime1).total_seconds())
    print("LinesOfCode =", linesOfCode)






def main(argv):
    if len(argv) < 3:
        print("Not Enough Arguments. Exiting...")
    elif len(argv) == 3:        # python3 simulator_se_api.py <data-file-name> <spec-file-name>
        dataFileName = argv[1]    # given data-file must be +nt in "SeApi/gen/data/"
        specFileName = argv[2]    # given spec-file must be +nt in "SeApi/specification/"
        execute(dataFileName, specFileName)
    elif len(argv) == 6:        # not working
        if argv[3] == "-data_spec_filepaths":
            print("\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



if __name__ == '__main__':
    main(sys.argv)

