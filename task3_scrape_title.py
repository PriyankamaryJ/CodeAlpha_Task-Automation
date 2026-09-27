"""
CodeAlpha - Python Programming Internship
Task 3 (Option C): Task Automation with Python Scripts
Scrape the title of a fixed webpage and save it to a file.

Key Concepts Used: requests, file handling.

Note: requires the 'requests' library.
    pip install requests
"""

import re
import requests

FIXED_URL = "https://www.python.org"


def get_page_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def save_title(title, url, output_file="page_title.txt"):
    with open(output_file, "w") as f:
        f.write(f"URL: {url}\n")
        f.write(f"Title: {title}\n")
    print(f"Saved title to '{output_file}'.")


if __name__ == "__main__":
    print("=== Scrape Webpage Title ===\n")
    url = input(f"Enter a URL (press Enter to use default '{FIXED_URL}'): ").strip() or FIXED_URL

    title = get_page_title(url)
    if title:
        print(f"\nPage Title: {title}")
        save_title(title, url)
    else:
        print("Could not retrieve the page title.")
