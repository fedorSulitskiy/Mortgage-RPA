from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Operations():
    
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
            css_string (str): css identifier unique to the menu in question.
            no_options (int): number of options in the menu; useful for error message.
            prob_column (str): the column in the input table that is used by this method; useful for the error message.
            option (int, optional): index of menu option chosen. Defaults to 0.

        Raises:
            ValueError: error raised when input index is outside the range of the menu.
        """
        options_list = [i for i in range(no_options)]
        if int(option) not in options_list:
            # self.quit()
            raise ValueError(f'You can only have either {options_list} options. Value given: {option} from {prob_column}')
        
        option = int(option)
        css_string = f'{css_string}{option}"]'    
        menu_option = self.find_elements(By.CSS_SELECTOR, css_string)        
        menu_option[0].click()
        
    def type_amount(self, id_string, amount):
        """
        Input the amount of money asked by the calculator.

        Args:
            id_string (str): html id string identifying the text input field in question.
            amount (int): amount of money input into the text field
        """
        input_field = self.find_elements(By.ID, id_string)[0]
        
        amount = int(amount)
        input_field.clear()
        input_field.send_keys(amount)
        
    def select_from_menu(self, id_string, no_options, option, prob_column, plz_select = True,):
        """
        Selects an option from drop-down menu.

        Args:
            id_string (str): html id string identifying the drop-down menu in question.
            no_options (int): number of options in the menu; useful for error message.
            option (int): index of menu option chosen. Usually kept above 0 since at index 0 there is neutral "please select" option which disallows progression.
            prob_column (str): the column in the input table that is used by this method; useful for the error message.
            plz_select (bool, optional): TO DO MAYBE. Defaults to True.

        Raises:
            ValueError: error raised when input index is outside the range of the menu.
        """
        options_list = [i+1 for i in range(no_options)]
        if int(option) not in options_list:
            # self.quit()
            raise ValueError(f'You can only have either {options_list} options. Value given: {option} from {prob_column}.')
        
        option = int(option)
        select_element = self.find_elements(By.ID, id_string)[0]
        select = Select(select_element)
        select.select_by_index(option)
        
