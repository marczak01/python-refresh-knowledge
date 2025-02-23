def validate_email(email):
    print(email)
    if email.find("@"):
        monkeyIndex = email.index("@")
        print(f"index ' @ ' : {monkeyIndex}")
        if email[monkeyIndex:].find("."):
            print(f"indeks ' . ' po @ : {email[monkeyIndex:].index(".") + monkeyIndex}")

validate_email('madasd.m@o2.pl')
validate_email('marczak01@icloud.com')