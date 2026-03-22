import re

# 1. Define your security policy as a dictionary
SECURITY_POLICY = {
    "PermitRootLogin": "no",
    "PasswordAuthentication": "no",
    "X11Forwarding": "no"
}

def parse_config(file_path):
    """Reads a file and returns a dictionary of key-value pairs."""
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignore comments and empty lines
                if line.startswith('#') or not line.strip():
                    continue
                # Split key and value by whitespace
                parts = line.split()
                if len(parts) >= 2:
                    config_data[parts[0]] = parts[1]
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
        return None
    return config_data

def run_compliance_check(file_path, policy):
    """Compares actual config against the security policy."""
    actual_config = parse_config(file_path)
    
    if actual_config is None:
        return

    print(f"--- Compliance Report for {file_path} ---")
    compliant = True
    
    for key, expected_value in policy.items():
        actual_value = actual_config.get(key)
        
        if actual_value == expected_value:
            print(f"[PASS] {key} is set to {expected_value}")
        else:
            print(f"[FAIL] {key} is '{actual_value}'! Expected: '{expected_value}'")
            compliant = False
            
    if compliant:
        print("\nStatus: System is fully compliant.")
    else:
        print("\nStatus: Non-compliant configuration detected.")

# Execute the check
if __name__ == "__main__":
    # Point this to your test SSH config
    run_compliance_check("/etc/ssh/sshd_config", SECURITY_POLICY)
