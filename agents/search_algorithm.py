class RLSearchAlgorithm:
    def __init__(self):
        self.content_metadata = []
        self.search_history = []
        self.reward_matrix = []

    def index_content(self, chapters):
        self.content_metadata = chapters

    def search(self, query):
        return self.content_metadata[:4]
