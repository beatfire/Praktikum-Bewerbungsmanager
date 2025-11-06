from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import List, Optional

from flask import Flask, jsonify, request, send_from_directory


DATA_FILE = os.path.join(os.path.dirname(__file__), "companies.json")
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")


@dataclass
class Company:
    id: int
    name: str
    focus: str
    city: str = ""
    industry: str = ""
    contact: str = ""
    contactTitle: str = ""
    email: str = ""
    phone: str = ""
    website: str = ""
    status: str = "Noch nicht gestartet"
    applicationDate: str = ""
    followupDate: str = ""
    specialFeatures: str = ""
    notes: str = ""


def load_companies() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        pass
    return []


def save_companies(companies: List[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(companies, f, ensure_ascii=False, indent=2)


def load_config() -> dict:
    if not os.path.exists(CONFIG_FILE):
        return get_default_config()
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return get_default_config()


def get_default_config() -> dict:
    return {
        "internship": {
            "period": {
                "start": "27.04.2026",
                "end": "01.12.2026"
            },
            "examPreparation": [
                {
                    "name": "Prüfungsvorbereitung 1",
                    "start": "17.08.2026",
                    "end": "28.08.2026"
                },
                {
                    "name": "Prüfungsvorbereitung 2",
                    "start": "12.10.2026",
                    "end": "23.10.2026"
                }
            ]
        },
        "dashboard": {
            "importantDates": {
                "title": "Wichtige Termine",
                "items": [
                    {"label": "Praktikum", "value": "27.04.2026 - 01.12.2026"},
                    {"label": "Prüfungsvorbereitung 1", "value": "17.08. - 28.08.2026"},
                    {"label": "Prüfungsvorbereitung 2", "value": "12.10. - 23.10.2026"}
                ]
            },
            "focusAreas": {
                "title": "Schwerpunkte",
                "items": ["Netzwerktechnik", "Cybersecurity", "IT-Infrastruktur", "Cloud Computing"]
            },
            "importantInfo": {
                "title": "Wichtige Info",
                "content": "Das Praktikum ist für den Betrieb kostenfrei, da es im Rahmen einer Umschulung bei CBW Hamburg durch die Arbeitsagentur finanziert wird."
            }
        }
    }


def next_id(companies: List[dict]) -> int:
    base = int(datetime.utcnow().timestamp() * 1000)
    existing = {c.get("id") for c in companies if isinstance(c.get("id"), int)}
    candidate = base
    while candidate in existing:
        candidate += 1
    return candidate


app = Flask(__name__, static_folder=".")


@app.route("/")
def root():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/companies", methods=["GET"])
def api_get_companies():
    return jsonify(load_companies())


@app.route("/api/companies", methods=["POST"])
def api_create_company():
    companies = load_companies()
    data = request.get_json(force=True, silent=True) or {}
    cid = data.get("id")
    if not isinstance(cid, int):
        cid = next_id(companies)
    company = Company(
        id=cid,
        name=data.get("name", "").strip(),
        focus=data.get("focus", "").strip(),
        city=data.get("city", ""),
        industry=data.get("industry", ""),
        contact=data.get("contact", ""),
        contactTitle=data.get("contactTitle", ""),
        email=data.get("email", ""),
        phone=data.get("phone", ""),
        website=data.get("website", ""),
        status=data.get("status", "Noch nicht gestartet"),
        applicationDate=data.get("applicationDate", ""),
        followupDate=data.get("followupDate", ""),
        specialFeatures=data.get("specialFeatures", ""),
        notes=data.get("notes", ""),
    )
    companies.append(asdict(company))
    save_companies(companies)
    return jsonify(asdict(company)), 201


@app.route("/api/companies/<int:cid>", methods=["PUT"])
def api_update_company(cid: int):
    companies = load_companies()
    data = request.get_json(force=True, silent=True) or {}
    idx = next((i for i, c in enumerate(companies) if c.get("id") == cid), None)
    if idx is None:
        return jsonify({"error": "Not found"}), 404
    updated = {**companies[idx], **data, "id": cid}
    companies[idx] = updated
    save_companies(companies)
    return jsonify(updated)


@app.route("/api/companies/<int:cid>", methods=["DELETE"])
def api_delete_company(cid: int):
    companies = load_companies()
    new_list = [c for c in companies if c.get("id") != cid]
    if len(new_list) == len(companies):
        return jsonify({"error": "Not found"}), 404
    save_companies(new_list)
    return ("", 204)


@app.route("/api/config", methods=["GET"])
def api_get_config():
    return jsonify(load_config())


if __name__ == "__main__":
    # Run with: python server.py
    app.run(host="127.0.0.1", port=5000, debug=True)


