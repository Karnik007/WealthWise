"""
Explainability Module for FiscalPilot

Generates human-readable explanations for financial decisions.
"""


def generate_explanation(asset_type, asset_fit_result, financial_data):
    """
    Generate comprehensive human-readable explanation for the decision.
    
    Args:
        asset_type: 'gold' or 'reits'
        asset_fit_result: dict from asset_fit_engine.evaluate_asset_fit()
        financial_data: dict from financial_analysis.calculate_financial_stability_score()
    
    Returns:
        dict with:
        - decision_summary: brief summary
        - explanation: detailed explanation
        - risks: list of risks
        - recommendations: list of improvement recommendations
        - tax_note: tax information
    """
    decision = asset_fit_result['decision']
    fit_score = asset_fit_result['fit_score']
    reasons = asset_fit_result['reasons']
    
    stability_score = financial_data['stability_score']
    savings_rate = financial_data['savings_rate']
    emi_ratio = financial_data['emi_ratio']
    risk_level = financial_data['risk_level']
    
    # Generate decision summary
    if decision == 'ALLOW':
        decision_summary = f"Your financial profile supports {asset_type.upper()} investment (Fit Score: {fit_score}/100)"
    else:
        decision_summary = f"We recommend waiting before investing in {asset_type.upper()} (Fit Score: {fit_score}/100)"
    
    # Build detailed explanation
    explanation_parts = []
    explanation_parts.append(f"Based on your financial analysis, your stability score is {stability_score}/100 with a {risk_level} risk level.")
    explanation_parts.append(f"You have a savings rate of {savings_rate:.1f}% and an estimated EMI ratio of {emi_ratio:.1f}% of income.")
    
    if decision == 'ALLOW':
        explanation_parts.append(f"The analysis indicates that investing in {asset_type.upper()} aligns with your current financial situation.")
    else:
        explanation_parts.append(f"At this time, your financial profile suggests it's better to wait before investing in {asset_type.upper()}.")
    
    # Add key reasons
    explanation_parts.append("\nKey factors:")
    for i, reason in enumerate(reasons[:5], 1):  # Top 5 reasons
        explanation_parts.append(f"{i}. {reason}")
    
    explanation = "\n".join(explanation_parts)
    
    # Identify risks
    risks = []
    
    if asset_type == 'gold':
        risks.append("Gold prices can be volatile in the short term")
        risks.append("Storage costs for physical gold")
        risks.append("Lower returns compared to equities historically")
        if savings_rate < 15:
            risks.append("Low savings rate may limit your ability to invest meaningfully")
        if emi_ratio > 30:
            risks.append("High debt obligations may strain your finances")
    
    elif asset_type == 'reits':
        risks.append("REITs are subject to market volatility")
        risks.append("Interest rate sensitivity - rising rates can hurt REIT prices")
        risks.append("Property market downturns can impact REIT performance")
        if savings_rate < 20:
            risks.append("REITs typically require larger investments - ensure adequate savings")
        if risk_level == 'HIGH':
            risks.append("High financial risk profile - REITs may not be suitable")
        if emi_ratio > 40:
            risks.append("High debt ratio increases financial stress - prioritize debt reduction")
    
    # Generate recommendations
    recommendations = []
    
    if decision == 'WAIT':
        if savings_rate < 20:
            recommendations.append("Build your savings rate to at least 20% before investing")
        if emi_ratio > 30:
            recommendations.append("Reduce your debt obligations - aim for EMI ratio below 30%")
        if stability_score < 50:
            recommendations.append("Improve your overall financial stability by increasing income or reducing expenses")
        recommendations.append("Consider building an emergency fund (3-6 months expenses) first")
        if asset_type == 'reits' and savings_rate < 25:
            recommendations.append("REITs require significant savings - continue building your savings")
    else:
        recommendations.append(f"You're in a good position to invest in {asset_type.upper()}")
        if savings_rate < 25:
            recommendations.append("Continue building your savings rate for better financial security")
        recommendations.append("Start with a small investment and gradually increase as you gain confidence")
        if asset_type == 'reits':
            recommendations.append("Consider diversifying across different REIT sectors (residential, commercial, healthcare)")
    
    # Tax notes (simplified)
    if asset_type == 'gold':
        tax_note = "Gold investments may be subject to capital gains tax. Physical gold and gold ETFs have different tax treatments. Long-term capital gains (held >3 years for physical gold, >1 year for gold ETFs) may qualify for lower tax rates. Consult a tax advisor for specifics in your jurisdiction."
    else:  # reits
        tax_note = "REIT dividends are typically taxed as ordinary income at your marginal tax rate. Capital gains from REIT sales are subject to capital gains tax. Some jurisdictions offer tax advantages for REIT investments. Consult a tax advisor for specifics in your jurisdiction."
    
    return {
        'decision_summary': decision_summary,
        'explanation': explanation,
        'risks': risks,
        'recommendations': recommendations,
        'tax_note': tax_note
    }
