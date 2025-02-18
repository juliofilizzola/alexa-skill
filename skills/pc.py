import os


def handle_intent(intent):
    commands = {
        "TurnOnPCIntent": ("wakeonlan <MAC_ADDRESS>", "Ligando o computador."),
        "TurnOffPCIntent": ("shutdown /s /t 1", "Desligando o computador.")
    }

    command, response = commands.get(intent, (None, "Comando não reconhecido."))

    if command:
        os.system(command)
    return {"response": response}
