import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'foodbridge-super-secret-key-2026')
    
    # Ensure database path is absolute when using SQLite
    db_env = os.getenv('DATABASE_URL')
    if not db_env or db_env.startswith('sqlite:///food_bridge.db'):
        db_path = BASE_DIR / 'instance' / 'food_bridge.db'
        DATABASE_URL = f"sqlite:///{db_path.as_posix()}"
    else:
        DATABASE_URL = db_env

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload folder for food donation photos & safety evidence
    UPLOAD_FOLDER = BASE_DIR / 'app' / 'static' / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}
    
    # Map & Geolocation Defaults (Default Metro Area: Bengaluru Urban / Custom)
    DEFAULT_LAT = float(os.getenv('DEFAULT_LATITUDE', 12.9716))
    DEFAULT_LNG = float(os.getenv('DEFAULT_LONGITUDE', 77.5946))
    DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'Bengaluru')
    
    # AI Engine Settings
    MAX_DISPATCH_RADIUS_KM = 35.0  # Max pickup/delivery distance considered
    SAFETY_BUFFER_MINUTES = 45     # Minimum safe buffer before donation expiry
    
    # WhatsApp & Twilio Configuration
    WHATSAPP_DEMO_MODE = os.getenv('WHATSAPP_DEMO_MODE', 'true').lower() in ['true', '1', 'yes']
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')
    TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')
    
    # Flask-Mail / Gmail SMTP Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true', '1', 'yes']
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False').lower() in ['true', '1', 'yes']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', os.getenv('MAIL_USERNAME'))

    # AI Notifier Agent Configuration
    AI_AGENT_CHECK_INTERVAL_SECONDS = int(os.getenv('AI_AGENT_CHECK_INTERVAL_SECONDS', 60))
    AI_AGENT_MAX_DISPATCH_RADIUS_KM = float(os.getenv('AI_AGENT_MAX_DISPATCH_RADIUS_KM', 5.0))
    
    @classmethod
    def init_app(cls, app):
        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(BASE_DIR / 'instance', exist_ok=True)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
