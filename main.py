import pandas as pd
import sqlite3
import os
import logging

logging.basicConfig(
    filename="app_log.txt",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
)


def process_csv_to_sqlite(filename):

    while True:
        # Step 1: Show available CSV files in current folder
        csv_files = [f for f in os.listdir() if f.endswith(".csv")]
        if not csv_files:
            print(" No CSV files found in this folder! Please add one and try again.")
            logging.warning("No CSV files found in current directory.")
            break

        print(" Available CSV files:")
        for i, file in enumerate(csv_files, 1):
            print(f"{i}. {file}")

        # Step 2: Ask user to pick a file
        choice = input("\nEnter the number of the file you want to load: ")

        try:
            choice = int(choice)
            filename = csv_files[choice - 1]
            logging.info(f"user selected file; {filename}")
            
            df = pd.read_csv(filename)
            print("Original data: ")
            print(df)
            logging.info(f"File '{filename}' loaded successfully with {len(df)} rows.")

        
            bad_rows = df[df.isnull().any(axis=1)]
            if not bad_rows.empty:

                bad_rows.to_csv("bad_rows.csv", index=False)
                print(f"{len(bad_rows)} bad rows found")
                logging.warning(f"{len(bad_rows)} bad rows found and saved to bad_rows.csv.")
            else:
                print("bad_rows not found")
                logging.info("No Bad rows found")

            df = df.drop_duplicates(subset=["name", "age", "city"] , keep= 'first')
            print("After Removing Duplicate: ")
            print(df)
            logging.info("Removed duplicate rows based on ['name', 'age', 'city'].")

            df = df.dropna()
            print("dropping Nan value")
            print(df)
            logging.info("Dropped rows with missing values.")

            df[['name', 'city']] = df[['name', 'city']].apply(lambda x:x.str.title())
            print("After Formatting")
            print(df)
            logging.info("Formatted text columns ('name', 'city') to title case.")

            for col in df.columns:
                try:
                    df[col] = pd.to_numeric(df[col])
                    print(f"convert {col} to numeric type")
                    logging.info(f"convert a {col} to numeric form")
                except Exception:
                    print(f"{col} is not changed")
            print("all columns adjust their data type")
            logging.info("All column adjust their data type")


            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            df.to_sql("people", conn, if_exists="replace", index = False)
            logging.info("Cleaned data inserted into SQLite database (table: people).")

            result = pd.read_sql("SELECT * FROM people", conn)
            print("Data from database")
            print(result)

            conn.close()
            logging.info("Database connection closed successfully.")
            print("\n All done! Check 'app_log.txt' for details.\n")
            return True
            break

        except (ValueError, IndexError):
            print("Invalid choice! Please enter a valid number.\n")  
            logging.error("User entered invalid file choice.")  
            return False,"invalid file"
        except FileNotFoundError:
            print(f"your file '{filename}' doesn't exist. try again")
            logging.error(f"File '{filename}' not found.")
            return False,"file not found"
        except pd.errors.EmptyDataError:
            print("the file exist but it is empty")
            logging.error(f"File '{filename}' is empty.")
            return False, "file is empty"
        except Exception as e:
            print(f"an error occured: {e}")
            logging.exception(f"Unexpected error: {e}")
            return False, f"an error occured{e}"