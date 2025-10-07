# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is developed by a student. It uses random trees in scikit-learn 1.5.1.

## Intended Use

This model uses various demographic information to classify whether an individual would or would not have an income of $50k per year.

## Training Data
The data was provided by the US Census Beureau:
https://archive.ics.uci.edu/ml/datasets/census+income

## Evaluation Data

20% of the source data was used as the test set.

## Metrics

The following metrics were used to score the model:
Precision: 0.7384
Recall: 0.6378
F1: 0.6844

## Ethical Considerations
The data collected by the Census Beureau may or may not have been collected ethically or willingly. This model can be used on data that may or may not be ethically or willingly collected.

## Caveats and Recommendations
The data the model was trained on may be biased and can influence the output. Caution is recommended.