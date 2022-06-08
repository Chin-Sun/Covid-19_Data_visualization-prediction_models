import pandas as pd

# 直接从github读取数据,并生成csv文件
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv', error_bad_lines=False )
#df.loc[:,'Last_Update'] = pd.to_datetime(df.loc[:,'Last_Update'], format='%m/%d/%y')
print(df.shape)
outputpath='c:/9.8辅助.csv'
df.to_csv(outputpath,sep=',',index=False,header=False)
