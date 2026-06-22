# AI SEO Content Engine

A production-grade LangGraph-powered AI research and content generation system that combines deep web research, website style analysis, local trend intelligence, SEO strategy, and article generation into a single automated workflow.

## Overview

AI SEO Content Engine is an advanced multi-stage content generation platform that transforms three user inputs:

* **Keyword** – Primary topic or target keyword
* **Website** – Reference website for style and brand voice analysis
* **Pincode** – Geographic location for local trend and SEO context

into a fully researched, fact-checked, SEO-optimized article that aligns with the writing style of the provided website while remaining original and source-backed.

---

## Key Features

### Deep Research Pipeline

* Multi-stage web research using Tavily
* Source aggregation and ranking
* Evidence synthesis
* Structured knowledge extraction

### Website Style Analysis

* Tone detection
* Brand voice analysis
* Heading structure analysis
* Paragraph and content rhythm analysis
* CTA pattern detection
* Writing style profiling

### Local SEO Intelligence

* Pincode-based location discovery
* Local trend identification
* Regional search intent analysis
* Local context enrichment

### SEO Strategy Generation

* Primary keyword planning
* Secondary keyword expansion
* Semantic keyword discovery
* Search intent classification
* Content structure optimization

### Article Generation

* Long-form article creation
* Website-style alignment
* Local context integration
* SEO optimization
* FAQ generation
* Reference compilation

### Quality Assurance

* Fact checking
* Style auditing
* SEO auditing
* Refinement loops
* Source validation

---

# System Architecture

```text
User Inputs
│
├── Keyword
├── Website
└── Pincode
      │
      ▼

Layer 1: Context Intelligence
│
├── Website Style Analysis
├── Brand Voice Analysis
├── Pincode Analysis
└── Trend Discovery

      ▼

Layer 2: Research Planning
│
├── Intent Analysis
├── SEO Expansion
├── Research Planning
└── Search Query Planning

      ▼

Layer 3: Deep Research
│
├── Tavily Search
├── Content Extraction
├── Research Agent
├── Evidence Synthesis
└── Knowledge Graph

      ▼

Layer 4: Content Strategy
│
├── SEO Strategy
├── Article Architecture
├── Local Context Injection
└── Style Alignment

      ▼

Layer 5: Writing & Validation
│
├── Draft Writing
├── Fact Checking
├── SEO Auditing
├── Style Auditing
├── Refinement
└── Final Formatting

      ▼

Final SEO Article
```

---

# Project Structure

```text
seo-content-engine/
│
├── app/
├── schemas/
├── services/
├── tools/
├── nodes/
│   ├── layer1_context/
│   ├── layer2_planning/
│   ├── layer3_research/
│   ├── layer4_strategy/
│   └── layer5_writing/
│
├── prompts/
├── graphs/
├── utils/
├── tests/
│
├── main.py
├── api.py
├── requirements.txt
└── README.md
```

---

# Workflow

## Step 1: Input Collection

Example:

```json
{
  "keyword": "AI Website Development",
  "website": "https://example.com/blog",
  "pincode": "700091"
}
```

---

## Step 2: Context Intelligence

The system analyzes:

### Website

Extracts:

* Tone
* Voice
* Heading patterns
* Content structure
* CTA style
* Vocabulary complexity

### Pincode

Discovers:

* City
* Region
* Audience characteristics
* Local trends
* Business relevance

---

## Step 3: Research Planning

The system generates:

* Search intent
* SEO opportunities
* Research objectives
* Search queries
* Competitor angles

---

## Step 4: Deep Research

Using Tavily and Gemini:

* Searches the web
* Collects evidence
* Extracts useful information
* Removes duplicates
* Builds a structured knowledge base

---

## Step 5: Content Strategy

Creates:

* SEO plan
* Article outline
* Keyword placement strategy
* Local relevance plan
* Style guidelines

---

## Step 6: Article Generation

Produces:

* SEO title
* Meta description
* Full article
* FAQs
* References

---

## Step 7: Validation

The article undergoes:

* Fact checking
* SEO review
* Style matching review
* Refinement cycles

---

# Technology Stack

## Orchestration

* LangGraph
* LangChain

## Language Models

* Gemini API

## Search & Research

* Tavily

## Web Processing

* httpx
* BeautifulSoup4
* markdownify

## Data Validation

* Pydantic

## API Layer

* FastAPI

## Testing

* Pytest

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd seo-content-engine
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

MODEL_NAME=gemini-2.5-flash

MAX_SEARCH_RESULTS=10
MAX_RESEARCH_ITERATIONS=5

CACHE_ENABLED=true
LOG_LEVEL=INFO
```

---

# Running the Project

## CLI Mode

```bash
python main.py
```

---

## API Mode

```bash
uvicorn api:app --reload
```

---

# Example Request

```json
{
  "keyword": "AI Website Development",
  "website": "https://example.com/blog",
  "pincode": "700091"
}
```

---

# Example Output

```markdown
# AI Website Development in 2026

Meta Description:
Explore how AI website development is transforming businesses and how local trends are shaping adoption.

## Introduction

...

## Benefits of AI Website Development

...

## Local Market Insights

...

## Frequently Asked Questions

...

## References

...
```

---

# Testing

Run all tests:

```bash
pytest
```

Run unit tests:

```bash
pytest tests/unit
```

Run integration tests:

```bash
pytest tests/integration
```

---

# Future Enhancements

* Multi-language article generation
* Competitor content gap analysis
* Internal linking recommendations
* CMS publishing integrations
* Keyword clustering
* Content calendar generation
* RAG-based memory layer
* Vector database support
* Agent observability dashboard
* Human-in-the-loop review workflow

---

# Disclaimer

This project is intended for educational, research, and content-generation workflows. Generated content should always be reviewed by a human before publication. Website analysis is used solely for style and structural understanding. Content is generated to be original and should not reproduce copyrighted material from analyzed sources.
