from PySide6.QtWidgets import QDialog, QHBoxLayout, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap, QFont, QPalette, QFontDatabase
import random
import os
import requests

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.setStyleSheet("""
            QLineEdit {
                background-color: dark-grey;
                color: aqua;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

        self.w = None
        self.setWindowTitle("Pokedex")        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
      
        bgImg = QPixmap("assets/landing.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, bgImg)
        self.setPalette(palette)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.pokedex = QLabel(self)
        self.pokedex.setGeometry(250,0,600,500)

        self.imgLabel = QLabel(self)
        self.imgLabel.setVisible(False)
        self.imgLabel.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.imgLabel.setGeometry(470,50,200,200)
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        self.pokemonName =QLabel(self)
        self.pokemonName.setVisible(False)
        self.pokemonName.setText("pokeName")
        self.pokemonName.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.pokemonName.setGeometry(470,10,200,30)

        self.infoLabel1 = QLabel(self)
        self.infoLabel1.setVisible(False)
        self.infoLabel1.setText("infoLabel1")
        self.infoLabel1.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.infoLabel1.setGeometry(365,260,200,70)

        self.infoLabel2 = QLabel(self)
        self.infoLabel2.setVisible(False)
        self.infoLabel2.setText("infoLabel2")
        self.infoLabel2.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.infoLabel2.setGeometry(575,260,200,70)

        self.pokemonAbilities =QLabel(self)
        self.pokemonAbilities.setVisible(False)
        self.pokemonAbilities.setText("pokemonAbilities")
        self.pokemonAbilities.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.pokemonAbilities.setGeometry(365,340,200,70)
        
        self.pokemonType =QLabel(self)
        self.pokemonType.setVisible(False)
        self.pokemonType.setText("pokemonType")
        self.pokemonType.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.pokemonType.setGeometry(575,340,200,70)

        self.pokemonDetails =QLabel(self)
        self.pokemonDetails.setVisible(False)
        self.pokemonDetails.setText("pokemonDetails")
        self.pokemonDetails.setStyleSheet('QLabel { color: aqua ; background-color: dark-grey; border: 1px solid #BA263E; border-radius:10px ; padding-top: 5px;} ')
        self.pokemonDetails.setGeometry(365,420,410,50)

        enterButton = QPushButton("Search", self)
        enterButton.setGeometry(50, 300, 160, 43)
        enterButton.clicked.connect(self.searchPokemon)
        
        captureButton = QPushButton("Capture", self)
        captureButton.setGeometry(50, 350, 160, 43)
        captureButton.clicked.connect(self.capturePokemon)

        displayButton = QPushButton("Display", self)
        displayButton.setGeometry(50, 400, 160, 43)
        displayButton.clicked.connect(self.displayPokemon)

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    def displayDetails(self,pData):
        pDex = QPixmap("assets/pokedex.jpg")
        self.pokedex.setScaledContents(True)
        self.pokedex.setPixmap(pDex)

        name = pData['name'].upper()
        ability = random.choice(pData['abilities'])
        types = [typeData['type']['name'] for typeData in pData['types']]
        stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in pData['stats']]
        namePokemon = name
        pokemonAbilitiesbs = "Ability : \n "+str(ability['ability']['name'])
        typePokemon = f"Types: \n{', '.join(types)}\n"
        
        infoText1,infoText2 = "",""
        for i in stats[:3]:
            infoText1 = infoText1+str(i)+"\n" 
        for i in stats[3:]:
            infoText2 = infoText2+str(i)+"\n" 

        self.pokemonDetails.clear()
        self.pokemonDetails.setVisible(False)
        self.infoLabel1.setText(infoText1)
        self.infoLabel1.setVisible(True)
        self.infoLabel2.setText(infoText2)
        self.infoLabel2.setVisible(True)
        self.pokemonAbilities.setText(pokemonAbilitiesbs)
        self.pokemonAbilities.setVisible(True)
        self.pokemonName.setText(namePokemon)
        self.pokemonName.setVisible(True)
        self.pokemonType.setText(typePokemon)
        self.pokemonType.setVisible(True)
    
    def searchPokemon(self):
        self.pName = self.textbox.text().strip().lower()
        if not self.pName:
            return
        
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{self.pName}"
        self.response = requests.get(self.api_url)

        if self.response.status_code == 200:
            self.pData = self.response.json()
            self.displayDetails(self.pData)
            
            imgUrl = self.pData["sprites"]['other']['official-artwork']["front_default"]
            print(imgUrl)
            self.image = QPixmap()
            self.imgLabel.clear()
            self.imgLabel.setVisible(True)
            self.image.loadFromData(requests.get(imgUrl).content)
            self.imgLabel.setPixmap(self.image)
            self.imgLabel.setScaledContents(True)
            self.imgLabel.show()
        else:
            self.infoLabel1.clear()
            self.infoLabel1.setVisible(False)
            self.infoLabel2.clear()
            self.infoLabel2.setVisible(False)
            self.pokemonAbilities.clear()
            self.pokemonAbilities.setVisible(False)
            self.pokemonType.clear()
            self.pokemonType.setVisible(False)
            self.pokemonName.clear()
            self.pokemonName.setVisible(False)
            self.pokemonDetails.setText("Pokemon Not Found!")
            self.pokemonDetails.setVisible(True) 
            self.imgLabel.clear()
            self.imgLabel.setVisible(False) 

    # 2 #
    # Capture the Pokémon i.e. download the image.

    def capturePokemon(self):
        if hasattr(self, 'pData'):
            pName = self.pData['name'].upper()
            imgUrl = self.pData['sprites']['other']['official-artwork']['front_default']

            save_folder = "images/"
            os.makedirs(save_folder, exist_ok=True)
            dlPath = os.path.join(save_folder, f"{pName}.png")

            if os.path.exists(dlPath):
                self.pokemonDetails.setText(f"{pName} is already captured.")
                self.pokemonDetails.setVisible(True) 
                return

            response = requests.get(imgUrl)

            if response.status_code == 200:
                with open(dlPath, 'wb') as file:
                    file.write(response.content)
                self.pokemonDetails.setText(f"Captured {pName}")
                self.pokemonDetails.setVisible(True)
            else:
                self.pokemonDetails.setText(f"Failed to capture {pName}")
                self.pokemonDetails.setVisible(True)
        else:
            self.pokemonDetails.setText("No Pokémon to capture.")
            self.pokemonDetails.setVisible(True)
        
    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
            
    def displayPokemon(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Captured Pokémon")
        layout = QVBoxLayout()
        imgFiles = [f for f in os.listdir("images/") if f.endswith(".png")]

        self.curImgIndex = 0

        self.imgLabel = QLabel()
        self.displayImg()
        layout.addWidget(self.imgLabel)
        btnLayout = QHBoxLayout()
        preBtn = QPushButton("Previous")
        nextBtn = QPushButton("Next")

        def preImg():
            self.curImgIndex -= 1
            if self.curImgIndex < 0:
                self.curImgIndex = len(imgFiles) - 1
            self.displayImg()
        def nextImg():
            self.curImgIndex += 1
            if self.curImgIndex >= len(imgFiles):
                self.curImgIndex = 0
            self.displayImg()

        preBtn.clicked.connect(preImg)
        nextBtn.clicked.connect(nextImg)
        btnLayout.addWidget(preBtn)
        btnLayout.addWidget(nextBtn)
        layout.addLayout(btnLayout)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def displayImg(self):
        imgFiles = [f for f in os.listdir("images/") if f.endswith(".png")]
        if not imgFiles:
            self.imgLabel.clear()
            return
        curImgFile = imgFiles[self.curImgIndex]
        imgPath = os.path.join("images/", curImgFile)
        pixmap = QPixmap(imgPath)
        self.imgLabel.setPixmap(pixmap.scaledToHeight(300))

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())