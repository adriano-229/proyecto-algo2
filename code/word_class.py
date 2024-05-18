lista_descartes = [
    # pronombres
    {
        'esa', 'algunos', 'esos', 'les', 'ninguno', 'varios', 'algunas', 'sus', 'alguien', 'estos', 'tu', 'otras',
        'aquella', 'otros', 'la', 'esas', 'quién', 'alguna', 'ella', 'eso', 'vuestra', 'cuántas', 'estas', 'algo',
        'ellas', 'quiénes', 'aquello', 'nuestros', 'le', 'vuestro', 'aquellos', 'tus', 'cuánto', 'aquel', 'quien',
        'cuyas', 'esta', 'ellos', 'os', 'qué', 'nuestro', 'ninguna', 'este', 'él', 'aquellas', 'mi', 'que', 'nuestra',
        'cuántos', 'me', 'nuestras', 'ningunas', 'las', 'alguno', 'yo', 'vosotros', 'los', 'lo', 'tú', 'cuyo', 'su',
        'vuestros', 'varias', 'ese', 'ningunos', 'te', 'cuya', 'cuánta', 'vuestras', 'cuál', 'nosotros', 'mis', 'esto',
        'nos', 'quienes', 'cuáles', 'cuyos'
    },

    # preposiciones
    {
        "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta",
        "mediante", "para", "por", "según", "sin", "sobre", "tras", "versus", "vía"
    },

    # conjunciones
    {
        'mientras', 'entonces', 'también', 'o', 'sino', 'además', 'cuando', 'pero', 'así que', 'por otro lado',
        'sin embargo', 'asimismo', 'si', 'porque', 'no obstante', 'aun cuando', 'ya que', 'si bien', 'a pesar de',
        'por el contrario', 'a la vez', 'así', 'en cambio', 'aun', 'aunque', 'y', 'incluso', 'por lo tanto', 'luego',
        'por tanto', 'después', 'antes'
    },

    # articulos
    {
        "del", "el", "la", "los", "las", "un", "una", "unos", "unas"
    }
]

cambios = {'-': '', '¡': '', '!': '', '¿': '', '?': '', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
prefixs = {'re', 'sobre', 'sub', 'tele', 'tras', 'trans', 'ante', 'ex', 'post', 'inter', 'des', 'vice', 'semi'}
suffixs = {'ismo': '', 'is':'i','os':'o','as':'a','es':'e', 'us': 's'}

def clean_prefix(w):
    for sym in prefixs:
        if len(w) - len(sym) > len(w)//2:
            w = w.removeprefix(sym)
    return w

def clean_suffix(w):
    for sym, rpl in suffixs:
        if len(w) - len(sym) > len(w)//2:
            w = w.replace(sym,rpl)
    return w


def clean(word):
    for sym, rpl in cambios.items():
        word = word.replace(sym, rpl)
        try:
            if int(word) not in range(1000, 3001):
                return None
        except:
            pass
    return word


def make_descartes_set():
    sin_repetidos = set()
    for conjuntos in lista_descartes:
        for item in conjuntos:
            palabras = item.split(' ')
            for pal in palabras:
                pal = clean(pal)
                sin_repetidos.add(pal)
    return sin_repetidos


descartes = make_descartes_set()
print(clean_prefix("recondito"))
