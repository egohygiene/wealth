from enum import Enum, unique

@unique
class AssetType(str, Enum):
    STOCK = "stock"
    ETF = "etf"
    MUTUAL_FUND = "mutual_fund"
    CRYPTO = "crypto"
    REIT = "reit"
    BOND = "bond"
    OPTION = "option"
    FUTURE = "future"
    CASH = "cash"
    COMMODITY = "commodity"
    COLLECTIBLE = "collectible"
    CROWDFUNDING = "crowdfunding"
    ANGEL_INVESTMENT = "angel_investment"
    REAL_ESTATE = "real_estate"
    BUSINESS_EQUITY = "business_equity"
    OTHER = "other"
