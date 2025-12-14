"""
Responsabilidades
- Hash de senha (nunca salvar senha pura)
- Geração de JWT
- Base da autenticação
- JWT não deve confiar em email
- sub (subject) é o ID do usuário
- Mais seguro, mais rápido, padrão de mercado
"""

from passlib.context import CryptContext
from jose import jwt, JWTError

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hash):
    return pwd_context.verify(password, hash)

def create_token(user_id: int):
    payload = {"sub": str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload.get("sub"))
    except JWTError:
        return None
