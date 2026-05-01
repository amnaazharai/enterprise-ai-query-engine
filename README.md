# Enterprise AI Query Engine

A production-oriented system for querying enterprise data using natural language, powered by LLMs, a governed semantic layer, and BigQuery.

---

## 🚀 Overview

Accessing enterprise data typically requires SQL expertise, creating a bottleneck between business users and data teams.

This project simulates a real-world solution:

> An AI-powered query engine that translates natural language into safe, governed SQL queries over enterprise data.

---

## 🧠 System Capabilities

The system enables users to ask:

* “What is total revenue by product category?”
* “Which traffic sources drive the highest conversions?”
* “Who are our highest value customers in the last 30 days?”

Behind the scenes, the system:

1. Interprets the query using an LLM (Gemini via Vertex AI)
2. Grounds the request using a semantic layer
3. Generates structured SQL
4. Applies guardrails to enforce safety
5. Executes queries in BigQuery
6. Returns results and optional explanations
7. Logs all activity for auditability

---

## 🏗️ Architecture

### High-Level Flow

User Query
→ FastAPI Backend
→ LLM (Gemini via Vertex AI)
→ SQL Generation
→ Guardrails Layer
→ BigQuery Execution
→ Results + Audit Logging

---

## 🧱 Data Model

The system uses a relational model combining behavioral and transactional data.

### Tables

* **customers** — user attributes and lifecycle data
* **products** — product catalog and pricing
* **orders** — transactional purchase records
* **events** — behavioral interaction data (page views, cart actions, purchases)

### Design Rationale

* `events` capture user behavior across the funnel
* `orders` represent confirmed financial outcomes
* Linking both enables conversion and revenue analysis

---

## 🧠 Semantic Layer

A structured semantic layer provides:

* table descriptions
* column definitions
* business-friendly abstractions

This layer grounds the LLM and ensures generated SQL aligns with business logic rather than raw schema guessing.

---

## 🔐 Guardrails

This system enforces query safety to simulate production constraints:

* blocks `SELECT *` queries
* prevents full table scans
* restricts sensitive fields
* validates schema usage before execution

This transforms the system from a demo into a **governed data access layer**.

---

## ⚙️ Tech Stack

* **Cloud**: Google Cloud Platform
* **Data Warehouse**: BigQuery
* **LLM**: Gemini (via Vertex AI)
* **Backend**: FastAPI (Python)
* **Frontend**: Streamlit or Next.js

---

## 🚧 Roadmap

* [ ] Implement semantic layer (YAML-driven)
* [ ] Build SQL generation service
* [ ] Add guardrails and validation layer
* [ ] Deploy backend to Cloud Run
* [ ] Add authentication and role-based access
* [ ] Enhance audit logging and monitoring

---

## 🧠 Key Takeaways

This project demonstrates how to design systems that:

* make data accessible via natural language
* maintain governance and control
* bridge business users and data platforms

---

## 📌 Status

In progress — actively building core system components.
