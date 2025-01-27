class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class FlatematesBillSplitter:
    def __init__(self):
        self.flatmates = []
        
    def add_flatemate(self, name, days_in_house):
        flatemate = Flatmate(name, days_in_house)
        self.flatmates.append(flatemate)
        # print(self.faltemates)
        
    def calculate_shares(self, bill):
        total_days = sum(flatmate.days_in_house for flatmate in self.flatmates)
        print(total_days)
        shares = {}
        for flatmate in self.flatmates:
            shares[flatmate.name] = self.calculate_bills(
                total_bill=bill.amount, 
                total_days=total_days,
                days_in_house= flatmate.days_in_house,
                )
        return shares

    def display_shares(self, bill):
        print(f"\nBill Period: {bill.period}")
        print(f"Total Bill Amount: ${bill.amount}\n")
        shares = self.calculate_shares(bill)
        # print(shares)
        for name, share in shares.items():
            print(f"{name} owes: ${share}")
        
    def show_flatemates(self):
        print("\nList of Flatmates:")
        for flatemate in self.faltemates:
            print(f"Name: {flatemate.name}, Days Stayed: {flatemate.days_in_house}")
            
    def calculate_bills(self, total_bill, total_days, days_in_house):
        return round((days_in_house / total_days) * total_bill, 2)
        


# Here is the main function
if __name__ == "__main__":
    splitter = FlatematesBillSplitter()
    
    print("Enter details for flatmates:")
    n = int(input("How many flatmates? "))
    
    for i in range(n):
        name = input(f"Name of the flatemate: ")
        while True:
            try:
                days = int(input(f"Days {name} stayed (must be <= 31): "))
                if 1 <= days <= 31:
                    break
                else:
                    print("Error: Days must be between 1 and 31.")
            except ValueError:
                print("Error: Please enter a valid number.") 
                       
        splitter.add_flatemate(name, days)
    
    # splitter.show_flatemates()
    amount = float(input("\nEnter total bill amount: $"))
    period = input("Enter billing period (e.g., March 2025): ")
    bill = Bill(amount, period)
    splitter.display_shares(bill)
    