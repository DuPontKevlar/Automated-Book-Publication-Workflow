import google.generativeai as genai

class AIProcessor:
    def __init__(self, config):
        self.config = config
        if config.gemini_api_key:
            genai.configure(api_key=config.gemini_api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
