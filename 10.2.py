#24331A05E7
# to perform sorting and slicing operations in pandas.  
 
import pandas as pd
data = {
   'Name': ['vamsi', 'spidyy', 'krishh', 'maxyy'],
   'Age': [20, 21, 24, 22],
   'Marks': [90, 88, 92, 80],
   'Fav subject': ['Biology','mathematics','chemistry','physics']
}
df = pd.DataFrame(data)
print("Sorted by Marks:")
print(df.sort_values(by='Marks'))
print("\nSelect Name and Marks columns:")
print(df[['Name', 'Marks']])
