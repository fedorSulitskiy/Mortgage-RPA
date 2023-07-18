import constants as const
from auto.indents.level1_paths import Level1Paths

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import time

class Robot(webdriver.Chrome, Level1Paths):
    """
    Robot class which will perform automated input. It outlines the general structure of the calcualtor navigation.
    It's methods are loosely following the unindented layer of inputs from the README.md document.
    """
    def __init__(self, name, surname):
        # Persistent attributes
        self.name_of_client = name
        self.surname_of_client = surname
        self.purpose = 0
        self.retired = False
        self.has_found_new_home = False
        self.not_buying_new = False
        self.amount_bonus = 0
        self.amount_overtime = 0
        self.amount_commission = 0

        # Set option for chrome to remain open after code stopped running.
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
        super(Robot, self).__init__(options=chrome_options)
        self.implicitly_wait(5)

        # Initialize input data.
        self.df = pd.read_csv("input/input.csv")
        self.data = self.df.loc[((self.df["name"] == name) & (self.df["surname"] == surname))]
        
        # Common methods
        self.step1_common = self.Step1Common
        self.step3_common = self.Step3Common
    
    class Step1Common():
        """
        Nested class with repeating/common methods to avoid code duplication.
        """
        def amount_to_borrow(self, input_field_index=20):
            amount = self.data['123_amount_borrowed'].values[0]
            id_string = f'AffCalc-q{input_field_index}-BorrowingAmount'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
        
        def mortgage_term_length(self):
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
            
        def type_of_ownership(self, is_new):
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
                self.step1_standart_ownership_type(new=is_new)
            elif ownership_type == 2:
                self.step1_shared_equity(new=is_new)
            elif ownership_type == 3:
                self.step1_right_to_buy(new=is_new)
            elif ownership_type == 4:
                self.step1_shared_ownership(new=is_new)
                
        def is_property_in_scotland(self):
            column = '123_is_in_scotland'
            is_it_in_scotland = self.data[column].values[0]
            css_string = 'label[for="AffCalc-q135-RegionCode-'
            self.select_option(
                css_string=css_string,
                no_options=2,
                prob_column=column,
                option=is_it_in_scotland,
            )
            
        def property_legal_status(self,column='23_legal_status'):
            column = column
            value = self.data[column].values[0]
            id_string = 'AffCalc-q70-PropertyTenure'
            self.select_from_menu(
                id_string=id_string,
                no_options=4,
                option=value,
                prob_column=column,
                plz_select=True,
            )
            
        def what_sort_is_this_property(self,column='23_what_sort'):
            column = column
            value = self.data[column].values[0]
            id_string = 'AffCalc-q80-PropertyType'
            self.select_from_menu(
                id_string=id_string,
                no_options=8,
                option=value,
                prob_column=column,
                plz_select=True,
            )
            
        def borrow_for_unsecured_debt(self):
            column = '23_repay_unsecured_debt'
            value = self.data[column].values[0]
            css_string = 'label[for="AffCalc-q15-RemortagingToRepayDebts-'
            self.select_option(
                css_string=css_string,
                no_options=2,
                prob_column=column,
                option=value,
            )
            
        def current_estimated_value(self, input_field_id='AffCalc-q120-CurrentEstimatedValue'):
            amount = self.data['23_estimate_value'].values[0]
            borrowing_amount_input = input_field_id
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
            
        def purchase_price(self, input_field_index=100):
            amount = self.data['1_purchase_price'].values[0]
            borrowing_amount_input = f'AffCalc-q{input_field_index}-PurchasePrice'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
            
        def full_market_value(self):
            amount = self.data['234_market_value'].values[0]
            id_string = 'AffCalc-q50-MarketValue'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            ) 
    
    class Step3Common():
        """
        Nested class with repeating/common methods to avoid code duplication.
        """
        def time_in_business(self, sj, input_field_index=280, sj_input_field_index=470, is_small_director = False):
            if is_small_director: work_years, work_months = 'JobYears', 'JobMonths'
            else: work_years, work_months = 'BusinessYears', 'BusinessMonths'
            term = self.data[f'2345{sj}_time_in_business'].values[0].split(",")
            years = term[0]
            months = term[1]
            if sj == '_sj': 
                term_length_years = f'AffCalc-q{sj_input_field_index}-{work_years}'
                term_length_months = f'AffCalc-q{sj_input_field_index}-{work_months}'
            else:
                term_length_years = f'AffCalc-q{input_field_index}-{work_years}'
                term_length_months = f'AffCalc-q{input_field_index}-{work_months}'
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            ) 
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )
            
        def salary_before_tax(self, sj, sub = False, column_index = 125):
            if sub: amount = self.data[f'1{sj}_salary_before_tax'].values[0]
            else: amount = self.data[f'{column_index}{sj}_salary_before_tax'].values[0]
            if sj == '_sj': id_string = 'AffCalc-q510-GrossAnnualIncome'
            else: id_string = 'AffCalc-q320-GrossAnnualIncome'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            ) 
            
        def earn_bonus(self, sj, sub=False, column_index = 125):
            if sub: self.amount_bonus = self.data[f'1{sj}_bonus'].values[0]
            else: self.amount_bonus = self.data[f'{column_index}{sj}_bonus'].values[0]
            if sj == '_sj': id_string = 'AffCalc-q520-Bonus'
            else: id_string = 'AffCalc-q330-Bonus'
            self.type_amount(
                id_string=id_string,
                amount=self.amount_bonus,
            )
            
        def earn_overtime(self, sj, sub=False, column_index = 125):
            if sub: self.amount_overtime = self.data[f'1{sj}_overtime'].values[0]
            else: self.amount_overtime = self.data[f'{column_index}{sj}_overtime'].values[0]
            if sj == '_sj': id_string = 'AffCalc-q530-Overtime'
            else: id_string = 'AffCalc-q340-Overtime'
            self.type_amount(
                id_string=id_string,
                amount=self.amount_overtime,
            )
            
        def earn_commission(self, sj, sub=False, column_index = 125):
            if sub: self.amount_commission = self.data[f'1{sj}_commission'].values[0]
            else: self.amount_commission = self.data[f'{column_index}{sj}_commission'].values[0]
            if sj == '_sj': id_string = 'AffCalc-q540-Commission'
            else: id_string = 'AffCalc-q350-Commission'
            self.type_amount(
                id_string=id_string,
                amount=self.amount_commission,
            )
            
        def how_often_bonus_paid(self, sj, sub=False, column_index = 125):
            if sub: column = f'1{sj}_how_often_bonus_paid'
            else: column = f'{column_index}{sj}_how_often_bonus_paid'
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
            
        def how_often_overtime_paid(self, sj, sub=False, column_index = 125):
            if sub: column = f'1{sj}_how_often_overtime_paid'
            else: column = f'{column_index}{sj}_how_often_overtime_paid'
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
            
        def how_often_commission_paid(self, sj, sub=False, column_index = 125):
            if sub: column = f'1{sj}_how_often_commission_paid'
            else: column = f'{column_index}{sj}_how_often_commission_paid'
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
    
    def open_calc(self, url=const.CALC_URL):
        """
        Opens the online afforability calculator by Nationwide building society.
        """
        self.get(url)
        
    def next(self, step):
        """
        Move on to the next step.
        """
        current_page = self.find_elements(By.CSS_SELECTOR, f'fieldset.Affordability-step.Affordability-step--{step}')[0]
        next_button = current_page.find_elements(By.CLASS_NAME, 'Affordability-nextStep')[0]
        next_button.click()

    def flow(self):
        """
        The order of navigation and action method. It will trigger the different predetermined paths corresponding to
        the options in the calculator.
        """

        # Open calculator
        self.open_calc()
        
        # Trigger step 1 chain of decisions
        self.step1()
        
        # Move to step 2
        self.next(step=0)
        
        # Trigger step 2 chain of decisions
        self.step2()
        
        # Move to step 3
        self.next(step=1)
        time.sleep(0.2) # Selenium needs to be slowed down a little here
        
        # Trigger step 3 chain of decisions
        self.step3()
        
        # Move to step 4
        self.next(step=2)
        
        # Trigger step 4 chain of decisions
        self.step4()
        
        # Move towards the finish
        self.next(step=3)
        
        # Get final result and store in the input table
        result = self.get_output()        
        self.df.loc[((self.df["name"] == self.name_of_client) & (self.df["surname"] == self.surname_of_client)), 'output_program'] = result
        self.df.loc[((self.df["name"] == self.name_of_client) & (self.df["surname"] == self.surname_of_client)), 'valid'] = (result == self.df.loc[((self.df["name"] == self.name_of_client) & (self.df["surname"] == self.surname_of_client)), 'output_manual'])
        self.df.to_csv('input/input.csv', index=False)
        
        self.quit()
        
    def step1(self):
        """
        Collection of input methods and decision-making corresponsing to Step 1 on the calculator.
        """
        
        # Close cookies and choose number of people borrowing
        self.step1_start()
        
        # What's the mortgage for?
        column = 'mortgage_purpose'
        purpose = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q10-ApplicationType-'
        self.select_option(
            css_string=css_string,
            no_options=3,
            prob_column=column,
            option=purpose,
        )
        if purpose == 0:
            self.step1_buy_new_property()
        elif purpose == 1:
            self.not_buying_new = True
            self.step1_remortgage_existing_property()
        else:
            self.not_buying_new = True
            self.step1_borrow_more()
            
        self.purpose = int(purpose)
            
    def step2(self):
        """
        Collection of input methods and decision-making corresponsing to Step 2 on the calculator.
        """
        
        # Ask for date of birth and status
        self.step2_start(purpose=self.purpose)
        
        # Does your client have financially dependent children or other people in their care?
        column = 'dependent_children'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q150-HaveDependents-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            self.step2_have_children()
        elif value == 1:
            pass
        
        # Is your client retired?
        column = 'retirement_status'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q170-IsCustomerRetired-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            self.retired = True
            pass
        elif value == 1:
            self.step2_client_is_not_retired()
            
    def step3(self):
        """
        Collection of input methods and decision-making corresponsing to Step 3 on the calculator.
        """
        
        if not self.retired:
            # Starting parameters for the first job
            id = 240
            no_options = 8
            column = 'employment_status'
            sj = '' # Indicator that we aren't looking at the second job
            for i in range(2):
                # How is your client employed?
                status = self.data[column].values[0]
                status_input_id = f'AffCalc-q{id}-EmploymentCategory'
                self.select_from_menu(
                    id_string=status_input_id,
                    no_options=no_options,
                    option=status,
                    prob_column=column,
                    plz_select=True,
                )
                if status == 1:
                    # Employed
                    self.step3_employed(sj=sj)
                elif status == 2:
                    # Self employed (partner)
                    self.step3_self_employed_partner(sj=sj)
                elif status == 3:
                    # Self employed (sole trader)
                    self.step3_self_employed_sole(sj=sj)
                elif status == 4:
                    # Director / Shareholder (20% or less)
                    self.step3_director_less_20(sj=sj)
                elif status == 5:
                    # Director / Shareholder (above 20%)
                    self.step3_director_more_20(sj=sj)
                elif status == 6 or status == 7 or status == 8:
                    # Homemaker / Student / Unemployed
                    break
                
                # Do they have a second job?
                column = '12345_second_job'
                value = self.data[column].values[0]
                css_string = 'label[for="AffCalc-q420-HasSecondJob-'
                self.select_option(
                    css_string=css_string,
                    no_options=2,
                    prob_column=column,
                    option=value,
                )
                if value == 0:
                    pass
                elif value == 1:
                    break
                
                # Reset parameters to fill information about the second job
                id = 430
                no_options = 5
                column = '1_employment_status'
                sj = '_sj'
                
        
        # Does your client have any other income?
        column = 'other_income'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q610-HasOtherIncome-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            self.step3_has_other_income()
        elif value == 1:
            pass
        
    def step4(self):
        """
        Collection of input methods and decision-making corresponsing to Step 4 on the calculator.
        """
        
        # Input all general outgoings and regular costs
        self.step4_start()
        
        # Does the first applicant have any other mortgages?
        column = 'other_mortgages'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q1540-HasExistingMortgages-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            # How many other mortgages does the first applicant have?
            column = '1_how_many'
            value = self.data[column].values[0]
            
            no_mortgages_input_id = 'AffCalc-q1570-NoOfExistingMortgages'
            self.select_from_menu(
                id_string=no_mortgages_input_id,
                no_options=6,
                option=value,
                prob_column=column,
                plz_select=False,
            )
            self.step4_applicant_has_other_mortgages(value=value)
        elif value == 1:
            pass
        
        if self.has_found_new_home or self.not_buying_new:
            # Council tax?
            amount = self.data['council_tax'].values[0]
            id_string = 'AffCalc-q1620-CouncilTax'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
            
            # Buildings insurance?
            amount = self.data['buildings_insurance'].values[0]
            id_string = 'AffCalc-q1630-BuildingInsurance'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
            
            # Service/Estate charges?
            amount = self.data['service_estate_charge'].values[0]
            id_string = 'AffCalc-q1640-ServiceCharge'
            self.type_amount(
                id_string=id_string,
                amount=amount,
            )
        