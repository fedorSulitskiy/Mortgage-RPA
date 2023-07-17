import constants as const
from auto.indents.level1_paths import Level1Paths

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd

class Robot(webdriver.Chrome, Level1Paths):
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
        next_button = self.find_elements(By.CLASS_NAME, 'Affordability-nextStep')[0]
        next_button.click()

    def start(self):
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
        self.next()
        
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

    
        
        
        

