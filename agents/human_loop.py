class HumanInTheLoop:
    def __init__(self, config):
        self.config = config

    def get_human_feedback(self, chapter, stage):
        # Simulated feedback
        return f"Simulated feedback for stage: {stage}"

    def should_continue_iteration(self, feedback):
        return "needs" in feedback.lower()
