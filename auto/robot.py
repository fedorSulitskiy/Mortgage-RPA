from auto.indent.level_1 import Level1
import constants as const

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd


class Robot(webdriver.Chrome, Level1):
    """
    Robot class which will perform automated scraping.
    """
    def __init__(self, name, surname):
        # Set option for chrome to remain open after code stopped running.
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(Robot, self).__init__(options=chrome_options)

        # Initialize input data.
        df = pd.read_csv("input/input.csv")
        self.data = df.loc[((df["name"] == name) & (df["surname"] == surname))]

    def open_calc(self, url=const.CALC_URL):
        """
        Opens the online afforability calculator by Nationwide building society.
        """
        self.get(url)
        
    def next(self):
        """
        Move on to the next step.
        """
        next_button = self.find_elements(By.CLASS, 'Affordability-nextStep')
        next_button.click()

    def start(self):
        """
        Initialization method. It will trigger the different predetermined paths corresponding to
        the options in the calculator.
        """
        print("Let's Go!")

        self.open_calc()

        self.close_cookies()

        column = 'no_people_buying'
        no_people_buying = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q0-NumberOfApplicants-'
        self.select_option(
            css_string=css_string, 
            no_options=2, 
            prob_column=column,
            option=no_people_buying,
        )
        
        column = 'mortgage_purpose'
        purpose = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q10-ApplicationType-'
        self.select_option(
            css_string=css_string,
            no_options=3,
            prob_column=column,
            option=purpose,
        )
        
        amount = self.data['123_amount_borrowed'].values[0]
        borrowing_amount_input = 'AffCalc-q20-BorrowingAmount'
        self.type_amount(
            id_string=borrowing_amount_input,
            amount=amount,
        )
        
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
        
        column = '12_ownership_type'
        ownership_type_input = 'AffCalc-q40-OwnershipType'
        purpose = self.data[column].values[0]
        self.select_from_menu(
            id_string=ownership_type_input,
            no_options=5,
            option=purpose,
            prob_column=column,
            plz_select=True,
        )
        
        column = '1_found_new_home'
        has_found_new_home = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q60-PropertyFound-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=has_found_new_home,
        )
        
        column = '123_is_in_scotland'
        is_it_in_scotland = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q135-RegionCode-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=is_it_in_scotland,
        )
        
        amount = self.data['1_purchase_price'].values[0]
        borrowing_amount_input = 'AffCalc-q90-PurchasePrice'
        self.type_amount(
            id_string=borrowing_amount_input,
            amount=amount,
        )
        
        self.next()
        
        
        

