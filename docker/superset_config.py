import os 
SECRET_KEY='6lpogNyGwdDmNqOy2SqR+gNqO5GnwtTuyRi3fLosUFmlrqaREUGqf1Jf'
WTF_CSRF_ENABLED =False
REDIS_HOST = os.getenv("REDIS_HOST", "superset_cache")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

#RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG




#SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=10).total_seconds()) #Tempo de resposta para consulta

BABEL_DEFAULT_LOCALE = "pt_BR"
LANGUAGES= { "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"} } # Linguagem padrão da plataforma


FEATURE_FLAGS = {
'HORIZONTAL_FILTER_BAR': True,
'EMBEDDABLE_CHARTS': True,
'DRILL_TO_DETAIL': True,
'DRILL_BY': True,
'JAVASCRIPT_CONTROLS': True, # uso de java para configurar mapas
'ENABLE_JAVASCRIPT_CONTROLS': True, # uso de java para configurar mapas
'THUMBNAILS': True, # Icones de gráficos, Mas precisa de um webserver
'EMBEDDED_SUPERSET': True, # incorporar gráficos a sites
'ENABLE_TEMPLATE_PROCESSING': True, # Jinja template

'TEMPLATE_PROCESSING': True
}

#Formato de saída da moeda e formato de número
D3_FORMAT = { 
"decimal": ",",
"thousands": ".",
"grouping": [3],
"currency": ["R$", ""]
}

HTML_SANITIZATION = False
 
HTML_SANITIZATION_SCHEMA_EXTENSIONS = {
  "attributes": {
    "*": ["style","className"],
  },
  "tagNames": ["style"],
}


### teste CSS
TALISMAN_ENABLED = False
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'"],
        "img-src": ["'self'", "blob:", "data:"],
       "worker-src": ["'self'", "blob:"],
        "connect-src": [
            "'self'",
            "https://api.mapbox.com",
            "https://events.mapbox.com",
        ],
        "object-src": "'none'",
        "style-src": [
            "'self'",
            "'unsafe-inline'",
        ],
        "script-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
    },
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": False,
}
