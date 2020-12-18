import os
import argparse
import pandas as pd

data_directory = 'data'
raw_filepath = os.path.join(os.path.relpath('.'), 'data', 'raw', 'all-the-news-2-1.csv')
    
def convert_os_filepath(filepath):
    '''Replace Windows-style ".\\" filepath into linux-style "./"'''
    return filepath.replace('\\','/')

def remove_empty_articles(dataset):
    '''Remove empty article columns'''
    return dataset[~dataset.article.isna()]

def impute_nans(dataset):
    '''Impute string nans of author and section with "unknown" '''
    dataset.loc[dataset.author.isna(), 'author'] = 'unknown'
    dataset.loc[dataset.section.isna(), 'section'] = 'unknown'
    return dataset

def load_first_subset(filepath, rows):
    '''Load the first n rows of raw data'''
    filepath = convert_os_filepath(filepath)
    dataset = pd.read_csv(filepath, nrows=rows,
                 usecols = ["date","author","title","publication","section","url", "article"],
                 parse_dates=['date'])
    dataset = remove_empty_articles(dataset)
    dataset = impute_nans(dataset)    
    return dataset

def save_to_parquet(dataset, filename= "subset_first_15000"):
    '''Save first subset as interim file'''
    filepath = os.path.join(data_directory, 'interim', filename)
    dataset.to_parquet(f'{filepath}.gzip', compression='gzip')
    print(f'>>>>> Post processing,  {dataset.shape[0]} rows are stored as {filepath}.gzip')

def main(filepath=raw_filepath, rows=15000):
    print(f'>>>>> Loading the first {rows} rows from {raw_filepath}')
    df = load_first_subset(filepath, rows)
    save_to_parquet(df, f'subset_first_{rows}')
    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Load n_rows of allnews dataset from data folder')
    parser.add_argument('-f', '--filepath', action='store_const', const=raw_filepath, 
                        help='path to data folder')
    parser.add_argument('-r', '--rows', action='store_const', const=15000, 
                        help='number of rows to load')
    args = parser.parse_args()
    filepath, n_rows = vars(args)['filepath'], vars(args)['rows']

    main(filepath, n_rows)
