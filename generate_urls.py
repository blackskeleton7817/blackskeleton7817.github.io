import os
import sys
import json
from urllib.parse import quote


def generate_json(directory, base_url, output_file="data.json"):
    urls = []

    directory = os.path.abspath(directory)

    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)

            rel_path = os.path.relpath(full_path, directory)
            rel_path = rel_path.replace(os.sep, "/")

            # URL-encode the path to handle spaces and special characters
            encoded_path = "/".join(
                quote(part, safe="") for part in rel_path.split("/")
            )

            url = f"{base_url.rstrip('/')}/{encoded_path}"
            urls.append(url)

    data = {"data": urls}

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Generated {output_file} with {len(urls)} entries.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_urls.py <directory> <base_url>")
        sys.exit(1)

    directory = sys.argv[1]
    base_url = sys.argv[2]

    generate_json(directory, base_url)
