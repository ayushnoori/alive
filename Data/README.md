# DrugAge Database

The DrugAge database contains an extensive compilation of drugs, compounds and supplements (including natural products and nutraceuticals) with anti-ageing properties that extend longevity in model organisms. We use the fourth build of the DrugAge database, released on November 20, 2021 with 3,265 entries and 1,097 drugs.

For more information, please see the [DrugAge website](https://genomics.senescence.info/drugs/release.html) or:
> Barardo, D. *et al.* The DrugAge database of aging-related drugs. *Aging Cell* **16**, 594–597 (2017). doi: [10.1111/acel.12585](https://doi.org/10.1111/acel.12585)


# Drug ID Mapping

The file `drug-mappings.tsv` (see [source](https://github.com/iit-Demokritos/drug_id_mapping/blob/main/drug-mappings.tsv)) lists thousands of known drugs and IDs available in drug databases. Please see [iit-Demokritos/drug_id_mapping](https://github.com/iit-Demokritos/drug_id_mapping) for more information.

The authors retrieved drug information included in Drugbank (version 5.1.8, released on 2021-01-03) as well as in the latest Therapeutic Target Database (version 7.1.01, released on 2019.07.14) in a file. Then, they add identifiers from the following sources:
*  The web services API of ChEMBL Database.
*  The PUG REST API of PubChem Database.
*  The drugs file in the FTP server of the KEGG Database.
*  The UMLS Metathesaurus vocabulary Database, using the MetamorphoSys tool.
*  The mapping files of the STITCH Database.

For more information, please see:
> Aisopos, F., Paliouras, G. Comparing methods for drug–gene interaction prediction on the biomedical literature knowledge graph: performance versus explainability. *BMC Bioinformatics* **24**, 272 (2023), doi: [10.1186/s12859-023-05373-2](https://doi.org/10.1186/s12859-023-05373-2).