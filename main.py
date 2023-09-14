import csv
import logging
import os
import requests
import sys
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO)


def read_config(args: List[str]) -> List[dict]:
    """Parse a config. Format should be: <url>,<path, separated with / chars>,<filename>"""
    assert len(args) == 2, "There should be exactly 1 argument!"
    item_list = []
    with open(args[1], "r") as conf:
        lines = csv.reader(conf)

        for line in lines:
            assert len(line) == 3, "There should be 3 elements each line, separated with comma!"
            obj = {
                "url": line[0],
                "path": line[1],
                "filename": line[2]
            }
            item_list.append(obj)

    return item_list


def process_item(item: dict):
    """Read and download a file from given url to the specified path"""
    url = item["url"]
    path = item["path"]
    filename = item["filename"]

    resp = requests.get(url)

    Path(path).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(path, filename), "wb") as file:
        file.write(resp.content)

    logging.info(f"Processed {url} content to {path}/{filename}")


def main(args: List[str]):
    """Process items in config file"""
    item_list = read_config(args)
    for item in item_list:
        process_item(item)

    logging.info("DONE")


if __name__ == "__main__":
    main(sys.argv)
