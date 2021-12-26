import numpy as np 
import pandas as pd 
import json 
import subprocess

def main():
    
    # Read options 
    with open('opts.json','r') as inFile:
        opts = json.load(inFile)

    # Compute risk score 
    if opts['keep_ambiguous']:
        bashCommand = "bash utils/calc_rs.sh"
    else:
        bashCommand = "bash utils/calc_rs_ignore_amb.sh"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()





if __name__ == "__main__":
    main()