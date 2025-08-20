from flask import Blueprint, jsonify, request
from users.users_model import (
    listar_users,
    user_por_id,
    adicionar_user,
    atualizar_user,
    excluir_user
)

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(listar_users()), 200

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_por_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@user_bp.route ("/users", methods=["POST"])
def create_user():
    novos_dados = request.json
    novo_user = adicionar_user(novos_dados)
    return jsonify(novo_user), 201

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    novos_dados = request.json
    user = atualizar_user(user_id, novos_dados)
    if user:
        return jsonify(user), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if excluir_user(user_id):
        return jsonify({"message": "Usuário excluído com sucesso"}), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404
