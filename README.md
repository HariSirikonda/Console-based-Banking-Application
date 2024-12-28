# 💳 Console Based Banking System 🏦

Welcome to the **State Bank of India Banking System**, a Python-based application that simulates basic banking operations such as account creation, deposit, withdrawal, and account display using CSV file storage. 📁

---

## 📝 Features
- 🧾 **Open a Bank Account**: Add new accounts with details like name, Aadhar number, PIN, and initial balance.
- 💰 **Deposit Money**: Add funds to an existing account.
- 💸 **Withdraw Money**: Subtract funds from an existing account.
- 👀 **Display All Accounts**: View all stored account details.
- 🔄 **Update and Save Data**: Persistent storage of account data in a CSV file.

---

## 🛠️ Prerequisites
Before running the project, ensure the following are installed:
- 🐍 Python 3.x
- 📦 Required libraries:
  - `pandas` 📊
  - `datetime` ⏰
  - `os` 🗂️

Install dependencies using:
```bash
pip install pandas
```

## 🚀 Getting Started
1. **Clone the Repository**:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Run the Application**: Execute the program using:
```bash
python banking_system.py
```
3. **Explore the Features**: Follow the on-screen menu to interact with the banking system.

## 📂 File Structure
- **Accounts.csv**: Stores all account data persistently.
- **banking_system.py**: Main Python script for the banking system.

## 📖 How It Works
### 🆕 Open an Account:
- Input personal details and set a PIN.
- An account number is generated automatically.

### 💵 Deposit Money:
- Provide the account number and the deposit amount.
- The balance updates instantly.

### 🏧 Withdraw Money:
- Enter the account number and the withdrawal amount.
- Ensures sufficient balance before deduction.

### 📋 Display Accounts:
- Shows all existing account records in a tabular format.

## ⚙️ Project Workflow
### Account Creation:
- Takes user input and appends to a DataFrame.
- Saves the updated DataFrame to `Accounts.csv`.

### Deposit/Withdrawal:
- Validates the account number.
- Updates the balance and saves changes.

### Data Persistence:
- Reads and writes data to `Accounts.csv` to ensure persistence.

## 🛡️ Security Features
- ✅ **PIN-based authentication** for account creation.
- ✅ **Data stored locally**, reducing exposure to online threats.


## 🌟 Future Enhancements
- 🔒 **PIN-based login** for transactions.
- 📱 **Add support for a GUI**.
- 🌐 **Integration with online databases** for scalability.

## 📜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute! 🚀

## 🤝 Contribution
We welcome contributions to make this project even better! 🛠️ Fork the repo, make changes, and submit a pull request.

## 📞 Contact
For any queries or suggestions, feel free to reach out. 📩
