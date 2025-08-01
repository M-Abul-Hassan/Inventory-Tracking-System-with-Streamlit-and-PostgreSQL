import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date

# Database connection setup (adjust credentials accordingly)
db_url = "postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db"
engine = create_engine(db_url)

# Create table if not exists
def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
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
            )
        """))

# Insert new item
def add_item(data):
    with engine.begin() as conn:
        query = text("""
            INSERT INTO store (
                vendor, dwg_number, item_name, total_ordered_qty,
                received_qty, received_date, balance_qty,
                issue_to_dept, issue_date, rfr_qty, consume_in_test,
                qualified_qty, rejected_qty, user_acceptance,
                user_acceptance_date, send_to_vendor_qty,
                send_to_vendor_date, net_balance_qty, unit_price,
                total_price, current_status
            ) VALUES (
                :vendor, :dwg_number, :item_name, :total_ordered_qty,
                :received_qty, :received_date, :balance_qty,
                :issue_to_dept, :issue_date, :rfr_qty, :consume_in_test,
                :qualified_qty, :rejected_qty, :user_acceptance,
                :user_acceptance_date, :send_to_vendor_qty,
                :send_to_vendor_date, :net_balance_qty, :unit_price,
                :total_price, :current_status
            )
        """)
        conn.execute(query, data)

# Load all data
def load_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM store ORDER BY id DESC"))
        return pd.DataFrame(result.fetchall(), columns=result.keys())

# Streamlit UI
st.title("📦 Inventory Tracking and Management System")

create_table()

st.subheader("Add / Update Item")
with st.form("item_form"):
    vendor = st.text_input("Vendor")
    dwg_number = st.text_input("Drawing Number")
    item_name = st.text_input("Item Name")
    total_ordered_qty = st.number_input("Total Ordered Quantity", 0)
    received_qty = st.number_input("Received Quantity", 0)
    received_date = st.date_input("Received Date", value=date.today())
    balance_qty = st.number_input("Balance Quantity", 0)
    issue_to_dept = st.text_input("Issue to Department")
    issue_date = st.date_input("Issue Date", value=date.today())
    rfr_qty = st.number_input("RFR Quantity", 0)
    consume_in_test = st.number_input("Consumed in Test", 0)
    qualified_qty = st.number_input("Qualified Quantity", 0)
    rejected_qty = st.number_input("Rejected Quantity", 0)
    user_acceptance = st.text_input("User Acceptance")
    user_acceptance_date = st.date_input("User Acceptance Date", value=date.today())
    send_to_vendor_qty = st.number_input("Send to Vendor Quantity", 0)
    send_to_vendor_date = st.date_input("Send to Vendor Date", value=date.today())
    unit_price = st.number_input("Unit Price", 0.0, step=0.01)
    current_status = st.selectbox("Current Status", ["QAD", "Store", "Rejected", "Approved", "Vendor Site", "Send to User After Acceptance",])

    # Auto-calculations
    total_price = total_ordered_qty * unit_price
    net_balance_qty = total_ordered_qty - (issued_qty := (balance_qty + send_to_vendor_qty))

    submitted = st.form_submit_button("Submit")
    if submitted:
        item_data = {
            "vendor": vendor,
            "dwg_number": dwg_number,
            "item_name": item_name,
            "total_ordered_qty": total_ordered_qty,
            "received_qty": received_qty,
            "received_date": received_date,
            "balance_qty": balance_qty,
            "issue_to_dept": issue_to_dept,
            "issue_date": issue_date,
            "rfr_qty": rfr_qty,
            "consume_in_test": consume_in_test,
            "qualified_qty": qualified_qty,
            "rejected_qty": rejected_qty,
            "user_acceptance": user_acceptance,
            "user_acceptance_date": user_acceptance_date,
            "send_to_vendor_qty": send_to_vendor_qty,
            "send_to_vendor_date": send_to_vendor_date,
            "net_balance_qty": net_balance_qty,
            "unit_price": unit_price,
            "total_price": total_price,
            "current_status": current_status
        }
        add_item(item_data)
        st.success("Item added successfully!")

st.divider()
st.subheader("📊 Inventory Table")
data = load_data()
st.dataframe(data, use_container_width=True)
