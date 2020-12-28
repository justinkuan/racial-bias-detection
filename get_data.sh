#!/bin/bash
# Create a subset of news data, default to first ~15000 rows
python ./src/data_prep/preprocessing_helpers.py -f -r
# Add labels to subset using topic modeling
python ./src/date_prep/topic_modeling_helpers.py
