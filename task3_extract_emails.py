"""
CodeAlpha - Python Programming Internship
Task 3 (Option B): Task Automation with Python Scripts
Extract all email addresses from a .txt file and save them to another file.

Key Concepts Used: re, file handling.
"""

import re

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    emails = re.findall(EMAIL_PATTERN, content)
    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("No email addresses found.")
        return

    with open(output_file, "w") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email address(es).")
    print(f"Saved to '{output_file}'.")
    print("\nEmails found:")
    for email in unique_emails:
        print(f"  {email}")


if __name__ == "__main__":
    print("=== Extract Email Addresses ===\n")
    input_path = input("Enter path to the .txt file to scan: ").strip()
    output_path = input("Enter output file name (e.g. emails.txt): ").strip() or "emails.txt"
    extract_emails(input_path, output_path)
