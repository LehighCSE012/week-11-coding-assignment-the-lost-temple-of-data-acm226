"""Week 11 Assignment
Written By Andreas Marangos"""

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    # Hint: Use pd.read_excel, specify sheet_name and skiprows
    # Replace 'pass' with your code
    try:
        df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {excel_filepath}")
        return pd.DataFrame()
    # return the resulting DataFrame

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    # Hint: Use pd.read_csv, specify the separator for tabs ('\t')
    # Replace 'pass' with your code
    try:
        df = pd.read_csv(tsv_filepath, sep='\t')
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {tsv_filepath}")
        return pd.DataFrame()
    # return the resulting DataFrame

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for MM/DD/YYYY format.
    # Pattern idea: r"\d{2}/\d{2}/\d{4}"
    # Replace 'pass' with your code
    pattern = r"(?:0[1-9]|1[0-2])/(?:0[1-9]|[12]\d|3[01])/\d{4}"
    dates = re.findall(pattern, journal_text)
    return dates
    # return the list of found dates

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for AZMAR- followed by 3 digits.
    # Pattern idea: r"AZMAR-\d{3}"
    # Replace 'pass' with your code
    pattern = r"AZMAR-\d{3}"
    codes = re.findall(pattern, journal_text)
    return codes
    # return the list of found codes


# --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
     # Define file paths (ASSUME these files exist in the same directory)
    EXCEL_FILE = 'artifacts.xlsx'
    TSV_FILE = 'locations.tsv'
    JOURNAL_FILE = 'journal.txt'

    print(f"--- Loading Artifact Data from {EXCEL_FILE} ---")
    try:
        artifacts_df = load_artifact_data(EXCEL_FILE)
        if not artifacts_df.empty:
            print("Successfully loaded DataFrame. First 5 rows:")
            print(artifacts_df.head())
            print("\nDataFrame Info:")
            artifacts_df.info()
        else:
            # Function might have printed its own error, or returned empty
            print(f"Could not load data from {EXCEL_FILE}. Check file existence and format.")
    except Exception as e: # Catch any unexpected error during the call
        print(f"An unexpected error occurred loading {EXCEL_FILE}: {e}")


    print(f"\n--- Loading Location Notes from {TSV_FILE} ---")
    try:
        locations_df = load_location_notes(TSV_FILE)
        if not locations_df.empty:
            print("Successfully loaded DataFrame. First 5 rows:")
            print(locations_df.head())
            print("\nDataFrame Info:")
            locations_df.info()
        else:
            print(f"Could not load data from {TSV_FILE}. Check file existence and format.")
    except Exception as e:
        print(f"An unexpected error occurred loading {TSV_FILE}: {e}")


    print(f"\n--- Processing Journal from {JOURNAL_FILE} ---")
    try:
        # Reading the file content still requires handling potential FileNotFoundError
        with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        extracted_dates = extract_journal_dates(journal_content)
        print(f"Found dates: {extracted_dates}")

        print("\nExtracting Secret Codes...")
        extracted_codes = extract_secret_codes(journal_content)
        print(f"Found codes: {extracted_codes}")

    except FileNotFoundError:
        # This handles the case where the journal file itself is missing
        print(f"Error: File not found at {JOURNAL_FILE}")
    except Exception as e:
        print(f"An error occurred processing the journal: {e}")
