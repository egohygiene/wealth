from enum import Enum, unique
from pydantic import Field

from wealth.models.wealth import Wealth
from wealth.models.frequency import Frequency

@unique
class IncomeType(str, Enum):
    ACTIVE = "active"                    # Salary, hourly wage, employment
    PASSIVE = "passive"                  # Dividends, high-yield savings, annuities
    FREELANCE = "freelance"              # Contract-based or 1099 work
    BUSINESS = "business"                # Self-employed, LLC, S-Corp distributions
    INVESTMENT = "investment"            # Capital gains, interest, dividends
    RENTAL = "rental"                    # Property rentals (Airbnb, long-term)
    PLATFORM = "platform"                # Twitch, Patreon, YouTube, etc.
    CRYPTO = "crypto"                    # Staking, airdrops, NFT sales
    ROYALTY = "royalty"                  # Music, books, licensing, IP
    RETIREMENT = "retirement"            # 401k, IRA, pension distributions
    SOCIAL_SECURITY = "social_security"  # US-based government retirement support
    STIPEND = "stipend"                  # Grants, academic, living allowance
    DISABILITY = "disability"            # Government or insurance disability income
    CHILD_SUPPORT = "child_support"      # Support payments received for children
    ALIMONY = "alimony"                  # Spousal support payments received
    WINDFALL = "windfall"                # Lottery, inheritance, lawsuit settlements
    OTHER = "other"                      # Unclassified or misc income

class Income(Wealth):
    source: str = Field(..., description="Name of the income source, e.g. MIT, Spotify, Freelance Client")
    amount: float = Field(0.0, description="Gross amount of income per cycle")
    frequency: Frequency = Field(default=Frequency.MONTHLY, description="How often this income is received")
    type: IncomeType = Field(default=IncomeType.ACTIVE, description="Type of income source")
