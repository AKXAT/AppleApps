import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
sns.set_theme(style="whitegrid")
apple_store_data = pd.read_excel(r'apple_store.xlsx')
#print(apple_store_data['PrimaryGenre'].nunique())
sorted_apple_data = apple_store_data.sort_values(by='TotalRatings',ascending=False)
fig,axes = plt.subplots(nrows=1,ncols=1,dpi=150)
sns.lineplot(data=sorted_apple_data,
x='PrimaryGenre',
y='AvgRating',
hue='FreePaid',
ci=None,
marker='o',
markerfacecolor='black')
plt.xticks(rotation=90)
plt.xlabel("App Geners",fontweight='bold',color='blue')
plt.ylabel("App Rating",fontweight='bold',color='blue')
plt.subplots_adjust(bottom=0.37,left=0.07,right=0.94,top=0.9)
plt.show()
all_genres = (apple_store_data['PrimaryGenre'].unique())
fig,axes = plt.subplots(nrows=1,ncols=1,dpi=60)
for each_gener in all_genres:
    top_five_apps = (apple_store_data.groupby('PrimaryGenre').get_group(each_gener)).sort_values(by='TotalRatings',ascending=False)[:5]
    print(each_gener)
    print(top_five_apps[['AppName','TotalRatings']])