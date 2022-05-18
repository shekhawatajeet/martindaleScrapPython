import pandas as pd
  
df = pd.read_excel (r'Sample File.xlsx')
a=df.groupby('Menu Name').sum()
grandTotal=a.sum()

grandTotal.name = 'grandTotal'

a = a.append(grandTotal.transpose())

a.to_csv('final.csv')
