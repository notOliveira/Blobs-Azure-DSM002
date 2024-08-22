import os
from azure.data.tables import TableServiceClient

class AzureTableService:
    def __init__(self):
        # Use a connection string para criar o cliente
        connection_string = os.getenv("CONNECTION_STRING")
        self.table_client = TableServiceClient.from_connection_string(connection_string)

    def list_entities(self):
        table_name = "tb04"  # Substitua pelo nome da sua tabela
        table_client = self.table_client.get_table_client(table_name)
        return list(table_client.list_entities())

    def create_entity(self, partition_key, row_key, **properties):
        table_name = "tb04"  # Substitua pelo nome da sua tabela
        table_client = self.table_client.get_table_client(table_name)
        entity = {'PartitionKey': partition_key, 'RowKey': row_key, **properties}
        table_client.create_entity(entity)

    def read_entity(self, partition_key, row_key):
        table_name = "tb04"  # Substitua pelo nome da sua tabela
        table_client = self.table_client.get_table_client(table_name)
        return table_client.get_entity(partition_key, row_key)

    def update_entity(self, partition_key, row_key, **properties):
        table_name = "tb04"  # Substitua pelo nome da sua tabela
        table_client = self.table_client.get_table_client(table_name)
        entity = {'PartitionKey': partition_key, 'RowKey': row_key, **properties}
        table_client.update_entity(entity)

    def delete_entity(self, partition_key, row_key):
        table_name = "tb04"  # Substitua pelo nome da sua tabela
        table_client = self.table_client.get_table_client(table_name)
        table_client.delete_entity(partition_key, row_key)
