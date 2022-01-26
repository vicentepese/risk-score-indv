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

    # Get risk score of patients with phenotype 
    pheno = pd.read_table(opts['file']['pheno'], sep =' ', header=None)
    pheno.columns = ['FID','IID', 'pheno']
    prs = pd.read_table(opts['file']['prs'], sep = ' ')

    # Filter 
    prs_filt = prs[prs.FID.isin(pheno['FID'])]

    # Write 
    prs_filt.to_csv('prs.csv', sep = ' ', header=True, index=False)





if __name__ == "__main__":
    main()