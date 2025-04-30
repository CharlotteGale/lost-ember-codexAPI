# Codex API (Lost Ember)

The Codex is a standalone, modular API serving as the **lore and systems database** for *Lost Ember* — a narrative-driven, browser-based RPG.

This service powers worldbuilding entries, abilities, dialects, item definitions, and more — allowing the game to query consistent, scalable data from a central source.

---

## 🔧 Tech Stack

- **Python (3.11+)** for core logic
- **Flask** for lightweight, RESTful API development
- **JSON-based content** for rapid iteration and expansion
- *(Planned: PostgreSQL for long-term storage & admin interface)*

---

## 🧠 Core Responsibilities

- Serve structured lore entries (lineages, origins, callings)
- Provide reference data for abilities, tags, spells, and gear
- Enable in-game lookups, glossary views, and NPC referencing
- Act as a central source of truth across multiple gameplay systems

---

## 🗺 Project Structure (WIP)
<pre>
.
├── README.md
├── requirements.txt
├── run.py
└── app
    ├── __init__.py
    ├── config/
    │   └── db_config.py
    ├── data/
    │   ├── entries.json
    │   └── tags.json
    ├── models/
    │   └── entry.py
    ├── routes/
    │   └── entries.py
    └── utils/
        └── seed.py
</pre>

## 🔍 Sample Endpoints (Planned)
- `GET /entries/` — List all Codex entries
- `GET /entries/:id` — Fetch a specific entry
- `GET /entries?category=lineage` — Filter entries by type
- `GET /tags` — List all available metadata tags (e.g. darkborn, spell, passive)

## ✍️ Design Notes
This API is designed to:
- Keep game logic and world data decoupled
- Enable dynamic querying of lore, abilities, and item traits
- Support both Lost Ember and future narrative modules
- Eventually provide CMS-style tooling for editors/writers

## 🚧 Status
In scaffolding phase — file structure is established, with JSON parsing and test endpoints underway.

Upcoming tasks:
- Populate initial entries.json dataset
- Scaffold /entries/ route
- Connect to frontend UI for in-game lookups

## 📃 License
This is a personal project in private development.
Public contributions may open post-alpha.