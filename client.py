# -*- coding: utf-8 -*-
"""
Personal Agent Habit Elasticity Tracker Client
Zero-dependency Lally habit automaticity kinetics modeler, behavioral friction
price elasticity analyzer, and minimum viable micro-habit scaling engine.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentHabitElasticityTracker:
    """
    Models personal habit formation curves, calculates behavioral friction elasticity,
    and dynamically scales habits down to minimum viable micro-versions on low-energy days.
    """

    COMPLEXITY_RATE_MAP = {
        "SIMPLE": 0.065,     # Glass of water, 1-min stretch (~21 days plateau)
        "MODERATE": 0.040,   # 20-min reading, journal (~50 days plateau)
        "COMPLEX": 0.022     # 45-min gym workout, coding session (~85 days plateau)
    }

    def model_habit_automaticity_curve(
        self,
        days_practiced: int,
        consistency_ratio: float = 0.90,
        habit_complexity: str = "MODERATE"
    ) -> Dict[str, Any]:
        """
        Lally Habit Automaticity Model:
        Automaticity(t) = A_max * (1 - exp(-k * t_eff))
        where t_eff = days_practiced * consistency_ratio.
        """
        days = max(0, int(days_practiced))
        consistency = max(0.1, min(1.0, float(consistency_ratio)))
        c_tier = habit_complexity.strip().upper() if habit_complexity else "MODERATE"
        k = self.COMPLEXITY_RATE_MAP.get(c_tier, 0.040)

        effective_days = days * consistency
        automaticity = round(1.0 - math.exp(-k * effective_days), 3)

        # Days to achieve 95% automaticity asymptote: 1 - exp(-k * t) = 0.95 -> t = -ln(0.05) / k
        target_days_for_automaticity = round(-math.log(0.05) / (k * consistency), 1)
        remaining_days = max(0.0, target_days_for_automaticity - days)

        if automaticity >= 0.85:
            stage = "SECOND_NATURE_HABITUAL"
        elif automaticity >= 0.50:
            stage = "CONSOLIDATION_PHASE"
        elif automaticity >= 0.20:
            stage = "ACTIVE_COGNITIVE_EFFORT"
        else:
            stage = "FRAGILE_INITIATION"

        return {
            "days_practiced": days,
            "consistency_ratio": consistency,
            "habit_complexity_tier": c_tier,
            "automaticity_score": automaticity,
            "habit_stage": stage,
            "projected_total_days_to_plateau": target_days_for_automaticity,
            "estimated_remaining_days": remaining_days,
            "identity_reinforcement_strength": round(automaticity * 100.0, 1)
        }

    def evaluate_behavioral_friction_elasticity(
        self,
        baseline_completions: int,
        friction_modified_completions: int,
        friction_change_pct: float
    ) -> Dict[str, Any]:
        """
        Calculates Price Elasticity of Behavioral Friction:
        Elasticity = (Delta_Completions / Base_Completions) / (Delta_Friction / Base_Friction)
        """
        base_c = max(1, int(baseline_completions))
        mod_c = max(0, int(friction_modified_completions))
        delta_friction = float(friction_change_pct) / 100.0

        if abs(delta_friction) < 1e-6:
            raise ValueError("Friction change percentage cannot be zero.")

        pct_change_completions = (mod_c - base_c) / float(base_c)
        elasticity = round(pct_change_completions / delta_friction, 2)
        abs_elasticity = abs(elasticity)

        if abs_elasticity >= 1.2:
            verdict = "HIGHLY_ELASTIC (Extremely sensitive to friction; lowering friction dramatically boosts streak)"
        elif abs_elasticity >= 0.7:
            verdict = "MODERATELY_ELASTIC (Responsive to environment setup)"
        else:
            verdict = "INELASTIC (Intrinsic motivation dominates; unaffected by minor barriers)"

        return {
            "baseline_completions": base_c,
            "modified_completions": mod_c,
            "friction_change_pct": friction_change_pct,
            "friction_elasticity_coefficient": elasticity,
            "behavioral_responsiveness": verdict,
            "recommended_strategy": "Radically eliminate setup steps" if abs_elasticity >= 1.0 else "Focus on intrinsic identity triggers"
        }

    def derive_minimum_viable_micro_habit(
        self,
        base_habit_title: str,
        full_target_reps: int,
        user_current_energy: float
    ) -> Dict[str, Any]:
        """
        Downscales habit target to a Minimum Viable Micro-Habit when user energy is low,
        preserving identity streak without cognitive resistance.
        Scale factor = max(0.10, min(1.0, current_energy / 0.75))
        """
        energy = max(0.05, min(1.0, float(user_current_energy)))
        reps = max(1, int(full_target_reps))

        scale = max(0.10, min(1.0, energy / 0.75))
        micro_reps = max(1, round(reps * scale))

        return {
            "base_habit": base_habit_title,
            "full_target_reps": reps,
            "user_current_energy": energy,
            "scale_factor": round(scale, 2),
            "prescribed_reps": micro_reps,
            "mode": "STANDARD_EXECUTION" if scale >= 0.90 else "MINIMUM_VIABLE_STREAK_PRESERVER",
            "psychological_reframing": f"Just complete {micro_reps} {base_habit_title} to preserve neural pathway continuity."
        }
