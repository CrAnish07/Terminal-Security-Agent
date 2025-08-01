from whitelist import ALLOWED_COMMANDS


def is_command_safe(command: str) -> bool:
    for allowed in ALLOWED_COMMANDS:
        if command.strip().startswith(allowed):
            return True
        
    return False