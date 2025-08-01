# 📦 Store Inventory Tracking System with Streamlit and PostgreSQL

A user-friendly web-based inventory tracking application developed using **Streamlit** and connected to a **PostgreSQL** database. This system allows users to efficiently track, manage, and analyze inventory items with full CRUD functionality.

---

## 🚀 Features

- Add, update, and view inventory item details.
- Beautiful, wide-screen layout with intuitive form inputs.
- Real-time calculations for total price and net balance quantity.
- Auto-handles dates and pricing with smart form logic.
- Persistent data storage using PostgreSQL.
- Tabular view of all stored inventory entries.

---

## 🖼️ UI Preview

> Landscape-style layout:
- Vendor & Drawing Number details on the first row
- Quantity and date inputs grouped logically
- Pricing and status shown dynamically

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: PostgreSQL
- **ORM**: SQLAlchemy
- **Tools**: PgAdmin 4, SQL Shell (psql)

---

## 🧰 Table Schema (`store`)

```sql
CREATE TABLE IF NOT EXISTS store (
    id SERIAL PRIMARY KEY,
    vendor VARCHAR(100),
    dwg_number VARCHAR(100),
    item_name VARCHAR(100),
    total_ordered_qty INTEGER,
    received_qty INTEGER,
    received_date DATE,
    balance_qty INTEGER,
    issue_to_dept VARCHAR(100),
    issue_date DATE,
    rfr_qty INTEGER,
    consume_in_test INTEGER,
    qualified_qty INTEGER,
    rejected_qty INTEGER,
    user_acceptance VARCHAR(100),
    user_acceptance_date DATE,
    send_to_vendor_qty INTEGER,
    send_to_vendor_date DATE,
    net_balance_qty INTEGER,
    unit_price NUMERIC(10, 2),
    total_price NUMERIC(12, 2),
    current_status VARCHAR(100)
);


🧪 How It Works
User fills in the form with details such as item name, quantities, supplier info, and dates.

Auto-calculation of:

total_price = unit_price × received_qty

net_balance_qty = balance_qty - (consume_in_test + send_to_vendor_qty + rejected_qty)

Data is stored in PostgreSQL using SQLAlchemy.

Table below shows all records with automatic updates.

🧱 Project Structure
graphql
Copy
Edit
inventory_tracking_app/
│
├── inventory_app.py            # Main Streamlit app
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── setup.sql                   # SQL table creation script
📦 Requirements
Python 3.8+

PostgreSQL & PgAdmin 4

Streamlit

SQLAlchemy

psycopg2-binary

pandas

Install using:

bash
Copy
Edit
pip install streamlit sqlalchemy psycopg2-binary pandas
🧑‍💻 How to Run
Start PostgreSQL and PgAdmin, create a database named: feedback_db.

Run this script in PgAdmin → Query Tool:

sql
Copy
Edit
CREATE DATABASE feedback_db;
-- Then connect to it and run the store table schema above.
Update your connection string in inventory_app.py:

python
Copy
Edit
db_url = "postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db"
Launch the app:

bash
Copy
Edit
streamlit run inventory_app.py
📈 Future Improvements
Add user authentication.

Export inventory to CSV or Excel.

Add item editing & deletion features.

Include visual dashboards (bar charts, pie charts).

Notify when items reach reorder level.

🧑‍🔧 Author
Engr. Muhammad Abul Hassan
