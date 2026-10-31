# -*- coding: utf-8 -*-
import json
from client import PersonalAgentHabitElasticityTracker

tracker = PersonalAgentHabitElasticityTracker()

print("=" * 64)
print("DEMO: Personal Habit Automaticity & Friction Elasticity")
print("=" * 64)

# 1. Automaticity Curve Modeling
auto = tracker.model_habit_automaticity_curve(days_practiced=28, consistency_ratio=0.88, habit_complexity="MODERATE")
print(f"\n1. Habit Automaticity (Day 28 of Moderate Habit):")
print(f"   Automaticity Score: {auto['automaticity_score']} ({auto['habit_stage']})")
print(f"   Plateau Target: {auto['projected_total_days_to_plateau']} days ({auto['estimated_remaining_days']} days remaining)")

# 2. Friction Elasticity
friction = tracker.evaluate_behavioral_friction_elasticity(baseline_completions=12, friction_modified_completions=22, friction_change_pct=-40.0)
print(f"\n2. Friction Elasticity Evaluation (-40% friction barrier):")
print(f"   Elasticity Coefficient: {friction['friction_elasticity_coefficient']}")
print(f"   Diagnosis: {friction['behavioral_responsiveness']}")

# 3. Minimum Viable Micro-Habit Scaling
micro = tracker.derive_minimum_viable_micro_habit("Pushups", full_target_reps=50, user_current_energy=0.30)
print(f"\n3. Low Energy Micro-Habit Scaling (Energy: {micro['user_current_energy']}):")
print(f"   Mode: {micro['mode']} -> Reps: {micro['prescribed_reps']} (down from {micro['full_target_reps']})")
print(f"   Mantra: {micro['psychological_reframing']}")
