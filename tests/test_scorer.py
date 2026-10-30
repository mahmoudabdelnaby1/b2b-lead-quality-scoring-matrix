import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from lead_scorer import score_b2b_leads

class TestLeadScorer(unittest.TestCase):
    def test_scoring(self):
        c = Path(__file__).resolve().parent.parent / "examples" / "b2b_inbound_leads.csv"
        r = Path(__file__).resolve().parent.parent / "config" / "scoring_rules.json"
        o = Path(__file__).resolve().parent.parent / "reports" / "scored_leads.csv"
        count = score_b2b_leads(str(c), str(r), str(o))
        self.assertGreaterEqual(count, 1)

if __name__ == "__main__":
    unittest.main()
