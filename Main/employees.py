class Employee():
    '''
    main class for the waiters
    has two methods to calculate the total money an employee has earned
    in cash and in credit
    '''
    def __init__(self):
        self.cash_person = None
        self.credit_person = None
        self.hours = None

    def cal_cash(self, cash_per_hour):
        '''
        method to calculate total cash a waiter is making
        :param cash_per_hour: cash per hour that the waiters made in the shift
        :return: the total cash a specific waiter made
        '''
        self.cash_person = self.hours * cash_per_hour
        self.cash_person = round(self.cash_person, 1)
        return self.cash_person

    def cal_credit(self, credit_per_hour):
        '''
        method to calculate total credit money a waiter is making
        :param credit_per_hour: credit per hour that the waiters made in the shift
        :return: he total credit a specific waiter made
        '''
        self.credit_person = self.hours * credit_per_hour
        self.credit_person = round(self.credit_person, 2)
        return self.credit_person

class Waiter (Employee):
    def __init__(self,name,hours):
        self.name = name
        self.hours = hours
        self.cash_person = None
        self.credit_person = None

    def shiftinfo_worker(self):
        '''
        prints the shift's report of specific employee
        '''
        print("{} has worked {} hours in today's the shift".format(self.name,self.hours))
        print("{} has earned {} NIS in cash and {} NIS in credit card tip".format(self.name,self.cash_person,self.credit_person))

    def cal_own_money(self,cash_per_hour,credit_per_hour):
        '''
        method to calculate the money an employee have earned in today's shift
        on both cash and credit lanes
        activates both primal methods from Employee
        :return: total money a person made in shift
        '''
        self.cal_cash(cash_per_hour)
        self.cal_credit(credit_per_hour)
        return self.cash_person, self.credit_person

class Bartender():
    '''
    class for bartenders
    '''
    def __init__(self,name,hours):
        self.name = name
        self.cash_person = None
        self.hours = hours

    def cal_own_money(self,cash_bar,num):
        '''
        Method that calculates the provision the bartenders get from the shift
        takes in considerations the diffrence in bartenders number in shift
        :param cash_bar: the amount of money provised to the bar
        :param num: number of bartenders in today's shift
        :return: the amount of money a specific bartender has made in shift
        '''
        if num == 1:
            self.cash_person = cash_bar
        else:
            self.cash_person = cash_bar/num
        return self.cash_person

    def shiftinfo_worker(self):
        '''
        prints the shift's report for a bartender
        '''
        print("{} has earned {} NIS in cash while working at the bar".format(self.name,round(self.cash_person, 1)))
