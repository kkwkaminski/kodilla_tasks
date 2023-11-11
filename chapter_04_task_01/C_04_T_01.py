def ispalindrome(tekst):
    # Usuwamy białe znaki i zmieniamy tekst na małe litery
    tekst = tekst.replace(" ", "").lower()
    # Porównujemy tekst z odwróconym tekstem
    return tekst == tekst[::-1]

