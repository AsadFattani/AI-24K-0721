username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))

userData = {
    "Username": username,
    "Password": password,
    "Age": age
}

print("\nUser Data:")
for key in userData:
    print(f"    {key}: {userData[key]}")


if age < 13:
    print("\nUnderage! Account creation not possible")
else:
    print("\nAccount created successfully!")

