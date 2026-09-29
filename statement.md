# Statement

## Problem Statement
Many students and individuals rely on a fixed budget or allowance but struggle to keep track of where their money goes. Manually noting down expenses in a notebook or memory-based tracking is slow, inconvenient, and prone to errors, making it hard to know spending patterns or whether one is staying within budget. There is a need for a simple, lightweight tool that lets a user log their income and expenses, automatically calculate totals, and clearly show whether they are within their set budget — without requiring internet access, an account, or complex software.

The Personal Expense & Budget Tracker addresses this by providing a straightforward command-line program that records transactions, calculates totals, and persists data locally, so users can track their finances quickly and reliably.

## Scope of the Project
This project covers:
- Recording individual income and expense transactions (date, category, amount, description)
- Viewing all recorded transactions
- Setting and updating a single overall budget value
- Calculating total spending, total income, and remaining budget
- Calculating spending totals grouped by category
- Deleting incorrect or unwanted transaction entries
- Persisting all data locally in a JSON file so it is retained across sessions

This project does **not** cover:
- Multi-user accounts or login/authentication
- Cloud storage or syncing across devices
- Monthly/recurring budget periods (only a single overall budget is supported)
- Graphical user interface (GUI) — the tool is command-line only
- Currency conversion or multi-currency support
- Bank account integration or automatic transaction import

## Target Users
- College/university students managing a personal allowance or monthly budget
- Individuals who want a simple, no-installation-hassle way to track daily expenses
- Beginner programmers and instructors, as a reference example of a beginner-friendly Python project using core concepts (loops, conditionals, functions, dictionaries, file I/O)

## High-Level Features
1. **Transaction Management** — Add income/expense entries and view them in a list.
2. **Budget Management** — Set an overall budget and update it at any time.
3. **Financial Summary** — Automatically calculate total spending, total income, and remaining budget.
4. **Category Analysis** — Break down spending by category to identify where money is going.
5. **Data Persistence** — Save all data to `expenses.json` automatically and reload it on the next run.
6. **Data Correction** — Delete incorrectly entered transactions.
7. **Simple Interface** — Menu-driven terminal interface requiring no technical setup beyond Python.