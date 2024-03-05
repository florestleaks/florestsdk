from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class FlorestDatabase:
    def __init__(
        self,
        db_url,
        pool_size=20,
        max_overflow=0,
        pool_timeout=30,
        pool_recycle=-1,
        echo=False,
        ssl_mode=None,
    ):
        engine_options = {
            "pool_size": pool_size,
            "max_overflow": max_overflow,
            "pool_timeout": pool_timeout,  # Em segundos
            "pool_recycle": pool_recycle,  # Em segundos, -1 desativa a reciclagem
            "echo": echo,  # Ativa o logging de SQL se necessário
            "connect_args": {"sslmode": ssl_mode} if ssl_mode else {},
        }
        self.engine = create_engine(db_url, **engine_options)
        self.Session = scoped_session(
            sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        )

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def create_schema(self, schema_name="florest"):
        with self.engine.connect() as conn:
            # Usa text() para criar um objeto SQL executável a partir da string
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
            conn.commit()

    def get_session(self):
        """Obtém uma sessão de banco de dados."""
        return self.Session()

    def close_session(self):
        """Fecha a sessão de banco de dados atual."""
        self.Session.remove()
