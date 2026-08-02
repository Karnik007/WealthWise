"""
Asset Fit Engine for FiscalPilot

Rule-based engine that determines if an asset (Gold/REIT) fits the user's financial situation.
Returns: decision (ALLOW/WAIT), fit_score (0-100)
"""
import json
import os


def load_asset_data(asset_type):
    """
    Load asset data from JSON files.
    asset_type: 'gold' or 'reits'
    """
    from django.conf import settings
    data_file = os.path.join(settings.BASE_DIR, 'data', f'{asset_type}.json')
    
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def get_credit_band(mock_credit_score):
    """
    Get credit band info based on mock credit score.
    """
    from django.conf import settings
    credit_file = os.path.join(settings.BASE_DIR, 'data', 'credit.json')
    
    try:
        with open(credit_file, 'r') as f:
            credit_data = json.load(f)
            
        for band in credit_data['credit_bands']:
            if band['min_score'] <= mock_credit_score <= band['max_score']:
                return band
    except FileNotFoundError:
        pass
    
    # Default if not found
    return {
        "risk_level": "MEDIUM",
        "description": "Unknown credit profile",
        "recommendation": "Proceed with caution"
    }


def calculate_mock_credit_score(financial_stability_score, savings_rate, emi_ratio):
    """
    Calculate a mock credit score (300-850) based on financial metrics.
    """
    # Base score from stability score
    base_score = 300 + (financial_stability_score / 100) * 450  # 300-750 range
    
    # Adjust based on savings rate
    if savings_rate > 30:
        base_score += 50
    elif savings_rate > 20:
        base_score += 30
    elif savings_rate < 10:
        base_score -= 30
    
    # Adjust based on EMI ratio
    if emi_ratio < 20:
        base_score += 50
    elif emi_ratio > 50:
        base_score -= 50
    
    return max(300, min(850, int(base_score)))


def evaluate_asset_fit(asset_type, financial_data, mock_credit_score=None):
    """
    Evaluate if an asset fits the user's financial situation.
    
    Args:
        asset_type: 'gold' or 'reits'
        financial_data: dict from financial_analysis.calculate_financial_stability_score()
        mock_credit_score: optional, will calculate if not provided
    
    Returns:
        dict with:
        - decision: 'ALLOW' or 'WAIT'
        - fit_score: 0-100
        - reasons: list of decision factors
    """
    stability_score = financial_data['stability_score']
    risk_level = financial_data['risk_level']
    savings_rate = financial_data['savings_rate']
    emi_ratio = financial_data['emi_ratio']
    
    # Calculate credit score if not provided
    if mock_credit_score is None:
        mock_credit_score = calculate_mock_credit_score(
            stability_score, savings_rate, emi_ratio
        )
    
    credit_band = get_credit_band(mock_credit_score)
    credit_risk = credit_band['risk_level']
    
    # Load asset data
    asset_data = load_asset_data(asset_type)
    if not asset_data:
        return {
            'decision': 'WAIT',
            'fit_score': 0,
            'reasons': ['Asset data not available']
        }
    
    # Initialize decision factors
    fit_score = 0
    reasons = []
    decision = 'WAIT'
    
    # Base score from financial stability
    fit_score += stability_score * 0.30
    
    # Asset-specific rules
    if asset_type == 'gold':
        # Gold rules (lower risk asset)
        if risk_level == 'LOW':
            fit_score += 30
            reasons.append("Low financial risk profile - suitable for gold")
        elif risk_level == 'MEDIUM':
            fit_score += 20
            reasons.append("Medium financial risk - gold is a conservative choice")
        else:
            fit_score += 10
            reasons.append("High financial risk - gold provides stability")
        
        if savings_rate >= 20:
            fit_score += 25
            reasons.append("Strong savings rate supports gold investment")
        elif savings_rate >= 10:
            fit_score += 15
            reasons.append("Moderate savings rate - gold is accessible")
        else:
            fit_score += 5
            reasons.append("Low savings rate - consider building savings first")
        
        if credit_risk == 'LOW':
            fit_score += 15
        elif credit_risk == 'MEDIUM':
            fit_score += 10
        else:
            fit_score += 5
        
        # Minimum threshold for ALLOW
        if fit_score >= 60 and savings_rate >= 10:
            decision = 'ALLOW'
        elif fit_score >= 50 and savings_rate >= 15:
            decision = 'ALLOW'
        else:
            reasons.append("Insufficient financial stability for gold investment at this time")
    
    elif asset_type == 'reits':
        # REITs rules (higher risk, requires stability)
        if risk_level == 'LOW':
            fit_score += 35
            reasons.append("Low financial risk - suitable for REITs")
        elif risk_level == 'MEDIUM':
            fit_score += 20
            reasons.append("Medium financial risk - REITs require stability")
        else:
            fit_score += 5
            reasons.append("High financial risk - REITs not recommended")
        
        if savings_rate >= 25:
            fit_score += 30
            reasons.append("Strong savings rate supports REIT investment")
        elif savings_rate >= 15:
            fit_score += 20
            reasons.append("Moderate savings rate - REITs possible")
        else:
            fit_score += 5
            reasons.append("Low savings rate - REITs require significant savings")
        
        if credit_risk == 'LOW':
            fit_score += 15
            reasons.append("Good credit profile supports REIT investment")
        elif credit_risk == 'MEDIUM':
            fit_score += 10
        else:
            fit_score += 0
            reasons.append("Poor credit profile - REITs not recommended")
        
        # REITs require higher thresholds
        if emi_ratio > 40:
            fit_score -= 20
            reasons.append("High EMI ratio - reduce debt before REIT investment")
        
        if fit_score >= 65 and savings_rate >= 20 and risk_level != 'HIGH':
            decision = 'ALLOW'
        elif fit_score >= 55 and savings_rate >= 25 and risk_level == 'LOW':
            decision = 'ALLOW'
        else:
            reasons.append("Insufficient financial stability for REIT investment at this time")
    
    # Cap fit score at 100
    fit_score = min(100, max(0, fit_score))
    
    # Add summary reason based on decision
    if decision == 'ALLOW':
        reasons.insert(0, f"Financial profile supports {asset_type.upper()} investment")
    else:
        reasons.insert(0, f"Financial profile does not currently support {asset_type.upper()} investment")
    
    return {
        'decision': decision,
        'fit_score': round(fit_score, 2),
        'reasons': reasons,
        'asset_type': asset_type,
        'mock_credit_score': mock_credit_score,
        'credit_risk': credit_risk
    }
