#client management Dashboard Window 
import sys
import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView


class Dashboard(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 800, 600)

        #add a menu bar 
        menu_bar = self.menuBar()



        Admin_menu = menu_bar.addMenu("Admin")

        
        Admin_menu.addAction("Add Client")

        # Create a toolbar
        toolbar = self.addToolBar("Toolbar")

        '''
        # Create a label for the title
        title_label = QLabel("Client Management Dashboard")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label) '''

        # Create a table for displaying client data
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())