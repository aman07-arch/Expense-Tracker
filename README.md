\# Personal Expense \& Budget Tracker



\## Overview

Personal Expense \& Budget Tracker is a command-line Python application that helps a user record their daily income and expenses, set a personal budget, and instantly see how much they have spent, earned, and how much budget remains. It removes the need for manual notebook tracking by storing every transaction in a local JSON file, so data is never lost between sessions.



This project was built as part of the "Introduction to Problem Solving and Programming" course to demonstrate core programming concepts: variables, loops, conditionals, functions, dictionaries, lists, and file handling.



\## Features

\- Add an expense or income entry with date, category, amount, and description

\- View all recorded transactions in a readable list

\- Set and update a total budget

\- Automatically calculate total spending, total income, and remaining budget

\- View category-wise spending totals (e.g. food, travel, rent)

\- Delete a transaction by its number

\- Persistent storage using a local `expenses.json` file

\- Simple menu-driven interface that runs in the terminal



\## Technologies / Tools Used

\- Language: Python 3

\- Built-in Library: `json` (for saving and loading data)

\- Storage: Local JSON file (`expenses.json`)

\- Interface: Command-line (terminal-based menu)

\- No external/third-party libraries required



\## Steps to Install \& Run the Project



\### Prerequisites

\- Python 3.x installed on your system

\- A terminal / command prompt



\### Installation

1\. Clone or download this repository:



git clone <your-repository-link>



2\. Navigate into the project folder:



cd personal-expense-budget-tracker





\### Running the Project

Run the following command in the project folder:



python main.py



or, depending on your system:



python3 main.py





On first run, since no `expenses.json` exists yet, the program will start with an empty transaction list and a budget of 0. A new `expenses.json` file will be created automatically the first time you add data or set a budget.



\## Instructions for Testing

The program can be tested manually by running it and using the menu options:



1\. \*\*Test adding a transaction\*\*

&#x20;  - Choose option `1`

&#x20;  - Enter type as `expense`, a date, category, amount, and description

&#x20;  - Confirm the message "Saved successfully" appears

&#x20;  - Choose option `2` to verify the entry appears in the list



2\. \*\*Test invalid input handling\*\*

&#x20;  - Try entering a non-numeric value for amount → program should show an error and not crash

&#x20;  - Try entering a type other than `expense`/`income` → program should reject it



3\. \*\*Test budget calculation\*\*

&#x20;  - Choose option `3` and set a budget (e.g. 5000)

&#x20;  - Add a few expense and income entries

&#x20;  - Choose option `4` to confirm total spending, total income, and remaining budget are calculated correctly



4\. \*\*Test category totals\*\*

&#x20;  - Add expenses under different categories (e.g. food, travel)

&#x20;  - Choose option `5` and confirm totals are grouped correctly by category



5\. \*\*Test delete functionality\*\*

&#x20;  - Choose option `6`, view the list, delete a valid entry number

&#x20;  - Try an invalid/out-of-range number → program should show an error, not crash



6\. \*\*Test data persistence\*\*

&#x20;  - Add a few entries, then choose option `7` to exit

&#x20;  - Re-run the program and choose option `2` → previously saved entries should still be there



7\. \*\*Test exit\*\*

&#x20;  - Choose option `7` and confirm the program saves data and closes without errors



\## Files in This Repository

\- `main.py` — complete source code for the application

\- `expenses.json` — auto-generated file that stores transaction and budget data

\- `README.md` — this file

\- `statement.md` — problem statement, scope, and features document

