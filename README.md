### Guide to input fields

Indented parts are conditional on the selection of the previous unindented field. For example:

* `employment_status`
    * `1_type_of_contract`
        * `1_no_years_on_job`
        * `12_salary_before_tax`

This means that `1_type_of_contract` coditionally appears depending on the selection chosen on `employment_status`. Index `1` in front of it indicates that it appears upon selecting the first option on the `employment_status` menu. Below, you can see `1_no_years_on_job` which is another field appearing on selection of the first option in the `1_type_of_contract` menu, but below it there is `12_salary_before_tax` where `12` indicates that it appears both upon selection of the first __and__ the second option on the `1_type_of_contract` menu.

Notable mention is on __step 3__ where employment status is concerned. When a second job is asked the consuquent fields are repeated with the first job, meaning the columns of the list must be repeated, hence I have included `<index>_sj_<column_name>` in the middle to differentiate the repeated columns. `sj` stands for "`s`econd `j`ob".

Furthermore on __step 4__ there is a section where user is asked how many mortgages their client has, which once again requires repetition of identical fiends corresponding to each mortgage. Here I use a similar convention to the one above: `<index>_<mortgage number>_<column name>`.

### Input fields:
#### Step 1
* name
* surname
* no_people_buying
* mortgage_purpose
    * 123_amount_borrowed
    * 123_mortgage_term
    * 12_ownership_type
        * 234_market_value
    * 1_found_new_home
        * 1_legal_status
        * 1_what_sort
    * 123_is_in_scotland
    * 1_purchase_price
    * 23_repay_unsecured_debt
    * 2_transferred_from_other_lender
    * 23_legal_status
    * 23_what_sort
    * 23_estimate_value
    * 3_same_term_as_existing
        * 2_existing_term
    * 3_outstanding_balance
    * 3_interest_only_basis
#### Step 2
* birth_date
* individual_status
* dependent_children
    * 1_no_of_dependent_children
* retirement_status
    * 1_planned_retirement_age
#### Step 3
* employment_status
    * 1_type_of_contract
        * 1_no_years_on_job
        * 125_salary_before_tax
        * 125_bonus
        * 125_how_often_bonus_paid
        * 125_overtime
        * 125_how_often_overtime_paid
        * 125_commission
        * 125_how_often_commission_paid
        * 2_time_contracting
        * 2_time_remaining
        * 34_employed_for_tax
            * 12_time_on_job
            * 12_time_remaining
            * 1_salary_before_tax
            * 1_bonus
            * 1_how_often_bonus_paid
            * 1_overtime
            * 1_how_often_overtime_paid
            * 1_commission
            * 1_how_often_commission_paid
            * 2_net_profit_latest
            * 2_net_profit_previous
        * 5_time_in_regular_work
    * 2345_time_in_business
    * 2_share_of_profit_latest
    * 2_share_of_profit_previous
    * 3_net_profit_latest
    * 3_net_profit_previous
    * 4_salary_before_tax
    * 4_bonus
    * 4_how_often_bonus_paid
    * 4_overtime
    * 4_how_often_overtime_paid
    * 4_commission
    * 4_how_often_commission_paid
    * 5_salary_div_latest
    * 5_salary_div_previous
    * 12345_second_job
        * 1_employment_status
            * 1_sj_type_of_contract
                * 1_sj_no_years_on_job
                * 125_sj_salary_before_tax
                * 125_sj_bonus
                * 125_sj_how_often_bonus_paid
                * 125_sj_overtime
                * 125_sj_how_often_overtime_paid
                * 125_sj_commission
                * 125_sj_how_often_commission_paid
                * 2_sj_time_contracting
                * 2_sj_time_remaining
                * 34_sj_employed_for_tax
                    * 12_sj_time_on_job
                    * 12_sj_time_remaining
                    * 1_sj_salary_before_tax
                    * 1_sj_bonus
                    * 1_sj_how_often_bonus_paid
                    * 1_sj_overtime
                    * 1_sj_how_often_overtime_paid
                    * 1_sj_commission
                    * 1_sj_how_often_commission_paid
                    * 2_sj_net_profit_latest
                    * 2_sj_net_profit_previous
                * 5_sj_time_in_regular_work
            * 2345_sj_time_in_business
            * 2_sj_share_of_profit_latest
            * 2_sj_share_of_profit_previous
            * 3_sj_net_profit_latest
            * 3_sj_net_profit_previous
            * 4_sj_salary_before_tax
            * 4_sj_bonus
            * 4_sj_how_often_bonus_paid
            * 4_sj_overtime
            * 4_sj_how_often_overtime_paid
            * 4_sj_commission
            * 4_sj_how_often_commission_paid
            * 5_sj_salary_div_latest
            * 5_sj_salary_div_previous
* other_income
    * 1_investments
    * 1_rent
    * 1_disability_benefits
    * 1_tax_credits
    * 1_child_benefits
    * 1_maintenance_income
    * 1_pension
### Step 4
* credit_card_debt
* personal_loans
* secured_loan_payments
* buy_now_pay_later
* travel
* student_loans
* other
* childcare
* school_fees
* maintenance
* additional_costs_dependents
* other_mortgages
    * 1_how_many
        * 1_1_total_balance
        * 1_1_interest_only_balance
        * 1_1_remaining_term
        * 1_1_do_they_let
            * 1_1_tenancy_agreement
                * 1_1_monthly_income
                * 1_1_monthly_payments
