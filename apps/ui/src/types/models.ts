// Auto-generated TypeScript models mirroring the Python pydantic models in the
// wealth backend. These interfaces enable typed communication between the UI
// and the API.

// Base entity shared across most objects
export interface Wealth {
  uuid: string
  user_id: string
  name: string
  description?: string
  parent_id?: string
  tags: string[]
  notes?: string
  is_active: boolean
  created_at: string
  updated_at: string
}

// --- Risk types --------------------------------------------------------------
export enum RiskType {
  LOW = 'low',
  MEDIUM = 'medium',
  HIGH = 'high',
  SPECULATIVE = 'speculative',
  GUARANTEED = 'guaranteed',
}

export enum RiskProfile {
  CONSERVATIVE = 'conservative',
  MODERATE = 'moderate',
  BALANCED = 'balanced',
  AGGRESSIVE = 'aggressive',
  SPECULATIVE = 'speculative',
}

export interface Risk {
  uuid: string
  name: string
  score: number
  level: RiskType
  description?: string
  source_object_type?: string
  source_object_id?: string
  created_at: string
  updated_at: string
}

// --- Service ----------------------------------------------------------------
export interface Service {
  uuid: string
  name: string
  url?: string
  logo_url?: string
  provider?: string
  notes?: string
}

// --- Asset and investment models -------------------------------------------
export enum AssetType {
  STOCK = 'stock',
  ETF = 'etf',
  MUTUAL_FUND = 'mutual_fund',
  CRYPTO = 'crypto',
  REIT = 'reit',
  BOND = 'bond',
  OPTION = 'option',
  FUTURE = 'future',
  CASH = 'cash',
  COMMODITY = 'commodity',
  COLLECTIBLE = 'collectible',
  CROWDFUNDING = 'crowdfunding',
  ANGEL_INVESTMENT = 'angel_investment',
  REAL_ESTATE = 'real_estate',
  BUSINESS_EQUITY = 'business_equity',
  OTHER = 'other',
}

export interface Investment extends Wealth {
  asset_type: AssetType
  amount_invested: number
  current_value: number
  platform?: string
  risk_score: number
  risk_level: RiskType
  risk?: Risk
}

// --- Allocations -------------------------------------------------------------
export enum AllocationType {
  FIXED = 'fixed',
  VARIABLE = 'variable',
}

export interface Allocation extends Wealth {
  allocation_type: AllocationType
  budget_amount?: number
  budget_percentage?: number
  savings_bucket?: string
  risk_score: number
  risk_level: RiskType
  risk?: Risk
  tags: string[]
  services: Service[]
  active: boolean
}

// --- Expenses ---------------------------------------------------------------
export enum ExpenseCategory {
  HOUSING = 'housing',
  UTILITIES = 'utilities',
  GROCERIES = 'groceries',
  TRANSPORTATION = 'transportation',
  HEALTHCARE = 'healthcare',
  INSURANCE = 'insurance',
  ENTERTAINMENT = 'entertainment',
  SUBSCRIPTIONS = 'subscriptions',
  EDUCATION = 'education',
  CHILDCARE = 'childcare',
  PETS = 'pets',
  CHARITY = 'charity',
  PERSONAL_CARE = 'personal_care',
  GIFTS = 'gifts',
  BUSINESS = 'business',
  TAXES = 'taxes',
  LOANS = 'loans',
  DEBT_REPAYMENT = 'debt_repayment',
  INVESTMENT = 'investment',
  OTHER = 'other',
}

export enum ExpenseFrequency {
  ONE_TIME = 'one_time',
  DAILY = 'daily',
  WEEKLY = 'weekly',
  BIWEEKLY = 'biweekly',
  SEMIMONTHLY = 'semimonthly',
  MONTHLY = 'monthly',
  BIMONTHLY = 'bimonthly',
  QUARTERLY = 'quarterly',
  SEMIANNUALLY = 'semiannually',
  ANNUALLY = 'annually',
  IRREGULAR = 'irregular',
}

export interface Expense extends Wealth {
  amount: number
  date: string
  category: ExpenseCategory
  frequency: ExpenseFrequency
  source_account: string
}

// --- Income -----------------------------------------------------------------
export enum IncomeType {
  ACTIVE = 'active',
  PASSIVE = 'passive',
  FREELANCE = 'freelance',
  BUSINESS = 'business',
  INVESTMENT = 'investment',
  RENTAL = 'rental',
  PLATFORM = 'platform',
  CRYPTO = 'crypto',
  ROYALTY = 'royalty',
  RETIREMENT = 'retirement',
  SOCIAL_SECURITY = 'social_security',
  STIPEND = 'stipend',
  DISABILITY = 'disability',
  CHILD_SUPPORT = 'child_support',
  ALIMONY = 'alimony',
  WINDFALL = 'windfall',
  OTHER = 'other',
}

export enum IncomeFrequency {
  ONE_TIME = 'one_time',
  DAILY = 'daily',
  WEEKLY = 'weekly',
  BIWEEKLY = 'biweekly',
  SEMIMONTHLY = 'semimonthly',
  MONTHLY = 'monthly',
  BIMONTHLY = 'bimonthly',
  QUARTERLY = 'quarterly',
  SEMIANNUALLY = 'semiannually',
  ANNUALLY = 'annually',
  IRREGULAR = 'irregular',
}

export interface Income extends Wealth {
  source: string
  amount: number
  frequency: IncomeFrequency
  type: IncomeType
}

// --- Debts ------------------------------------------------------------------
export enum DebtType {
  CREDIT_CARD = 'credit_card',
  PERSONAL_LOAN = 'personal_loan',
  STUDENT_LOAN = 'student_loan',
  AUTO_LOAN = 'auto_loan',
  MORTGAGE = 'mortgage',
  MEDICAL = 'medical',
  BUSINESS_LOAN = 'business_loan',
  LINE_OF_CREDIT = 'line_of_credit',
  BUY_NOW_PAY_LATER = 'buy_now_pay_later',
  OTHER = 'other',
}

export enum DebtStatus {
  OPEN = 'open',
  CLOSED = 'closed',
  DEFAULTED = 'defaulted',
  DEFERRED = 'deferred',
  PAID_OFF = 'paid_off',
}

export interface Debt extends Wealth {
  debt_type: DebtType
  status: DebtStatus
  balance: number
  apr: number
  min_payment: number
  snowball_priority?: number
  risk_score: number
  risk_level: RiskType
  risk?: Risk
  lender?: string
  account_number?: string
  due_day?: number
  is_tax_deductible: boolean
  auto_pay_enabled: boolean
}

// --- Portfolio --------------------------------------------------------------
export interface Portfolio extends Wealth {
  investments: Investment[]
  risk_profile?: RiskProfile
  strategy_label?: string
}

// --- Finance ----------------------------------------------------------------
export interface Finance {
  user_id: string
  allocations: Allocation[]
  expenses: Expense[]
  income_streams: Income[]
  debts: Debt[]
  investments: Investment[]
  portfolios: Portfolio[]
  services: Service[]
  roles: string[]
  features: string[]
  lifecycle_phase: LifecyclePhase
  risk_profile?: RiskProfile
  notes?: string
  created_at: string
  updated_at: string
}

export interface FinanceSummary {
  net_worth: number
  investment_count: number
  debt_count: number
  allocation_count: number
}

export enum LifecyclePhase {
  SURVIVING = 'surviving',
  STABILIZING = 'stabilizing',
  MAINTAINING = 'maintaining',
  SCALING = 'scaling',
  THRIVING = 'thriving',
  RETIRING = 'retiring',
}
