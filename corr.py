import pandas as pd
import plotly.express as px
df=pd.read_csv("coffe.csv")
fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
fig.show()
relation=df.corr()
print(relation)