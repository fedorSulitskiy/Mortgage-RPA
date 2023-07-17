from auto.opps import Operations

class Level2Paths(Operations):
    def __init__(self):
        pass
    
    def step1_standart_ownership_type(self, new):
        
        if new:
            # What's the purchase price?
            amount = self.data['1_purchase_price'].values[0]
            borrowing_amount_input = 'AffCalc-q90-PurchasePrice'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        else:
            #  What's the current estimated value?
            amount = self.data['23_estimate_value'].values[0]
            borrowing_amount_input = 'AffCalc-q120-CurrentEstimatedValue'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        
    def step1_shared_equity(self, new):
        
        # What's the full market value of the property?
        amount = self.data['234_market_value'].values[0]
        id_string = 'AffCalc-q50-MarketValue'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        if new:
            # What's the purchase price of their share? (This will be the deposit and mortgage combined)
            amount = self.data['1_purchase_price'].values[0]
            borrowing_amount_input = 'AffCalc-q100-PurchasePrice'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        else:
            # What will be the etimated value of their share at completion?
            amount = self.data['23_estimate_value'].values[0]
            borrowing_amount_input = 'AffCalc-q130-CurrentEstimatedValueShare'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
    
    def step1_right_to_buy(self, new):
        
        # What's the full market value of the property?
        amount = self.data['234_market_value'].values[0]
        id_string = 'AffCalc-q50-MarketValue'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        if new:
            # What's the discounted purchase price?
            amount = self.data['1_purchase_price'].values[0]
            borrowing_amount_input = 'AffCalc-q110-PurchasePrice'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        else:
            # What's the current estimated value?
            amount = self.data['23_estimate_value'].values[0]
            borrowing_amount_input = 'AffCalc-q120-CurrentEstimatedValue'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
    
    def step1_shared_ownership(self, new):
        
        # What's the full market value of the property?
        amount = self.data['234_market_value'].values[0]
        id_string = 'AffCalc-q50-MarketValue'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        if new:
            # What's the purchase price of their share? (This will be the deposit and mortgage combined)
            amount = self.data['1_purchase_price'].values[0]
            borrowing_amount_input = 'AffCalc-q100-PurchasePrice'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        else:
            # What will be the etimated value of their share at completion?
            amount = self.data['23_estimate_value'].values[0]
            borrowing_amount_input = 'AffCalc-q130-CurrentEstimatedValueShare'
            self.type_amount(
                id_string=borrowing_amount_input,
                amount=amount,
            )
        
    def step1_new_home_found(self):
        
        # What's the property's legal status?
        column = '1_legal_status'
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
        column = '1_what_sort'
        value = self.data[column].values[0]
        id_string = 'AffCalc-q80-PropertyType'
        self.select_from_menu(
            id_string=id_string,
            no_options=8,
            option=value,
            prob_column=column,
            plz_select=True,
        )
        
    def step1_existing_mortgage_term(self):
        
        # What is your client's existing mortgage term?
        term = self.data['2_existing_term'].values[0].split(",")
        years = term[0]
        months = term[1]
        term_length_years = 'AffCalc-q44-ExistingMortgageTermYears'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        term_length_months = 'AffCalc-q44-ExistingMortgageTermMonths'
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        