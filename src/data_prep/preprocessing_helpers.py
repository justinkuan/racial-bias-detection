import os
import argparse
import pandas as pd

data_directory = "data/"
raw_filepath = "data/raw/all-the-news-2-1.csv"
    
def remove_empty_articles(dataset):
    '''Remove empty article columns'''
    return dataset[~dataset.article.isna()]

def impute_nans(dataset):
    '''Impute string nans of author and section with "unknown" '''
    dataset.loc[dataset.author.isna(), 'author'] = 'unknown'
    dataset.loc[dataset.section.isna(), 'section'] = 'unknown'
    return dataset

def save_to_parquet(dataset, filename= "subset_first_15000"):
    '''Save first subset as interim file'''
    filepath = os.path.join(data_directory, 'interim', filename)
    dataset.to_parquet(f'{filepath}.gzip', compression='gzip')
    print(f'>>>>> Post processing,  {dataset.shape[0]} rows are stored as {filepath}.gzip')

def load_first_subset(filepath, rows):
    '''Load the first n rows of raw data'''
    dataset = pd.read_csv(filepath, nrows=rows,
                 usecols = ["date","author","title","publication","section","url", "article"],
                 parse_dates=['date'])
    dataset = remove_empty_articles(dataset)
    dataset = impute_nans(dataset)    
    return dataset

def main(filepath=raw_filepath, rows=15000):
    print(f'>>>>> Loading the first {rows} rows from {raw_filepath}')
    df = load_first_subset(filepath, rows)
    save_to_parquet(df, f'subset_first_{rows}')
    
if __name__=="__main__":
    my_parser = argparse.ArgumentParser(description='Reference the data folder')
    my_parser.add_argument('Path', metavar='path', type=str, help='the path to data folder')
    my_parser.add_argument('Rows', type=int, help='the number of rows to load')
    args = my_parser.parse_args()
    filepath, n_rows = args.Path, args.Rows
    main(filepath, n_rows)
    
    