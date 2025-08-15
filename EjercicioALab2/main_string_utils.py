# main_string_utils.py
from string_utils import normalize, is_palindrome, title_case, safe_truncate

def demo():
    print("== normalize ==")
    print(normalize("  ÁrBoL Ñandú  "))     # "arbol nandu"
    print(normalize("  Hola  ", to_lower=False))  # "Hola"

    print("\n== is_palindrome ==")
    print(is_palindrome("Anita lava la tina"))    # True
    print(is_palindrome("Python"))               # False

    print("\n== title_case ==")
    print(title_case("  juan de la cruz  "))      # "Juan de la Cruz"
    print(title_case("maria del rosario"))        # "Maria del Rosario"

    print("\n== safe_truncate ==")
    print(safe_truncate("Este es un mensaje muy largo", 15))  # "Este es un me…"

    print("\n== caso límite (error controlado) ==")
    try:
        # ERROR esperado: max_len <= len(ellipsis)
        safe_truncate("Hola", 1, ellipsis="…")
    except ValueError as e:
        print("OK, error controlado:", e)

if __name__ == "__main__":
    demo()
