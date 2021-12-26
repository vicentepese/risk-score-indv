#!/bin/bash

module load legacy/scg4
module load plink/1.90

plink --vcf Data/vcf/Stanford_125B3_131_133_to_141.vcf.gz\
    --vcf-half-call missing --double-id --biallelic-only 'strict' --recode --out Data/binary/Stanford_125B3_131_133_to_141