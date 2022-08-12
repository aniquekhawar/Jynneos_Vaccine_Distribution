import pandas as pd

today = pd.Timestamp.now(tz='US/Eastern').strftime('%Y-%m-%d')
url = 'https://aspr.hhs.gov/SNS/Pages/JYNNEOS-Distribution.aspx'
df = pd.read_html(url)[0]
replace_dict = {'Total Requested': 'Total Requested '}
df.columns = df.columns.str.replace('Total Requested', 'Total Requested ')
df.to_csv(f'data/JYNNEOS_vaccine_distribution_{today}.csv', index = False)