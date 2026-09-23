email = "support@paymentgateway.com"

at_position = email.find("@")

if at_position != -1:
    domain = email[at_position + 1:]
    print(f"Domain Name: {domain}")
else:
    print("Invalid Email Format")
