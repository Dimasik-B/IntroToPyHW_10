import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

result_df = data
result_df.loc[data['whoAmI']=='human', 'Human'] = '1'
result_df.loc[data['whoAmI']!='human', 'Human'] = '0'
result_df.loc[data['whoAmI']=='robot', 'Robot'] = '1'
result_df.loc[data['whoAmI']!='robot', 'Robot'] = '0'
result_df.pop('whoAmI')
print(result_df)