import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 5
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"

data = pd.read_csv(url, skiprows = 1) #opens data
data["J-D"] = pd.to_numeric(data["J-D"], errors = "coerce", downcast ='float')

year = data["Year"].tolist()
avg_temp = data["J-D"].tolist()


plt.plot(year,avg_temp)

plt.xlabel("Year")

plt.ylabel("Temperature anomalies")
plt.yticks(np.arange(-1, 1.5, step=0.25))

plt.show()
