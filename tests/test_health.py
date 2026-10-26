"""
Health tests for PromptLattice.
Signature: Mourad.Soltani
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import forge_prompt, estimate_tokens, SIGNATURE

class TestHealth(unittest.TestCase):
    def test_signature_present(self):
        result = forge_prompt("Test task")
        self.assertEqual(result["signature"], SIGNATURE)
        self.assertIn(SIGNATURE, result["full_prompt"])
    
    def test_token_estimate(self):
        text = "a" * 40
        self.assertEqual(estimate_tokens(text), 10)
    
    def test_forge_basic(self):
        result = forge_prompt("Write a function to reverse a string", role="Python expert")
        self.assertIn("Python expert", result["full_prompt"])
        self.assertIn("Write a function", result["full_prompt"])
        self.assertGreater(result["estimated_tokens"], 10)
        self.assertGreaterEqual(result["quality_score"], 60)
    
    def test_json_serializable(self):
        import json
        result = forge_prompt("Sample")
        json.dumps(result)  # should not raise

if __name__ == "__main__":
    unittest.main()
