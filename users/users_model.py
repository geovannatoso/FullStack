users_db = []
contador_id = 1

def listar_users():
    return users_db

def user_por_id(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
        return None
    
def adicionar_user(novos_dados):
    global contador_id
    novo_user = {
        "id": contador_id,
        "nome": novos_dados["nome"],
        "email": novos_dados["email"]
    }
    users_db.append(novo_user)
    contador_id += 1
    return novo_user

def atualizar_user(user_id,novos_dados):
    for user in users_db:
        if user["id"] == user_id:
            user["nome"] = novos_dados("nome", user["nome"])
            user["email"] = novos_dados("email", user["email"])
            return user
    return None

def excluir_user(user_id):
    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return True
        return False