![](./pic.png)

# enrichr-api

`query_enrichr_v0.1.py`: python script to programmatically enrich your data using Enrichr

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
## get it
git clone https://github.com/snewhouse/enrichr-api.git 
```

## Usage

```bash
python query_enrichr_v0.1.py <genelist> <listdesrciption> <enrichr_library> <enrichr_results>
```

**Positional Inputs**  
- **genelist**         : flat file with list of genes, one gene id per row
- **listdesrciption**  : name of analysis
- **enrichr_library**  : Enrichr Library to query. See below.
- **enrichr_results**  : out put file prefix

### Enrichr Libraries

- http://amp.pharm.mssm.edu/Enrichr/#stats  
- [enrichr_libs_list_June_2016](https://github.com/snewhouse/brain_gene_expression/blob/master/enrichr_api/enrichr_libs_list_June_2016.txt)  


******

### Example Run

Query `KEGG_2015`  

**Input Options:**

- **genelist**         : gene_list.txt
- **listdesrciption**  : my_test
- **enrichr_library**  : KEGG_2015
- **enrichr_results**  : KEGG_2015__enrichment

The code

```bash
## run it
python query_enrichr_v0.1.py gene_list.txt my_test KEGG_2015 KEGG_2015__enrichment
```

