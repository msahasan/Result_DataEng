#import pandas lib
import pandas as pd

#read data from file
df=pd.read_csv("dataset.csv",sep=",")

# define split function
def split_column_name(dataframe):
    # split the name column into first ,last 
    #    dataframe[['first_name','last_name']] dataframe["name"] = dataframe["name"].str.upper()
    dataframe['first_name']=""
    dataframe['last_name']=""
    dataframe[['first_name','last_name']] = df["name"].str.rsplit(' ',n=1).values.tolist()  
    # remove existing name 
    dataframe['name'].drop(axis=0,inplace=True)
    # And returns them
    return dataframe[['first_name','last_name']]

#define function for remove empty row in name field
def delete_empty_name(dataframe):
    empty_idx=df3[df3['name']=='']
    dataframe.drop(empty_idx.index,axis=0,inplace=True)
    return dataframe

#remove prefix zero in price field in available
def remove_zeros_inprice(dataframe):
    dr_idx=dataframe[dataframe["price"].str.contains('^0.*')]
    dataframe.drop(dr_idx.index,axis=0,inplace=True)
    return dataframe

# create new field in price above 100
def price_above_100(dataframe):
    if "above_100" not in df.columns:
        dataframe["above_100"]=""  
    
    if dataframe["price"] > 100:
        dataframe["above_100"]=dataframe["price"]
        
    return dataframe

#output store on new dataset
def new_dataset(dataframe):
    dataframe.to_csv('dataset_out.csv',index=False)
    
#define pipe line from data processing task    
# Create a pipeline that applies the split name into first name and last name function
(df.pipe(split_column_name)
    # then applies remove function the empty column name function
    .pipe(delete_empty_name)
    # remove prefix zeros on price field
     .pipe(remove_zeros_inprice)
     # add new column price greater than 100
     .pipe(price_above_100)
     # output result set stored to new file
     .pipe(new_dataset)
)
    
    
    