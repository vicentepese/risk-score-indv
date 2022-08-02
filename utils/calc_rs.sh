#!/bin/bash

module load legacy/scg4
module load r 

Rscript PRSice.R --dir /home/vipese/Documents/risk-score-indv/ \
    --prsice /home/vipese/Documents/risk-score-indv/PRSice_linux \
    --pheno /home/vipese/Documents/risk-score-indv/res/pheno.txt \
    --base /home/vipese/Documents/risk-score-indv/res/didriksen_snp.csv --snp SNP --chr CHR --bp POS --A1 EA --A2 OA --stat OR --pvalue PVAL\
    --target /labs/mignot/RLS_RS/IMPUTED_BY_CHR/RLS_GWAS \
    --cov /home/vipese/Documents/risk-score-indv/res/PCA_header.eigenvec --cov-col @PC[1-5]
    --all-score \
    --keep-ambig \
    --thread 1 \
    --stat OR \
    --binary-target T \
    --out risk_score

# Read from json 
OUTDIR=`jq .folder.out opts.json`
mv risk_score* out/