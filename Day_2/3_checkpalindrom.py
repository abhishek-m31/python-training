s = 'Was it a rat I saw'
revs = s[::-1]
print(s.lower())
print(revs.lower())

s =''.join([ch for ch in s if not ch.isspace()])
revs = ''.join([ch for ch in revs if not ch.isspace()])
if s.lower() == revs.lower():
    print("palindrome.")

