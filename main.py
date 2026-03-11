import pandas as pd

data_frame = pd.read_excel('Import_xlsx\\sample.xlsx', engine='openpyxl', index_col=False)

def filter_age(age=None):
    data_filtered = data_frame[data_frame['Idade'] <= age]
    return data_filtered['Email']
        
print(data_frame)
print('-=' * 50)
print(filter_age(30)) 