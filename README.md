# Advanced Project - Health Classifier

University project - Carmen Werrlein, Adetola Oluwatayo, Oluwaseyifunmi Alfred Olaniyan, Ben Puhalski

## Resources

CDC - 2021 BRFSS Survey Data [Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)

Description of variables in dataset: [PDF](https://www.cdc.gov/brfss/annual_data/2021/pdf/codebook21_llcp-v2-508.pdf)

## Setup

1. [Download](https://www.cdc.gov/brfss/annual_data/2021/files/LLCP2021ASC.zip) the dataset and extract into the ``data/`` directory.
2. Run the _top few lines_ of ``reduce.ipynb`` to get **LLCP2021.csv**
3. Run through ``reduce.ipynb`` to get **brfss_reduced.csv**
4. Run through ``data_clean.ipynb`` to get **brfss_clean.csv**
5. Run through ``impute.ipynb`` to get **brfss_imputed.csv**

## Setup Server

```bash
pip install flask
cd public
flask --app server run --debug
```
