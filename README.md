Transaction Wallet Simulator

A Python command-line wallet management project built using Object-Oriented Programming concepts.

Features

Create multiple wallet accounts
Deposit money
Withdraw money
Transfer money between wallets
View wallet details
View transaction history
Show all wallets
Save wallets to JSON file
Load wallets from JSON file
Encapsulation using private balance/history attributes


Project Structure

main.py - Runs menu system
handlers.py - Handles user input and menu actions
operations.py - Deposit, withdraw, transfer logic
storage.py - Save/load wallets from JSON
helpers.py - Utility display functions
model.py - WalletAccount class


Concepts Used

Classes and Objects
Encapsulation
Dictionaries
Loops
Functions
Error Handling
File Handling
JSON Storage
Modular Code Structure


How to Run

python3 src/main.py


Data Storage

Wallet data is stored in:
data/wallets.json


Sample Menu

Create Wallet
Deposit
Withdraw
Transfer
Show Wallet
Show History
Save Wallets
Load Wallets
Show All Wallets
Exit