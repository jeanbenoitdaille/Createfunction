    def get_value(dictionnaire, *args):
        args = list(args)
        default = args.pop(-1)
     
        for arg in args:
            dictionnaire = dictionnaire.get(arg)
            if not dictionnaire:
                return default
     
        return dictionnaire
     
    d = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
    a = get_value(d, "02", "identite", "nom", "valeur inconnue")
    print(a)
