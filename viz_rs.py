import seaborn as sns
import pandas as pd 
import json 
from numpy import var, mean, sqrt
from scipy.stats import ttest_ind

def cohend(d1, d2):

	# calculate the size of samples
	n1, n2 = len(d1), len(d2)
	# calculate the variance of the samples
	s1, s2 = var(d1, ddof=1), var(d2, ddof=1)
	# calculate the pooled standard deviation
	s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
	# calculate the means of the samples
	u1, u2 = mean(d1), mean(d2)
	# calculate the effect size

	return (u1 - u2) / s

def main():

    # Read options
    with open('opts.json','r') as infile:
        opts = json.load(infile)

    # Import dataframes and merge
    prs = pd.read_csv(opts['file']['viz_prs'], delimiter = ' ', header=0)
    pheno = pd.read_csv(opts['file']['pheno'], delimiter=' ', names=['FID', 'IID', 'pheno'])  
    prs_pheno = pd.merge(prs, pheno, on=['FID', 'IID'])

    # Count phenos 
    print(prs_pheno.pheno.value_counts())

    # Create histogram
    histogram = sns.histplot(data = prs_pheno, x='PRS', kde=True,  hue="pheno", stat='density', common_norm=False) 
    fig = histogram.get_figure()
    fig.savefig("out.png")  

    # Run t-test
    t_res = ttest_ind(prs_pheno[prs_pheno['pheno'] == 1]['PRS'], prs_pheno[prs_pheno['pheno'] == 2]['PRS'])
    print(t_res)

    # Compute cohen's d 
    cohen_val = cohend(prs_pheno[prs_pheno['pheno'] == 1]['PRS'], prs_pheno[prs_pheno['pheno'] == 2]['PRS'])
    print('Cohen\'s value: '+ str(cohen_val))
    

if __name__ == "__main__":
    main()