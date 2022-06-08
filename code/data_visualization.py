
#利用已抓取好的文件实现可视化
from plotly import graph_objects as go
import plotly.express as px
import pandas as pd


input_file1 = "c:/9.8最新版.csv"
input_file2 = "c:/9.8辅助.csv"
output_file = "C:/testOut2.csv"

df = pd.read_csv(input_file1, encoding='UTF-8')
location_lookup_table = pd.read_csv(input_file2, encoding='UTF-8')

df.loc[:,'Last_Update'] = pd.to_datetime(df.loc[:,'Last_Update'])
print(df.shape)

df.loc[:,'Last_Update'].min()
df.loc[:,'Last_Update'].max()
#

# #下面5行代码是用来提高pandas运行速度的，采用此方法后，fig图出来的速度幅度提高--->借鉴：https://blog.csdn.net/yuxiaosmd/article/details/87112688
df['Last_Update'] = pd.to_datetime(df['Last_Update'])
df['Last_Update'].dtype
#
data_store = pd.HDFStore('processed_data.h5')
#
# # 将 DataFrame 放进对象中，并设置 key 为 preprocessed_df
data_store['preprocessed_df'] = df
data_store.close()#储存对象
data_store = pd.HDFStore('processed_data.h5')

# 通过key获取数据
preprocessed_df = data_store['preprocessed_df']
data_store.close()

#def apply_tariff_digitize(df):
 #   prices = np.array([12, 20, 28])
  #  bins = np.digitize(df.index.hour.values, bins=[7, 17, 24])
   # df['cost_cents'] = prices[bins] * df['energy_kwh'].values

    #apply_tariff_digitize(df)

#创建画布
layout_default = go.Layout(
    # color theme
    template='plotly_dark',

    # set title
    title=dict(
        text='Default Title',
        font={
            'size': 30,
            'color': '#444'
        },
        x=0.5,  # [0,1,'auto']
        y=0.9  # [0,1, 'auto']
    ),

    # set axis
    xaxis=dict(
        visible=True,
        color='#444', #颜色重点显示不可被后者覆盖防止网页颜色发生冲突
        title='default xaxis'  # or dict
    ),
    yaxis=dict(
        visible=True,
        color='#444',
        title='default yaxis',  # or dict
        type='-',  # one of ( "-" | "linear" | "log" | "date" | "category" | "multicategory" )
        # range=[1,2]
    ),

    # set Figure's size
    autosize=False,
    height=600,  # in pixel
    width=1100,

    # set Legend
    showlegend=True
)

# 准备数据  六国的累计感染人数曲线
countries = ['DEU', 'ESP', 'FRA', 'GBR', 'ITA', 'USA']
df_country = df[(df['Province_State'].isna())&(df['Last_Update'] >= '2020-03-01')]

# pivot 六个国家的确诊人数
data= df_country.pivot_table(index='iso3',columns='Last_Update',values='Confirmed', fill_value=0, aggfunc='mean').loc[countries]

# 创建 figure
fig = go.Figure(layout=layout_default)
# x坐标
x= data.columns.strftime('%Y-%m-%d').values.tolist()

# 画多条曲线
for idx in data.index:
    # 官方API: https://plotly.com/python/reference/
    fig.add_trace(
        go.Scatter(
            x =x,
            y = data.loc[idx].values.tolist(),
            text = data.loc[idx].values.tolist(),
            mode = 'lines+markers',
            name= location_lookup_table[location_lookup_table['iso3'] == idx].iloc[0]['Country_Region'],
            hovertext = 'Population:{}'.format(int(location_lookup_table[location_lookup_table['iso3'] == idx].iloc[0]['Population'])),
            hoverinfo = 'all',# Examples: "x", "y", "x+y", "x+y+z", "all"
            opacity=0.5
        )
    )

# 略微更改一下布局
fig.update_layout(
    title = dict(
        text='<b>疫情大国</b>确诊<i>总人数</i>',
        font={'size':30},
        x=0.5, #[0,1,'auto']
        y=0.9 # [0,1, 'auto']
    ),
)

# 快速更改axis
fig.update_xaxes(
    title_text="<b>日期</b> 加粗"
)

fig.update_yaxes(
    title_text="<i>确诊人数</i> 斜体"
)

# 画图像——六国感染确诊人数图像
fig.show()

#全球感染严重程度以及发展情况
fig = px.scatter_geo(data_frame=df_country,
                     locations="iso3",
                     color="Incident_Rate",
                     hover_name="Country_Region",
                     size="Confirmed",
                     animation_frame=df_country["Last_Update"].astype(str),
                     projection="natural earth",
                     size_max=100,
                     width=1200, height=700)
fig.update_layout(
    template='plotly_dark'
)
#画图像——全球
fig.show()

# pandas.dataframe --> plotly.graph_objects.table
def TableFromPandas(df):
    columns = df.columns
    return go.Table(
        header=dict(values=list(columns),
                    align='left'),
        cells=dict(values=[df[i] for i in columns],
                   align='left')
    )
fig = go.Figure(
    data=[TableFromPandas(df_country)]
)
#表格
fig.show()