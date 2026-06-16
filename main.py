from scripts.extract import extract_sales_csv
from scripts.transform import transform_data
from scripts.load import load
def main():
    file_path = 'data/ecommerce_sales_data.csv'
    data = extract_sales_csv(file_path)
    transformed_data = transform_data(data)
    # load(transformed_data)
if __name__ == "__main__":
    main()