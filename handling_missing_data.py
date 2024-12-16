import pandas as pd

data_with_nan={
   'vin': ['1HGCM82633A123456', '1HGCM82633A654321', '1HGCM82633A789012'],
    'manufacturer': ['Toyota', 'Ford', None],
    'year': [2020, None, 2021],
    'color': ['black', 'white', 'silver'],
    'body_type': ['Sedan', 'SUV', 'Coupe'],
    'engine_type': ['petrol', 'diesel', 'electric'],
    'transmission': ['manual', 'automatic', 'manual'],
    'fuel_type': ['gasoline', 'diesel', 'electric'],
    'seating_capacity': [5, 7, None],
    'price': [20000.00, 25000.00, 30000.00],
    'status': [None, 'sold', 'inactive'],
    'registration_date': ['2020-05-20', '2018-07-15', '2021-01-10']
}
df_with_nan=pd.DataFrame(data_with_nan)
df_no_nan=df_with_nan.dropna()

print(df_no_nan)


df_filled_nan=df_with_nan.fillna({"manufacturer":"unkown","year":2023,"seating_capacity":34,"status":"activate"})

print(df_filled_nan)

grouped_df=df_filled_nan.groupby("manufacturer")['price'].sum()
print(grouped_df)
