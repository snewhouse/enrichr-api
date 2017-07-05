![](pic.png)

# enrichr-api

`query_enrichr_py*.py` : python scripts to programmatically enrich your data using Enrichr

*Note: all credit goes to the Enrichr folks...I just stuck their examples from http://amp.pharm.mssm.edu/Enrichr/help#api together*

[![DOI](https://zenodo.org/badge/61207176.svg)](https://zenodo.org/badge/latestdoi/61207176)

******

## **Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool.**  
BMC Bioinformatics. 2013 Apr 15;14:128. doi: 10.1186/1471-2105-14-128   
[PMID: 23586463 [PubMed - indexed for MEDLINE] PMCID: PMC3637064] (http://www.ncbi.nlm.nih.gov/pubmed/23586463)  

>Enrichr, ia an integrative web-based and mobile software application that includes new gene-set libraries, an alternative approach to rank enriched terms, and various interactive visualization approaches to display enrichment results using the JavaScript library, Data Driven Documents (D3). The software can also be embedded into any tool that performs gene list analysis. 
>Enrichr is an easy to use intuitive enrichment analysis web-based tool providing various types of visualization summaries of collective functions of gene lists. 

Enrichr is open source and freely available online at: [http://amp.pharm.mssm.edu/Enrichr](http://amp.pharm.mssm.edu/Enrichr) .

**********

## get it

```bash
git clone https://github.com/snewhouse/enrichr-api.git 
```

## Usage

#### python versin 2+
```bash
python query_enrichr_p2.py <genelist> <listdesrciption> <enrichr_library> <enrichr_results>
```

#### python version 3+
```bash
python query_enrichr_p3.py <genelist> <listdesrciption> <enrichr_library> <enrichr_results>
```

**Positional Inputs**  
- **genelist**         : flat file with list of genes, one gene id per row
- **listdesrciption**  : name of analysis
- **enrichr_library**  : Enrichr Library to query. See below.
- **enrichr_results**  : out put file prefix

## Requirements
- python 

Tested with Python 2.7.11  
Tested with Python 3.5.1 :: Anaconda 4.0.0 (x86_64)

## Enrichr Libraries

- http://amp.pharm.mssm.edu/Enrichr/#stats  
- [enrichr_libs_list_June_2016](https://github.com/snewhouse/brain_gene_expression/blob/master/enrichr_api/enrichr_libs_list_June_2016.txt)  


******

## Example Run

Query `KEGG_2015`  

**Input Options:**

- **genelist**         : gene_list.txt
- **listdesrciption**  : my_test
- **enrichr_library**  : KEGG_2015
- **enrichr_results**  : KEGG_2015__enrichment

The code

```bash
## run it
python query_enrichr_p3.py gene_list.txt my_test KEGG_2015 KEGG_2015__enrichment
```

