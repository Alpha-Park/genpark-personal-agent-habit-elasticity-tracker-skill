# -*- coding: utf-8 -*-
"""
Personal Agent Habit Elasticity Tracker FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentHabitElasticityTracker

mcp = FastMCP("genpark-personal-agent-habit-elasticity-tracker-skill")
tracker = PersonalAgentHabitElasticityTracker()

@mcp.tool()
def model_habit_automaticity_curve(
    days_practiced: int,
    consistency_ratio: float = 0.90,
    habit_complexity: str = "MODERATE"
) -> str:
    """
    Models habit automaticity kinetics and estimates days required to reach second nature.
    """
    res = tracker.model_habit_automaticity_curve(days_practiced, consistency_ratio, habit_complexity)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_behavioral_friction_elasticity(
    baseline_completions: int,
    friction_modified_completions: int,
    friction_change_pct: float
) -> str:
    """
    Evaluates behavioral sensitivity to environmental friction changes.
    """
    res = tracker.evaluate_behavioral_friction_elasticity(baseline_completions, friction_modified_completions, friction_change_pct)
    return json.dumps(res, indent=2)

@mcp.tool()
def derive_minimum_viable_micro_habit(
    base_habit_title: str,
    full_target_reps: int,
    user_current_energy: float
) -> str:
    """
    Calculates downscaled minimum viable habit reps on low-energy days to preserve streak integrity.
    """
    res = tracker.derive_minimum_viable_micro_habit(base_habit_title, full_target_reps, user_current_energy)
    return json.dumps(res, indent=2)

def main():
    print("Testing Habit Elasticity Tracker FastMCP Server:")
    print(model_habit_automaticity_curve(30, 0.95, "MODERATE"))

if __name__ == "__main__":
    main()
