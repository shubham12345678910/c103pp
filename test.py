import pandas as pd # This library is used for data analysis
import plotly.express as px # This libray is used for plotting 
df = pd.read_csv("data.csv")
fig=px.bar(df,x="Country",y="InternetUsers",title="pre capita income")
fig.show()