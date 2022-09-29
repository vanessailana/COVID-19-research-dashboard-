# COVID-19-research-dashboard-


The coronavirus disease 2019 (COVID-19, https://en.wikipedia.org/wiki/Coronavirus_disease_2019) is an infectious disease caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The disease has spread globally, resulting in the 2019–20 coronavirus pandemic. 

  
Research into a solution for this problem is at full steam and, so far, more than 2000 research papers related to this have been published. As this number grows, keeping track of what is happening, recent results, etc., is becoming harder and harder. This is where modern advances in AI, ML and NLP are called for coming into action.


## 
The goal of this repository is  to create a report or dashboard that can be used by decision-makers and researchers to know what science results are being produced. 


## Data 
Many institutions and organizations, like the World Health Organization (WHO, https://www.who.int), or the Center for Disease Control and Prevention (CDC, https://www.cdc.gov) are gathering data and information related to the pandemic. 

One of these organizations is the MIDAS Coordination Center (https://midasnetwork.us/mcc/). They are actively compiling and sharing information through the GitHub repository https://github.com/midas-network/COVID-19. In particular, they are sharing an export their Mendeley paper collection as XML files in   
https://github.com/midas-network/COVID-19/tree/master/documents/mendeley_library_files/xml_files 

## Task 

Given a list of papers create a report with the results of: 

1.  Read the most recent MIDAS Mendeley paper library XML file. 
-  Run the xml2csv.py  script to convert the XML files to a CSV format. (File is in the xml-to-csv directory) 
- Merge the CSV's into one CSV with the mergecsv.py (File is in the xml-to-csv directory) 


2. Generate groups of similar papers and assign a meaningful label or group of tags to each group.
- (We are using a K-Means algorithm and for dimensionality reduction Principal Componeny Analysis) 
- Code: is in NLP-COVID-dashboard.ipynb

3.  Outline what papers inside each group better represent that group.

Interactive Dashboard to understand what papers are inside each group is in the covid-19_literature-dashboard.html. 
You can hover over each cluster to see what papers are in that group. 



  
  
