from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import pandas as pd


class Ui_MainWindow(object):

    def datafrane(self):
        df = pd.read_csv('parsed666.csv', encoding='cp1251')
        df = pd.DataFrame(df)

        for i in range(len(df['lats'])):
            df['lats'][i] = (df['lats'][i])[2:-2].strip()
        for r in range(len(df['lons'])):
            df['lons'][r] = (df['lons'][r])[2:-2].strip()
        for j in range(len(df['name'])):
            df['name'][j] = (df['name'][j])[2:-2].strip()
        for z in range(len(df['name'])):
            df['places'][z] = (df['places'][z])[2:-2].strip()
        for w in range(len(df['types'])):
            df['types'][w] = (df['types'][w])[2:-2].strip()

        df['lats'] = pd.to_numeric(df['lats'])
        df['lons'] = pd.to_numeric(df['lons'])

        m = folium.Map(location=[49.2320162, 28.467975], tiles="OpenStreetMap", zoom_start=6)

        for l in range(0, len(df['lats'])):
            if df['places'][l] == str(self.comboBox.currentText()):
                if str(self.comboBox_2.currentText()) == 'Все варианты':
                    folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l]).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Архитектура":
                    if df['types'][l].find('Архитектура') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='green')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "История":
                    if df['types'][l].find('История') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='red')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Музеи":
                    if df['types'][l].find('Музеи') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='purple')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Природа":
                    if df['types'][l].find('Природа') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='orange')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Улицы, площади, видовые места":
                    if df['types'][l].find('Улицы, площади, видовые места') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='darkred')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Религия":
                    if df['types'][l].find('Религия') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='lightred')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Монументы и памятники":
                    if df['types'][l].find('Монументы и памятники') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='beige')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Развлечения":
                    if df['types'][l].find('Развлечения') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='darkblue')).add_to(m)
                elif str(self.comboBox_2.currentText()) == "Активный отдых":
                    if df['types'][l].find('Активный отдых') != -1:
                        folium.Marker(location=[df['lats'][l], df['lons'][l]], popup=df['name'][l],icon=folium.Icon(color='pink')).add_to(m)

        # Save it as html
        m.save('312_markers_on_folium_map1.html')

        url = 'file:///C:/Users/Roman/PycharmProjects/2%20%D0%9A%D1%83%D1%80%D1%81/project/312_markers_on_folium_map1.html'


        self.browser = QWebEngineView()
        self.browser.load(QUrl(url))
        self.browser.show()


    def Search(self):
        self.road_a = self.lineEdit.text()
        self.road_b = self.lineEdit_2.text()

        self.url = 'https://www.google.com.ua/maps/dir/' + self.road_a + '/' + self.road_b

        self.browser = QWebEngineView()
        self.browser.setGeometry(400,200,1000,800)
        self.browser.load(QUrl(self.url))
        self.browser.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 437)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 140, 381, 191))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 361, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Search)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 171, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 60, 171, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 171, 31))
        self.label_2.setObjectName("label_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 140, 381, 191))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 361, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.datafrane)

        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 171, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Львов","Киев", "Винница",
                   "Одесса", "Донецк", "Житомир", "Запорожье", "Ивано-Франковск", "Кропивницкий",
                    "Луганск", "Луцк", "Николаев","Полтава","Ровно","Сумы","Тернополь","Ужгород","Харьков","Херсон",
                    "Хмельницкий","Черкассы","Чернигов","Черновцы","Днепр"])

        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 60, 171, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Все варианты","Архитектура","История","Музеи","Природа",
                                  "Улицы, площади, видовые места","Религия",
                                  "Монументы и памятники","Развлечения","Активный отдых"])

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 171, 31))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Туристический гид"))
        self.groupBox.setTitle(_translate("MainWindow", "Прокладываем маршрут"))
        self.pushButton.setText(_translate("MainWindow", "Проложить маршрут"))
        self.label.setText(_translate("MainWindow", "Выберите пункт отправки"))
        self.label_2.setText(_translate("MainWindow", "Выберите пункт прибытия"))
        self.groupBox_2.setTitle(_translate("MainWindow", "поиск мест"))
        self.pushButton_2.setText(_translate("MainWindow", "Поиск"))
        self.label_3.setText(_translate("MainWindow", "Выберите город поиска"))
        self.label_4.setText(_translate("MainWindow", "Категорию"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())