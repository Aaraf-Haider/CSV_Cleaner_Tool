🧹 CSV Cleaner Tool: Simple, Smart Data CleaningA simple and smart Python project designed to automate the tedious tasks of cleaning and prepping CSV files, ensuring your data is ready for analysis or storage.✨ FeaturesThis tool performs essential data pipeline steps, focusing on automation and reliability.✅ Automatic File Detection: Detect and load all CSV files in the project folder automatically.🗑️ Duplicate Removal: Identifies and eliminates duplicate rows based on key columns (name, age, city).❌ Missing Value Handling: Detects and saves "bad rows" (those with missing values) to a separate file for later inspection.🔄 Type Conversion: Intelligently converts columns to the correct numeric types where possible, facilitating data operations.💾 Persistent Storage: Saves all cleaned and validated data into a robust SQLite database (database.db).📜 Activity Logging: Keeps a detailed record of all cleaning actions, errors, and warnings in app_log.txt.(Future Feature: Tkinter GUI)🧠 Tech StackCategoryTechnologyPurposeLanguagePython 3.xCore language for scripting and logic.Data ProcessingPandasHigh-performance data manipulation and cleaning.DatabaseSQLite3Lightweight, file-based database for storage.UtilitiesLogging ModuleTracking operations and errors.Future UI(Tkinter planned)Simple, native graphical user interface.⚙️ Get Started (Installation & Setup)To get this tool running locally, simply follow these commands:Clone the repository:Bashgit clone https://github.com/<your-username>/CSV_Cleaner_Tool.git
Navigate to the project directory:Bashcd CSV_Cleaner_Tool
Install the required libraries:Bashpip install pandas
▶️ How to Run the ProgramPlace your target CSV files (e.g., data.csv, sample.csv) in the CSV_Cleaner_Tool folder, then execute:Bashpython main.py
The script will automatically process your files, clean the data, and store the results.🧩 Example Output (Console)A clear visual output guides you through the process:Available CSV files:
1. sample.csv

Original Data Snapshot:
      name  age        city
    0 Aaraf   21     Karachi
    1 John    --    New York
    ...

After Cleaning:
     Name  Age        City
    0 Aaraf   21     Karachi
    ...

🎉 Cleaning complete! Data saved to database.db.
📦 Files GeneratedFile NameDescriptiondatabase.dbThe cleaned, validated data stored securely in an SQLite database.bad_rows.csvInvalid rows (with missing values) saved here for inspection and recovery.app_log.txtA comprehensive log file tracking all actions and reported errors.🚀 Future ImprovementsGUI: Implement a full Tkinter GUI for drag-and-drop file selection and settings configuration.SQL Browser: Add a utility for quick SQL query browsing of the cleaned database.Export Options: Introduce functionality to export cleaned data to Excel and other formats.👨‍💻 AuthorAaraf Haider📍 BSCS, UBIT | 💡 Python Developer | Data Enthusiast | Aspiring Data Engineer
