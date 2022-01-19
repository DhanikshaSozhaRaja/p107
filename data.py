import pandas as pd
import csv
import plotly.express as pgo

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
print(mean)

fig = pgo.scatter(mean, x = "student_id", y ="level",size = "attempt", color = "attempt")
fig.show()
