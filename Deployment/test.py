import unittest
import pandas as pd
from RevenueAnalyser import load_data, total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer, top_10_customers_by_revenue

class TestRevenueCalculations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up a sample dataset for testing
        data = {
            'order_id': [1, 2, 3, 4, 5],
            'customer_id': [1000, 1001, 1002, 1000, 1001],
            'order_date': [
                '2024-05-31 16:36:59.302125', '2024-06-15 16:36:59.302145', 
                '2024-06-23 16:36:59.302155', '2024-07-22 16:36:59.302160', 
                '2024-07-23 16:36:59.302160'
            ],
            'product_id': [26, 38, 33, 32, 45],
            'product_name': ['Product_26', 'Product_38', 'Product_33', 'Product_32', 'Product_45'],
            'product_price': [10.0, 20.0, 30.0, 40.0, 50.0],
            'quantity': [1, 2, 3, 4, 5]
        }
        cls.df = pd.DataFrame(data)
        # Calculate revenue for each row
        cls.df['revenue'] = cls.df['product_price'] * cls.df['quantity']
        # Convert order_date to datetime format
        cls.df['order_date'] = pd.to_datetime(cls.df['order_date'])

    def test_total_revenue_by_month(self):
        # Test total revenue calculation by month
        result = total_revenue_by_month(self.df)
        expected_data = {
            'year_month': ['2024-05', '2024-06', '2024-07'],
            'revenue': [10.0, 130.0, 410.0]
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df['year_month'] = pd.to_datetime(expected_df['year_month']).dt.to_period('M')
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_total_revenue_by_product(self):
        # Test total revenue calculation by product
        result = total_revenue_by_product(self.df)
        expected_data = {
            'product_name': ['Product_26', 'Product_32', 'Product_33', 'Product_38', 'Product_45'],
            'revenue': [10.0, 160.0, 90.0, 40.0, 250.0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_total_revenue_by_customer(self):
        # Test total revenue calculation by customer
        result = total_revenue_by_customer(self.df)
        expected_data = {
            'customer_id': [1000, 1001, 1002],
            'revenue': [170.0, 290.0, 90.0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_top_10_customers_by_revenue(self):
        # Test top 10 customers by revenue (or fewer if less than 10)
        result = top_10_customers_by_revenue(self.df)
        expected_data = {
            'customer_id': [1001, 1000, 1002],
            'revenue': [290.0, 170.0, 90.0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()
