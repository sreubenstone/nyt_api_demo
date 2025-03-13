# NYTimes Article Search Loader

This project is a simple Python-based loader that connects to the New York Times Article Search API to fetch and display articles in batches. It uses a generator to load data incrementally, flattens nested JSON responses for easier consumption, and even dynamically extracts the schema of the data.

## Features

- **Incremental Loading:** Uses a generator to fetch data in batches.
- **Data Flattening:** Converts nested JSON data into a flat dictionary format.
- **Dynamic Schema:** Extracts the schema (keys) from the first batch of results.
- **Environment Variables:** Manages sensitive data (API key) using environment variables.

## Prerequisites

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. **Clone the repository or download the project files.**

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Setup

1. Create a .env file in the root directory with the following content: ```  
   NYTIMES_API_KEY=your_actual_api_key Replace your_actual_api_key with your actual New York Times API key.

## Usage

To run the loader and see it in action, simply execute:

```
python main.py
```

This will run a sample query (e.g., "Silicon Valley"), print out the articles in batches, and display the dynamic schema of the returned data.

## File Structure

```
project/
├── nytimes_source.py    # Contains the NYTimesSource class and helper methods
├── main.py              # Entry point to run the article search query
├── .env                 # Environment file (not tracked in version control)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Help from external tools

- GPT-o3 mini-high was used to create documentation and README file
- GPT-o3 mini-high was used to write \_flatten_dict method
