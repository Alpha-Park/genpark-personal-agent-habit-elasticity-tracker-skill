---
name: genpark-personal-agent-habit-elasticity-tracker-skill
description: Personal Agent Habit Elasticity Tracker. Models Lally asymptotic habit automaticity curves, evaluates behavioral friction elasticity, and derives minimum viable micro-habits on low-energy days.
license: MIT
version: 1.0.0
tools:
  - model_habit_automaticity_curve
  - evaluate_behavioral_friction_elasticity
  - derive_minimum_viable_micro_habit
---

# Personal Agent Habit Elasticity Tracker

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent behavioral design and habit architect. Your purpose is to eliminate habit failure through empirical automaticity modeling, environmental friction reduction, and dynamic downscaling to minimum viable micro-habits.

## When to Activate This Skill
- When an agent or user reviews daily routines, habit formation goals, or streak continuity.
- When assessing environmental barriers and calculating friction reduction ROI.
- When user energy or motivation is compromised and a minimum viable habit adaptation is needed.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentHabitElasticityTracker

tracker = PersonalAgentHabitElasticityTracker()
res = tracker.derive_minimum_viable_micro_habit("Meditation Minutes", full_target_reps=20, user_current_energy=0.35)
print("Prescribed Micro Target:", res["prescribed_reps"])
```

### Option 2: FastMCP Tool Calling
- `model_habit_automaticity_curve(days_practiced, consistency_ratio=0.90, habit_complexity="MODERATE")`
- `evaluate_behavioral_friction_elasticity(baseline_completions, friction_modified_completions, friction_change_pct)`
- `derive_minimum_viable_micro_habit(base_habit_title, full_target_reps, user_current_energy)`

## Core Mathematical Principles
1. **Lally Automaticity Asymptote**: $A(t) = 1 - e^{-k \cdot t_{	ext{eff}}}$.
2. **Micro-Habit Scaling**: Scale factor $S = \max(0.10, \min(1.0, 	ext{Energy} / 0.75))$ prevents streak abandonment while maintaining neural continuity.
