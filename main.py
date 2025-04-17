# Import necessary packages
import pandas as pd
import numpy as np

airbnb_price = pd.read_csv('data/airbnb_price.csv') 
# Index(['listing_id', 'price', 'nbhood_full'], dtype='object')

excel_file = pd.ExcelFile('data/airbnb_room_type.xlsx')
airbnb_room_type = excel_file.parse('airbnb_room_type') 
print (airbnb_room_type.columns)
# Index(['listing_id', 'description', 'room_type'], dtype='object')

airbnb_last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t') 
## Index(['listing_id', 'host_name', 'last_review'], dtype='object')

######################### Check nah values #######################################
airbnb_price_nah = airbnb_price.isna().sum() # no missing data

airbnb_room_type_nah = airbnb_room_type.isna().sum() # description column: 10

airbnb_last_review_nah = airbnb_last_review.isna().sum() # host_name column: 8

###################### handle nah values ####################################
#threshold_airbnb_room_type_nah = len(airbnb_room_type)*0.05 # 1260.45 => drop
#airbnb_room_type.dropna (subset='description',inplace =True)

#threshold_airbnb_last_review_nah = len(airbnb_last_review)*0.05 # 1260.45 => drop
#airbnb_last_review.dropna (subset='host_name',inplace =True)

########################### the dates of the earliest and most recent reviews ###########################
airbnb_last_review['last_review'] = pd.to_datetime(airbnb_last_review['last_review'])
airbnb_last_review = airbnb_last_review.sort_values(by='last_review',ascending = True)
earliest_date = airbnb_last_review['last_review'].values[0]
airbnb_last_review = airbnb_last_review.sort_values(by='last_review',ascending = False)
recent_date = airbnb_last_review['last_review'].values[0]

############################## the number of private rooms ##############################
airbnb_room_type['room_type'] =airbnb_room_type['room_type'].str.lower()
airbnb_room_type['room_type'] =airbnb_room_type['room_type'].str.strip()
print (airbnb_room_type['room_type'].unique())
count = airbnb_room_type['room_type'].value_counts()
private_room = count['private room']
print (private_room)

########################### the average listing price ##############################
print (airbnb_price.columns)
print (airbnb_price[~airbnb_price['price'].str.contains('dollars',case = False, regex = False)])
total = airbnb_price['price'].shape[0]
airbnb_price['price without dollar string'] = airbnb_price['price'].str.replace('dollars','').astype(int)
print ( airbnb_price['price without dollar string'].dtypes)
average_listing_price = airbnb_price['price without dollar string'].agg('mean')
average_listing_price = np.round(average_listing_price,2)
print (average_listing_price)

################################
review_dates=pd.DataFrame({'first_reviewed':earliest_date,'last_reviewed':recent_date,'nb_private_rooms':private_room,'avg_price':average_listing_price}, index=[0])
print (review_dates)
review_dates.to_csv("final_result.csv", index=False)