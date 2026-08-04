import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QTextStream


from app.ui.main_window import MainWindow

from app.core.config import ensure_config

from app.utils.logger import logger




def load_theme(app):

    """
    Load giao diện QSS.
    """

    try:

        with open(
            "app/styles/theme.qss",
            "r",
            encoding="utf-8"
        ) as file:

            app.setStyleSheet(
                file.read()
            )


    except Exception as e:

        logger.warning(
            f"Không load được theme: {e}"
        )




def main():


    try:


        ensure_config()



        app = QApplication(
            sys.argv
        )


        app.setApplicationName(
            "GS1 Scanner"
        )


        app.setOrganizationName(
            "GS1Scanner"
        )



        load_theme(
            app
        )



        window = MainWindow()



        window.show()



        sys.exit(
            app.exec()
        )



    except Exception as e:


        logger.exception(
            e
        )

        raise




if __name__ == "__main__":

    main()