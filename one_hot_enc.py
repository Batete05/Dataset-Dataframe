import pandas as pd

data={
    "color": ["red","yellow","blue"]
}

df=pd.DataFrame(data)

one_hot_enconder_df=pd.get_dummies(df,columns=['color'])

one_hot_enconder_df=one_hot_enconder_df.astype(int)

print(one_hot_enconder_df)