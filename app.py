import csv_utils

record_date = "05-12-2020"
url_path = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

all_country_df = csv_utils.ingest_coviddata(record_date, url_path)
print(all_country_df.columns)

us_state_df = csv_utils.csv_to_us_df(record_date)

print(us_state_df.head(5))
