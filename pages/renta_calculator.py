import streamlit as st
import pandas as pd
from finance import Property, Loan
from utils import format_number, get_percentage_increment


st.title("_Renta_ Calculator :bar_chart:")

square = 20.0
property_work = 0
expenses = 1000
monthly_rent = 750
rental_vacancies = 0.0
furniture = 0
loan_amount_furniture = 0
contribution = 0

# -------------------------------------------------- #
# Proporty data
col1, col2, col3 = st.columns(3)
property_price_notax = col1.number_input("Prix d'achat", min_value=0, value=100000)
agency_fees_rate = col2.number_input("Frais d'agence %", min_value=0.0, value=5.78)
notary_fees_rate = col3.number_input("Frais de notaire %", min_value=0.0, value=8.0)

# Creation of Property and Loan objects
property_instance = Property(
    agency_fees_rate=agency_fees_rate,
    notary_fees_rate=notary_fees_rate,
    price=property_price_notax,
    work_cost=property_work,
    square=square,
    furniture=loan_amount_furniture,
    contribution=contribution,
    monthly_rent=monthly_rent,
    rental_vacancies=rental_vacancies,
    expenses=expenses,
)

property_price_with_agency_fees, agency_fees_amount = (
    property_instance.get_property_price_with_agency_fees()
)
property_price_with_fees, notary_fees_amount = (
    property_instance.get_property_price_with_notary_fees()
)

# Print results
col1.metric(
    label="Prix d'achat (Frais d'agence et notaire inclus)",
    value=f"{format_number(property_price_with_fees)}",
)
col2.metric(label="Frais d'agence", value=f"{format_number(agency_fees_amount)}")
col3.metric(label="Frais de notaire", value=f"{format_number(notary_fees_amount)}")

# -------------------------------------------------- #
# Investment data
st.subheader("Données sur l'investissement", divider="gray")
col1, col2 = st.columns(2)
square = col1.number_input("Surface en m2", min_value=5.0, value=20.0)
property_work = col1.number_input("Travaux", min_value=0, value=0)
monthly_rent = col2.number_input("Loyer mensuel", min_value=0, value=750)
rental_vacancies = col2.number_input(
    "Vacances locatives (1,0 = un mois)", min_value=0.0, value=0.0
)
expenses = col2.number_input(
    "Charges annuelles (Taxe foncière, copro, entretien, etc)", min_value=0, value=1000
)
furniture = col1.number_input("Ameublement", min_value=0, value=0)
furniture_choice = col1.selectbox(
    "Inclure l'ameublement dans le prêt ?",
    ("Non", "Oui"),
    label_visibility="visible",
)


if furniture_choice == "Non":
    # Do not include the price of the furniture in the loan
    loan_amount_furniture = 0
else:
    # Include it in the loan
    loan_amount_furniture = furniture


# -------------------------------------------------- #
# Banking data
st.subheader("Données bancaires", divider="gray")
col1, col2 = st.columns(2)
contribution = col2.number_input("Apport", min_value=0, value=0)
bank_interest_rate = col2.slider("Taux d'intérêts", 0.01, 8.00, 3.59)
loan_duration_year = col2.slider("Durée de l'emprunt", 1, 25, 20)
insurance_choice = col2.selectbox(
    "Inclure les assurances dans le prêt ?",
    ("Non", "Oui"),
    label_visibility="visible",
)
monthly_loan_insurance_cost = col2.number_input(
    "Coût assurance emprunteur (mois)", min_value=0, value=50
)
monthly_pno_insurance_cost = col2.number_input(
    "Coût assurance propriétaire non occupant (mois)", min_value=0, value=10
)

if insurance_choice == "Non":
    # Do not include the price of the insurances in the loan
    monthly_loan_insurance_cost = 0
    monthly_pno_insurance_cost = 0
else:
    # Include it in the loan
    pass


# Creation of Property and Loan objects
property_instance = Property(
    agency_fees_rate=agency_fees_rate,
    notary_fees_rate=notary_fees_rate,
    price=property_price_notax,
    work_cost=property_work,
    square=square,
    furniture=loan_amount_furniture,
    contribution=contribution,
    monthly_rent=monthly_rent,
    rental_vacancies=rental_vacancies,
    expenses=expenses,
)

loan_amount = property_instance.get_loan_amount()
price_per_square_meter = property_instance.get_price_per_square_meter()

loan_instance = Loan(
    amount=loan_amount,
    interest_rate=bank_interest_rate,
    duration_years=loan_duration_year,
    loan_insurance_cost=monthly_loan_insurance_cost,
    pno_insurance_cost=monthly_pno_insurance_cost,
)

# Calculs
profitability = property_instance.profitability()
monthly_payment = loan_instance.get_loan_insurance_monthly_payment()
total_loan_cost = loan_instance.total_cost()
loan_cost = loan_instance.loan_cost()
monthly_cashflow_pretax = (
    property_instance.calculate_cashflow_pretax(monthly_payment) / 12
)
monthly_payment_with_expenses = loan_instance.calculate_loan_and_expenses(
    monthly_payment, expenses
)

turnover = property_instance.get_turnover_amount()

# Print results
col1.metric(label="Montant à emprunter", value=f"{format_number(loan_amount)}")
col1.metric(label="Coût total du crédit", value=f"{format_number(total_loan_cost)}")
col1.metric(label="Mensualités de crédit", value=f"{format_number(monthly_payment)}")
# st.info("Des frais de dossier et de garantie peuvent s'ajouter, selon la banque. En général, ces frais représentent environ 1,5 fois le montant du prix du bien.", icon="ℹ️")


# -------------------------------------------------- #
# Print results
st.subheader("Synthèse", divider="gray")
col1, col2, col3 = st.columns(3)
col1.metric(label="Rentabilité", value=f"{profitability:.1f}%")
col1.metric(
    label="Prix au m2 après travaux (hors frais de notaire)",
    value=f"{format_number(price_per_square_meter)}",
)
col2.metric(
    label="Emprunt et charges (mois)",
    value=f"{format_number(monthly_payment_with_expenses)}",
)
col3.metric(
    label="Cashflow avant impôts (mois)",
    value=f"{format_number(monthly_cashflow_pretax)}",
)
col2.metric(
    label="Emprunt et charges annuel",
    value=f"{format_number(monthly_payment_with_expenses*12)}",
)
col3.metric(label="CA annuel", value=f"{format_number(turnover)}")
# col1.metric(label="Coût total de l'opération", value=f"{format_number(property_instance.get_operation_cost() + furniture)}")

# Summary table
data = {
    "Élément": [
        "Acquisition",
        "Travaux",
        "Meubles",
        "Apport",
        "Coût total de l'opération",
    ],
    "Montant (€)": [
        f"{format_number(property_price_with_fees)}",
        f"{format_number(property_work)}",
        f"{format_number(furniture)}",
        f"{format_number(contribution)}",
        f"{format_number(property_instance.get_operation_cost() + furniture)}",
    ],
}
summary = pd.DataFrame(data)
st.table(summary)
