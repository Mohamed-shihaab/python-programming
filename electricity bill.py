service_number = input("Enter Service Number: ")
previous_month_reading = int(input("Enter Previous Month Reading: "))
current_month_reading = int(input("Enter Current Month Reading: "))
units_consumed = current_month_reading - previous_month_reading
electricity_charges = units_consumed * 1.50
print("------------------ELECTRICITY  BILL------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Enter service number                                   : ",service_number)
print("Enter previous month reading                 :",previous_month_reading)
print("Enter current month reading                    :",current_month_reading)
print("Units consumed                                              :",units_consumed)
print("Electricity charges in (rs)                            :",electricity_charges)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
