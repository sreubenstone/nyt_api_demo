import requests

# This class handles connecting to the New York Times Article Search API.
# It includes methods to fetch articles in batches and to figure out what data fields are returned.
class NYTimesSource:
    def __init__(self, api_key):
        # Save your API key for later use.
        self.api_key = api_key

    # This private helper method flattens nested dictionaries.
    # It converts a nested dict into a single-level dict with keys joined by dots.
    @staticmethod
    def _flatten_dict(d, parent_key='', sep='.'):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(NYTimesSource._flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    # This method is a generator that fetches and yields batches of articles for a given query.
    # It returns flattened articles, making it easier to work with the data.
    def getDataBatch(self, query, max_batches=1):
        """
        Generator that yields batches of flattened articles for the given query.
        """
        page = 0
        batch_count = 0
        while batch_count < max_batches:
            url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
            params = {"api-key": self.api_key, "q": query, "page": page}
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                articles = data.get("response", {}).get("docs", [])
                if not articles:
                    break
                flattened_articles = [NYTimesSource._flatten_dict(article) for article in articles]
                yield flattened_articles
                batch_count += 1
                page += 1
            except Exception as e:
                print(f"Error: {e}")
                break

    # This method gets a dynamic schema (i.e. list of keys) based on the first batch of results.
    # It's a quick way to see what fields you can expect in your flattened articles.
    def getSchema(self, query):
        """
        Return a dynamic schema based on the first batch of articles for the given query.
        """
        for batch in self.getDataBatch(query, max_batches=1):
            if batch:
                return list(batch[0].keys())
        return []
