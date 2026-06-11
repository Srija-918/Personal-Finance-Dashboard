import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide"
)
st.sidebar.title("💰 Finance Dashboard")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Reports"]
)
budget = st.sidebar.number_input(
    "Monthly Budget (₹)",
    min_value=0,
    value=10000
)
st.sidebar.markdown("---")
st.sidebar.write("Made by Srija")
st.title("💰 Personal Finance Dashboard")
df = pd.read_csv("expenses.csv")
st.write("Expense Data")
st.dataframe(df)
st.subheader("📈 Expense Trend")
st.line_chart(df["Amount"])
total_expense = df["Amount"].sum()
remaining = budget - total_expense
st.subheader("💸 Budget Tracker")
st.progress(min(total_expense / budget, 1.0))
st.write(f"Budget: ₹{budget}")
st.write(f"Spent: ₹{total_expense}")
st.write(f"Remaining: ₹{remaining}")
highest_expense = df["Amount"].max()
average_expense = df["Amount"].mean()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Total Expense", f"₹{total_expense}")
with col2:
    st.metric("📈 Highest Expense", f"₹{highest_expense}")
with col3:
    st.metric("📊 Average Expense", f"₹{average_expense:.2f}")
category_expense = df.groupby("Category")["Amount"].sum()
st.write("Expenses by Category")
st.write(category_expense)
fig, ax=plt.subplots()
category_expense.plot(kind="bar",ax=ax)
ax.set_title("Expenses by category")
ax.set_xlabel("Category")
ax.set_ylabel("Amount")
st.pyplot(fig)
fig2, ax2 = plt.subplots()
category_expense.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)
ax2.set_ylabel("")
st.pyplot(fig2)
uploaded_file = st.file_uploader(
    "Upload Expense CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
st.download_button(
    "Download Data",
    df.to_csv(index=False),
    "expenses_report.csv",
    "text/csv"
)