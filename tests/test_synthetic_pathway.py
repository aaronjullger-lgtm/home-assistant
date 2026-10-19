import unittest
from pathlib import Path


PACKAGE = Path(__file__).parents[1] / "config/packages/context_pathway_demo.yaml"


class SyntheticPathwayConfigTests(unittest.TestCase):
    def test_clear_motion_restarts_pathway_hold(self):
        config = PACKAGE.read_text()
        automation = config.split("  - id: demo_pathway_off_after_hold", 1)[0]
        self.assertIn("entity_id: input_boolean.demo_entry_motion", automation)
        self.assertIn('to: "off"', automation)
        self.assertIn("entity_id: timer.demo_pathway_hold", automation)


if __name__ == "__main__":
    unittest.main()
