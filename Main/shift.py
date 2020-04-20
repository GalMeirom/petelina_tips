class Shift():
    '''
    class for the shift itself
    '''
    def __init__(self):
        self.shift_cash = None
        self.shift_credit = None
        self.cash_waiters = None
        self.total_hours = 0
        self.credit_per_hour = None
        self.cash_per_hour = None
        self.cash_bar = None

    def cal_credit_per_hour(self):
        '''
        method calculates the credit per hour the waiters have earned
        :return: credit per hour for the shift
        '''
        self.credit_per_hour = float(self.shift_credit / self.total_hours)
        return self.credit_per_hour

    def bar_provision(self,num):
        '''
        Method that provise money to the bartenders according to the number
        of bartenders that have worked in shift
        also calculates accordingly the cash money that the waiters have made
        :param num: number of bartenders
        :return: the anmount of provised money to the bar, total cash money the waiters made
        '''
        if num > 1:
            self.cash_bar = (self.shift_cash + (self.shift_credit * 0.8)) * 0.1
            self.cash_waiters = self.shift_cash - self.cash_bar
        else:
            self.cash_bar = (self.shift_cash + (self.shift_credit * 0.8)) * 0.08
            self.cash_waiters = self.shift_cash - self.cash_bar
        return self.cash_bar, self.cash_waiters

    def cal_cash_per_hour(self):
        '''
        method calculates cash per hour for waiters in today's shift
        :return: cash per hour in shift
        '''
        self.cash_per_hour = self.cash_waiters / self.total_hours
        return self.cash_per_hour

    def cal_per_hours(self):
        '''
        calculates both cash per hour and credit per hour for the waiters in shift
        :return: cash and credit per hour
        '''
        self.cal_credit_per_hour()
        self.cal_cash_per_hour()
        return self.credit_per_hour, self.cash_per_hour

    def shift_input(self):
        '''
        Method that collects the Data on the shit
        intakes the money and the credit the intire staff have made in shift
        :return: cash earned in shift, credit earned in shift
        '''
        print("lets start collecting data to help you!")
        self.shift_cash = int(input("Firstly, How much cash money have you guys earned in today's shift ? "))
        self.shift_credit = float(input("Secondly, How much tip have you guys earned in today's shift on credit card ? "))
        print("Thank you for the information on the shift !")
        return self.shift_cash, self.shift_credit
