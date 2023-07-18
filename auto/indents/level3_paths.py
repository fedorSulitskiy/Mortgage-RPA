from auto.opps import Operations

class Level3Paths(Operations):
    def __init__(self):
        pass
    
    def step3_are_not_employed_for_tax_purposes(self, sj, sub, fixed):
        
        # How long have they been in their job?
        if sub: term = self.data[f'12{sj}_time_on_job'].values[0].split(",")
        else: term = self.data[f'2{sj}_time_contracting'].values[0].split(",")
        years = term[0]
        months = term[1]
        if sj == '_sj': 
            term_length_years = 'AffCalc-q300-ContractYears'
            term_length_months = 'AffCalc-q300-ContractMonths'
        else:
            term_length_years = 'AffCalc-q490-ContractYears'
            term_length_months = 'AffCalc-q490-ContractMonths'
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
                term_length_years = 'AffCalc-q310-ContractYears'
                term_length_months = 'AffCalc-q310-ContractMonths'
            else:
                term_length_years = 'AffCalc-q500-ContractYears'
                term_length_months = 'AffCalc-q500-ContractMonths'
            self.type_amount(
                id_string=term_length_years,
                amount=years,
            ) 
            self.type_amount(
                id_string=term_length_months,
                amount=months,
            )
        
        # What's their net profit, before tax, for the latest period?
        amount = self.data[f'2{sj}_net_profit_latest'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q550-LatestPeriodProfit'
        else: id_string = 'AffCalc-q360-LatestPeriodProfit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        
        # What's their net profit, before tax, for the previous period?
        amount = self.data[f'2{sj}_net_profit_previous'].values[0]
        if sj == '_sj': id_string = 'AffCalc-q560-PreviousPeriodProfitn'
        else: id_string = 'AffCalc-q370-PreviousPeriodProfit'
        self.type_amount(
            id_string=id_string,
            amount=amount,
        )
        