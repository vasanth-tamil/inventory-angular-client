from flask import current_app

class Model:

    def __init__(self) -> None:
        self.cursor = current_app.mysql.connection.cursor()

    def commit(self):
        current_app.mysql.connection.commit()

    def close(self):
        current_app.mysql.connection.close()