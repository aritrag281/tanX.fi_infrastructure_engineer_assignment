import pandas as pd

def load_data(file_path):
    """
    Load CSV data, compute revenue, and convert order_date to datetime.
    """
    df = pd.read_csv(file_path)  # Load data
    df['revenue'] = df['product_price'] * df['quantity']  # Compute revenue
    df['order_date'] = pd.to_datetime(df['order_date'])  # Convert date
    return df

def total_revenue_by_month(df):
    """
    Calculate total revenue per month.
    """
    df['year_month'] = df['order_date'].dt.to_period('M')  # Extract month
    monthly_revenue = df.groupby('year_month')['revenue'].sum().reset_index()  # Group by month
    return monthly_revenue

def total_revenue_by_product(df):
    """
    Calculate total revenue per product.
    """
    product_revenue = df.groupby('product_name')['revenue'].sum().reset_index()  # Group by product
    return product_revenue

def total_revenue_by_customer(df):
    """
    Calculate total revenue per customer.
    """
    customer_revenue = df.groupby('customer_id')['revenue'].sum().reset_index()  # Group by customer
    return customer_revenue

def top_10_customers_by_revenue(df):
    """
    Get the top 10 customers by revenue.
    """
    customer_revenue = total_revenue_by_customer(df)  # Get revenue by customer
    top_customers = customer_revenue.sort_values(by='revenue', ascending=False).head(10)  # Sort and select top 10
    return top_customers

if __name__ == "__main__":
    file_path = 'orders.csv'  # File path
    df = load_data(file_path)  # Load data
    
    print("Total Revenue by Month:")
    print(total_revenue_by_month(df))  # Revenue by month
    
    print("\nTotal Revenue by Product:")
    print(total_revenue_by_product(df))  # Revenue by product
    
    print("\nTotal Revenue by Customer:")
    print(total_revenue_by_customer(df))  # Revenue by customer
    
    print("\nTop 10 Customers by Revenue:")
    print(top_10_customers_by_revenue(df))  # Top 10 customers
