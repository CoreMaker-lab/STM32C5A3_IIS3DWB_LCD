"""Bounded local serial evidence, no per-packet disk writes."""
import json, logging, time, threading
from datetime import datetime, timezone
from pathlib import Path
from logging.handlers import RotatingFileHandler
class Journal:
    def __init__(self, directory):
        directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
        # One rolling log across sessions: <= 3 * 2MiB, including backups.
        self.path=directory/'serial_diagnostics.jsonl'
        self.logger=logging.Logger('iis3dwb_'+str(id(self)))
        self.handler=RotatingFileHandler(self.path,maxBytes=2*1024*1024,backupCount=2,encoding='utf-8')
        self.handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(self.handler)
        self.write('session_start',thread=threading.current_thread().name)
    def write(self,event,**fields):
        self.logger.info(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),monotonic=time.monotonic(),event=event,**fields),ensure_ascii=False))
    def close(self):
        self.write('session_end');self.handler.close();self.logger.removeHandler(self.handler)
