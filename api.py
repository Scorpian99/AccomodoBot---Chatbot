import requests
import pandas as pd

def fetch_data(url):
    """
    Fetches data from the given URL and returns it as a pandas DataFrame.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        pandas.DataFrame: The fetched data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    data = pd.read_csv(response.text)
    return data

def save_data(data, file_name):
    """
    Saves the given data to a CSV file.

    Args:
        data (pandas.DataFrame): The data to save.
        file_name (str): The name of the CSV file.
    """
    data.to_csv(file_name, index=False)

if __name__ == "__main__":
    url = "https://www.squareyards.com/projects-by-api-sqaure-reality-in-mumbai"
    data = fetch_data(url)

    if data is not None:
        save_data(data, "imported_data.csv")