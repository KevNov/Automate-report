from plugins.send_to_slack import send_to_slack
from plugins.transform.read_transform import apend_all_files
import matplotlib.pyplot as plt


file_bytes = "C:\\Users\\kevnov\\Documents\\Digital Skola\\automate_report\\output\\sales_per_month.png"

 # analyze and create graph
data_Product = apend_all_files('C:\\Users\\kevnov\\Documents\\Digital Skola\\automate_report\\sales_product_data\\Sales_December_2019.csv')

# read and transform data by product

data_Product.drop(
    data_Product[data_Product["Quantity Ordered"] == "Quantity Ordered"].index, inplace=True
)

data_Product["total_price"] = data_Product["Quantity Ordered"].astype(
        float) * data_Product["Price Each"].astype(float)/1000

   
data_transformed = data_Product.groupby('Product').agg({'total_price':'sum'}).reset_index().nlargest(4,'total_price')
data_transformed1 = data_Product.groupby('Product').agg({'total_price':'sum'}).reset_index().nsmallest(4,'total_price')


print(data_transformed)

fig, ax = plt.subplots(2,1,figsize=(9,10))

ax[0].bar(data_transformed ['Product'], data_transformed['total_price'],label=False)
ax[0].set_xlabel('Product',loc=('center'))
ax[0].set_ylabel('Total Sales (USD)',loc=('center'))
ax[0].set_title('Top 4 sales')

ax[1].bar(data_transformed1 ['Product'], data_transformed1['total_price'])
ax[1].set_xlabel('Product',loc=('center'))
ax[1].set_ylabel('Total Sales (USD)',loc=('center'))
ax[1].set_title('Bottom 4 sales')

fig.savefig(file_bytes,dpi=220)

send_to_slack.execute('Monthly report', '#automate_report', file_bytes)
   
   

    

