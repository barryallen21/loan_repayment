class Loan:
    """
    Loan Class
    """
    def __init__(self, input):
        """
        init for loan class
        :param input: This include details of loan
        """
        self.input = input
        self.accounts = []

    def create_account(self):
        """
        This method creates account and saves data to in json file
        :return: account data
        """
        self.accounts.append(input)
        self.update_data_to_json("account_data.json", self.accounts)
        return self.accounts

    def emi_calculator(self):
        """
        This method calculates monthly emi
        :return: emi
        """
        r = self.input["interest"]/ 12 / 100
        emi = (self.input["principal_amount"] * r * ((1 + r) ** self.input["duration"])) / (((1 + r) ** self.input["duration"]) - 1)
        return emi

    def loan_amount_calculator(self):
        """
        This method calculates total loan including interest
        :return: loan amount including interest
        """
        total_loan_amount = self.input["principal_amount"] + (self.input["principal_amount"] / self.input["duration"])
        return total_loan_amount

    def calculate_remaning_amount(self, installment):
        """
        This method returns remaining amount after n months
        :param installment: no. of installments
        :return: remaining amount after n months
        """
        emi = self.emi_calculator()
        total_loan_amount = self.loan_amount_calculator()
        return (total_loan_amount - (installment * emi))

    def save_monthly_repayment(self, amount, month):
        """
        This method saves the history of payment
        :param amount: amount given each month
        :param month: name of month
        :return:
        """
        repay_history = dict()
        repay_history["month"] = month
        repay_history["amount"] = amount
        self.update_data_to_json("repayment_history.json", repay_history)

    def update_data_to_json(self, filename, data):
        """
        updates data into json file
        :param filename: name of file
        :param data: data to be written
        :return:
        """
        with open(filename, "a") as file:
            file.write(str(data) + "\n")
            file.close()

    def write_data_to_json(self, filename, data):
        """
        writes data into json file
        :param filename: name of file
        :param data: data to be written
        :return:
        """
        with open(filename, "w") as file:
            file.write(str(data) + "\n")
            file.close()

    def read_data_from_json(self, filename="repayment_history.json"):
        """
        read data from json file
        :param filename: name of file
        :return:
        """
        with open(filename, "r") as file:
            data = file.read()
        return data

# ***************************** input variables **********************************
input = {
    "borrower_name": "ABC",
    "principal_amount": 10000,
    "interest": 10,
    "duration": 12
}
check_amount_after_installments = 2
monthly_amount = 1000
month_name = 'January'

# ****************************** function callers **********************************
obj = Loan(input)
account_details = obj.create_account()
total_loan_amount = obj.loan_amount_calculator()
emi = obj.emi_calculator()
remaining_amount = obj.calculate_remaning_amount(check_amount_after_installments)
obj.save_monthly_repayment(month_name, monthly_amount)
payment_history = obj.read_data_from_json()

# ****************************** console printers ***************************************
print({"account_details": account_details})
print({"Total loan amount including interest": total_loan_amount})
print({"Total emi": emi})
print({"remaining balance after n payments": remaining_amount})
print({"history of payment": payment_history})