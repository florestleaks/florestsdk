from abc import ABC, abstractmethod


class ICompanyRepository(ABC):
    @abstractmethod
    def create_client(self, nome: str, email: str):
        pass

    @abstractmethod
    def get_client_by_name(self, name: str):
        pass

    @abstractmethod
    def get_client_by_id(self, client_id: int):
        pass

    @abstractmethod
    def update_client(self, client_id: int, new_name: str, new_email: str):
        pass

    @abstractmethod
    def delete_client(self, client_id: int):
        pass

    @abstractmethod
    def list_clients(self) -> list:
        pass
