import csv
import random
import uuid
from datetime import datetime, timedelta

NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 200
NUM_ORDERS = 30000
NUM_EVENTS = 100000

countries = ["USA", "Canada", "UK", "Germany", "France"]
cities = ["New York", "Toronto", "London", "Berlin", "Paris"]
channels = ["organic", "paid_ads", "referral"]

event_types = ["page_view", "add_to_cart", "purchase", "login"]
devices = ["mobile", "desktop", "tablet"]
browsers = ["chrome", "safari", "firefox", "edge"]
traffic_sources = ["google", "direct", "email", "ads"]

# -------------------
# Generate Products
# -------------------
products = []

with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "product_id", "product_name", "category", "subcategory",
        "brand", "price_usd", "cost_usd", "margin_percentage",
        "is_active", "created_at"
    ])

    for i in range(NUM_PRODUCTS):
        product_id = f"P{i:04d}"
        price = round(random.uniform(10, 500), 2)
        cost = round(price * random.uniform(0.4, 0.8), 2)
        margin = round((price - cost) / price * 100, 2)

        writer.writerow([
            product_id,
            f"Product_{i}",
            random.choice(["Electronics", "Clothing", "Home"]),
            random.choice(["SubA", "SubB", "SubC"]),
            random.choice(["BrandX", "BrandY", "BrandZ"]),
            price,
            cost,
            margin,
            True,
            datetime.now().isoformat()
        ])

        products.append(product_id)

# -------------------
# Generate Customers
# -------------------
customers = []

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "customer_id", "first_name", "last_name", "email",
        "country", "city", "signup_date", "acquisition_channel",
        "is_active", "lifetime_value_usd", "last_purchase_date"
    ])

    for i in range(NUM_CUSTOMERS):
        customer_id = f"C{i:05d}"
        signup_date = datetime.now() - timedelta(days=random.randint(30, 1000))

        writer.writerow([
            customer_id,
            f"First{i}",
            f"Last{i}",
            f"user{i}@example.com",
            random.choice(countries),
            random.choice(cities),
            signup_date.date(),
            random.choice(channels),
            random.choice([True, False]),
            round(random.uniform(50, 5000), 2),
            datetime.now().isoformat()
        ])

        customers.append(customer_id)

# -------------------
# Generate Orders
# -------------------
orders = []

with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "order_id", "customer_id", "product_id",
        "order_date", "amount_usd", "status"
    ])

    for i in range(NUM_ORDERS):
        order_id = f"O{i:06d}"
        customer_id = random.choice(customers)
        product_id = random.choice(products)
        order_date = datetime.now() - timedelta(days=random.randint(0, 365))
        amount = round(random.uniform(20, 500), 2)

        row = [
            order_id,
            customer_id,
            product_id,
            order_date.isoformat(),
            amount,
            random.choice(["completed", "cancelled", "refunded"])
        ]

        writer.writerow(row)
        orders.append(row)

# -------------------
# Generate Events (Linked to Orders)
# -------------------
with open("events.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "event_id", "customer_id", "session_id", "event_type",
        "event_timestamp", "page_url", "product_id",
        "order_id", "device_type", "browser",
        "country", "traffic_source"
    ])

    for i in range(NUM_EVENTS):
        event_type = random.choices(
            event_types,
            weights=[0.6, 0.2, 0.1, 0.1]
        )[0]

        customer_id = random.choice(customers)
        session_id = str(uuid.uuid4())
        timestamp = datetime.now() - timedelta(days=random.randint(0, 365))

        order_id = ""
        product_id = ""

        if event_type == "purchase":
            order = random.choice(orders)
            order_id = order[0]
            customer_id = order[1]
            product_id = order[2]
        else:
            product_id = random.choice(products)

        writer.writerow([
            str(uuid.uuid4()),
            customer_id,
            session_id,
            event_type,
            timestamp.isoformat(),
            f"/page/{random.randint(1, 50)}",
            product_id,
            order_id,
            random.choice(devices),
            random.choice(browsers),
            random.choice(countries),
            random.choice(traffic_sources)
        ])

print("✅ Done: customers.csv, products.csv, orders.csv, events.csv generated.")
