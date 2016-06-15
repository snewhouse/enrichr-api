# enrichr-api

`query_enrichr_v0.1.py`: python script to programmatically enrich your data using Enrichr

******

[Enrichr](http://amp.pharm.mssm.edu/Enrichr)  

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

