from logging.config import fileConfig
from dotenv import load_dotenv
load_dotenv('.env')
from configparser import ConfigParser

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import os
import sys


user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
host = os.getenv("MYSQL_HOST")

db_url = os.environ.get('DB_URL')



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.file import File
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", db_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Crea un objeto `metadata` que contenga los modelos que deseas incluir en la migración.
    target_metadata = [
        File.metadata,
        # Agrega otros modelos aquí
]


def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")
    

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
