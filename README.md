# enrichr-api

`query_enrichr_v0.1.py`: python script to programmatically enrich your data using Enrichr

- http://amp.pharm.mssm.edu/Enrichr/  


## get it
```bash
## get it
git clone https://github.com/snewhouse/enrichr-api.git 
```

## Usage

```bash
python query_enrichr_v0.1.py <genelist> <listdesrciption> <enrichr_library> <enrichr_results>
```

**Inputs**  
- genelist  
- listdesrciption  
- enrichr_library  
- enrichr_results  

### Example

```bash
## run it
cd enrichr-api
python query_enrichr_v0.1.py gene_list.txt my_test KEGG_2015 KEGG_2015__enrichment
```


## Enrichr Libraries

- http://amp.pharm.mssm.edu/Enrichr/#stats  
- [enrichr_libs_list_June_2016](https://github.com/snewhouse/brain_gene_expression/blob/master/enrichr_api/enrichr_libs_list_June_2016.txt)  
