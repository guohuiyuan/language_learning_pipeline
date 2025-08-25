import json
import csv
import ast


def convert_json_to_csv():
    # Read the JSON file
    # with open("output.json", "r", encoding="utf-8") as json_file:
    # with open("eudic_cards_output.json", "r", encoding="utf-8") as json_file:
    with open("eudic2.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Parse the JSON string to get the actual data
    word_data = data["key0"]

    # Define CSV output file
    csv_file = "output2.csv"

    # Write to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        # Define fieldnames based on the JSON structure
        fieldnames = ["单词", "单词释义"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write each row
        for item in word_data:
            writer.writerow(item)

    print(f"CSV file '{csv_file}' has been created successfully!")
    print(f"Converted {len(word_data)} records.")


if __name__ == "__main__":
    convert_json_to_csv()
