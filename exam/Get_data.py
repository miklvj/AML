import pandas as pd
import requests
import gzip
import os

def read_gzipped_json_from_url(url, save_dir="C:/Users/mikke/OneDrive - Syddansk Universitet/Data Science/10. Anvendt Maskinlæring/data", chunk_size=1024*1024, max_rows=1_000_000):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filename = url.split('/')[-1]
    json_filepath = os.path.join(save_dir, filename)
    csv_filepath = json_filepath.replace('.json.gz', '.csv')

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        file_size = int(response.headers.get('content-length', 0))
        print(f"Downloading {filename} of size {file_size / 1024 / 1024:.2f} MB")

        with open(json_filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)

        with gzip.open(json_filepath, 'rb') as gz:
            df = pd.read_json(gz, lines=True, nrows=max_rows)
            df.to_csv(csv_filepath, index=False)  # Save as CSV
        return df
    else:
        print(f"Failed to retrieve data: status code {response.status_code}")
        return None

#amazon_fashion = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/AMAZON_FASHION.json.gz'
luxury_beauty = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Luxury_Beauty_5.json.gz'
#all_beauty = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/All_Beauty.json.gz'
#arts_crafts_and_sewing = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/Arts_Crafts_and_Sewing.json.gz'
#clothing_shoes_and_jewelry = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Clothing_Shoes_and_Jewelry_5.json.gz'
#sports_and_outdoors = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFilesSmall/Sports_and_Outdoors_5.json.gz'

#df_amazon_fashion = read_gzipped_json_from_url(amazon_fashion).reset_index(drop=True)
df_luxury_beauty = read_gzipped_json_from_url(luxury_beauty).reset_index(drop=True)
#df_all_beauty = read_gzipped_json_from_url(all_beauty).reset_index(drop=True)
#df_arts_crafts_and_sewing = read_gzipped_json_from_url(arts_crafts_and_sewing).reset_index(drop=True)
#clothing_shoes_and_jewelry = read_gzipped_json_from_url(clothing_shoes_and_jewelry).reset_index(drop=True)
#sports_and_outdoors = read_gzipped_json_from_url(sports_and_outdoors).reset_index(drop=True)


