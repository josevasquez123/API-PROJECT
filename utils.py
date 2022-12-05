from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#ENCRYPT PASSWORD
def encrypt_pwd(password: str):
    return pwd_context.hash(password)

#VERIFY ENCRYPTED PASSWORD
def verify(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)