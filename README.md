# AI-Powered Work Order Management System  
🚀 Automating work order processing using AI, FastAPI, and AWS  

---

## Overview  
This project automates work order creation from email requests using AI-powered parsing. It integrates email processing, a FastAPI backend, LLMs (GPT-4o), a PostgreSQL database, and an FSM (Field Service Management) software to streamline service request handling.  

## Features  
✅ **Email Processing** – Automatically receives and parses work order requests via SendGrid.  
✅ **AI-Powered Parsing** – Uses GPT-4o to extract structured order details.  
✅ **Database Storage** – Stores work orders and agent data in AWS RDS PostgreSQL.  
✅ **FSM Integration** – Creates work orders in an FSM system for task execution.  
✅ **Frontend Dashboard** – Next.js UI for tracking orders and managing requests.  

---

## Tech Stack  
- **Frontend**: [Next.js](https://nextjs.org/) (Hosted on Vercel)  
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Deployed on AWS ECS)  
- **AI/NLP**: [GPT-4o](https://openai.com/) for order parsing  
- **Database**: [AWS RDS PostgreSQL](https://aws.amazon.com/rds/)  
- **Email Processing**: [SendGrid](https://sendgrid.com/)  
- **FSM Software**: External integration for work order automation  

---

## System Architecture  
```
1. Email Request → Sent to SendGrid Parse
2. SendGrid → Forwards structured email data to FastAPI
3. FastAPI → Uses GPT-4o to extract order details
4. FastAPI → Stores extracted data in AWS RDS PostgreSQL
5. FastAPI → Creates work order in FSM software
6. Next.js Frontend → Displays orders and status updates
```

### Architecture Diagram  
![System Architecture](./docs/architecture.png)

---

## Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/pedrovs16/muro_test.git
cd muro_test
```

### 2. Backend Setup (FastAPI)  
#### Install Dependencies  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Set Up Environment Variables  
Create a `.env` file in the `backend/` directory:  
```ini
SENDGRID_API_KEY=your_sendgrid_api_key
OPENAI_API_KEY=your_gpt4_api_key
DATABASE_URL=postgresql://user:password@aws-rds-url/dbname
FSM_API_URL=your_fsm_api_endpoint
```

#### Run the API Locally  
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### 3. Frontend Setup (Next.js)  
#### Install Dependencies  
```bash
cd frontend
npm install
```

#### Run Next.js Locally  
```bash
npm run dev
```

---

## API Endpoints (FastAPI)  
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/parse-email` | `POST` | Receives and processes email content |
| `/create-order` | `POST` | Creates a work order in FSM software |
| `/orders` | `GET` | Retrieves all stored work orders |

---

## Possibles Enhancements  
- ✅ Implement **user authentication** with AWS Cognito.  
- ✅ Add **real-time order tracking** via WebSockets.  
- ✅ Enhance AI parsing for better request understanding.  