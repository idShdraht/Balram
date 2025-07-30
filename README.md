# ATM Management System

A **Python-based ATM Management System** with **MySQL integration**.  
This project provides basic banking features like **customer registration, account creation, withdrawal, and account search** through a simple console menu interface.

---

## **Features**
- **Customer Management**: Add new customers and store their details.  
- **Account Management**: Create accounts with account type, balance, and PIN.  
- **Search Functionality**: Search customers and accounts by ID or account number.  
- **Withdrawals**: Secure withdrawal using a PIN (with limited attempts).  
- **Display Records**: View all customers and accounts in a tabular format.  

---

## **Technologies Used**
- **Python 3.12**  
- **MySQL** (via `mysql-connector-python`)  
- **Pandas** (for tabular data display)

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ATM-Management-System.git
cd ATM-Management-System

Install Required Packages
go to cmd and execute the below:
pip install mysql-connector-python pandas

Configure MySQL
Make sure MySQL is running on localhost.

Update the username and password inside ATMsenttomam.py:
userName = "root"
password = "YOUR_MYSQL_PASSWORD"

Run the Program
python ATMsenttomam.py
On first run, it will automatically create a database named ATM and required tables.

Menu Options:
1 - Add New Customer
2 - Display All Customers
3 - Search Customer
4 - Open New Account
5 - Display All Accounts
6 - Search Account
7 - Withdraw Amount
8 - Exit
0 - Help

DataBase Schema
Customer Table
| Column  | Type        |
| ------- | ----------- |
| CID     | INT (PK)    |
| CNAME   | VARCHAR(30) |
| ADDRESS | VARCHAR(30) |
| PHONE   | VARCHAR(55) |

Account Table
| Column        | Type         |
| ------------- | ------------ |
| CID           | INT          |
| ACCOUNT\_NO   | INT (PK)     |
| ACCOUNT\_TYPE | VARCHAR(90)  |
| AMOUNT        | INT          |
| PIN           | INT (Unique) |

Future Improvements
Add transaction history (deposits/withdrawals).
Encrypt PINs for better security.
Add GUI support for a better user experience.

Author
Your Name
📧 Email: [balaraman182006100@gmail.com]
GitHub: https://github.com/idShdraht
