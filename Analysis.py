import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy
data = pd.read_excel("excel.xlsx")
sns.set_theme(style="ticks")

p = sns.regplot(
    data = data,x="Qty",y="Price_€", fit_reg=True
)
slope, intercept, r, p, sterr =scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                       y=p.get_lines()[0].get_ydata())

plt.text(1,5,'y = ' + str((slope)) +'x'+ ' + '+str(intercept))
#plt.show()
print(slope,intercept,r)
temp = []
for i,names in data.iterrows():
    temp.append(abs(
        names["Qty"]*slope+r*names["Price_€"]+intercept)
    )

data["Distance"]=temp


sns.regplot(
    data = data,x="Qty",y="Price_€", fit_reg=True
)
sns.jointplot(data=data, kind="scatter",
            x="Name",y="Distance")


plt.xticks(rotation = 90,fontsize=10)

plt.show()