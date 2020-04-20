import datetime
def intro():
    '''
    introduction func
    '''
    print ("Hello Petelina employee !")
    print("This is a simple calculator to help you calculate how much have the waiters and the bartenders have earned in today's shift")

def waiters_input(list):
    '''
    takes data on each waiter that have worked in today's shift
    intakes the name of the waiter and the amount of hours he worked
    :param list: list contains raw data on all the shift's employees
        (shoud be empty)
    :return: list containning raw data of all the waiters
    '''
    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    i = 0
    print("Lets Collect the data of the waiters!")
    num = int(input("How many waiters have worked in today's shift ? "))
    for n in range(num):
        i += 1
        name = input("Whats the name of the {} one ? ".format([ordinal(n) for n in range(10)][i]))
        h = float(input("And how many hours has {} worked ? ".format(name)))
        person = (name,h)
        list.append(person)
    return list

def bartenders_input(list):
    '''
    Func takes raw data on bartenders in shift
    :param list: list contains raw data on all the shift's employees
        (has the raw data of the waiters)
    :return: list containning raw data of all the waiters
    '''
    print("Now we'll collect the bartenders data")
    num = int(input("How many bartenders have workes in today's shift? "))
    if num > 1:
        ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
        i = 0
        for m in range (num):
            i += 1
            name = input("Whats the name of the {} bartender? ".format([ordinal(n) for n in range(4)][i]))
            person = (name,0)
            list.append(person)
    else:
        name = input("Whats the name of the bartender? ")
        list.append((name,0))
    return list

def cal_money_emp(list,cash_per_hour,credit_per_hour,cash_bar,num):
    '''
    Func calculates the total money a specific employee has made in shift
    according to its kind (Waiter\Bartender)
    :param list: list of all employees in shift
    :param cash_per_hour: cash per hour made in today's shift
    :param credit_per_hour: credit per hour made in today's shift
    :param cash_bar: amount of money provised to bartenders
    :param num: number of bartenders in today's shift
    :return: list of employees after each one inherited the money he made in shift
    '''
    for person in list:
        if person.hours > 0:
            person.cal_own_money(cash_per_hour,credit_per_hour)
        else:
            person.cal_own_money(cash_bar,num)
    return list

def shift_report(list,cash_per_hour,credit_per_hour):
    '''
    prints todays report
    prints each employee report for the shift
    :param list: list of employees
    :param cash_per_hour: cash per hour in shift
    :param credit_per_hour: credit per hour in shift
    '''
    print("This is the shift's report: ")
    print("In the {} shift of {}".format(time_ditermin() ,datetime.date.today()))
    print("The Waiters have earned {} NIS cash per hour and {} NIS in credit card per hour".format(round(cash_per_hour,2),round(credit_per_hour, 2)))
    for person in list:
        person.shiftinfo_worker()

def add_hour(list, num):
    '''
    Func adds all the hours the waiters have worked in order to calculate per hour
    :param list: list of employees
    :param num: the total amount of hours in shift (should be 0)
    :return: the total hours all waiters have worked
    '''
    for person in list:
        num = num + person.hours
    return num

def time_ditermin():
    '''
    func detrmined whether its a morning or evening shift
    '''
    if datetime.datetime.now().time().hour > 22:
        return "evening"
    else:
        return "morning"



