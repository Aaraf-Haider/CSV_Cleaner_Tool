CSV Cleaner Tool

A simple and smart Python project that:

Cleans CSV files automatically

Removes duplicates and missing values

Formats text

Converts column types

Saves cleaned data to SQLite database

Logs all actions to a file

(Future feature: Tkinter GUI)

🧰 Features

✅ Automatically detect and load CSV files
✅ Detects and saves bad rows (missing values)
✅ Removes duplicates based on name, age, city
✅ Converts columns to numeric where possible
✅ Saves cleaned data into SQLite
✅ Keeps track of actions & errors in app_log.txt

🧠 Tech Stack

Python 3.x

Pandas

SQLite3

Logging Module

(Tkinter planned for GUI)

⚙️ Installation

Clone this repository:

git clone https://github.com/<your-username>/CSV_Cleaner_Tool.git


Go to project folder:

cd CSV_Cleaner_Tool


Install required libraries:

pip install pandas

▶️ Run the Program
python main.py


The script will:

Detect CSV files in your folder

Clean and save data automatically

Log all actions into app_log.txt

🧩 Example Output
Available CSV files:
1. sample.csv

Original Data:
   name   age   city
   Aaraf  21    Karachi
   ...

After Cleaning:
   Name   Age   City
   Aaraf  21    Karachi

📦 Files Generated
File	Description
database.db	Cleaned data stored in SQLite
bad_rows.csv	Invalid/missing rows saved here
app_log.txt	All actions & errors logged here
🚀 Future Improvements

GUI using Tkinter

SQL query browser

Export to Excel

👨‍💻 Author

Aaraf Haider
📍 BSCS, UBIT
💡 Python Developer | Data Enthusiast | Aspiring Data Engineer