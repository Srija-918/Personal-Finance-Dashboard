import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Personal Finance Dashboard")
df = pd.read_csv("expenses.csv")
st.write("Expense Data")
st.dataframe(df)
total_expense = df["Amount"].sum()
st.write("Total Expense:", total_expense)
highest_expense = df["Amount"].max()
average_expense = df["Amount"].mean()
st.write("Highest Expense:", highest_expense)
st.write("Average Expense:", average_expense)
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
