from app import app
from config import cfg

app.run(cfg.host, port=cfg.port, debug=cfg.debug)