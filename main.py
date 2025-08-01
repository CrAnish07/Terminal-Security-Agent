from langchain.agents import Tool, initialize_agent
from langchain.tools.shell.tool import ShellTool
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.validators import is_command_safe
from dotenv import load_dotenv


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


class SafeShellTool(ShellTool):
    def run(self, command: str) -> str:
        if is_command_safe(command):
            return super().run(command)
        else:
            return "Unsafe Command Detected.."
        
shell_tool = SafeShellTool()
shell_tool.description = (
    "Useful for running Linux security audit commands like 'netstat', "
    "ufw status', 'find / -perm -o=w', etc. Only safe commands are allowed."
)

tools = [
    Tool(
        name="SecureShell",
        func=shell_tool.run,
        description=shell_tool.description
    )
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)


print("\n Terminal Security Agent (type 'exit' to quit)\n")


while True:
    user_input = input("Ask: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting..")
        break

    result = agent.run(user_input)
    print(f"\n Result:\n{result}\n")