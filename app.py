import pandas as pd
import requests


record_date = "04-12-2020"
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{record_date}.csv"
r = requests.get(url, allow_redirects=True)
print(url)
open(f'{record_date}.csv', 'wb').write(r.content)

df = pd.read_csv(f'{record_date}.csv', header=0)

#print(df.groupby('Country_Region').agg({'Deaths':['sum', 'max']}))

us_df = df[(df.Country_Region == 'US')]
print(us_df)
#print(us_df.groupby('Province_State').agg({'Deaths':['sum']}))