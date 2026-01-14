# Terminal Security Agent

An AI-powered terminal assistant using **LangChain’s ShellTool** to perform safe Linux security audits via natural-language queries. Convert queries like "check firewall status" into appropriate shell commands while ensuring system safety via a strict whitelist.

---

##  Features

-  **Natural Language Queries**  
  Ask in plain English—for example, "Which ports are open?" or "Are there any world-writable files?"

-  **Safe Command Execution**  
  Executes only vetted, read-only commands such as `ss -tuln`, `ufw status`, `iptables -L`, and `find / -perm -o=w`.

-  **Whitelist-Based Security**  
  Prevents destructive or modifying commands by enforcing a strict whitelist for command execution.

-  **Clear, Human-Readable Results**  
  Outputs are summarized back to the user in a clear, non-technical way for easy understanding.

---

##  Getting Started

### Prerequisites

- Python 3.9+
- OpenAI API key  
- Basic familiarity with running Python in a Unix/Linux environment

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CrAnish07/Terminal-Security-Agent.git
   cd Terminal-Security-Agent 

2. Create a `.env` file with your OpenAI or GOOGLE API key:
   
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here

4. Install dependencies:

   ```bash
   pip install -r requirements.txt

5. Run the assistant:

   ```bash
   python main.py

## Project Structure

```
security-audit-assistant/
├── main.py              # Agent orchestration using LangChain
├── whitelist.py         # Safe command whitelist definitions
├── prompts/
│   └── intro.txt        # System prompt guidelines
├── utils/
│   └── validators.py    # Logic to verify command safety
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # Project overview and usage
```

## Sample Interaction

```
$ python main.py
Terminal Security Agent (type 'exit' to quit)

Ask: Which ports are open?
Result:
- Port 22 (SSH) is open.
- PostgreSQL is listening on localhost only.
```


   


