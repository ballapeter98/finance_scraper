# finance_scraper

## Setup

Download and install Python from here: https://www.python.org/downloads/release/python-3913/ (see Windows installer at the bottom of the page)

Download and extract the project from github (Code -> Download ZIP)

Open a Command Prompt window (type cmd in Windows search bar).

Navigate to the <path> where you have extracted the project with cd command then install the required dependencies:

```bash
cd <path>
python -m pip install -e requirements.txt
```

## Usage

In the project folder, you can run the program like this:

```bash
python main.py input.txt
```

Where input.txt is a config file in which each line follows the structure of the one supplied in the project:
url,path,filename