from auto.indents.level3_paths import Level3Paths

class Level2Paths(Level3Paths):
    def __init__(self):
        super(Level2Paths, self).__init__()
    
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

    def step3_permanent(self, sj):
        
        # How long have they been in their job?
        term = self.data[f'1{sj}_no_years_on_job'].values[0].split(",")
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
        amount = self.data[f'125{sj}_salary_before_tax'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q510-GrossAnnualIncome'
        else: id_string = 'AffCalc-q320-GrossAnnualIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        # Do they earn any bonus?
        amount_bonus = self.data[f'125{sj}_bonus'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q520-Bonus'
        else: id_string = 'AffCalc-q330-Bonus'
        self.type_amount(
            id_string=id_string,
            amount=amount_bonus,
        )
        
        # Do they earn any overtime?
        amount_overtime = self.data[f'125{sj}_overtime'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q530-Overtime'
        else: id_string = 'AffCalc-q340-Overtime'
        self.type_amount(
            id_string=id_string,
            amount=amount_overtime,
        )
        
        # Do they earn any commission?
        amount_commission = self.data[f'125{sj}_commission'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q540-Commission'
        else: id_string = 'AffCalc-q350-Commission'
        self.type_amount(
            id_string=id_string,
            amount=amount_commission,
        )
            
        if amount_bonus > 0:
            # How often is the bonus paid?
            column = f'125{sj}_how_often_bonus_paid'
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
            column = f'125{sj}_how_often_overtime_paid'
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
            column = f'125{sj}_how_often_commission_paid'
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
    
    def step3_fixed_term_contract(self, sj, sub = False, fixed = True):
        
        # How long have they been in their job?
        if sub: term = self.data[f'12{sj}_time_on_job'].values[0].split(",")
        else: term = self.data[f'2{sj}_time_contracting'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q490-ContractYears'
            term_length_months = 'AffCalc-q490-ContractMonths'
        else:
            term_length_years = 'AffCalc-q300-ContractYears'
            term_length_months = 'AffCalc-q300-ContractMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        if fixed:
            # What's the remaining term on their contract?
            if sub: term = self.data[f'12{sj}_time_remaining'].values[0].split(",")
            else: term = self.data[f'2{sj}_time_remaining'].values[0].split(",")
            years = term[0]
            months = term[1]
            if sj == '_sj': 
                term_length_years = 'AffCalc-q500-ContractYears'
                term_length_months = 'AffCalc-q500-ContractMonths'
            else:
                term_length_years = 'AffCalc-q310-ContractYears'
                term_length_months = 'AffCalc-q310-ContractMonths'
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            ) 
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )
        
        # What's their salary before tax?
        if sub: amount = self.data[f'1{sj}_salary_before_tax'].values[0]
        else: amount = self.data[f'125{sj}_salary_before_tax'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q510-GrossAnnualIncome'
        else: id_string = 'AffCalc-q320-GrossAnnualIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        # Do they earn any bonus?
        if sub: amount_bonus = self.data[f'1{sj}_bonus'].values[0]
        else: amount_bonus = self.data[f'125{sj}_bonus'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q520-Bonus'
        else: id_string = 'AffCalc-q330-Bonus'
        self.type_amount(
            id_string=id_string,
            amount=amount_bonus,
        ) 
        
        # Do they earn any overtime?
        if sub: amount_overtime = self.data[f'1{sj}_overtime'].values[0]
        else: amount_overtime = self.data[f'125{sj}_overtime'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q530-Overtime'
        else: id_string = 'AffCalc-q340-Overtime'
        self.type_amount(
            id_string=id_string,
            amount=amount_overtime,
        ) 
        
        # Do they earn any commission?
        if sub: amount_commission = self.data[f'1{sj}_commission'].values[0]
        else: amount_commission = self.data[f'125{sj}_commission'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q540-Commission'
        else: id_string = 'AffCalc-q350-Commission'
        self.type_amount(
            id_string=id_string,
            amount=amount_commission,
        )
            
        if amount_bonus > 0:
            # How often is the bonus paid?
            if sub: column = f'1{sj}_how_often_bonus_paid'
            else: column = f'125{sj}_how_often_bonus_paid'
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
            if sub: column = f'1{sj}_how_often_overtime_paid'
            else: column = f'125{sj}_how_often_overtime_paid'
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
            if sub: column = f'1{sj}_how_often_commission_paid'
            else: column = f'125{sj}_how_often_commission_paid'
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
    
    def step3_sub_contract(self, sj, fixed):
        
        # Are they treated as employed for tax purposes?
        column = '34_employed_for_tax'
        value = self.data[column].values[0]
        css_string = 'label[for="AffCalc-q260-TreatedAsEmployedForTax-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            self.step3_fixed_term_contract(sj=sj, sub=True, fixed=fixed)
        elif value == 1:
            self.step3_are_not_employed_for_tax_purposes(sj=sj, sub=True, fixed=fixed)
    
    def step3_temporary(self, sj):
        
        # How long have they been in their job?
        term = self.data[f'5{sj}_time_in_regular_work'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q480-RegularYears'
            term_length_months = 'AffCalc-q480-RegularMonths'
        else:
            term_length_years = 'AffCalc-q290-RegularYears'
            term_length_months = 'AffCalc-q290-RegularMonths'
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        ) 
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )
        
        # What's their salary before tax?
        amount = self.data[f'125{sj}_salary_before_tax'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q510-GrossAnnualIncome'
        else: id_string = 'AffCalc-q320-GrossAnnualIncome'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        ) 
        
        # Do they earn any bonus?
        amount_bonus = self.data[f'125{sj}_bonus'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q520-Bonus'
        else: id_string = 'AffCalc-q330-Bonus'
        self.type_amount(
            id_string=id_string,
            amount=amount_bonus,
        )
        
        # Do they earn any overtime?
        amount_overtime = self.data[f'125{sj}_overtime'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q530-Overtime'
        else: id_string = 'AffCalc-q340-Overtime'
        self.type_amount(
            id_string=id_string,
            amount=amount_overtime,
        ) 
        
        # Do they earn any commission?
        amount_commission = self.data[f'125{sj}_commission'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q540-Commission'
        else: id_string = 'AffCalc-q350-Commission'
        self.type_amount(
            id_string=id_string,
            amount=amount_commission,
        )
            
        if amount_bonus > 0:
            # How often is the bonus paid?
            column = f'125{sj}_how_often_bonus_paid'
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
            column = f'125{sj}_how_often_overtime_paid'
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
            column = f'125{sj}_how_often_commission_paid'
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
  
    def step4_they_let_on_this_mortgate(self, i):
        # Is there a tenancy agreement in place?
        column = f'1_{i+1}_do_they_let'
        value = self.data[column].values[0]
        css_string = f'label[for="AffCalc-q1580-{i}-4-HasTenancyAgreement-'
        self.select_option(
            css_string=css_string,
            no_options=2,
            prob_column=column,
            option=value,
        )
        if value == 0:
            self.step4_tenancy_agreement_in_place(i=i)
        elif value == 1:
            pass