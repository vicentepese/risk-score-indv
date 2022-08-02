import numpy as np 
import pandas as pd
import json 

def main():

    # Load options
    with open("opts.json", "r") as inFile:
        opts = json.load(inFile)

    # Import PCA
    pca = pd.read_table(opts['file']['PCA'], sep = ' ',header=None )

    # Add columns
    pca.columns  = ["FID", "IID"] + ["PC" + str(i+1) for i in range(len(pca.columns)-2)]

    # Rewrite
    pca.to_csv("PCA.eigenvec", sep = " ", index=False)


    pass

if __name__ == "__main__":
    main()