import streamlit
from loguru import logger

from config import log_file_name, log_file_max_size, log_clean_log_after


class QueryVerse:
    def __init__(self):
        try:
            # Initialize the logger
            logger.add(f"{log_file_name}", rotation=log_file_max_size, retention=log_clean_log_after, enqueue=True)
            self.st = streamlit
        except Exception as error:
            logger.error(str(error))
            print(str(error))

    def main(self):
        """
        Author - Lav Sharma
        Description - This is the main function which starts the chat page on the streamlit.
        """
        try:
            logger.info("Hi! You have successfully initialized main() function")
            self.st.title("Query Verse")

            prompt = self.st.chat_input("Say something")
            if prompt:
                self.st.chat_message("user").write(prompt)
                self.st.chat_message("assistant").write(f"Echo: {prompt}")
        except Exception as error:
            print(str(error))


if __name__ == "__main__":
    QueryVerse().main()
