import sqlite3
import json
 
# logs overall danger score and hotspot every second
# doesnt log the full 10x10 grid every tick thats too much data
# just logs the summary - score, hotspot, alert level, timestamp
 
DB = "stampede_log.db"
 
 
class DataLogger:
 
    def __init__(self):
        self._init()
 
    def _init(self):
        con = sqlite3.connect(DB)
        con.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp   TEXT,
                tick        INTEGER,
                overall_score REAL,
                alert_level TEXT,
                hotspot_row INTEGER,
                hotspot_col INTEGER,
                evac_msg    TEXT
            )
        """)
        con.commit()
        con.close()
 