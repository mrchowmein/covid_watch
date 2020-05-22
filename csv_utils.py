import pandas as pd
import requests


def ingest_coviddata(date_str : str):
    url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date_str}.csv"
    try:
        r = requests.get(url, allow_redirects=True)
        open(f'data/{date_str}.csv', 'wb').write(r.content)
    except requests.exceptions.RequestException as e:
        print(f"Requests Exceptions {e}")

def csv_to_df(date_str : str):

    try:
        df = pd.read_csv(f'data/{date_str}.csv', header=0)
        us_df = df[(df.Country_Region == 'US')]
        print(us_df.head(5))
        print(us_df.columns)
        us_state_df = us_df.groupby('Province_State').agg({'Deaths': 'sum',})
        print(us_state_df)
        return us_state_df
    except OSError as e:
        print(f"{e}")





#print(df.groupby('Country_Region').agg({'Deaths':['sum', 'max']}))

#print(us_df.groupby('Province_State').agg({'Deaths':['sum']}))