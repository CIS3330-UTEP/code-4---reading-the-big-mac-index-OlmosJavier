import pandas as pd

big_mac_file = './big-mac-full-index.csv'
def get_big_mac_price_by_year(file_path, year, country_code):
    total_price = 0
    count = 0

    with open(file_path, 'r') as file:
        reader = pd.DictReader(file)
        for row in reader:
            if row['year'] == year and row['country_code'] == country_code:
                total_price += float(row['dollar_price'])
                count += 1

    return round(total_price / count, 2) if count > 0 else None
price = get_big_mac_price_by_year('big_mac_data.csv', '2023', 'us')
print(price)

      

def get_big_mac_price_by_country(country, big_mac_file):
    df = pd.read_csv(big_mac_file)
    return round(df[df['country'] == country]['dollar_price'].mean(), 2)

     
def get_the_cheapest_big_mac_price_by_year(year):
   def get_the_cheapest_big_mac_price_by_year(year, big_mac_file):
    df = pd.read_csv(big_mac_file)
    min_price_row = df[df['year'] == year]['dollar_price'].idxmin()
    return f"{df.loc[min_price_row, 'country']}({df.loc[min_price_row, 'country_code']}): ${df.loc[min_price_row, 'dollar_price']}"
    


def get_the_most_expensive_big_mac_price_by_year(year, big_mac_file):
    df = pd.read_csv(big_mac_file)
    max_price_row = df[df['year'] == year]['dollar_price'].idxmax()
    return f"{df.loc[max_price_row, 'country']}({df.loc[max_price_row, 'country_code']}): ${df.loc[max_price_row, 'dollar_price']}"
    

'''
if __name__ == "__main__":
    pass # Remove this line and code your user interface
'''