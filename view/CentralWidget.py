from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QSlider, QPushButton, QPlainTextEdit

from algorithm.CardanGrille import codeByCardanGrille, arrayToString, decodeByCardanGrille


class CentralWidget(QWidget):

    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        titleLabel = QLabel("Encryption algorithm <<Cardan Grille>>")

        self.grilleSizeLabel = QLabel("Small grille size (1):")
        self.grilleSizeSlider = QSlider(Qt.Horizontal)
        self.grilleSizeSlider.setRange(1, 10)
        self.grilleSizeSlider.setTickInterval(1)
        self.grilleSizeSlider.setPageStep(1)
        minLabel = QLabel(str(self.grilleSizeSlider.minimum()))
        maxLabel = QLabel(str(self.grilleSizeSlider.maximum()))
        maxLabel.setAlignment(Qt.AlignRight)

        self.originalTextLabel = QLabel("Original text (0 out of 4):")
        self.originalTextField = QLineEdit()
        self.originalTextField.setMaxLength(4)

        codeButton = QPushButton("Code")

        keyLabel = QLabel("Key:")
        self.keyField = QPlainTextEdit()

        codedTextLabel = QLabel("Coded text:")
        self.codedTextField = QPlainTextEdit()

        decodeButton = QPushButton("Decode")

        layout.addWidget(titleLabel, 0, 0, 1, 12)
        layout.addWidget(self.grilleSizeLabel, 1, 0, 1, 6)
        layout.addWidget(self.grilleSizeSlider, 2, 0, 1, 6)
        layout.addWidget(minLabel, 3, 0)
        layout.addWidget(maxLabel, 3, 5)
        layout.addWidget(self.originalTextLabel, 4, 0, 1, 8)
        layout.addWidget(self.originalTextField, 5, 0, 1, 8)
        layout.addWidget(codeButton, 5, 9, 1, 3)
        layout.addWidget(keyLabel, 6, 0, 1, 6)
        layout.addWidget(codedTextLabel, 6, 6, 1, 6)
        layout.addWidget(self.keyField, 7, 0, 1, 6)
        layout.addWidget(self.codedTextField, 7, 6, 1, 6)
        layout.addWidget(decodeButton, 8, 9, 1, 3)

        self.origSS = self.originalTextField.styleSheet()
        self.errSS = "border: 2px solid red;"

        self.grilleSizeSlider.valueChanged.connect(self.grilleSizeChanged)
        self.originalTextField.textChanged.connect(self.originalTextChanged)
        codeButton.clicked.connect(self.codeClick)
        decodeButton.clicked.connect(self.decodeClick)

        self.setLayout(layout)

    @pyqtSlot()
    def codeClick(self):
        originalText = self.originalTextField.text()
        grilleSize = self.grilleSizeSlider.value()

        if originalText:
            codedRes = codeByCardanGrille(originalText, grilleSize)

            key = arrayToString(codedRes[1])
            codedMsg = arrayToString(codedRes[0])

            self.keyField.setPlainText(key)
            self.codedTextField.setPlainText(codedMsg)

            self.originalTextField.setStyleSheet(self.origSS)
        else:
            self.originalTextField.setStyleSheet(self.errSS)

    @pyqtSlot()
    def decodeClick(self):
        key = self.keyField.toPlainText()
        codedMsg = self.codedTextField.toPlainText()

        if len(key) == len(codedMsg):
            decodedRes = decodeByCardanGrille(codedMsg, key)

            grilleSize = decodedRes[1] // 2
            decodedMsg = decodedRes[0]

            self.grilleSizeSlider.setValue(grilleSize)
            self.originalTextField.setText(decodedMsg)

            self.keyField.setStyleSheet(self.origSS)
            self.codedTextField.setStyleSheet(self.origSS)
        else:
            self.keyField.setStyleSheet(self.errSS)
            self.codedTextField.setStyleSheet(self.errSS)

    @pyqtSlot()
    def grilleSizeChanged(self):
        size = self.grilleSizeSlider.value()
        currentSize = len(self.originalTextField.text())

        self.grilleSizeLabel.setText(f"Small grille size ({str(size)}):")
        self.originalTextLabel.setText(f"Original text ({currentSize} out of {str(4*size**2)}):")
        self.originalTextField.setMaxLength(4*size**2)

    @pyqtSlot()
    def originalTextChanged(self):
        maxSize = self.originalTextField.maxLength()
        currentSize = len(self.originalTextField.text())

        self.originalTextLabel.setText(f"Original text ({currentSize} out of {maxSize}):")
