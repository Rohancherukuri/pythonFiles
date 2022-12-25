# Exploratory analysis using sweetviz package
import pandas as pd
import sweetviz as sv

try:
    df = pd.read_csv("/home/rohanoxob/Downloads/credit_record.csv")
    print(df.head())

    # Analyzing the dataset 
    summary = sv.analyze(df)
    summary.show_html('Credit.html')
except Exception as e:
    print("Sorry error occured: "+str(e))