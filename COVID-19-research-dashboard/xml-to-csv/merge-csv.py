import pandas as pd
import glob
import os


# setting the path where converted csv's are placed.
path = "/Users/vanessaklotzman/Documents/GitHub/COVID-19/documents/mendeley_library_files/xml_files/CSV-data/"


# 2. creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.startswith('mendeley_document')]

# 3. creates empty list to include the content of each file converted to pandas DF
csv_list = []
 
# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))

    print(csv_list)

csv_merged = pd.concat(csv_list, ignore_index=True)

csv_merged.to_csv('midas-data.csv')
