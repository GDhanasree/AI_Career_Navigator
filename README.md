# Skill-Bridge Career Navigator 

## Candidate Name:

Dhanasree Gidijala

## Scenario Chosen:

Skill-Bridge Career Navigator

---

## Overview

I chose this problem because it closely relates to students and early-career professionals navigating today’s competitive job market.

This project aims to bridge the gap between a user’s current skill set and the requirements of their target role by providing:

* Clear skill gap analysis
* Structured, phase-wise learning roadmap
* AI-assisted career guidance
* Interview preparation support

The goal was to build a **practical, intuitive, and reliable system** that provides direction rather than overwhelming users with scattered information.

---

##  Quick Start

### Prerequisites:

* Python 3.9+
* pip

### Run:

```bash
pip install streamlit transformers torch sentencepiece
streamlit run app.py
```

### Run Tests:

```bash
pytest
```

---

##  Design & Approach

The system follows a **hybrid architecture**:

* **Rule-based logic** → ensures correctness and structured outputs
* **AI model (HuggingFace - FLAN-T5)** → enhances guidance and recommendations

This approach was chosen to balance:

* Reliability
* Simplicity within time constraints
* Meaningful AI usage

---

##  Core Features

### 1. Skill Gap Analysis

* Extracts skills from synthetic resume input
* Compares against role-specific requirements
* Identifies missing skills

---

### 2. Structured Industry Gap Breakdown

* Groups missing skills into categories like:

  * Core ML
  * Deep Learning
  * MLOps
  * Data Processing

---

### 3. Learning Roadmap (Phase-Based)

* Step-by-step roadmap:

  * Foundations
  * Core Skills
  * Advanced Topics
  * Deployment
  * Portfolio Building

---

### 4. AI Integration + Fallback

* Uses HuggingFace model for generating career guidance
* Includes fallback mechanism to ensure system reliability even if AI fails

---

### 5. Mock Interview Questions

* Skill-based interview preparation

---

### 6. Progress Simulation

* Simulates user learning progress and job readiness

---

## AI Disclosure

* **Used AI tools:** Yes (HuggingFace AI model + ChatGPT for development support)

### Verification:

* Outputs were validated manually
* Core system remains deterministic for accuracy

### Example Adjustment:

- Initial AI-generated outputs were overly simplistic, with minimal data for roles and learning resources.  
- The early approach relied on directly subtracting current skills from expected role skills and retrieving content from a static JSON file, which resulted in very basic and less meaningful outputs.  

To improve this, I:
- Expanded the synthetic dataset to include richer and more representative skill mappings for each role  
- Introduced structured categorization of skills (e.g., core concepts, advanced topics, deployment)  
- Integrated a HuggingFace model to generate contextual learning guidance instead of relying solely on static data  

This transition helped transform the system from a basic lookup mechanism into a more structured and user-oriented recommendation engine.

---

## Tradeoffs & Prioritization

### Constraints:
- Strict 4–6 hour time limit  
- Limited access to external APIs (OpenAI) due to payment restrictions  
- Focus on building a reliable end-to-end prototype within time  

---

### Decisions:
- Prioritized **core functionality and end-to-end flow over UI polish**  
- Used a **synthetic dataset** to simulate real-world role-skill mappings instead of integrating external data sources  
- Adopted a **hybrid approach**:
  - Rule-based logic for deterministic and structured outputs  
  - HuggingFace model for generating contextual guidance  
- Replaced initial simple JSON-based retrieval with a **more structured roadmap generation approach** to improve clarity and usefulness  

---

### Outcome:
These decisions ensured that the system remained:
- Reliable  
- Interpretable  
- Complete within the given time constraints  

---

## 🔮 Future Enhancements

- **Semantic Skill Matching**  
  Use embeddings and vector search (e.g., FAISS) to match skills based on meaning rather than exact keywords  

- **Resume Parsing (PDF Support)**  
  Allow users to upload resumes directly and extract structured information automatically  

- **Integration with Real Job Data**  
  Connect with job postings to dynamically update required skills and trends  

- **Personalized Learning Preferences**  
  Adapt roadmap recommendations based on user preferences such as:
  - Reading documentation or blogs  
  - Watching video tutorials (YouTube)  
  - Structured courses (Coursera, Udemy)  
  This increases the likelihood of users consistently following the learning path  

- **Automated Progress Tracking & Nudges**  
  Track user progress dynamically and:
  - Update readiness levels automatically  
  - Send periodic reminders or nudges  
  - Recommend next steps based on progress  

- **End-to-End Career Development Platform**  
  Expand into a full platform that supports:
  - Skill development  
  - Career transitions  
  - Continuous learning across domains  

The goal is to evolve this into a personalized, adaptive career companion rather than a static recommendation tool.

---

## Known Limitations

- Skill extraction is primarily keyword-based and may miss semantically similar skills  
- Synthetic dataset may not fully capture real-world job market variations  
- AI-generated guidance may occasionally be generic or lack deep contextual personalization  
- Current system does not support resume parsing (PDF/structured input)  
- Progress simulation is illustrative and not based on real user tracking  

---

## Data Safety

- Only synthetic data is used throughout the system  
- No personal or sensitive user data is stored or processed  
- No external APIs or third-party services requiring credentials are used  
- All processing is performed locally, ensuring user privacy and control  

---

## Demo Video

https://youtu.be/I0U52TRRy7Q
