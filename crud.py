from banco import conectar

def adicionar_usuario(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def atualizar_usuario(id, novo_nome, novo_email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
