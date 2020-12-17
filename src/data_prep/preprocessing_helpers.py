import os
import sys
import argparse
import pandas as pd

data_directory = "../../data/"
default_path = "data/raw/all-the-news-2-1.csv"

def load_first_subset(filepath, rows):
    '''Load the raw data file using the first n rows'''
    dataset = pd.read_csv(filepath, nrows=rows,
                 usecols = ["date","author","title","publication","section","url", "article"],
                 parse_dates=['date'])
    return dataset
    
def remove_empty_articles(dataset):
    '''Remove empty article columns'''
    return dataset[~dataset.article.isna()]

def impute_nans(dataset):
    '''Impute string nans of author and section with "unknown" '''
    dataset.loc[dataset.author.isna(), 'author'] = 'unknown'
    dataset.loc[dataset.section.isna(), 'section'] = 'unknown'

def save_to_parquet(dataset, filename= "subset_1"):
    '''Save first subset as interim file'''
    filepath = os.path.join(data_directory, 'interim', filename)
    dataset.to_parquet(f'{filepath}.gzip', compression='gzip')

def main(filepath=default_path, rows=150000):
    df = load_first_subset(filepath)
    remove_empty_articles(df)
    impute_nans(df)
    save_to_parquet(df)
    print("first subset of data is created!")
    
if __name__=="__main__":
    my_parser = argparse.ArgumentParser(description='Reference the data folder')
    my_parser.add_argument('Path', metavar='path', type=str,
                           help='the path to data folder')
    my_parser.add_argument('Rows', metavar='rows', type=str,
                           help='the number of rows to load')
    args = my_parser.parse_args()
    filepath = args.Path
    n_rows = args.Rows

    main(filepath, n_rows)
    
    