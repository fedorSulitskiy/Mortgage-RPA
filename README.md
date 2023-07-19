## Introduction

I have designed an __almost__ comprehensive, RPA (Robotic Process Automation) program for the Nationwide building society afforability calculator. It takes in the .csv file containing user's inputs and runs them through the calculator at great speed using Selenium library. It validates the output by registering the amount of money Nationwide would be willing to let according to the calculator and it compares it to the value yielded from manually inputting the same set of information.

It is designed to be able to take in __any__ combination of inputs the afforability calculator is able to handle, __subject to__ limitations mentioned below, hence it is __almost__ comprehensive.

![Example of operations.](https://github.com/fedorSulitskiy/Mortgage-RPA/blob/main/README_media/example_of_use.gif)

## How to use.

Although it is a limitation in its own right, since it is unnecessary, the chromedriver.exe for verion 114.0.5735 is included in the repository meaning if your chrome is of the same general version there is no need to install a new one. I am aware that a better practice would be to access the chromedriver through PATH, but in this case I was more focused on immediate usability, without requiring the user to download the new chromedriver, or missing with PATH variables.

__Step 1__ - Install selenium and pandas packages.

__Step 2__ - Input the parameters for the online calculator into the csv file according to the advice below.

__Step 3__ - Run the launch command in the directory of the application:
   `python main.py`
   
__(optional) Step 4__ - Rerun the program, changing the restart_index variable in the `main.py` file in case it crashes.


Validation table will be returned upon completion of the program and will be available in the initial input.csv file.

![Screenshot of validation table returned.](https://github.com/fedorSulitskiy/Mortgage-RPA/blob/main/README_media/final_output.png)

## Guide to input fields

Within the input table there is a number of fields which roughly follow and correspond to most potential inputs within the calculator. Hence to use the tool each field must be filled in according to the order and logic supplied by the calculator itself, so that the program can successfully execute the inputs. 

__Hence it is recommended to reference the Input Fields array below whenever setting the data in the input.csv file. The procedure that works best is to have the calculator open, input the data into it and mirror the inputs to the input.csv file.__

The input array starts with name and surname which are not essential for the calculator but were my creative choice to uniquely identify each test scenario. Naturally I have called everyone "John". The indented parts are conditional on the selection of the previous unindented field. For example:

* `employment_status`
    * `1_type_of_contract`
        * `1_no_years_on_job`
        * `12_salary_before_tax`

This means that `1_type_of_contract` coditionally appears depending on the selection chosen on `employment_status`. Index `1` in front of it indicates that it appears upon selecting the first option on the `employment_status` menu. Below, you can see `1_no_years_on_job` which is another field appearing on selection of the first option in the `1_type_of_contract` menu, but below it there is `12_salary_before_tax` where `12` indicates that it appears both upon selection of the first __and__ the second option on the `1_type_of_contract` menu.

Notable mention is on __step 3__ where employment status is concerned. When a second job is asked the consequent fields are repeated with the first job, meaning the columns of the list must be repeated, hence I have included `<index>_sj_<column_name>` in the middle to differentiate the repeated columns. `sj` stands for "`s`econd `j`ob".

Furthermore on __step 4__ there is a section where user is asked how many mortgages their client has, which once again requires repetition of identical fiends corresponding to each mortgage. Here I use a similar convention to the one above: `<index>_<mortgage number>_<column name>`. However in practice my code was not able to select the multiple mortgages option, hence the fields for additional mortgages were removed from the array of input fields.

## Input fields:
### Step 1
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
### Step 2
* birth_date
* individual_status
* dependent_children
    * 1_no_of_dependent_children
* retirement_status
    * 1_planned_retirement_age
### Step 3
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
* how_much_debt_cleared_per_month
* all_credit_cards_cleared_next_month
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
* council_tax
* buildings_insurance
* service_estate_charge
* ground_rent

## Limitations

The program has __four__ main limitations that I am currently aware of, which can all be improved given more time:

   * The input table is very large, has redundancies and is difficult to fill in for a person trying to do it first time. With more experimentation and greater thought it can be reformed to have no repetitive fields, and a more easy to follow naming/indexing convention. With excellent implementation this should not change the code itself, apart from the names of the columns which supply information and some logic related to choosing the relevant columns.
   * The program is unable to perform calculation for __two__ applicants. I decided to go against it for this task since it would double the number of input fields and introduce additional complexity which will take too much time to implement. Unfortunately I am limited in the amount of time I can spend on this project.
   * As mentioned above, the program is unable to input the information for clients that have more than one additional mortgage. I have programmed a loop and accounted for this in the input field naming convention however, for an unknown reason I am unable to select more than one additional mortgages in the relevant field. I am inclined to conclude that it is a problem caused by the Selenium library that I am using, and would have loved to find a way to fix it.
   * Apart from the limitations mentioned above, the program is __probably not comprehensive__. The test scenario suite I ran doesn't test every method within the code I wrote, once again due to time concerns, and I have not been able to manually test every possible combination of inputs within the original calculator. Hence I would not be surprised if certain inputs are missed or certain situations are not accounted for. Nonetheless I am confident that the foundation that I have built would be flexible enough to account for these ommissions.
