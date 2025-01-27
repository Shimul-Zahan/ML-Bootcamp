# Flatmate Bill Splitter

## Overview
This project is a Python-based program that helps manage shared bills among flatmates using Object-Oriented Programming (OOP). It calculates how much each flatmate owes based on the number of days they stayed in the flat.

---

## Features
- Calculate bill shares based on the days each flatmate stayed.
- Input details for the total bill, flatmates, and billing period.
- Display the calculated share for each flatmate.

---

## Classes and Responsibilities

### 1. **`Flatmate`**
   - **Attributes**:
     - `name`: Name of the flatmate.
     - `days_in_house`: Number of days the flatmate stayed.
   - **Methods**:
     - `calculate_share(total_bill, total_days)`: Calculates the flatmate's share of the total bill.

### 2. **`Bill`**
   - **Attributes**:
     - `amount`: Total amount of the bill.
     - `period`: Billing period (e.g., "March 2025").

### 3. **`FlatmatesBillSplitter`**
   - **Attributes**:
     - `flatmates`: A list of `Flatmate` objects.
   - **Methods**:
     - `add_flatmate(name, days_in_house)`: Adds a flatmate to the list.
     - `calculate_shares(bill)`: Calculates each flatmate’s share of the total bill.
     - `display_shares(bill)`: Displays each flatmate’s share.