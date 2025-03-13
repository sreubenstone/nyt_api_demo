import os
from dotenv import load_dotenv
from nytimes_source import NYTimesSource

load_dotenv() 

# This function runs a New York Times article search query.
# It takes your API key, a search term, and optionally how many batches to fetch.
# It then prints out the articles in batches and shows the schema of the results.
def run_nytimes_article_search_query(api_key, query, max_batches=2):
    """
    Run a search query to get New York Times articles.

    This function uses your API key and query to fetch articles in batches.
    It prints out each batch of articles and the overall schema of the fetched data.
    """
    ny_times_loader = NYTimesSource(api_key)
    print(f"Articles for query: {query}")
    for batch in ny_times_loader.getDataBatch(query, max_batches=max_batches):
        print("Batch:")
        for article in batch:
            print(" -", article.get("headline.main", "No headline"))

    schema = ny_times_loader.getSchema(query)
    print("\nSchema for query:", query)
    print(schema)


if __name__ == "__main__":
    # When running this file directly, we fetch articles for a preset query.
    api_key = os.getenv("NYTIMES_API_KEY")
    query = "Silicon Valley"
    run_nytimes_article_search_query(api_key, query)
