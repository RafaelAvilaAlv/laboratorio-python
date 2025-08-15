# Importación absoluta del paquete y/o de su API pública
from textkit import normalize, is_palindrome, token_count
import textkit.clean as clean          # absoluto (paquete.modulo)
import textkit.metrics as metrics      # absoluto (paquete.modulo)

def demo():
    s = "  ÁrBoL   Ñandú  "
    print("normalize:", normalize(s))                   # desde __init__.py
    print("squeeze_spaces:", clean.squeeze_spaces(s))   # absoluto a clean.py
    print("is_palindrome('Anita lava la tina'):", metrics.is_palindrome("Anita lava la tina"))
    print("token_count('hola   mundo  cruel'):", token_count("hola   mundo  cruel"))

if __name__ == "__main__":
    demo()
