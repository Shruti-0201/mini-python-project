import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="bank"
)

cursor = db.cursor()


def open_account(customer_id, initial_balance):
    sql = " insert into accounts (customer_id, balance) values (%s, %s)"
    cursor.execute(sql, (customer_id, initial_balance))
    db.commit()
    print("Account created successfully.")

def deposit(account_number, amount):
    sql = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    cursor.execute(sql, (amount, account_number))
    db.commit()
    print("Amount deposited successfully.")

def withdraw(account_number, amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        sql = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
        cursor.execute(sql, (amount, account_number))
        db.commit()
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")

def view_accounts():
    cursor.execute("""
        SELECT accounts.account_number, customers.name, accounts.balance
        FROM accounts
        JOIN customers ON accounts.customer_id = customers.customer_id
    """)
    for (acc_no, name, balance) in cursor.fetchall():
        print(f"Account No: {acc_no}, Customer: {name}, Balance: ₹{balance}")

while True:
    print("\n--- Banking Management System ---")
    print("1. Open Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Accounts")
    print("5. Exit")

    choice = int(input("Enter your choice: "))


    if  choice == 1:
        customer_id = int(input("Enter customer ID: "))
        balance = float(input("Enter initial balance: "))
        open_account(customer_id, balance)

    elif choice == 2:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        deposit(acc_no, amount)

    elif choice == 3:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        withdraw(acc_no, amount)

    elif choice == 4:
        view_accounts()

    elif choice == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

cursor.close()
db.close()

