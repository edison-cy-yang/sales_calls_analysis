from pymongo import MongoClient


class DatabaseClient:
    def __init__(
        self, db_name="sales_call_analysis", collection_name="queries_responses"
    ):
        # Initialize the MongoDB client
        self.client = MongoClient("localhost", 12345)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def store_query_response(self, query, response):
        # Insert a new query and response into the MongoDB collection.
        document = {"query": query, "response": response}
        self.collection.insert_one(document)

    def close(self):
        self.client.close()
