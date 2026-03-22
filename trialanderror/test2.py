#part2
#comparison


file_path="/Users/thilak/Documents/Thilak/Samplesshdconf"


print(f" the compliance report is for path {file_path}")

#actual_value
#expected_value

#getting keyvalues from a dictionary

policy = {"PermitRootLogin":"no","PasswordAuthentication":"no"}


for key, expected_value in policy.items():

    actual_value=config_data.get(key)

    if actual_value == expected_value:

        print("Compliant, no changed required")

    else:

        print("Non-Compliant")

        

    




