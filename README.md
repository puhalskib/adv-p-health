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

## Building html

```bash
jupyter nbconvert --to html reduce.ipynb ; mv reduce.html html/reduce.html
jupyter nbconvert --to html data_clean.ipynb ; mv data_clean.html html/data_clean.html
jupyter nbconvert --to html impute.ipynb ; mv impute.html html/impute.html
jupyter nbconvert --to html class_model_evaluation.ipynb ; mv class_model_evaluation.html html/class_model_evaluation.html
jupyter nbconvert --to html make_prediction.ipynb ; mv make_prediction.html html/make_prediction.html
```
<a href="https://ai.benpuhalski.com/reduce.html">ai.benpuhalski.com/reduce.html</a>

<a href="https://ai.benpuhalski.com/data_clean.html">ai.benpuhalski.com/data_clean.html</a>

<a href="https://ai.benpuhalski.com/impute.html">ai.benpuhalski.com/impute.html</a>

<a href="https://ai.benpuhalski.com/class_model_evaluation.html">ai.benpuhalski.com/class_model_evaluation.html</a>

<a href="https://ai.benpuhalski.com/make_prediction.html">ai.benpuhalski.com/make_prediction.html</a>