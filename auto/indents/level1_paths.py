from auto.indents.level2_paths import Level2Paths


class Level1Paths(Level2Paths):
    """
    Collection of input and decision methods corresponding to first indented layer of user input from the README.md guide.

    Args:
        Level2Paths (class): Second layer of input and decision methods.
    """

    def __init__(self):
        super(Level1Paths, self).__init__()

    def step1_start(self):
        self.close_cookies()

        # How many people are applying?
        column = "no_people_buying"
        # no_people_buying = self.data[column].values[0]
        no_people_buying = 0  # I have hardcoded this to develop later, since 2 people
        # will yield too much complexity.
        css_string = 'label[for="AffCalc-q0-NumberOfApplicants-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=no_people_buying,
        )

    def step1_buy_new_property(self):
        # How much would your client(s) like to borrow?
        self.step1_common.amount_to_borrow(self)

        # How long does the mortgage term need to be?
        self.step1_common.mortgage_term_length(self)

        # What type of ownership will it be?
        self.step1_common.type_of_ownership(self, is_new=True)

        # Has your client(s) found a new home?
        column = "1_found_new_home"
        has_found_new_home = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q60-PropertyFound-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=has_found_new_home,
        )
        if has_found_new_home == 0:
            self.step1_new_home_found()
            self.has_found_new_home = True
        elif has_found_new_home == 1:
            pass

        # Is the property in Scotland?
        self.step1_common.is_property_in_scotland(self)

    def step1_remortgage_existing_property(self):
        # How much would your client(s) like to borrow?
        self.step1_common.amount_to_borrow(self)

        # How long does the mortgage term need to be?
        self.step1_common.mortgage_term_length(self)

        # Are you borrowing any funds to repay unsecured debts?
        self.step1_common.borrow_for_unsecured_debt(self)

        # Amount transferred from other lender
        amount = self.data["2_transferred_from_other_lender"].values[0]
        id_string = "AffCalc-q25-AmountTransferredFromOtherLender"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # What type of ownership will it be?
        self.step1_common.type_of_ownership(self, is_new=False)

        # Is the property in Scotland?
        self.step1_common.is_property_in_scotland(self)

        # What's the property's legal status?
        self.step1_common.property_legal_status(self)

        # What sort of property is it?
        self.step1_common.what_sort_is_this_property(self)

    def step1_borrow_more(self):
        # Are you borrowing any funds to repay unsecured debts?
        self.step1_common.borrow_for_unsecured_debt(self)

        # How much would your client(s) like to borrow?
        self.step1_common.amount_to_borrow(self, input_field_index=22)

        # How long does the mortgage term need to be?
        self.step1_common.mortgage_term_length(self)

        # Is the property in Scotland?
        self.step1_common.is_property_in_scotland(self)

        # What's the property's legal status?
        self.step1_common.property_legal_status(self)

        # What sort of property is it?
        self.step1_common.what_sort_is_this_property(self)

        # Is this or will this be the same term as the existing mortgage?
        column = "3_same_term_as_existing"
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q42-BorrowMoreTermMatchesExisting-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            pass
        elif value == 1:
            self.step1_existing_mortgage_term()

        # What is the total outstanding balance of your client's existing mortgage?
        amount = self.data["3_outstanding_balance"].values[0]
        id_string = "AffCalc-q46-ExistingMortgageBalance"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Of this amount, how much is held on an interest only basis?
        amount = self.data["3_interest_only_basis"].values[0]
        id_string = "AffCalc-q48-ExistingInterestOnlyMortgageBalance"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # What's the current estimated value?
        self.step1_common.current_estimated_value(self)

    def step2_start(self, purpose):
        # What's your client's date of birth?
        bday = self.data["birth_date"].values[0].split(",")
        days = bday[0]
        months = bday[1]
        years = bday[2]
        bday_days = "AffCalc-q140-Day"
        self.type_amount(
            id_string=bday_days,
            amount=days,
        )
        bday_months = "AffCalc-q140-Month"
        self.type_amount(
            id_string=bday_months,
            amount=months,
        )
        bday_years = "AffCalc-q140-Year"
        self.type_amount(
            id_string=bday_years,
            amount=years,
        )

        if purpose == 0 or purpose == 1:
            # What's the individual's status?
            column = "individual_status"
            status = self.data[column].values[0]
            status_input_id = "AffCalc-q145-PropertyTenure"
            self.select_from_menu(
                id_string=status_input_id,
                no_options=3,
                option=status,
                prob_column=column,
                plz_select=True,
            )

    def step2_have_children(self):
        # How many financial dependants does your client have?
        ages = self.data["1_no_of_dependent_children"].values[0].split(",")
        aged0_5 = ages[0]
        aged6_11 = ages[1]
        aged12_17 = ages[2]
        aged18_over = ages[3]
        aged0_5_id_string = "AffCalc-q160-Age0to5-0"
        self.type_amount(
            id_string=aged0_5_id_string,
            amount=aged0_5,
        )
        aged6_11_id_string = "AffCalc-q160-Age6to11-1"
        self.type_amount(
            id_string=aged6_11_id_string,
            amount=aged6_11,
        )
        aged12_17_id_string = "AffCalc-q160-Age12to17-2"
        self.type_amount(
            id_string=aged12_17_id_string,
            amount=aged12_17,
        )
        aged18_over_id_string = "AffCalc-q160-Age18More-3"
        self.type_amount(
            id_string=aged18_over_id_string,
            amount=aged18_over,
        )

    def step2_client_is_not_retired(self):
        # What's their planned retirement age?
        amount = self.data["1_planned_retirement_age"].values[0]
        id_string = "AffCalc-q180-RetirementAge"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step3_has_other_income(self):
        # Investments?
        amount = self.data["1_investments"].values[0]
        id_string = "AffCalc-q620-MonthlyInvestmentIncome"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Rent from mortgage-free properties?
        amount = self.data["1_rent"].values[0]
        id_string = "AffCalc-q630-MortgageFreeMonthlyRentalIncome"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # State Disability Benefit?
        amount = self.data["1_disability_benefits"].values[0]
        id_string = "AffCalc-q640-MonthlyStateDisabilityBenefit"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Universal credits or Tax credits?
        amount = self.data["1_tax_credits"].values[0]
        id_string = "AffCalc-q650-MonthlyUniversalCreditsTaxCredits"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Child benefit?
        amount = self.data["1_child_benefits"].values[0]
        id_string = "AffCalc-q660-MonthlyChildBenefit"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Maintenance income?
        amount = self.data["1_maintenance_income"].values[0]
        id_string = "AffCalc-q670-MonthlyMaintenanceIncome"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Pension?
        amount = self.data["1_pension"].values[0]
        id_string = "AffCalc-q680-MonthlyPensionIncome"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step3_employed(self, sj):
        if sj == "_sj":
            status_input_id = "AffCalc-q440-EmploymentType"
        else:
            status_input_id = "AffCalc-q250-EmploymentType"

        # What sort of contract are they on?
        column = f"1{sj}_type_of_contract"
        status = self.data[column].values[0]
        self.select_from_menu(
            id_string=status_input_id,
            no_options=5,
            option=status,
            prob_column=column,
            plz_select=True,
        )
        if status == 1:
            self.step3_permanent(sj=sj)
        elif status == 2:
            self.step3_fixed_term_contract(sj=sj)
        elif status == 3:
            # Fixed term sub contract
            self.step3_sub_contract(sj=sj, fixed=True)
        elif status == 4:
            # Open ended sub contract
            self.step3_sub_contract(sj=sj, fixed=False)
        elif status == 5:
            self.step3_temporary(sj=sj)

    def step3_self_employed_partner(self, sj):
        # How long have they been in business?
        self.step3_common.time_in_business(self, sj=sj)

        # What's their share of net profit, for the latest period?
        amount = self.data[f"2{sj}_share_of_profit_latest"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q570-LatestPeriodProfitShare"
        else:
            id_string = "AffCalc-q380-LatestPeriodProfitShare"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # What's their share of net profit, for the previous period?
        amount = self.data[f"2{sj}_share_of_profit_previous"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q580-PreviousPeriodProfitShare"
        else:
            id_string = "AffCalc-q390-PreviousPeriodProfitShare"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step3_self_employed_sole(self, sj):
        # How long have they been in business?
        self.step3_common.time_in_business(self, sj=sj)

        # What's their net profit, before tax, for the latest period?
        amount = self.data[f"3{sj}_net_profit_latest"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q550-LatestPeriodProfit"
        else:
            id_string = "AffCalc-q360-LatestPeriodProfit"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # What's their net profit, before tax, for the previous period?
        amount = self.data[f"3{sj}_net_profit_previous"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q560-PreviousPeriodProfit"
        else:
            id_string = "AffCalc-q370-PreviousPeriodProfit"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step3_director_less_20(self, sj):
        # How long have they been in their job?
        self.step3_common.time_in_business(
            self, sj=sj, input_field_index=270, sj_input_field_index=460, is_small_director=True
        )

        # What's their salary before tax?
        self.step3_common.salary_before_tax(self, sj=sj, column_index=4)

        # Do they earn any bonus?
        self.step3_common.earn_bonus(self, sj=sj, column_index=4)

        # Do they earn any overtime?
        self.step3_common.earn_overtime(self, sj=sj, column_index=4)

        # Do they earn any commission?
        self.step3_common.earn_commission(self, sj=sj, column_index=4)

        if self.amount_bonus > 0:
            # How often is the bonus paid?
            self.step3_common.how_often_bonus_paid(self, sj=sj, column_index=4)

        if self.amount_overtime > 0:
            # How often is the overtime paid?
            self.step3_common.how_often_overtime_paid(self, sj=sj, column_index=4)

        if self.amount_commission > 0:
            # How often is the commision paid?
            self.step3_common.how_often_commission_paid(self, sj=sj, column_index=4)

    def step3_director_more_20(self, sj):
        # How long have they been in business?
        self.step3_common.time_in_business(self, sj=sj)

        # What's their salary, including dividends, for the latest period?
        amount = self.data[f"5{sj}_salary_div_latest"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q590-LatestPeriodSalary"
        else:
            id_string = "AffCalc-q400-LatestPeriodSalary"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # What's their salary, including dividends, for the previous period?
        amount = self.data[f"5{sj}_salary_div_previous"].values[0]
        if sj == "_sj":
            id_string = "AffCalc-q600-PreviousPeriodSalary"
        else:
            id_string = "AffCalc-q410-PreviousPeriodSalary"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step4_start(self):
        # What's the total your client owes on all credit cards?
        amount = self.data["credit_card_debt"].values[0]
        id_string = "AffCalc-q1320-TotalCreditCardBalances"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        if self.not_buying_new:
            # Of this amount how much will be cleared on or before completion?
            amount = self.data["how_much_debt_cleared_per_month"].values[0]
            id_string = "AffCalc-q1325-TotalCreditCardBalanceToBeCleared"
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )

            # Are all credit cards cleared in full each month?
            column = "all_credit_cards_cleared_next_month"
            value = self.data[column].values[0]
            css_string = 'label[for="AffCalc-q1328-CreditCardBalanceClearedMonthly-'
            self.select_option(
                css_string=css_string,
                no_options=2,
                prob_column=column,
                option=value,
            )

        # Personal loans and hire purchases?
        amount = self.data["personal_loans"].values[0]
        id_string = "AffCalc-q1330-MonthlyPersonalLoanOrHire"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Secured loan payments?
        amount = self.data["secured_loan_payments"].values[0]
        id_string = "AffCalc-q1340-MonthlySecuredLoanPayments"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Buy now, pay later agreements?
        amount = self.data["buy_now_pay_later"].values[0]
        id_string = "AffCalc-q1350-MonthlyDpaPayment"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Student loan payments?
        amount = self.data["student_loans"].values[0]
        id_string = "AffCalc-q1360-MonthlyStudentLoan"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Travel?
        amount = self.data["travel"].values[0]
        id_string = "AffCalc-q1370-MonthlyTravelCosts"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Other regular monthly costs, if any?
        amount = self.data["other"].values[0]
        id_string = "AffCalc-q1380-MonthlyOtherExpenditure"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Childcare?
        amount = self.data["childcare"].values[0]
        id_string = "AffCalc-q1390-MonthlyChildCare"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # School fees?
        amount = self.data["school_fees"].values[0]
        id_string = "AffCalc-q1400-MonthlySchoolFees"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Maintenance?
        amount = self.data["maintenance"].values[0]
        id_string = "AffCalc-q1410-MonthlyDependentMaintenance"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

        # Any additional costs for financial dependants?
        amount = self.data["additional_costs_dependents"].values[0]
        id_string = "AffCalc-q1420-MonthlyCostOfFinancialDependents"
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )

    def step4_applicant_has_other_mortgages(self, value):
        # For some reason I am unable to select more than one mortgage. However nonetheless
        # I have programmed a loop to facilitate this in case a fix can be found in the future.
        for i in range(int(value)):
            # What will the total balance be on this other mortgage?
            amount = self.data[f"1_{i+1}_total_balance"].values[0]
            id_string = f"AffCalc-q1580-{i}-0-TotalBalance"
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )

            # What will the interest-only balance be on this other mortgage?
            amount = self.data[f"1_{i+1}_interest_only_balance"].values[0]
            id_string = f"AffCalc-q1580-{i}-1-InterestOnlyBalance"
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )

            # What will the remaining term of the loan be?
            term = self.data[f"1_{i+1}_remaining_term"].values[0].split(",")
            years = term[0]
            months = term[1]
            term_length_years = f"AffCalc-q1580-{i}-2-RemainingTermOfLoanYY"
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            )
            term_length_months = f"AffCalc-q1580-{i}-2-RemainingTermOfLoanMM"
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )

            # Does your client let the property linked to this mortgage?
            column = f"1_{i+1}_do_they_let"
            value = self.data[column].values[0]
            css_string = f'label[for="AffCalc-q1580-{i}-3-PropertyLet-'
            self.select_option(
                css_string=css_string,
                no_options=2,
                prob_column=column,
                option=value,
            )
            if value == 0:
                self.step4_they_let_on_this_mortgate(i=i)
            elif value == 1:
                pass
