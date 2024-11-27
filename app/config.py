
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def load_secrets():
    try:
        # Azure Key Vault URL
        vault_url = "https://midtermkeyvault123.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)

        # Sırları çek
        secrets = {
            "DB_HOST": client.get_secret("db-host").value,
            "DB_NAME": client.get_secret("db-name").value,
            "DB_USER": client.get_secret("db-user").value,
            "DB_PASSWORD": client.get_secret("db-password").value,
        }
        print("Secrets successfully loaded from Azure Key Vault.")
        return secrets
    except Exception as e:
        raise RuntimeError(f"Failed to load secrets from Azure Key Vault: {str(e)}")
