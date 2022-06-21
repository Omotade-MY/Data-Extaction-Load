from crud import load_data, csv_to_db
from extract import extract_coindata

data , cols = extract_coindata()

load_data(data, cols)
