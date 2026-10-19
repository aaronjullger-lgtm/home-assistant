import unittest
from pathlib import Path


PACKAGE = Path(__file__).parents[1] / "config/packages/context_pathway_demo.yaml"
CONFIG = PACKAGE.read_text()


def automation_block(automation_id: str, next_id: str) -> str:
    start = CONFIG.index(f"  - id: {automation_id}")
    end = CONFIG.index(f"  - id: {next_id}", start)
    return CONFIG[start:end]


class SyntheticPathwayConfigTests(unittest.TestCase):
    def test_entry_motion_requires_occupied_and_routine_modes(self):
        automation = automation_block(
            "demo_pathway_on_entry_motion", "demo_pathway_restart_hold_on_clear"
        )
        self.assertIn('entity_id: input_boolean.demo_sleep_mode\n        state: "off"', automation)
        self.assertIn('entity_id: input_boolean.demo_manual_override\n        state: "off"', automation)
        self.assertIn('entity_id: binary_sensor.demo_house_occupied\n        state: "on"', automation)

    def test_clear_motion_restarts_pathway_hold(self):
        automation = automation_block(
            "demo_pathway_restart_hold_on_clear", "demo_pathway_off_after_hold"
        )
        self.assertIn("entity_id: input_boolean.demo_entry_motion\n        to: \"off\"", automation)
        self.assertIn('entity_id: input_boolean.demo_pathway_light\n        state: "on"', automation)
        self.assertIn("entity_id: timer.demo_pathway_hold", automation)

    def test_timer_expiry_only_turns_pathway_off_when_motion_is_clear(self):
        automation = automation_block(
            "demo_pathway_off_after_hold", "demo_manual_override_auto_clear"
        )
        self.assertIn('entity_id: input_boolean.demo_entry_motion\n        state: "off"', automation)
        self.assertIn("entity_id: input_boolean.demo_pathway_light", automation)


if __name__ == "__main__":
    unittest.main()
