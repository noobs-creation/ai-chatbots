"""
Standard ChatGPT
"""
from __future__ import annotations

# import base64
# import contextlib
import json
# import logging
import os
import os.path as osp
# import time
import uuid
# from functools import wraps
from os import environ
from os import getenv
import subprocess
# from typing import NoReturn
import pyttsx3
import requests
from httpx import AsyncClient
from OpenAIAuth import Authenticator
from OpenAIAuth import Error as AuthError
import random
import utils_chatgpt as t

#  https://chat.openai.com/backend-api/conversation


free_proxy = [
    "https://bypass.churchless.tech/api/",
    "https://gpt.pawan.krd/backend-api/",
    "https://api.pawan.krd/backend-api/",
    "https://bypass.churchless.tech/api/",
    "https://bypass.duti.tech/api/"
]

BASE_URL = str(free_proxy[3])


# BASE_URL = 'https://chat.openai.com/api/'

print(BASE_URL)

class Chatbot:
    """
    Chatbot class for ChatGPT
    """

    # @logger(is_timed=True)
    def __init__(
        self,
        config: dict[str, str],
        conversation_id: str | None = None,
        parent_id: str | None = None,
        session_client=None,
        lazy_loading: bool = False,
    ) -> None:
        """Initialize a chatbot

        Args:
            config (dict[str, str]): Login and proxy info. Example:
                {
                    "email": "OpenAI account email",
                    "password": "OpenAI account password",
                    "session_token": "<session_token>"
                    "access_token": "<access_token>"
                    "proxy": "<proxy_url_string>",
                    "paid": True/False, # whether this is a plus account
                }
                More details on these are available at https://github.com/acheong08/ChatGPT#configuration
            conversation_id (str | None, optional): Id of the conversation to continue on. Defaults to None.
            parent_id (str | None, optional): Id of the previous response message to continue on. Defaults to None.
            session_client (_type_, optional): _description_. Defaults to None.

        Raises: 
            Exception: _description_
        """
        user_home = getenv("HOME")
        if user_home is None:
            self.cache_path = osp.join(os.getcwd(), ".chatgpt_cache.json")
        

        self.config = config
        self.session = session_client() if session_client else requests.Session()
        
        self.conversation_id = conversation_id
        self.parent_id = parent_id
        self.conversation_mapping = {}
        self.conversation_id_prev_queue = []
        self.parent_id_prev_queue = []
        self.lazy_loading = lazy_loading

        self.__check_credentials()

    # @logger(is_timed=True)
    def __check_credentials(self) -> None:
        """Check login info and perform login

        Any one of the following is sufficient for login. Multiple login info can be provided at the same time and they will be used in the order listed below.
            - access_token
            - session_token
            - email + password

        Raises:
            Exception: _description_
            AuthError: _description_
        """
        if "access_token" in self.config:
            self.set_access_token(self.config["access_token"])
        elif "session_token" in self.config:
            pass
        elif "email" not in self.config or "password" not in self.config:
            error = t.AuthenticationError("Insufficient login details provided!")
            raise error
        if "access_token" not in self.config:
            try:
                self.login()
            except AuthError as error:
                raise error

    # @logger(is_timed=False)
    def set_access_token(self, access_token: str) -> None:
        """Set access token in request header and self.config, then cache it to file.

        Args:
            access_token (str): access_token
        """
        self.session.headers.clear()
        self.session.headers.update(
            {
                "Accept": "text/event-stream",
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "X-Openai-Assistant-App-Id": "",
                "Connection": "close",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://chat.openai.com/chat",
            },
        )
        self.session.cookies.update(
            {
                "library": "revChatGPT",
            },
        )

        self.config["access_token"] = access_token

        # email = self.config.get("email", None)
        # if email is not None:
        #     self.__cache_access_token(email, access_token)


    # @logger(is_timed=True)
    def login(self) -> None:
        if (
            "email" not in self.config or "password" not in self.config
        ) and "session_token" not in self.config:
            # log.error("Insufficient login details provided!")
            print('Insufficient login details provided!')
            raise Exception("Insufficient login details provided!")
        auth = Authenticator(
            email_address=self.config.get("email"),
            password=self.config.get("password")
            # password=self.config.get("password"),
            # proxy=self.config.get("proxy"),
        )
        if self.config.get("session_token"):
            # log.debug("Using session token")
            print('USING SESSION TOKEN')
            auth.session_token = self.config["session_token"]
            auth.get_access_token()
            if auth.access_token is None:
                del self.config["session_token"]
                self.login()
                return
        else:
            # log.debug("Using authenticator to get access token")
            print('USING AUTHENTICATOR TO GET ACCESS TOKEN')
            auth.begin()
            self.config["session_token"] = auth.session_token
            auth.get_access_token()

        self.set_access_token(auth.access_token)

    # @logger(is_timed=True)
    def ask(
        self,
        prompt: str,
        conversation_id: str | None = None,
        parent_id: str | None = None,
        timeout: float = 360,
    ) -> str:
        """Ask a question to the chatbot
        Args:
            prompt (str): The question
            conversation_id (str | None, optional): UUID for the conversation to continue on. Defaults to None.
            parent_id (str | None, optional): UUID for the message to continue on. Defaults to None.
            timeout (float, optional): Timeout for getting the full response, unit is second. Defaults to 360.

        Raises:
            Error: _description_
            Exception: _description_
            Error: _description_
            Error: _description_
            Error: _description_

        Yields:
            _type_: _description_
        """

        if parent_id is not None and conversation_id is None:
            # log.error("conversation_id must be set once parent_id is set")
            print('conversation_id must be set once parent_id is set')
            error = t.Error(
                source="User",
                message="conversation_id must be set once parent_id is set",
                code=t.ErrorType.USER_ERROR,
            )
            raise error

        if conversation_id is not None and conversation_id != self.conversation_id:
            # log.debug("Updating to new conversation by setting parent_id to None")
            print("Updating to new conversation by setting parent_id to None")
            self.parent_id = None

        conversation_id = conversation_id or self.conversation_id
        parent_id = parent_id or self.parent_id
        if conversation_id is None and parent_id is None:
            parent_id = str(uuid.uuid4())
            # log.debug("New conversation, setting parent_id to new UUID4: %s", parent_id)
            print("New conversation, setting parent_id to new UUID4: ", parent_id)

        
        data = {
            "action": "next",
            "messages": [
                {
                    "id": str(uuid.uuid4()),
                    "role": "user",
                    "author": {"role": "user"},
                    "content": {"content_type": "text", "parts": [prompt]},
                },
            ],
            "conversation_id": conversation_id,
            "parent_message_id": parent_id,
            "model": self.config.get("model")
            or (
                "text-davinci-002-render-paid"
                if self.config.get("paid")
                else "text-davinci-002-render-sha"
            ),
        }
        # log.debug("Sending the payload")
        # log.debug(json.dumps(data, indent=2))
        # print("Sending the payload")
        # print(json.dumps(data, indent=2))

        self.conversation_id_prev_queue.append(
            data["conversation_id"],
        )
        self.parent_id_prev_queue.append(data["parent_message_id"])
        response = self.session.post(
            url=f"{BASE_URL}conversation",
            data=json.dumps(data),
            timeout=timeout,
            stream=True,
        )
        self.__check_response(response)
        done: bool = False
        for line in response.iter_lines():
            # remove b' and ' at the beginning and end and ignore case
            line = str(line)[2:-1]
            if line.lower() == "internal server error":
                # log.error("Internal Server Error: %s", line)
                print("Internal Server Error: %s", line)
                error = t.Error(
                    source="ask",
                    message="Internal Server Error",
                    code=t.ErrorType.SERVER_ERROR,
                )
                raise error
            if line == "" or line is None:
                continue
            if "data: " in line:
                line = line[6:]
            if line == "[DONE]":
                done = True
                break

            line = line.replace('\\"', '"')
            line = line.replace("\\'", "'")
            line = line.replace("\\\\", "\\")

            try:
                line = json.loads(line)
            except json.decoder.JSONDecodeError:
                continue
            if not self.__check_fields(line) or response.status_code != 200:
                # log.error("Field missing", exc_info=True)
                # log.error(response.text)
                print("Field missing", exc_info=True)
                print(response.text)
                
                if response.status_code == 401:
                    error = t.Error(
                        source="ask",
                        message="Permission denied",
                        code=t.ErrorType.AUTHENTICATION_ERROR,
                    )
                    raise error
                elif response.status_code == 403:
                    error = t.Error(
                        source="ask",
                        message="Cloudflare triggered a 403 error",
                        code=t.ErrorType.CLOUDFLARE_ERROR,
                    )
                    raise error
                elif response.status_code == 429:
                   error = t.Error(
                        source="ask",
                        message="Rate limit exceeded",
                        code=t.ErrorType.RATE_LIMIT_ERROR,
                    )
                   raise error
                else:
                    error = t.Error(
                        source="ask",
                        message=line,
                        code=t.ErrorType.SERVER_ERROR,
                    )
                    raise error
            message: str = line["message"]["content"]["parts"][0]
            if message == prompt:
                continue
            conversation_id = line["conversation_id"]
            parent_id = line["message"]["id"]
            try:
                model = line["message"]["metadata"]["model_slug"]
            except KeyError:
                model = None
            # log.debug("Received message: %s", message)
            # log.debug("Received conversation_id: %s", conversation_id)
            # log.debug("Received parent_id: %s", parent_id)
            # print("Received message: %s", message)
            # print("Received conversation_id: %s", conversation_id)
            # print("Received parent_id: %s", parent_id)
            
            yield {
                "message": message.strip("\n"),
                "conversation_id": conversation_id,
                "parent_id": parent_id,
                "model": model,
            }
        if not done:
            pass
        self.conversation_mapping[conversation_id] = parent_id
        if parent_id is not None:
            self.parent_id = parent_id
        if conversation_id is not None:
            self.conversation_id = conversation_id

    # @logger(is_timed=False)
    def __check_fields(self, data: dict) -> bool:
        try:
            data["message"]["content"]
        except (TypeError, KeyError):
            return False
        return True

    # @logger(is_timed=False)
    def __check_response(self, response: requests.Response) -> None:
        """Make sure response is success

        Args:
            response (_type_): _description_

        Raises:
            Error: _description_
        """
        if response.status_code != 200:
            print(response.text)
            error = t.Error(
                source="OpenAI",
                message=response.text,
                code=response.status_code,
            )
            raise error

    # @logger(is_timed=True)
    def get_conversations(
        self,
        offset: int = 0,
        limit: int = 20,
        encoding: str | None = None,
    ) -> list:
        """
        Get conversations
        :param offset: Integer
        :param limit: Integer
        """
        url = f"{BASE_URL}conversations?offset={offset}&limit={limit}"
        response = self.session.get(url)
        self.__check_response(response)
        if encoding is not None:
            response.encoding = encoding
        data = json.loads(response.text)
        return data["items"]

    

    # @logger(is_timed=False)
    def reset_chat(self) -> None:
        """
        Reset the conversation ID and parent ID.

        :return: None
        """
        self.conversation_id = None
        self.parent_id = str(uuid.uuid4())

    


# @logger(is_timed=False)
# def configure() -> dict:
    # """
    # Looks for a config file in the following locations:
    # """
    # config_files = ["config.json"]
    # # if xdg_config_home := getenv("XDG_CONFIG_HOME"):
    # #     config_files.append(f"{xdg_config_home}/revChatGPT/config.json")
    # # if user_home := getenv("HOME"):
    # #     config_files.append(f"{user_home}/.config/revChatGPT/config.json")

    # if config_file := next((f for f in config_files if osp.exists(f)), None):
    #     with open(config_file, encoding="utf-8") as f:
    #         config = json.load(f)
    # else:
    #     print("No config file found.")
    #     raise Exception("No config file found.")
    # return config


def exit():
    """
    Exit the program
    """
    import sys

    print("Exiting program...")
    sys.exit(0)

# def speak(audio, lock):
#     lock.value = 1
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice',voices[1].id)
#     print(f"recorded : {audio}")
#     engine.say(audio)
#     engine.runAndWait()
#     lock.value = 0

# @logger(is_timed=False)
# def main_chatbot(lock, conversation_id_from_main_process, prompt):
def main_chatbot(prompt, conversation_id_from_main_process, parent_id_from_main_process):
    """
    Main function for the chatGPT program.
    """
    # conversation_id_from_main_process = str(uuid.uuid4())
    # parent_id_from_main_process = str(uuid.uuid4())
    config_files = ["config.json"]
    if config_file := next((f for f in config_files if osp.exists(f)), None):
        with open(config_file, encoding="utf-8") as f:
            config = json.load(f)
    else:
        print("No config file found.")
        raise Exception("No config file found.")


    if conversation_id_from_main_process is None and parent_id_from_main_process is None:    
        chatbot = Chatbot(
            config,
            # conversation_id=conversation_id_from_main_process,
            # parent_id=parent_id_from_main_process,
            conversation_id=config.get('conversation_id'),
            parent_id=config.get("parent_id"),
        )
    
    if conversation_id_from_main_process is not None and parent_id_from_main_process is not None:
        chatbot = Chatbot(
            config,
            conversation_id=conversation_id_from_main_process,
            parent_id=parent_id_from_main_process,
            # conversation_id=config.get('conversation_id'),
            # parent_id=config.get("parent_id"),
        )

    print()
    try:
        # while True:
        # print(f"{bcolors.OKBLUE + bcolors.BOLD}You: {bcolors.ENDC}")
        print("You: ",prompt)
        # prompt = input('ENTER YOUR TEXT:    ')
        # if prompt.startswith("!") and handle_commands(prompt):
        #     continue
        print()
        # print(f"{bcolors.OKGREEN + bcolors.BOLD}Chatbot: {bcolors.ENDC}")
        print('Chatbot: ')
        prev_text = ""
        temp_text = ""
        
        
        # print(data_main)
        # for data in data_main:
        #     print(data)
        for data in chatbot.ask(prompt):
            message = data["message"][len(prev_text) :]
            temp_text += message
            print(message, end="", flush=True)
            message = ""
            prev_text = data["message"]
        print(data)
        # print(bcolors.ENDC)
        # speak(temp_text, lock)
        print()
    except (KeyboardInterrupt, EOFError):
        exit()
    except BaseException as e:
        error = t.CommandError("command line program unknown error")
        raise error from e
    return temp_text, data["conversation_id"], data['parent_id']


# if __name__ == "__main__":
    # print(
    #     """
    #     ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
    #     Repo: github.com/acheong08/ChatGPT
    #     """,
    # )
    # print("Type '!help' to show a full list of commands")
    # print("Press Esc followed by Enter or Alt+Enter to send a message.")
    # main_chatbot()
