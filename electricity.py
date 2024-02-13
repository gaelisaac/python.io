#bill calculator
def kplc(customer_id,customer_name,units):
    if units >=199:
        charge=1.2*units 
    elif units >=200 and units <=400: 
        charge = units *1.8
    elif units >=400 and units <=600: 
        charge = units *2
        return charge
    customer_id=int(input("enter the id of thecustomer"))
    customer_name=int(input("enter the name of thecustomer"))
    units_consumed=int(input("enter the units"))
    print(kplc(customer_id,customer_name,units_consumed))
        
