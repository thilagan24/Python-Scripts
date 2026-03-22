
file_path="/Users/thilak/Documents/Thilak/Samplesshdconf" #custom path. edit per requirement.

policy = {"PermitRootLogin":"no","PasswordAuthentication":"no"} #custom policy. edit per requirement.


def parse_config(file_path):

    #parsing or making ready key-value pair info for checking
    
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignore comments and empty lines
                # boolean output of line.strip is flase is empty
                # so put not before it to make true for skipping

                if line.startswith('#') or not line.strip():
                    continue
                # Split key and value by whitespace
                parts = line.split()
                if len(parts) >= 2:
                    config_data[parts[0]] = parts[1]
        print(config_data)
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
        return None
    return config_data

parse_config("/Users/thilak/Documents/Thilak/Samplesshdconf")


def run_check(file_path, policy):

    

    config_data = parse_config(file_path)

    print(f" the compliance report is for path {file_path}")

    #actual_value
    #expected_value

    #getting keyvalues from a dictionary

    


    for key, expected_value in policy.items():

        actual_value=config_data.get(key)

        if actual_value == expected_value:

            print("Compliant, no changed required")

        else:

            print("Non-Compliant")


run_check(file_path, policy)
