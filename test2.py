import pandas as pd # This library is used for data analysis
import plotly.express as px # This libray is used for plotting 
df = pd.read_csv("Copy+of+data+-+data.xls")
fig=px.bar(df,x="cases",y="date",title="country")
fig.show()