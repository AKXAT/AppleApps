import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
apple_store_data = pd.read_excel(r'apple_store.xlsx')
fig,axes = plt.subplots(nrows=1,ncols=1,dpi=150)
sns.lineplot(data=apple_store_data,x='PrimaryGenre',y='AvgRating',hue='FreePaid',ci=None,marker='o',markerfacecolor='black')
plt.xticks(rotation=90)
plt.xlabel("App Geners",fontweight='bold',color='blue')
plt.ylabel("App Rating",fontweight='bold',color='blue')
plt.subplots_adjust(bottom=0.37,left=0.07,right=0.94,top=0.9)
plt.show()
