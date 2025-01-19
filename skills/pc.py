import json
import socket
import struct

from config.config import get_env


def lambda_handler(event, context):
    request_type = event['request']['type']

    if request_type == "LaunchRequest":
        return on_launch(event)
    elif request_type == "IntentRequest":
        return on_intent(event)
    elif request_type == "SessionEndedRequest":
        return on_session_ended(event)


def on_launch(event):
    return build_response("Welcome to the PC control skill!")


def on_intent(event):
    intent_name = event['request']['intent']['name']

    if intent_name == "TurnOnPCIntent":
        mac_address = get_env("MAC_ADDRESS")  # Substitua pelo endereço MAC do seu PC
        send_wol_packet(mac_address)
        return build_response("Turning on your PC.")
    else:
        return build_response("I don't know that one.")


def on_session_ended(event):
    return {}


def build_response(speech_text):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech_text
            },
            'shouldEndSession': True
        }
    }


def send_wol_packet(mac_address):
    # Envia um pacote Wake-on-LAN para o endereço MAC especificado
    addr_byte = bytes.fromhex(mac_address.replace(':', ''))
    msg = b'\xff' * 6 + addr_byte * 16
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(msg, ('<broadcast>', 9))