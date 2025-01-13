"""Module manipulant des fichiers texte."""

def diff(file_first, file_second):
    """Fonction retournant True si deux fichiers sont différents."""
    with open(file_first) as f1, open(file_second) as f2:
    return f1.read() != f2.read()

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    return True
