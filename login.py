class Login():

    def autenticacao_usuario(usu):
        usuario = 'admin'
        i = 0
        while i < len(usuario):
            if usuario[i] != usu[i]:
                return False
                break
            i += 1
        return True


    def autenticacao_senha(sen):
        senha = 'Python'
        i = 0
        while i < len(senha):
            if senha[i] != sen[i]:
                return False
                break
            
        return True
