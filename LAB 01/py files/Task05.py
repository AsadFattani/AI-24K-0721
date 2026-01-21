
def fun ():
    str = input("Enter a string: ")
    totalchar = len(str)
    totalupper = len([c for c in str if c.isupper()])
    totallower = len([c for c in str if c.islower()])
    totaldigit = len([c for c in str if c.isdigit()])

    dict = {
        "Total Characters": totalchar,
        "Total Uppercase Letters": totalupper,
        "Total Lowercase Letters": totallower,
        "Total Digits": totaldigit
    }
    return dict

dict = fun()
print("\nString Analysis:")
for key in dict:
    print(f"    {key}: {dict[key]}")
