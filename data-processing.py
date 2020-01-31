#import pandas lib
import pandas as pd

#read data from file
df=pd.read_csv("dataset.csv",sep=",")

# define split function
def split_column_name(dataframe):
    # split the name column into first ,last 
    dataframe['first_name']=""
    dataframe['last_name']=""
    dataframe[['first_name','last_name']] = dataframe["name"].str.rsplit(' ',n=1).values.tolist()  
    # remove existing name 
    dataframe.drop(['name'],axis=1,inplace=True)
    # And returns them
    return dataframe[['first_name','last_name']]

#define function for remove empty row in name field
def delete_empty_name(dataframe):
    empty_idx=dataframe[dataframe['name']=='']
    dataframe.drop(empty_idx.index,axis=0,inplace=True)
    return dataframe

#remove prefix zero in price field in available
def remove_zeros_inprice(dataframe):
    df.astype({'price': 'int32'}).dtypes
    return dataframe

# create new field in price above 100
def price_above_100(dataframe):
    try:
        if "above_100" not in df.columns:
            dataframe["above_100"]=""  
#         else:
#             dataframe["above_100"]=""  
  
        #apply value if price > 100 to above_100 column
        bool_df=(dataframe["price"] > 100)
        tmp_dataframe=dataframe[bool_df]
        dataframe['above_100']=tmp_dataframe["price"]
    except:
        print("KeyError on price above_100 field")

    return dataframe

#output store on new dataset
def new_dataset(dataframe):
    dataframe.to_csv('dataset_out.csv',index=False)
    
#define pipe line from data processing task    
# then applies remove function the empty column name function
(df.pipe(delete_empty_name)
    # remove prefix zeros on price field
     .pipe(remove_zeros_inprice)
     # Create a pipeline that applies the split name into first name and last name function
     .pipe(split_column_name)
     # add new column price greater than 100
     .pipe(price_above_100)
     # output result set stored to new file
     .pipe(new_dataset)
)
    
    
    