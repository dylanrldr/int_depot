"""Module manipulant des fichiers texte."""

def diff(file_first, file_second):
    """Fonction retournant True si deux fichiers sont différents."""
    with open(file_first, 'r', encoding='utf-8') as f1, open(file_second, 'r', encoding='utf_8') as f2:
		return f1.read() != f2.read()

def same(file_first, file_second):
    """Fonction retournant True si deux fichiers sont identiques."""
    
    return not diff(file_first, file_second)
