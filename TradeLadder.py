from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# load the ui file
		uic.loadUi("TradeLadder.ui", self)

		# Define our widgets

		# set column widths
		self.tableWidget.setColumnWidth(0, 200)  # Volume
		self.tableWidget.setColumnWidth(1, 200)  # Buy Orders
		self.tableWidget.setColumnWidth(2, 100)  # Bid Size
		self.tableWidget.setColumnWidth(3, 100)  # Price
		self.tableWidget.setColumnWidth(4, 100)  # AskSize
		self.tableWidget.setColumnWidth(5, 200)  # SellOrders
		self.tableWidget.setColumnWidth(6, 200)  # OpenPL

		# load some data
		self.loadData()

		# show the app
		self.show()
	
	# get some pseudo data
	data = [ 
		#    0            1               2            3                4              5               6
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.50, "AskSize":"", "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.49, "AskSize":"", "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":5, "Price":221.48, "AskSize":"", "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.47, "AskSize":180, "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":300, "Price":221.46, "AskSize":"", "SellOrders":"", "OpenPL":""},
		{"Volume":1321, "BuyOrders":"", "BidSize":180, "Price":221.45, "AskSize":279, "SellOrders":"", "OpenPL":450.25},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.44, "AskSize":300, "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":10, "Price":221.43, "AskSize":10, "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.42, "AskSize":2, "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.41, "AskSize":"", "SellOrders":"", "OpenPL":""},
		{"Volume":"", "BuyOrders":"", "BidSize":"", "Price":221.40, "AskSize":"", "SellOrders":"", "OpenPL":""},
	] 

	# refactored this code to clean up the loadData fn
	def setItemDataAndColor(self, data, bgColor, fgColor=(255, 255, 255)):
		(bgR, bgG, bgB) = bgColor
		(fgR, fgG, fgB) = fgColor
		strData = str(data)
		item = QtWidgets.QTableWidgetItem(strData)
		item.setBackground(QtGui.QColor(bgR, bgG, bgB))
		brush = QtGui.QBrush(QtGui.QColor(fgR, fgG, fgB))
		brush.setStyle(QtCore.Qt.SolidPattern)
		item.setForeground(brush)
		return item

	def loadData(self):
		dkGray = (47, 47, 47)
		dkGreen = (0, 90, 0)
		dkRed = (90, 0, 0)
		medBlue = (0,78,135)
		profitColor = (0,200,0)
		lossColor = (200,0,0)
		self.tableWidget.setRowCount(len(self.data))
		row = 0
		for datum in self.data:
			# change the color if we actually have data
			if type(datum["OpenPL"]) == float:
				self.tableWidget.setItem(row, 0, self.setItemDataAndColor(datum["Volume"], medBlue))
			else:
				self.tableWidget.setItem(row, 0, self.setItemDataAndColor(datum["Volume"], dkGray))

			self.tableWidget.setItem(row, 1, self.setItemDataAndColor(datum["BuyOrders"], dkGray))
			self.tableWidget.setItem(row, 2, self.setItemDataAndColor(datum["BidSize"], dkGreen))
			self.tableWidget.setItem(row, 3, self.setItemDataAndColor(datum["Price"], dkGray))
			self.tableWidget.setItem(row, 4, self.setItemDataAndColor(datum["AskSize"], dkRed))
			self.tableWidget.setItem(row, 5, self.setItemDataAndColor(datum["SellOrders"], dkGray))
			# change the color if we actually have data
			if type(datum["OpenPL"]) == float:
				# set the color to reflect profit or loss
				if datum["OpenPL"] >= 0:
					self.tableWidget.setItem(row, 6, self.setItemDataAndColor(datum["OpenPL"], profitColor, (0,0,0)))
				else:
					self.tableWidget.setItem(row, 6, self.setItemDataAndColor(datum["OpenPL"], lossColor))
			else:
				self.tableWidget.setItem(row, 6, self.setItemDataAndColor(datum["OpenPL"], dkGray))

			row += 1


# initialize the app
app = QApplication(sys.argv)
UIWindow  = UI()

sys.exit(app.exec_())