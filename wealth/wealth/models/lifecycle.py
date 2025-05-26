from enum import Enum, unique

@unique
class LifecyclePhase(str, Enum):
    SURVIVING = "surviving"        # Just trying to make it day-to-day
    STABILIZING = "stabilizing"    # Gaining control, working on debt/structure
    MAINTAINING = "maintaining"    # Budgeting is consistent, basic needs are met
    SCALING = "scaling"            # Investing, growing income, optimizing
    THRIVING = "thriving"          # Fully aligned, building legacy/systems
    RETIRING = "retiring"          # Transitioning into lower output mode
