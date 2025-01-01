import pytest
from finance import Property, Loan

def test_property_calculation():
    prop = Property(
        agency_fees_rate=5.78,
        notary_fees_rate=8.0,
        price=150000,
        work_cost=20000,
        square=33.12,
        furniture=5000,
        contribution=30000,
        monthly_rent=800,
        rental_vacancies=1.0,
        expenses=2000,
    )

    # Test property price with agency fees
    property_price_with_agency_fees, agency_fees_amount = prop.get_property_price_with_agency_fees()
    assert agency_fees_amount == prop.price * (prop.agency_fees_rate / 100), \
        f"Expected agency fees to be {prop.price * (prop.agency_fees_rate / 100)}, got {agency_fees_amount}"

    # Test property price with notary fees
    property_price_with_notary_fees, notary_fees_amount = prop.get_property_price_with_notary_fees()
    assert notary_fees_amount == property_price_with_agency_fees * (prop.notary_fees_rate / 100), \
        f"Expected notary fees to be {property_price_with_agency_fees * (prop.notary_fees_rate / 100)}, got {notary_fees_amount}"

    # Test operation cost
    operation_cost = prop.get_operation_cost()
    expected_operation_cost = property_price_with_notary_fees + prop.work_cost + prop.furniture
    assert operation_cost == expected_operation_cost, \
        f"Expected operation cost to be {expected_operation_cost}, got {operation_cost}"

    # Test loan amount
    loan_amount = prop.get_loan_amount()
    expected_loan_amount = operation_cost - prop.contribution
    assert loan_amount == expected_loan_amount, \
        f"Expected loan amount to be {expected_loan_amount}, got {loan_amount}"

    # Test rental vacancies amount
    rental_vacancies_amount = prop.get_rental_vacancies_amount()
    expected_rental_vacancies = prop.rental_vacancies * prop.monthly_rent
    assert rental_vacancies_amount == expected_rental_vacancies, \
        f"Expected rental vacancies amount to be {expected_rental_vacancies}, got {rental_vacancies_amount}"

    # Test turnover amount
    turnover_amount = prop.get_turnover_amount()
    expected_turnover = (prop.monthly_rent * 12) - rental_vacancies_amount
    assert turnover_amount == expected_turnover, \
        f"Expected turnover amount to be {expected_turnover}, got {turnover_amount}"

    # Test net income amount
    net_income_amount = prop.get_net_income_amount()
    expected_net_income = turnover_amount - prop.expenses
    assert net_income_amount == expected_net_income, \
        f"Expected net income amount to be {expected_net_income}, got {net_income_amount}"

    # Test price per square meter
    price_per_square_meter = prop.get_price_per_square_meter()
    expected_price_per_square_meter = (property_price_with_agency_fees + prop.work_cost) / prop.square
    assert price_per_square_meter == expected_price_per_square_meter, \
        f"Expected price per square meter to be {expected_price_per_square_meter}, got {price_per_square_meter}"

    # Test profitability
    profitability = prop.profitability()
    assert profitability > 0, "Profitability should be greater than 0"
    expected_profitability = (net_income_amount / loan_amount) * 100
    assert profitability == expected_profitability, \
        f"Expected profitability to be {expected_profitability}, got {profitability}"

    # Test cashflow pretax
    cashlow_pretax = prop.calculate_cashflow_pretax(500)
    expected_cashlow_pretax = net_income_amount - (500 * 12)
    assert cashlow_pretax == expected_cashlow_pretax, \
        f"Expected cashflow pretax to be {expected_cashlow_pretax}, got {cashlow_pretax}"



def test_loan_calculation():
    loan = Loan(
        amount=200000,
        interest_rate=3.0,
        duration_years=20,
        loan_insurance_cost=50,
        pno_insurance_cost=10,
    )
    loan_insurance_amount = loan.get_monthly_insurance_costs()
    assert loan_insurance_amount == loan.loan_insurance_cost + loan.pno_insurance_cost

    monthly_payment_amount = loan.get_loan_monthly_payment()
    assert monthly_payment_amount == 1109.1951957078415

    loan_insurance_monthly_payment = loan.get_loan_insurance_monthly_payment()
    assert loan_insurance_monthly_payment == 1109.1951957078415 + loan_insurance_amount

    total_cost = loan.total_cost()
    assert total_cost == loan_insurance_monthly_payment * (loan.duration_years * 12)
