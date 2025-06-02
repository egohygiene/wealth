from enum import Enum, unique

@unique
class Frequency(str, Enum):
    ONE_TIME = "one_time"
    DAILY = "daily"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    SEMIMONTHLY = "semimonthly"
    MONTHLY = "monthly"
    BIMONTHLY = "bimonthly"
    QUARTERLY = "quarterly"
    SEMIANNUALLY = "semiannually"
    ANNUALLY = "annually"
    YEARLY = "yearly"
    IRREGULAR = "irregular"

    def to_monthly_multiplier(self) -> float:
        """Return a factor for converting this frequency to a monthly value."""
        mapping: dict[Frequency, float] = {
            Frequency.ONE_TIME: 0.0,
            Frequency.DAILY: 30.44,
            Frequency.WEEKLY: 4.33,
            Frequency.BIWEEKLY: 2.17,
            Frequency.SEMIMONTHLY: 2.0,
            Frequency.MONTHLY: 1.0,
            Frequency.BIMONTHLY: 0.5,
            Frequency.QUARTERLY: 0.33,
            Frequency.SEMIANNUALLY: 0.17,
            Frequency.ANNUALLY: 1/12,
            Frequency.YEARLY: 1/12,
            Frequency.IRREGULAR: 0.0,
        }
        return float(mapping.get(self, 1.0))

    def to_annual_multiplier(self) -> float:
        """Return a factor for converting this frequency to an annual value."""
        mapping: dict[Frequency, float] = {
            Frequency.ONE_TIME: 0.0,
            Frequency.DAILY: 365,
            Frequency.WEEKLY: 52,
            Frequency.BIWEEKLY: 26,
            Frequency.SEMIMONTHLY: 24,
            Frequency.MONTHLY: 12,
            Frequency.BIMONTHLY: 6,
            Frequency.QUARTERLY: 4,
            Frequency.SEMIANNUALLY: 2,
            Frequency.ANNUALLY: 1,
            Frequency.YEARLY: 1,
            Frequency.IRREGULAR: 0.0,
        }
        return float(mapping.get(self, 1.0))

    def from_monthly(self, amount: float) -> float:
        """Convert a monthly amount to this frequency."""
        return round(amount * self.to_monthly_multiplier(), 2)

    def normalize_to_monthly(self, amount: float) -> float:
        """Convert any frequency-based amount to monthly equivalent."""
        reverse = self.to_monthly_multiplier()
        return round(amount / reverse, 2) if reverse else 0.0
