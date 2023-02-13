# Advanced Project - Health Classifier

University project - Carmen Werrlein, Adetola Oluwatayo, Oluwaseyifunmi Alfred Olaniyan, Ben Puhalski

## Resources

CDC - 2021 BRFSS Survey Data [Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)

Description of variables in dataset: [PDF](https://www.cdc.gov/brfss/annual_data/2021/pdf/codebook21_llcp-v2-508.pdf)

## Setup

[Download](https://www.cdc.gov/brfss/annual_data/2021/files/LLCP2021ASC.zip) the dataset and extract into the ``data/`` directory.

## Building html

```bash
jupyter nbconvert --to html main.ipynb ; mv main.html html/index.html
jupyter nbconvert --to html preprocessing.ipynb ; mv preprocessing.html html/pre.html
jupyter nbconvert --to html playground.ipynb ; mv playground.html html/play.html
```
<a href="https://ai.benpuhalski.com">ai.benpuhalski.com</a>

<a href="https://ai.benpuhalski.com">ai.benpuhalski.com/play.html</a>

<a href="https://ai.benpuhalski.com">ai.benpuhalski.com/pre.html</a>
