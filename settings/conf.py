from . import get_env_variable
from pathlib import Path
import os
import sys
from web3 import Web3

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))


ADMIN_SITE_URL = get_env_variable("ADMIN_SITE_URL")

SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = get_env_variable("DEBUG")


binance_testnet_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(binance_testnet_rpc_url))
print(f"Is connected: {web3.isConnected()}")
print(f"gas price: {web3.eth.gas_price} BNB")
print(f"current block number: {web3.eth.block_number}")
print(f"number of current chain is {web3.eth.chain_id}") 

ALLOWED_HOSTS = []

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'deploy.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AUTH_USER_MODEL = 'auths.CustomUser'


EMAIL_BACKEND = get_env_variable("EMAIL_BACKEND")
EMAIL_USE_TLS = get_env_variable("EMAIL_USE_TLS")
EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_PORT = get_env_variable("EMAIL_PORT")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")