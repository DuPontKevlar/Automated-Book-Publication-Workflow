from dataclasses import dataclass

@dataclass
class WorkflowConfig:
    source_url: str
    output_dir: str = "./data"
    gemini_api_key: str = None
    max_iterations: int = 3
