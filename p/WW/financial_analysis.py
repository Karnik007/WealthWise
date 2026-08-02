"""
Financial Analysis Module for FiscalPilot

Calculates financial stability metrics:
- Monthly income
- Total expenses
- EMI ratio (estimated)
- Savings rate
- Financial stability score (0-100)
- Risk level (LOW/MEDIUM/HIGH)
"""
from decimal import Decimal
from .models import Income, Expense, User
from datetime import datetime


def calculate_monthly_income(user, months_to_analyze=3):
    """
    Calculate average monthly income from recent months.
    Default: last 3 months
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    # Get last N months (simplified - using first N months for demo)
    recent_months = months[:months_to_analyze]
    
    total_income = Decimal('0.0')
    month_count = 0
    
    for month in recent_months:
        month_incomes = Income.objects.filter(user=user, month=month)
        if month_incomes.exists():
            month_total = sum(inc.amount for inc in month_incomes)
            total_income += month_total
            month_count += 1
    
    avg_monthly_income = total_income / month_count if month_count > 0 else Decimal('0.0')
    return float(avg_monthly_income)


def calculate_monthly_expenses(user, months_to_analyze=3):
    """
    Calculate average monthly expenses from recent months.
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    recent_months = months[:months_to_analyze]
    
    total_expenses = Decimal('0.0')
    month_count = 0
    
    for month in recent_months:
        month_expenses = Expense.objects.filter(user=user, month=month)
        if month_expenses.exists():
            month_total = sum(exp.amount for exp in month_expenses)
            total_expenses += month_total
            month_count += 1
    
    avg_monthly_expenses = total_expenses / month_count if month_count > 0 else Decimal('0.0')
    return float(avg_monthly_expenses)


def estimate_emi_ratio(user, monthly_income, monthly_expenses):
    """
    Estimate EMI ratio as percentage of income.
    Simplified: assume 30% of expenses are EMI/debt payments if no explicit debt data.
    In production, this would come from a debt/loan model.
    """
    if monthly_income == 0:
        return 0.0
    
    # Simplified: assume significant portion of expenses could be debt
    estimated_emi = monthly_expenses * 0.30  # 30% of expenses assumed to be EMI
    emi_ratio = (estimated_emi / monthly_income) * 100
    
    return min(emi_ratio, 100.0)  # Cap at 100%


def calculate_savings_rate(monthly_income, monthly_expenses):
    """
    Calculate savings rate as percentage of income.
    """
    if monthly_income == 0:
        return 0.0
    
    savings = monthly_income - monthly_expenses
    savings_rate = (savings / monthly_income) * 100
    
    return max(savings_rate, 0.0)  # No negative savings rate


def calculate_financial_stability_score(user):
    """
    Calculate overall financial stability score (0-100).
    Factors:
    - Savings rate (40% weight)
    - EMI ratio (30% weight) - lower is better
    - Income consistency (30% weight) - simplified
    
    Returns: dict with score, metrics, and risk level
    """
    monthly_income = calculate_monthly_income(user)
    monthly_expenses = calculate_monthly_expenses(user)
    emi_ratio = estimate_emi_ratio(user, monthly_income, monthly_expenses)
    savings_rate = calculate_savings_rate(monthly_income, monthly_expenses)
    
    # Component scores (0-100)
    # Savings rate score: 0-20% = 0-40 points, 20%+ = 40-60 points, 40%+ = 60-80, 50%+ = 80-100
    if savings_rate < 0:
        savings_score = 0
    elif savings_rate < 10:
        savings_score = savings_rate * 2  # 0-20 points
    elif savings_rate < 20:
        savings_score = 20 + (savings_rate - 10) * 2  # 20-40 points
    elif savings_rate < 40:
        savings_score = 40 + (savings_rate - 20) * 1.5  # 40-70 points
    else:
        savings_score = 70 + min((savings_rate - 40) * 1.5, 30)  # 70-100 points
    
    # EMI ratio score: lower is better
    # 0-20% EMI = 100 points, 20-40% = 70 points, 40-60% = 40 points, 60%+ = 0-20 points
    if emi_ratio <= 20:
        emi_score = 100
    elif emi_ratio <= 30:
        emi_score = 100 - (emi_ratio - 20) * 3  # 100-70
    elif emi_ratio <= 40:
        emi_score = 70 - (emi_ratio - 30) * 3  # 70-40
    elif emi_ratio <= 60:
        emi_score = 40 - (emi_ratio - 40) * 2  # 40-0
    else:
        emi_score = max(0, 20 - (emi_ratio - 60) * 0.5)
    
    # Income consistency score (simplified: assume consistent if income > 0)
    if monthly_income > 0:
        income_consistency_score = 80  # Assume consistent for now
    else:
        income_consistency_score = 0
    
    # Weighted final score
    stability_score = (
        savings_score * 0.40 +
        emi_score * 0.30 +
        income_consistency_score * 0.30
    )
    
    stability_score = max(0, min(100, stability_score))  # Clamp 0-100
    
    # Determine risk level
    if stability_score >= 70:
        risk_level = "LOW"
    elif stability_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"
    
    return {
        'stability_score': round(stability_score, 2),
        'monthly_income': round(monthly_income, 2),
        'monthly_expenses': round(monthly_expenses, 2),
        'emi_ratio': round(emi_ratio, 2),
        'savings_rate': round(savings_rate, 2),
        'risk_level': risk_level,
        'component_scores': {
            'savings_score': round(savings_score, 2),
            'emi_score': round(emi_score, 2),
            'income_consistency_score': round(income_consistency_score, 2)
        }
    }
