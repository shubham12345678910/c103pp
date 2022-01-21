import pandas as pd # This library is used for data analysis
import plotly.express as px # This libray is used for plotting 
df = pd.read_csv("line_chart.csv")
fig=px.scatter(df,x="Year",y="Per capita income",color="Country",title="pre capita income")
fig.show()

