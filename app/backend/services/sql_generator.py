import yaml
from typing import Dict

# In real implementation, this will call Vertex AI (Gemini)
# For now, we simulate structure


class SQLGenerator:
    def __init__(self, semantic_model_path: str):
        self.semantic_model = self._load_semantic_model(semantic_model_path)

    def _load_semantic_model(self, path: str) -> Dict:
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def build_prompt(self, user_query: str) -> str:
        """
        Construct LLM prompt using semantic layer
        """
        return f"""
You are an expert data analyst.

Use ONLY the tables and columns defined below.

Semantic Model:
{self.semantic_model}

User Question:
{user_query}

Instructions:
- Generate valid BigQuery SQL
- Do NOT use columns not defined above
- Do NOT use SELECT *
- Use explicit joins when needed
- Prefer aggregation when appropriate

Return ONLY SQL.
"""

    def generate_sql(self, user_query: str) -> str:
        """
        Placeholder for LLM call
        """
        prompt = self.build_prompt(user_query)

        # TODO: Replace with Vertex AI call
        print("=== PROMPT SENT TO LLM ===")
        print(prompt)

        return "-- SQL will be generated here"
