from auto.indents.level2_paths import Level2Paths

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Level1Paths(Level2Paths):
    
    def step1_start(self):
        self.close_cookies()
        
        # How many people are applying?
        column = 'no_people_buying'
        # no_people_buying = self.data[column].values[0]
        no_people_buying = 0 # I have hardcoded this to develop later, since 2 people
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
        amount = self.data['123_amount_borrowed'].values[0]
        id_string = 'AffCalc-q20-BorrowingAmount'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # How long does the mortgage term need to be?
        term = self.data['123_mortgage_term'].values[0].split(",")
        years = term[0]
        months = term[1]
        term_length_years = 'AffCalc-q30-MortgageTermYears'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        term_length_months = 'AffCalc-q30-MortgageTermMonths'
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What type of ownership will it be?
        column = '12_ownership_type'
        ownership_type = self.data[column].values[0]
        ownership_type_input_id = 'AffCalc-q40-OwnershipType'
        self.select_from_menu(
            id_string=ownership_type_input_id,
            no_options=5,
            option=ownership_type,
            prob_column=column,
            plz_select=True,
        )
        if ownership_type == 1:
            self.step1_standart_ownership_type(new=True)
        elif ownership_type == 2:
            self.step1_shared_equity(new=True)
        elif ownership_type == 3:
            self.step1_right_to_buy(new=True)
        elif ownership_type == 4:
            self.step1_shared_ownership(new=True)
            
        # Has your client(s) found a new home?
        column = '1_found_new_home'
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
        elif has_found_new_home == 1:
            pass
        
        # Is the property in Scotland?
        column = '123_is_in_scotland'
        is_it_in_scotland = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q135-RegionCode-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=is_it_in_scotland,
        )    
        
    def step1_remortgage_existing_property(self):        
        
        # How much would your client(s) like to borrow?
        amount = self.data['123_amount_borrowed'].values[0]
        id_string = 'AffCalc-q20-BorrowingAmount'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # How long does the mortgage term need to be?
        term = self.data['123_mortgage_term'].values[0].split(",")
        years = term[0]
        months = term[1]
        term_length_years = 'AffCalc-q30-MortgageTermYears'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        term_length_months = 'AffCalc-q30-MortgageTermMonths'
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # Are you borrowing any funds to repay unsecured debts?
        column = '23_repay_unsecured_debt'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q15-RemortagingToRepayDebts-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        
        # Amount transferred from other lender
        amount = self.data['2_transferred_from_other_lender'].values[0]
        id_string = 'AffCalc-q25-AmountTransferredFromOtherLender'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What type of ownership will it be?
        column = '12_ownership_type'
        ownership_type = self.data[column].values[0]
        ownership_type_input_id = 'AffCalc-q40-OwnershipType'
        self.select_from_menu(
            id_string=ownership_type_input_id,
            no_options=5,
            option=ownership_type,
            prob_column=column,
            plz_select=True,
        )
        if ownership_type == 1:
            self.step1_standart_ownership_type(new=False)
        elif ownership_type == 2:
            self.step1_shared_equity(new=False)
        elif ownership_type == 3:
            self.step1_right_to_buy(new=False)
        elif ownership_type == 4:
            self.step1_shared_ownership(new=False)    
            
        # Is the property in Scotland?
        column = '123_is_in_scotland'
        is_it_in_scotland = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q135-RegionCode-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=is_it_in_scotland,
        )   
        
        # What's the property's legal status?
        column = '23_legal_status'
        value = self.data[column].values[0]
        id_string = 'AffCalc-q70-PropertyTenure'
        self.select_from_menu(
            id_string=id_string,
            no_options=4,
            option=value,
            prob_column=column,
            plz_select=True,
        )
        
        # What sort of property is it?
        column = '23_what_sort'
        value = self.data[column].values[0]
        id_string = 'AffCalc-q80-PropertyType'
        self.select_from_menu(
            id_string=id_string,
            no_options=8,
            option=value,
            prob_column=column,
            plz_select=True,
        ) 
    
    def step1_borrow_more(self):
        
        # Are you borrowing any funds to repay unsecured debts?
        column = '23_repay_unsecured_debt'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q15-RemortagingToRepayDebts-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        
        # How much would your client(s) like to borrow?
        amount = self.data['123_amount_borrowed'].values[0]
        id_string = 'AffCalc-q22-BorrowingAmount'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # How long does the mortgage term need to be?
        term = self.data['123_mortgage_term'].values[0].split(",")
        years = term[0]
        months = term[1]
        term_length_years = 'AffCalc-q30-MortgageTermYears'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        term_length_months = 'AffCalc-q30-MortgageTermMonths'
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # Is the property in Scotland?
        column = '123_is_in_scotland'
        is_it_in_scotland = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q135-RegionCode-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=is_it_in_scotland,
        )
        
        # What's the property's legal status?
        column = '23_legal_status'
        value = self.data[column].values[0]
        id_string = 'AffCalc-q70-PropertyTenure'
        self.select_from_menu(
            id_string=id_string,
            no_options=4,
            option=value,
            prob_column=column,
            plz_select=True,
        )
        
        # What sort of property is it?
        column = '23_what_sort'
        value = self.data[column].values[0]
        id_string = 'AffCalc-q80-PropertyType'
        self.select_from_menu(
            id_string=id_string,
            no_options=8,
            option=value,
            prob_column=column,
            plz_select=True,
        )
        
        # Is this or will this be the same term as the existing mortgage?
        column = '3_same_term_as_existing'
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
        amount = self.data['3_outstanding_balance'].values[0]
        id_string = 'AffCalc-q46-ExistingMortgageBalance'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Of this amount, how much is held on an interest only basis?
        amount = self.data['3_interest_only_basis'].values[0]
        id_string = 'AffCalc-q48-ExistingInterestOnlyMortgageBalance'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What's the current estimated value?
        amount = self.data['23_estimate_value'].values[0]
        borrowing_amount_input = 'AffCalc-q120-CurrentEstimatedValue'
        self.type_amount(
            id_string=borrowing_amount_input,
            amount=amount,
        )

    def step2_start(self, purpose):
        
        # What's your client's date of birth?
        bday = self.data['birth_date'].values[0].split(",")
        days = bday[0]
        months = bday[1]
        years = bday[2]
        bday_days = 'AffCalc-q140-Day'
        self.type_amount(
            id_string=bday_days,
            amount=days,
        )
        bday_months = 'AffCalc-q140-Month'
        self.type_amount(
            id_string=bday_months,
            amount=months,
        )
        bday_years = 'AffCalc-q140-Year'
        self.type_amount(
            id_string=bday_years,
            amount=years,
        )
        
        if purpose == 0 or purpose == 1:
            # What's the individual's status?
            column = 'individual_status'
            status = self.data[column].values[0]
            status_input_id = 'AffCalc-q145-PropertyTenure'
            self.select_from_menu(
                id_string=status_input_id,
                no_options=3,
                option=status,
                prob_column=column,
                plz_select=True,
            )

    def step2_have_children(self):
        
        # How many financial dependants does your client have?
        ages = self.data['1_no_of_dependent_children'].values[0].split(",")
        aged0_5 = ages[0]
        aged6_11 = ages[1]
        aged12_17 = ages[2]
        aged18_over = ages[3]
        aged0_5_id_string = 'AffCalc-q160-Age0to5-0'
        self.type_amount(
            id_string=aged0_5_id_string,
            amount=aged0_5,
        )
        aged6_11_id_string = 'AffCalc-q160-Age6to11-1'
        self.type_amount(
            id_string=aged6_11_id_string,
            amount=aged6_11,
        )
        aged12_17_id_string = 'AffCalc-q160-Age12to17-2'
        self.type_amount(
            id_string=aged12_17_id_string,
            amount=aged12_17,
        )
        aged18_over_id_string = 'AffCalc-q160-Age18More-3'
        self.type_amount(
            id_string=aged18_over_id_string,
            amount=aged18_over,
        )
        
    def step2_client_is_not_retired(self):
        
        # What's their planned retirement age?
        amount = self.data['1_planned_retirement_age'].values[0]
        id_string = 'AffCalc-q180-RetirementAge'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
    
    def step3_has_other_income(self):
        
        # Investments?
        amount = self.data['1_investments'].values[0]
        id_string = 'AffCalc-q620-MonthlyInvestmentIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Rent from mortgage-free properties?
        amount = self.data['1_rent'].values[0]
        id_string = 'AffCalc-q630-MortgageFreeMonthlyRentalIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # State Disability Benefit?
        amount = self.data['1_disability_benefits'].values[0]
        id_string = 'AffCalc-q640-MonthlyStateDisabilityBenefit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Universal credits or Tax credits?
        amount = self.data['1_tax_credits'].values[0]
        id_string = 'AffCalc-q650-MonthlyUniversalCreditsTaxCredits'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Child benefit?
        amount = self.data['1_child_benefits'].values[0]
        id_string = 'AffCalc-q660-MonthlyChildBenefit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Maintenance income?
        amount = self.data['1_maintenance_income'].values[0]
        id_string = 'AffCalc-q670-MonthlyMaintenanceIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Pension?
        amount = self.data['1_pension'].values[0]
        id_string = 'AffCalc-q680-MonthlyPensionIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
    def step3_employed(self, sj):
        if sj == '_sj':
            status_input_id = 'AffCalc-q440-EmploymentType'
        else:
            status_input_id = 'AffCalc-q250-EmploymentType'
            
        # What sort of contract are they on?
        column = f'1{sj}_type_of_contract'
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
        term = self.data[f'2345{sj}_time_in_business'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q470-BusinessYears'
            term_length_months = 'AffCalc-q470-BusinessMonths'
        else:
            term_length_years = 'AffCalc-q280-BusinessYears'
            term_length_months = 'AffCalc-q280-BusinessMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What's their share of net profit, for the latest period?
        amount = self.data[f'2{sj}_share_of_profit_latest'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q570-LatestPeriodProfitShare'
        else: id_string = 'AffCalc-q380-LatestPeriodProfitShare'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What's their share of net profit, for the previous period?
        amount = self.data[f'2{sj}_share_of_profit_previous'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q580-PreviousPeriodProfitShare'
        else: id_string = 'AffCalc-q390-PreviousPeriodProfitShare'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
    
    def step3_self_employed_sole(self, sj):
        
        # How long have they been in business?
        term = self.data[f'2345{sj}_time_in_business'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q470-BusinessYears'
            term_length_months = 'AffCalc-q470-BusinessMonths'
        else:
            term_length_years = 'AffCalc-q280-BusinessYears'
            term_length_months = 'AffCalc-q280-BusinessMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What's their net profit, before tax, for the latest period?
        amount = self.data[f'3{sj}_net_profit_latest'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q550-LatestPeriodProfit'
        else: id_string = 'AffCalc-q360-LatestPeriodProfit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What's their net profit, before tax, for the previous period?
        amount = self.data[f'3{sj}_net_profit_previous'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q560-PreviousPeriodProfit'
        else: id_string = 'AffCalc-q370-PreviousPeriodProfit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
    
    def step3_director_less_20(self, sj):
        
        # How long have they been in their job?
        term = self.data[f'2345{sj}_time_in_business'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q460-JobYears'
            term_length_months = 'AffCalc-q460-JobMonths'
        else:
            term_length_years = 'AffCalc-q270-JobYears'
            term_length_months = 'AffCalc-q270-JobMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What's their salary before tax?
        amount = self.data[f'4{sj}_salary_before_tax'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q510-GrossAnnualIncome'
        else: id_string = 'AffCalc-q320-GrossAnnualIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        # Do they earn any bonus?
        amount_bonus = self.data[f'4{sj}_bonus'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q520-Bonus'
        else: id_string = 'AffCalc-q330-Bonus'
        self.type_amount(
            id_string=id_string,
            amount=amount_bonus,
        )
        
        # Do they earn any overtime?
        amount_overtime = self.data[f'4{sj}_overtime'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q530-Overtime'
        else: id_string = 'AffCalc-q340-Overtime'
        self.type_amount(
            id_string=id_string,
            amount=amount_overtime,
        )
        
        # Do they earn any commission?
        amount_commission = self.data[f'4{sj}_commission'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q540-Commission'
        else: id_string = 'AffCalc-q350-Commission'
        self.type_amount(
            id_string=id_string,
            amount=amount_commission,
        )
            
        if amount_bonus > 0:
            # How often is the bonus paid?
            column = f'4{sj}_how_often_bonus_paid'
            value = self.data[column].values[0]
            if sj == '_sj': id_string = 'AffCalc-q525-BonusFrequency'
            else: id_string = 'AffCalc-q335-BonusFrequency'
            self.select_from_menu(
                id_string=id_string,
                no_options=5,
                option=value,
                prob_column=column,
                plz_select=True,
            )
        if amount_overtime > 0:
            # How often is the overtime paid?
            column = f'4{sj}_how_often_overtime_paid'
            value = self.data[column].values[0]
            if sj == '_sj': id_string = 'AffCalc-q535-OvertimeFrequency'
            else: id_string = 'AffCalc-q345-OvertimeFrequency'
            self.select_from_menu(
                id_string=id_string,
                no_options=5,
                option=value,
                prob_column=column,
                plz_select=True,
            )
        if amount_commission > 0:
            # How often is the commision paid?
            column = f'4{sj}_how_often_commission_paid'
            value = self.data[column].values[0]
            if sj == '_sj': id_string = 'AffCalc-q545-CommissionFrequency'
            else: id_string = 'AffCalc-q355-CommissionFrequency'
            self.select_from_menu(
                id_string=id_string,
                no_options=5,
                option=value,
                prob_column=column,
                plz_select=True,
            )
    
    def step3_director_more_20(self, sj):
        
        # How long have they been in business?
        term = self.data[f'2345{sj}_time_in_business'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q470-BusinessYears'
            term_length_months = 'AffCalc-q470-BusinessMonths'
        else:
            term_length_years = 'AffCalc-q280-BusinessYears'
            term_length_months = 'AffCalc-q280-BusinessMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What's their salary, including dividends, for the latest period?
        amount = self.data[f'5{sj}_salary_div_latest'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q590-LatestPeriodSalary'
        else: id_string = 'AffCalc-q400-LatestPeriodSalary'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What's their salary, including dividends, for the previous period?
        amount = self.data[f'5{sj}_salary_div_previous'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q600-PreviousPeriodSalary'
        else: id_string = 'AffCalc-q410-PreviousPeriodSalary'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
    def step4_start(self):
        
        # What's the total your client owes on all credit cards?
        amount = self.data['credit_card_debt'].values[0]
        id_string = 'AffCalc-q1320-TotalCreditCardBalances'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Personal loans and hire purchases?
        amount = self.data['personal_loans'].values[0]
        id_string = 'AffCalc-q1330-MonthlyPersonalLoanOrHire'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Secured loan payments?
        amount = self.data['secured_loan_payments'].values[0]
        id_string = 'AffCalc-q1340-MonthlySecuredLoanPayments'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Buy now, pay later agreements?
        amount = self.data['buy_now_pay_later'].values[0]
        id_string = 'AffCalc-q1350-MonthlyDpaPayment'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Student loan payments?
        amount = self.data['student_loans'].values[0]
        id_string = 'AffCalc-q1360-MonthlyStudentLoan'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Travel?
        amount = self.data['travel'].values[0]
        id_string = 'AffCalc-q1370-MonthlyTravelCosts'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Other regular monthly costs, if any?
        amount = self.data['other'].values[0]
        id_string = 'AffCalc-q1380-MonthlyOtherExpenditure'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Childcare?
        amount = self.data['childcare'].values[0]
        id_string = 'AffCalc-q1390-MonthlyChildCare'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # School fees?
        amount = self.data['school_fees'].values[0]
        id_string = 'AffCalc-q1400-MonthlySchoolFees'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Maintenance?
        amount = self.data['maintenance'].values[0]
        id_string = 'AffCalc-q1410-MonthlyDependentMaintenance'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # Any additional costs for financial dependants?
        amount = self.data['additional_costs_dependents'].values[0]
        id_string = 'AffCalc-q1420-MonthlyCostOfFinancialDependents'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
    def step4_applicant_has_other_mortgages(self, value):
        
        for i in range(int(value)):
            
            # What will the total balance be on this other mortgage?
            amount = self.data[f'1_{i+1}_total_balance'].values[0]
            id_string = f'AffCalc-q1580-{i}-0-TotalBalance'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
            
            # What will the interest-only balance be on this other mortgage?
            amount = self.data[f'1_{i+1}_interest_only_balance'].values[0]
            id_string = f'AffCalc-q1580-{i}-1-InterestOnlyBalance'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
            
            # What will the remaining term of the loan be?
            term = self.data[f'1_{i+1}_remaining_term'].values[0].split(",")
            years = term[0]
            months = term[1]
            term_length_years = f'AffCalc-q1580-{i}-2-RemainingTermOfLoanYY'
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            )
            term_length_months = f'AffCalc-q1580-{i}-2-RemainingTermOfLoanMM'
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )
            
            # Does your client let the property linked to this mortgage?
            column = f'1_{i+1}_do_they_let'
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