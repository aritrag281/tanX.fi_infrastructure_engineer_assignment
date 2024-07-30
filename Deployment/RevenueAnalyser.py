# main.py
import pandas as pd
import psycopg2
import redis
from sqlalchemy import create_engine

def connect_to_db():
    return psycopg2.connect(
        dbname='revenue_db',
        user='user',
        password='password',
        host='db',
        port='5432'
    )

def connect_to_redis():
    return redis.StrictRedis(host='redis', port=6379, db=0)

def load_data():
    file_path = '/mnt/data/orders.csv'
    df = pd.read_csv(file_path)
    return df

def revenue_per_month(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    revenue_by_month = df.groupby('month')['revenue'].sum()
    return revenue_by_month

def revenue_per_product(df):
    revenue_by_product = df.groupby('product_id')['revenue'].sum()
    return revenue_by_product

def revenue_per_customer(df):
    revenue_by_customer = df.groupby('customer_id')['revenue'].sum()
    return revenue_by_customer

def top_10_customers(df):
    revenue_by_customer = revenue_per_customer(df)
    top_10 = revenue_by_customer.nlargest(10)
    return top_10

def store_results_to_db(results, table_name):
    engine = create_engine('postgresql://user:password@db:5432/revenue_db')
    results.to_frame(name='revenue').reset_index().to_sql(table_name, engine, if_exists='replace', index=False)

def cache_results_to_redis(results, key_prefix):
    r = connect_to_redis()
    for key, value in results.items():
        r.set(f"{key_prefix}:{key}", value)

def main():
    df = load_data()
    
    revenue_month = revenue_per_month(df)
    revenue_product = revenue_per_product(df)
    revenue_customer = revenue_per_customer(df)
    top_customers = top_10_customers(df)

    store_results_to_db(revenue_month, 'revenue_month')
    store_results_to_db(revenue_product, 'revenue_product')
    store_results_to_db(revenue_customer, 'revenue_customer')
    store_results_to_db(top_customers, 'top_customers')

    cache_results_to_redis(revenue_month, 'revenue_month')
    cache_results_to_redis(revenue_product, 'revenue_product')
    cache_results_to_redis(revenue_customer, 'revenue_customer')
    cache_results_to_redis(top_customers, 'top_customers')

if __name__ == '__main__':
    main()
