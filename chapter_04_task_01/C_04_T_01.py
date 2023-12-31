def ispalindrome(tekst):
    """    
    Funkcja sprawdzająca palidromiczność tekstu
    """
    # Usuwamy białe znaki i zmieniamy tekst na małe litery
    tekst = tekst.replace(" ", "").lower()
    # Porównujemy tekst z odwróconym tekstem
    return tekst == tekst[::-1]

print(ispalindrome("potop"))  # True
print(ispalindrome("Python"))  # False
help(ispalindrome)