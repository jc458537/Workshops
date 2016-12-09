__author__ = 'jc458537'
def tax_return(income):
    if income <= 16000:
        return 0
    else:
        return (income - 16000) * 0.3



