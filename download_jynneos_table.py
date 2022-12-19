import pandas as pd

# grab today
today_timestamp = pd.Timestamp.now(tz='US/Eastern')
today_str = today_timestamp.strftime('%Y-%m-%d')
last_updated_time = today_timestamp.strftime('%Y-%m-%d %H:%M')

# get data
url = 'https://aspr.hhs.gov/SNS/Pages/JYNNEOS-Distribution.aspx'
df = pd.read_html(url)[1]

# rename columns
replace_tuple = [('Total Requestedas', 'Total Requested as'), ('Total Shippedas', 'Total Shipped as'),
                 ('DosesAs', 'Doses As')]
for old_text, new_text in replace_tuple:
    df.columns = df.columns.str.replace(old_text, new_text)

# clean up data and dtypes
df = df.replace('-', 0)
cols = df.columns.tolist()
for col in cols:
    try:
        df[col] = df[col].astype('int')
    except:
        print(f'Could not convert column {col} of dtype {df[col].dtype} to integer.')
        continue

# update last updated field
df['Last Updated'] = last_updated_time

# save to CSV
df.to_csv(f'data/JYNNEOS_vaccine_distribution_{today_str}.csv', index = False)
df.to_csv(f'data/JYNNEOS_vaccine_distribution_latest.csv', index = False)
