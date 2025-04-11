from banco import criar_tabelas
from crud import adicionar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

criar_tabelas()

adicionar_usuario("Arthur", "arthur@email.com")
adicionar_usuario("Maria", "maria@email.com")

print("Usuários cadastrados:")
for usuario in listar_usuarios():
    print(usuario)

