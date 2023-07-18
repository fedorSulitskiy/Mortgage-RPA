from auto.indents.level3_paths import Level3Paths


class Level2Paths(Level3Paths):
    """
    Second layer of input and decision methods.

    Args:
        Level3Paths (class): Third layer of input and decision methods.
    """

    def __init__(self):
        super(Level2Paths, self).__init__()

    def step1_standart_ownership_type(self, new):
        if new:
            # What's the purchase price?
            self.step1_common.purchase_price(self, input_field_index=90)
        else:
            #  What's the current estimated value?
            self.step1_common.current_estimated_value(self)

    def step1_shared_equity(self, new):
        # What's the full market value of the property?
        self.step1_common.full_market_value(self)

        if new:
            # What's the purchase price of their share? (This will be the deposit and mortgage combined)
            self.step1_common.purchase_price(self)
        else:
            # What will be the etimated value of their share at completion?
            self.step1_common.current_estimated_value(
                self, input_field_id="AffCalc-q130-CurrentEstimatedValueShare"
            )

    def step1_right_to_buy(self, new):
        # What's the full market value of the property?
        self.step1_common.full_market_value(self)

        if new:
            # What's the discounted purchase price?
            self.step1_common.purchase_price(self, input_field_index=110)
        else:
            # What's the current estimated value?
            self.step1_common.current_estimated_value(self)

    def step1_shared_ownership(self, new):
        # What's the full market value of the property?
        self.step1_common.full_market_value(self)

        if new:
            # What's the purchase price of their share? (This will be the deposit and mortgage combined)
            self.step1_common.purchase_price(self)
        else:
            # What will be the etimated value of their share at completion?
            self.step1_common.current_estimated_value(
                self, input_field_id="AffCalc-q130-CurrentEstimatedValueShare"
            )

    def step1_new_home_found(self):
        # What's the property's legal status?
        self.step1_common.property_legal_status(self, column="1_legal_status")

        # What sort of property is it?
        self.step1_common.what_sort_is_this_property(self, column="1_what_sort")

    def step1_existing_mortgage_term(self):
        # What is your client's existing mortgage term?
        term = self.data["2_existing_term"].values[0].split(",")
        years = term[0]
        months = term[1]
        term_length_years = "AffCalc-q44-ExistingMortgageTermYears"
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        term_length_months = "AffCalc-q44-ExistingMortgageTermMonths"
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )

    def step3_permanent(self, sj):
        # How long have they been in their job?
        term = self.data[f"1{sj}_no_years_on_job"].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == "_sj":
            term_length_years = "AffCalc-q460-JobYears"
            term_length_months = "AffCalc-q460-JobMonths"
        else:
            term_length_years = "AffCalc-q270-JobYears"
            term_length_months = "AffCalc-q270-JobMonths"
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )

        # What's their salary before tax?
        self.step3_common.salary_before_tax(self, sj=sj)

        # Do they earn any bonus?
        self.step3_common.earn_bonus(self, sj=sj)

        # Do they earn any overtime?
        self.step3_common.earn_overtime(self, sj=sj)

        # Do they earn any commission?
        self.step3_common.earn_commission(self, sj=sj)

        if self.amount_bonus > 0:
            # How often is the bonus paid?
            self.step3_common.how_often_bonus_paid(self, sj=sj)

        if self.amount_overtime > 0:
            # How often is the overtime paid?
            self.step3_common.how_often_overtime_paid(self, sj=sj)

        if self.amount_commission > 0:
            # How often is the commision paid?
            self.step3_common.how_often_commission_paid(self, sj=sj)

    def step3_fixed_term_contract(self, sj, sub=False, fixed=True):
        # How long have they been in their job?
        if sub:
            term = self.data[f"12{sj}_time_on_job"].values[0].split(",")
        else:
            term = self.data[f"2{sj}_time_contracting"].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == "_sj":
            term_length_years = "AffCalc-q490-ContractYears"
            term_length_months = "AffCalc-q490-ContractMonths"
        else:
            term_length_years = "AffCalc-q300-ContractYears"
            term_length_months = "AffCalc-q300-ContractMonths"
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
            if sub:
                term = self.data[f"12{sj}_time_remaining"].values[0].split(",")
            else:
                term = self.data[f"2{sj}_time_remaining"].values[0].split(",")
            years = term[0]
            months = term[1]
            if sj == "_sj":
                term_length_years = "AffCalc-q500-ContractYears"
                term_length_months = "AffCalc-q500-ContractMonths"
            else:
                term_length_years = "AffCalc-q310-ContractYears"
                term_length_months = "AffCalc-q310-ContractMonths"
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            )
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )

        # What's their salary before tax?
        self.step3_common.salary_before_tax(self, sj=sj, sub=sub)

        # Do they earn any bonus?
        self.step3_common.earn_bonus(self, sj=sj, sub=sub)

        # Do they earn any overtime?
        self.step3_common.earn_overtime(self, sj=sj, sub=sub)

        # Do they earn any commission?
        self.step3_common.earn_commission(self, sj=sj, sub=sub)

        if self.amount_bonus > 0:
            # How often is the bonus paid?
            self.step3_common.how_often_bonus_paid(self, sj=sj, sub=sub)

        if self.amount_overtime > 0:
            # How often is the overtime paid?
            self.step3_common.how_often_overtime_paid(self, sj=sj, sub=sub)

        if self.amount_commission > 0:
            # How often is the commision paid?
            self.step3_common.how_often_commission_paid(self, sj=sj, sub=sub)

    def step3_sub_contract(self, sj, fixed):
        # Are they treated as employed for tax purposes?
        column = "34_employed_for_tax"
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
        term = self.data[f"5{sj}_time_in_regular_work"].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == "_sj":
            term_length_years = "AffCalc-q480-RegularYears"
            term_length_months = "AffCalc-q480-RegularMonths"
        else:
            term_length_years = "AffCalc-q290-RegularYears"
            term_length_months = "AffCalc-q290-RegularMonths"
        self.type_amount(
            id_string=term_length_years,
            amount=years,
        )
        self.type_amount(
            id_string=term_length_months,
            amount=months,
        )

        # What's their salary before tax?
        self.step3_common.salary_before_tax(self, sj=sj)

        # Do they earn any bonus?
        self.step3_common.earn_bonus(self, sj=sj)

        # Do they earn any overtime?
        self.step3_common.earn_overtime(self, sj=sj)

        # Do they earn any commission?
        self.step3_common.earn_commission(self, sj=sj)

        if self.amount_bonus > 0:
            # How often is the bonus paid?
            self.step3_common.how_often_bonus_paid(self, sj=sj)

        if self.amount_overtime > 0:
            # How often is the overtime paid?
            self.step3_common.how_often_overtime_paid(self, sj=sj)

        if self.amount_commission > 0:
            # How often is the commision paid?
            self.step3_common.how_often_commission_paid(self, sj=sj)

    def step4_they_let_on_this_mortgate(self, i):
        # Is there a tenancy agreement in place?
        column = f"1_{i+1}_do_they_let"
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
