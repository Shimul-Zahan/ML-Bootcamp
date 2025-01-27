import streamlit as st

class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class FlatmatesBillSplitter:
    def __init__(self):
        self.flatmates = []

    def add_flatmate(self, name, days_in_house):
        flatmate = Flatmate(name, days_in_house)
        self.flatmates.append(flatmate)

    def calculate_shares(self, bill):
        total_days = sum(flatmate.days_in_house for flatmate in self.flatmates)
        shares = {}
        for flatmate in self.flatmates:
            shares[flatmate.name] = round((flatmate.days_in_house / total_days) * bill.amount, 2)
        return shares

# Streamlit App Code
def main():
    st.title("Flatmate Bill Splitter")
    st.write("Easily split bills among flatmates based on their stay duration!")

    # Collect Bill Information
    st.header("Bill Information")
    bill_amount = st.number_input("Enter the total bill amount ($):", min_value=0.0, step=0.1)
    bill_period = st.text_input("Enter the billing period (e.g., March 2025):")

    # Flatmates Section
    st.header("Flatmates")
    flatmate_name = st.text_input("Flatmate Name:")
    days_in_house = st.number_input("Days in House:", min_value=1, max_value=31, step=1)

    # Manage Flatmates
    splitter = FlatmatesBillSplitter()

    if "flatmates" not in st.session_state:
        st.session_state["flatmates"] = []

    if st.button("Add Flatmate"):
        if flatmate_name and days_in_house:
            st.session_state["flatmates"].append((flatmate_name, days_in_house))
            st.success(f"Added {flatmate_name} ({days_in_house} days)")
        else:
            st.error("Please enter valid flatmate details.")

    # Display Added Flatmates
    if st.session_state["flatmates"]:
        st.subheader("Flatmates List:")
        for i, (name, days) in enumerate(st.session_state["flatmates"], start=1):
            st.write(f"{i}. {name} - {days} days")

    # Calculate Shares
    if st.button("Calculate Shares"):
        if not st.session_state["flatmates"]:
            st.error("Add at least one flatmate before calculating shares.")
        else:
            for name, days in st.session_state["flatmates"]:
                splitter.add_flatmate(name, days)
            bill = Bill(bill_amount, bill_period)
            shares = splitter.calculate_shares(bill)

            st.subheader(f"Bill Shares for {bill_period}:")
            for name, share in shares.items():
                st.write(f"{name} owes: ${share:.2f}")

# Run the Streamlit App
if __name__ == "__main__":
    main()
