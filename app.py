import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide"
)
st.sidebar.title("Finance Dashboard")
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
if page == "Dashboard":
    st.title("Personal Finance Dashboard")
    st.subheader("Add New Expense")
    st.write("Expense Data")
    st.subheader("Delete Expense")
expense_index = st.selectbox(
    "Select expense to delete",
    df.index
)
if st.button("Delete Expense"):
    df = df.drop(expense_index)
    df = df.reset_index(drop=True)
    df.to_csv("expenses.csv", index=False)
    st.success("Expense Deleted!")
    st.dataframe(df)
    st.subheader("Budget Tracker")
elif page == "Reports":
    st.title("Reports")
    st.subheader("Expense Trend")
    st.line_chart(df["Amount"])
    category_expense = df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    category_expense.plot(kind="bar", ax=ax)
    st.pyplot(fig)
    fig2, ax2 = plt.subplots()
    category_expense.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)
    st.download_button(
        "Download Data",
        df.to_csv(index=False),
        "expenses_report.csv",
        "text/csv"
    )
