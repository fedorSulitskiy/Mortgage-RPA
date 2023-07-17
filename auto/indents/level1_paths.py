from auto.indents.level2_paths import Level2Paths

class Level1Paths(Level2Paths):
    def __init__(self):
        pass
    
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
