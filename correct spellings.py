from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a word: ")
if word in corrector:
    print("No spelling error")
else: 
    corrected_word = corrector.correction(word)
    print("Correction spelling is ", corrected_word)