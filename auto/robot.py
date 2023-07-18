import constants as const
from auto.indents.level1_paths import Level1Paths

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import time

class Robot(webdriver.Chrome, Level1Paths):
    """
    Robot class which will perform automated scraping.
    """
    def __init__(self, name, surname):
        # Persistent data
        self.purpose = 0
        self.retired = False
        self.name_of_client = name
        self.surname_of_client = surname
        
        # Set option for chrome to remain open after code stopped running.
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(Robot, self).__init__(options=chrome_options)
        self.implicitly_wait(5)

        # Initialize input data.
        self.df = pd.read_csv("input/input.csv")
        self.data = self.df.loc[((self.df["name"] == name) & (self.df["surname"] == surname))]

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
        print(next_button)
        next_button.click()

    def flow(self):
        """
        Initialization method. It will trigger the different predetermined paths corresponding to
        the options in the calculator.
        """
        print("Let's Go!")

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
        self.df.to_csv('output/output.csv')
        
        self.quit()
        print('GREAT SUCCESS!!!')
        
    def step1(self):
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
            self.step1_remortgage_existing_property()
        else:
            self.step1_borrow_more()
            
        self.purpose = int(purpose)
            
    def step2(self):
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
        