import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Level1():
    
    def __init__(self):
        pass
    
    def close_cookies(self):
        """
        Automatically accept all cookies.
        """
        WebDriverWait(self, 60).until(
            EC.presence_of_element_located(
                (By.ID, "onetrust-accept-btn-handler")
            )
        )
        acceptCookiesButton = self.find_element(By.ID, 'onetrust-accept-btn-handler')
        acceptCookiesButton.click()
        
    def select_option(self, css_string, no_options, prob_column, option=0,):
        """
        Selects an option from multiple choice menu. 

        Args:
            css_string (str): _description_
            no_options (int): _description_
            prob_column (str): _description_
            option (int, optional): _description_. Defaults to 0.

        Raises:
            ValueError: _description_
        """
        options_list = [i for i in range(no_options)]
        if int(option) not in options_list:
            # self.quit()
            raise ValueError(f'ERROR: You can only have either {options_list} options. Value given: {option} from {prob_column}')
        
        css_string = f'{css_string}{option}"]'    
        menu_option = self.find_elements(By.CSS_SELECTOR, css_string)        
        menu_option[0].click()
        
    def type_amount(self, id_string, amount):
        input_field = self.find_elements(By.ID, id_string)[0]
        
        amount = int(amount)
        input_field.clear()
        input_field.send_keys(amount)
        
    def select_from_menu(self, id_string, no_options, option, prob_column, plz_select = True,):
        options_list = [i+1 for i in range(no_options)]
        if int(option) not in options_list:
            # self.quit()
            raise ValueError(f'ERROR: You can only have either {options_list} options. Value given: {option} from {prob_column}.')
        
        option = int(option)
        select_element = self.find_elements(By.ID, id_string)[0]
        select = Select(select_element)
        select.select_by_index(option)
        
