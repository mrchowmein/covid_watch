import pandas as pd
import requests

""""""
def ingest_coviddata(date_str : str, path : str):
    """Downloads global covid19 daily data with date and path string. Returns a dataframe of csv"""

    url = f"{path}{date_str}.csv"
    try:
        r = requests.get(url, allow_redirects=True)
        open(f'data/{date_str}.csv', 'wb').write(r.content)
        return pd.read_csv(f'data/{date_str}.csv', header=0)
    except requests.exceptions.RequestException as e:
        print(f"Requests Exceptions {e}")



def csv_to_us_df(date_str : str):
    """Function filters covid19 dataframe to US only using date. Returns a dataframe"""
    try:
        df = pd.read_csv(f'data/{date_str}.csv', header=0)
        us_df = df[(df.Country_Region == 'US')]
        us_state_df = us_df.groupby('Province_State').agg({'Deaths': 'sum',})
        return us_state_df
    except OSError as e:
        print(f"{e}")





#print(df.groupby('Country_Region').agg({'Deaths':['sum', 'max']}))

#print(us_df.groupby('Province_State').agg({'Deaths':['sum']}))