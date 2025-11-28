# Splitting complex function into simpler small functions

def fetch_sales():
    print(f"Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")

generate_report()