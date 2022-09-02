import decouple
import logging
import os

from decouple import config, Config, RepositoryEnv

def secret_or_env(SECRET_NAME):
    pw = config(SECRET_NAME, default=None)
    pw_file = config(f'{SECRET_NAME}_FILE', default=None)
    if pw and pw_file:
        logging.warning(f"both {SECRET_NAME}_FILE and {SECRET_NAME} are set.")
    
    if pw_file and not pw:
        try:
            with open(pw_file, 'r') as fh:
                pw = fh.read().rstrip('\n')
        except IOError as e:
            logging.error(f"{SECRET_NAME} not found")

    return pw

print("I am about to show the environment:")
user = config('DB_CONN_USER', default="")
host = config('DB_CONN_HOST', default="")
print(f"user: {user}")
print(f"host: {host}")
print("=========SECRETS---------")
pw = secret_or_env('POSTGRES_PASSWORD')
print(pw)
print("=========OTHER SECRETS---------")
secret_config = Config(RepositoryEnv(os.environ['DB_CON_FILE']))
print("DB_PASSWORD:", secret_config("DB_PASSWORD"))
print("DB_USER:", secret_config("DB_USER"))
