import re

def remove_leading_zeros(ip_address):
    # Define a regex pattern to match and remove leading zeros in each octet
    pattern = r'(\b0+)([1-9]+\d*)'
    
    # Use re.sub to remove leading zeros from each octet
    modified_ip = re.sub(pattern, r'\2', ip_address)
    
    return modified_ip

# Input IP address with leading zeros
input_ip = "192.012.001.001"

# Call the function to remove leading zeros
result_ip = remove_leading_zeros(input_ip)

# Print the modified IP address
print("Original IP:", input_ip)
print("Modified IP:", result_ip)
