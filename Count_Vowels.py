s=input("Enter you word:")
vowels = "aeiou"
count = sum(1 for i in s if i in vowels)
print("Vowel count:", count)
