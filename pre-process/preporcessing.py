import pandas as pd
import numpy as np
import os

##### Load joined.csv #######
df = pd.read_csv('joined.csv', encoding='utf-8').drop('Unnamed: 0',1)

print(df.head(3))

#calculate count with timestamp
from sklearn.preprocessing import LabelEncoder
labelencoder_timestamp_day = LabelEncoder()
cat = labelencoder_timestamp_day.fit_transform(df['timestamp_day'])
#cat = df['timestamp_day'].astype('category')
print(cat)

for i in range(len(cat)):
    df_tmp=df[df['timestamp_day']==cat[i]]
    df_group =df_tmp.groupby(['movieId']).count().reset_index().rename(columns={'userId': 'label'}) #get count by time stamp
    df_group['label_nom']=df_group['label']/np.sum(df_group['label'])
    #print(df_group.head(3))
    cols = ['movieId']
    ext = ['label','label_nom']
    df_tmp= df_tmp.join(df_group.set_index(cols)[ext], on=cols)
    print(len(cat)-i)
    #print(df_tmp.head(3))

    ######Save df_tmp #######
    # if file does not exist write header
    if not os.path.isfile('preprocess.csv'):
        df_tmp.to_csv('preprocess.csv', header='column_names')
    else:  # else it exists so append without writing the header
        df_tmp.to_csv('preprocess.csv', mode='a', header=False)


