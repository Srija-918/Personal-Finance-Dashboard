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
df=pd.read_csv("expenses.csv")
if page == "Dashboard":
    st.title("💰 Personal Finance Dashboard")
    st.subheader("➕ Add New Expense")

    expense_date = st.date_input("Date")

    category = st.selectbox(
        "Category",
        ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"]
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0
    )

    if st.button("Add Expense"):
        new_expense = pd.DataFrame({
            "Date": [expense_date],
            "Category": [category],
            "Amount": [amount]
        })

        df = pd.concat([df, new_expense], ignore_index=True)
        df.to_csv("expenses.csv", index=False)
        st.success("✅ Expense Added!")

    st.write("Expense Data")
    st.dataframe(df)

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

elif page == "Reports":

    st.title("📊 Reports")

    st.subheader("📈 Expense Trend")
    st.line_chart(df["Amount"])

    category_expense = df.groupby("Category")["Amount"].sum()

    st.write("Expenses by Category")
    st.write(category_expense)

    fig, ax = plt.subplots()
    category_expense.plot(kind="bar", ax=ax)
    ax.set_title("Expenses by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
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