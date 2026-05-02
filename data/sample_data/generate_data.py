import pandas as pd
import numpy as np
import uuid
import random
from datetime import datetime, timedelta

NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 100
NUM_ORDERS = 50000
NUM_EVENTS = 200000

# -----------------------
# Generate Customers
# -----------------------
def generate_customers(n):
    customers = []
    for _ in range(n):
        customer_id = str(uuid.uuid4())
        signup_date = datetime.now() - timedelta(days=random.randint(0, 1000))
        customers.append({
            "customer_id": customer_id,
            "first_name": f"Name{random.randint(1,1000)}",
            "last_name": f"Surname{random.randint(1,1000)}",
            "email": f"user{random.randint(1,100000)}@example.com",
            "country": random.choice(["US", "UK", "CA", "DE", "FR"]),
            "signup_date": signup_date.date()
        })
    return pd.DataFrame(customers)

# -----------------------
# Generate Products
# -----------------------
def generate_products(n):
    categories = ["Electronics", "Clothing", "Home", "Sports"]
    products = []
    for i in range(n):
        products.append({
            "product_id": f"P{i}",
            "product_name": f"Product_{i}",
            "category": random.choice(categories),
            "price_usd": round(random.uniform(10, 500), 2)
        })
    return pd.DataFrame(products)

# -----------------------
# Generate Orders
# -----------------------
def generate_orders(customers_df, products_df, n):
    orders = []
    for _ in range(n):
        order_id = str(uuid.uuid4())
        customer = customers_df.sample(1).iloc[0]
        product = products_df.sample(1).iloc[0]

        order_date = datetime.now() - timedelta(days=random.randint(0, 365))

        orders.append({
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "order_date": order_date,
            "amount_usd": product["price_usd"]
        })
    return pd.DataFrame(orders)

# -----------------------
# Generate Events
# -----------------------
def generate_events(customers_df, products_df, orders_df, n):
    events = []
    event_types = ["view", "add_to_cart", "purchase"]

    for _ in range(n):
        event_id = str(uuid.uuid4())
        customer = customers_df.sample(1).iloc[0]
        product = products_df.sample(1).iloc[0]

        event_type = random.choices(
            event_types,
            weights=[0.7, 0.2, 0.1],
            k=1
        )[0]

        timestamp = datetime.now() - timedelta(days=random.randint(0, 365))

        events.append({
            "event_id": event_id,
            "customer_id": customer["customer_id"],
            "event_type": event_type,
            "product_id": product["product_id"],
            "timestamp": timestamp,
            "session_id": str(uuid.uuid4())
        })

    # Add purchase events tied to orders (IMPORTANT)
    for _, order in orders_df.iterrows():
        events.append({
            "event_id": str(uuid.uuid4()),
            "customer_id": order["customer_id"],
            "event_type": "purchase",
            "product_id": order["product_id"],
            "timestamp": order["order_date"],
            "session_id": str(uuid.uuid4())
        })

    return pd.DataFrame(events)

# -----------------------
# Main Execution
# -----------------------
def main():
    print("Generating data...")

    customers = generate_customers(NUM_CUSTOMERS)
    products = generate_products(NUM_PRODUCTS)
    orders = generate_orders(customers, products, NUM_ORDERS)
    events = generate_events(customers, products, orders, NUM_EVENTS)

    customers.to_csv("customers.csv", index=False)
    products.to_csv("products.csv", index=False)
    orders.to_csv("orders.csv", index=False)
    events.to_csv("events.csv", index=False)

    print("Data generation complete.")

if __name__ == "__main__":
    main()
