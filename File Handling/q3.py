name = input("Enter the name: ")
phone = input("Enter the phone number: ")
email = input("Enter the email: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""

print(vcard_content)

with open("contact.vcf", "w") as file:
    file.write(vcard_content)

print("vCard file created successfully.")