# engine/database_engine.py

import sqlite3
from pathlib import Path
import json
import time
from typing import Iterable, Dict, Any

try:
    import psycopg
except ImportError:
    psycopg = None  # optional


class DatabaseEngine:
    def __init__(self, settings):
        self.settings = settings
        self.db_path = self._resolve_db_path()
        self._ensure_schema()

    def _resolve_db_path(self) -> Path:
        if self.settings.sqlite_path:
            return self.settings.sqlite_path
        if self.settings.vault_path:
            return self.settings.vault_path / "theophysics.db"
        return Path("theophysics.db")

    def update_db_path(self, p: Path):
        self.db_path = p
        self._ensure_schema()

    def _ensure_schema(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE,
            title TEXT,
            yaml TEXT,
            tags TEXT,
            links TEXT,
            hash TEXT,
            updated_at INTEGER
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT UNIQUE,
            aliases TEXT,
            classification TEXT,
            body TEXT,
            status TEXT,
            file_path TEXT,
            updated_at INTEGER
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS research_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT,
            source TEXT,
            url TEXT
        )
        """)

        conn.commit()
        conn.close()

    # -------- Notes --------

    def store_notes(self, notes: Iterable[Dict[str, Any]], replace: bool = False):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        if replace:
            c.execute("DELETE FROM notes")
        now = int(time.time())
        for n in notes:
            c.execute("""
            INSERT OR REPLACE INTO notes (path, title, yaml, tags, links, hash, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                n["path"],
                n["title"],
                json.dumps(n["yaml"]),
                json.dumps(n["tags"]),
                json.dumps(n["links"]),
                n["hash"],
                now
            ))
        conn.commit()
        conn.close()

    def get_metrics(self) -> dict:
        """Get vault metrics with ACTUAL counts (not string lengths)."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Count notes
        c.execute("SELECT COUNT(*) FROM notes")
        notes_count = c.fetchone()[0]

        # Count actual tags and links by parsing the JSON
        c.execute("SELECT tags, links FROM notes")
        rows = c.fetchall()
        
        total_tags = 0
        unique_tags = set()
        total_links = 0
        unique_links = set()
        
        for tags_json, links_json in rows:
            try:
                tags = json.loads(tags_json) if tags_json else []
                links = json.loads(links_json) if links_json else []
                
                total_tags += len(tags)
                unique_tags.update(tags)
                
                total_links += len(links)
                unique_links.update(links)
            except (json.JSONDecodeError, TypeError):
                pass

        # Count definitions
        c.execute("SELECT COUNT(*) FROM definitions")
        defs_count = c.fetchone()[0]

        conn.close()

        return {
            "notes": notes_count,
            "tags": len(unique_tags),  # Unique tag count
            "tags_total": total_tags,   # Total tag occurrences
            "links": len(unique_links), # Unique link count
            "links_total": total_links, # Total link occurrences
            "definitions": defs_count,
            "errors": 0,
        }

    # -------- Definitions --------

    def upsert_definition(self, data: Dict[str, Any]):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        now = int(time.time())
        c.execute("""
        INSERT INTO definitions (term, aliases, classification, body, status, file_path, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(term) DO UPDATE SET
            aliases = excluded.aliases,
            classification = excluded.classification,
            body = excluded.body,
            status = excluded.status,
            file_path = excluded.file_path,
            updated_at = excluded.updated_at
        """, (
            data["term"],
            json.dumps(data.get("aliases", [])),
            data.get("classification"),
            data.get("body"),
            data.get("status", "draft"),
            data.get("file_path"),
            now
        ))
        conn.commit()
        conn.close()

    def list_definitions(self) -> list[dict]:
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT term, status, file_path FROM definitions ORDER BY term")
        rows = c.fetchall()
        conn.close()
        return [{"term": r[0], "status": r[1] or "", "file_path": r[2] or ""} for r in rows]

    def get_definition(self, term: str) -> dict | None:
        """Get full definition by term."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
        SELECT term, aliases, classification, body, status, file_path
        FROM definitions WHERE term = ?
        """, (term,))
        row = c.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return {
            "term": row[0],
            "aliases": json.loads(row[1]) if row[1] else [],
            "classification": row[2],
            "body": row[3],
            "status": row[4],
            "file_path": row[5],
        }

    # -------- Research links --------

    def add_research_link(self, term: str, source: str, url: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO research_links (term, source, url) VALUES (?, ?, ?)",
                  (term, source, url))
        conn.commit()
        conn.close()

    def get_research_links(self) -> dict:
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT term, source, url FROM research_links")
        rows = c.fetchall()
        conn.close()

        result: dict[str, list[dict]] = {}
        for term, source, url in rows:
            result.setdefault(term.lower(), []).append({"source": source, "url": url})
        return result

    # -------- Query helpers --------

    def get_all_notes(self) -> list[dict]:
        """Get all notes from database."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT path, title, yaml, tags, links, hash FROM notes")
        rows = c.fetchall()
        conn.close()
        
        return [{
            "path": r[0],
            "title": r[1],
            "yaml": json.loads(r[2]) if r[2] else {},
            "tags": json.loads(r[3]) if r[3] else [],
            "links": json.loads(r[4]) if r[4] else [],
            "hash": r[5],
        } for r in rows]

    def get_note_by_path(self, path: str) -> dict | None:
        """Get single note by path."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT path, title, yaml, tags, links, hash FROM notes WHERE path = ?", (path,))
        row = c.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return {
            "path": row[0],
            "title": row[1],
            "yaml": json.loads(row[2]) if row[2] else {},
            "tags": json.loads(row[3]) if row[3] else [],
            "links": json.loads(row[4]) if row[4] else [],
            "hash": row[5],
        }

    # -------- Aggregation / Maintenance --------

    def aggregate_data(self):
        # Placeholder for future aggregation logic
        return True

    def vacuum_sqlite(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("VACUUM")
        conn.close()
        return True

    # -------- Postgres export --------

    def export_to_postgres(self) -> tuple[bool, str]:
        if not self.settings.postgres_conn_str:
            return False, "Postgres connection string not set."

        if psycopg is None:
            return False, "psycopg is not installed. Run: pip install psycopg[binary]"

        try:
            with psycopg.connect(self.settings.postgres_conn_str) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        path TEXT PRIMARY KEY,
                        title TEXT,
                        yaml JSONB,
                        tags JSONB,
                        links JSONB,
                        hash TEXT,
                        updated_at BIGINT
                    )
                    """)
                    cur.execute("""
                    CREATE TABLE IF NOT EXISTS definitions (
                        term TEXT PRIMARY KEY,
                        aliases JSONB,
                        classification TEXT,
                        body TEXT,
                        status TEXT,
                        file_path TEXT,
                        updated_at BIGINT
                    )
                    """)

                    # export Notes
                    sconn = sqlite3.connect(self.db_path)
                    sc = sconn.cursor()
                    sc.execute("SELECT path, title, yaml, tags, links, hash, updated_at FROM notes")
                    
                    note_count = 0
                    for row in sc.fetchall():
                        cur.execute("""
                        INSERT INTO notes (path, title, yaml, tags, links, hash, updated_at)
                        VALUES (%s, %s, %s::jsonb, %s::jsonb, %s::jsonb, %s, %s)
                        ON CONFLICT(path) DO UPDATE SET
                            title = EXCLUDED.title,
                            yaml = EXCLUDED.yaml,
                            tags = EXCLUDED.tags,
                            links = EXCLUDED.links,
                            hash = EXCLUDED.hash,
                            updated_at = EXCLUDED.updated_at
                        """, row)
                        note_count += 1

                    # export Definitions
                    sc.execute("SELECT term, aliases, classification, body, status, file_path, updated_at FROM definitions")
                    
                    def_count = 0
                    for row in sc.fetchall():
                        cur.execute("""
                        INSERT INTO definitions (term, aliases, classification, body, status, file_path, updated_at)
                        VALUES (%s, %s::jsonb, %s, %s, %s, %s, %s)
                        ON CONFLICT(term) DO UPDATE SET
                            aliases = EXCLUDED.aliases,
                            classification = EXCLUDED.classification,
                            body = EXCLUDED.body,
                            status = EXCLUDED.status,
                            file_path = EXCLUDED.file_path,
                            updated_at = EXCLUDED.updated_at
                        """, row)
                        def_count += 1

                    sconn.close()

            return True, f"Export complete: {note_count} notes, {def_count} definitions"
        except Exception as e:
            return False, f"Postgres export error: {e}"
