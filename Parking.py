import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #Liste des places occupée ou disponible
        Places = [0 for x in range(70)]
        
        #Creation variables
        labelPlace = []
        buttonPlace = []
        xPlaceA = 0
        xPlaceB = 0
        
        #Bouton prendre ou quitter un place
        self.buttonInPark = tk.Button(master,text="Prendre une place",width=20,height=3,fg='green', bg='#bbbbbb', command = lambda:accesPlace(), font=('Helvetica bold',10))
        self.buttonInPark.place(x=520, y=160)
        self.buttonOutPark = tk.Button(master,text="Quitter une place",width=20,height=3,fg='red', bg='#bbbbbb', command = lambda:quitPlace(), font=('Helvetica bold',10))
        self.buttonOutPark.place(x=750, y=160)

        #Affichage du nombre de place disponible 
        nbPLaceDiosponible = "Place(s) restante : "+str(Places.count(0))
        self.nbPlaceDispo = tk.Label(master,text=nbPLaceDiosponible,width=20,height=2,fg = 'black', font=('Helvetica bold',10))
        self.nbPlaceDispo.place(x=3, y=170)
        
        #Creation des places verte a l'ouverture du programme
        for i in range(70):
            if i < 35 :
                numeroVariable = str(i+1)
                nameLabel = "A"+numeroVariable
                textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = '#80b918')
                labelPlace.append(textLabel)
                textLabel.place(x=xPlaceA, y=0)
                xPlaceA = xPlaceA + 42
            else:
                nameLabel = "B"+str(i+1)
                textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = '#80b918')
                labelPlace.append(textLabel)
                textLabel.place(x=xPlaceB, y=100)
                xPlaceB = xPlaceB + 42
        
        
        
        #Fonction pour detruire toute les places
        def destroy():
            if labelPlace:
                array_length = len(labelPlace)
                for i in range(array_length):
                    labelPlace[i].destroy()
                labelPlace.clear()
            if buttonPlace:
                array_length = len(buttonPlace)
                for i in range(array_length):
                    buttonPlace[i].destroy()
                buttonPlace.clear()



        #Fonction pour quitter le parking (la ou nous pouvons cliquer sur les places)
        def quitPark(place,quitOrAcces):
            try:
                self.MessageCenter.destroy()
            except AttributeError:
                print("noError")

            destroy()
            
            xPlaceA2 = 0
            xPlaceB2 = 0
            
            self.buttonInPark = tk.Button(master,text="Prendre une place",width=20,height=3,fg='green', bg='#bbbbbb', command = lambda:accesPlace(), font=('Helvetica bold',10))
            self.buttonInPark.place(x=520, y=160)
            self.buttonOutPark = tk.Button(master,text="Quitter une place",width=20,height=3,fg='red', bg='#bbbbbb', command = lambda:quitPlace(), font=('Helvetica bold',10))
            self.buttonOutPark.place(x=750, y=160)
            
            #Affichage du nombre de place disponible
            try:
                if self.nbPlaceDispo :
                    self.nbPlaceDispo.destroy()
            except AttributeError:
                print("noError")
            nbPLaceDiosponible = "Place(s) restante : "+str(Places.count(0))
            self.nbPlaceDispo = tk.Label(master,text=nbPLaceDiosponible,width=20,height=2,fg = 'black', font=('Helvetica bold',10))
            self.nbPlaceDispo.place(x=3, y=170)
            
            if quitOrAcces == "acces":
                txtMessageLabel = ""
                if place < 35 :
                    txtMessageLabel = "Merci de votre confiance,vous avez choisi la place A"+str(place+1)
                else:
                    txtMessageLabel = "Merci de votre confiance,vous avez choisi la place B"+str(place+1)
                self.MessageCenter = tk.Label(master,text=txtMessageLabel,width=50,height=2,fg = 'black', font=('Helvetica bold',10))
                self.MessageCenter.place(x=535, y=55)
            else:
                self.MessageCenter = tk.Label(master,text="Merci de votre confiance, au revoir",width=50,height=2,fg = 'black', font=('Helvetica bold',10))
                self.MessageCenter.place(x=535, y=55)
    
            #Re Creation des places non cliquable
            for i in range(70):
                if i < 35:
                    numeroVariable = str(i+1)
                    nameLabel = "A"+numeroVariable
                    if Places[i] == 0:
                        textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = '#80b918')
                    else:
                        textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = 'red')
                    labelPlace.append(textLabel)
                    textLabel.place(x=xPlaceA2, y=0)
                    xPlaceA2 = xPlaceA2 + 42
                else:
                    nameLabel = "B"+str(i+1)
                    if Places[i] == 0:
                        textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = '#80b918')
                    else:
                        textLabel = tk.Label(master,text=nameLabel,width=3,height=3,bg = 'red')
                    labelPlace.append(textLabel)
                    textLabel.place(x=xPlaceB2, y=100)
                    xPlaceB2 = xPlaceB2 + 42



         #Fonction pour changer la couleur et l'etat des places (libre ou occuper)          
        def changeColor(place, quitOrAcces):
            if quitOrAcces == "acces":
                if Places[place] == 0:
                    try:
                         self.MessageCenter.destroy()
                    except AttributeError:
                        print("noError")
                    Places[place] = 1
                    buttonPlace[place]['bg'] = 'red'
                    quitPark(place,quitOrAcces)
                else:
                    try:
                         self.MessageCenter.destroy()
                    except AttributeError:
                        print("noError")
                    self.MessageCenter = tk.Label(master,text="Cette place n'est pas disponible, veulliez selectionner une autre place",width=65,height=2,fg = 'red', font=('Helvetica bold',10))
                    self.MessageCenter.place(x=520,y=60)
            else:
                if Places[place] == 1:
                    try:
                         self.MessageCenter.destroy()
                    except AttributeError:
                        print("noError")
                    Places[place] = 0
                    buttonPlace[place]['bg'] = '#80b918'
                    quitPark(place,quitOrAcces)
                else:
                    try:
                         self.MessageCenter.destroy()
                    except AttributeError:
                        print("noError")
                    self.MessageCenter = tk.Label(master,text="Cette place ne peux pas etre quitter",width=50,height=2,fg = 'red', font=('Helvetica bold',10))
                    self.MessageCenter.place(x=550,y=60)
                    
                    
                    
        #Fonction pour occuper une place libre           
        def accesPlace():
            if 0 in Places :
                try:
                    self.MessageCenter.destroy()
                except AttributeError:
                    print("noError")
                    
                destroy()
                
                xPlaceA1 = 0
                xPlaceB1 = 0
                
                self.buttonInPark.destroy()
                self.buttonOutPark.destroy()
                self.MessageCenter = tk.Label(master,text="Veuillez choisir votre place en cliquant dessus",width=50,height=2,fg = 'black', font=('Helvetica bold',10))
                self.MessageCenter.place(x=540, y=55)
                
                
                #Creation des places cliquable
                for i in range(70):
                    if i < 35 :
                        nameButton = "A"+str(i+1)
                        if Places[i] == 0:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = '#80b918', command = lambda i=i: changeColor(i,"acces"),font=('Helvetica bold',8))
                        else:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = 'red', command = lambda i=i: changeColor(i,"acces"),font=('Helvetica bold',8))
                        buttonPlace.append(textButton)
                        textButton.place(x=xPlaceA1, y=0)
                        xPlaceA1 = xPlaceA1 + 42
                    else:
                        nameButton = "B"+str(i+1)
                        if Places[i] == 0:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = '#80b918',command = lambda i=i: changeColor(i,"acces"),font=('Helvetica bold',8))
                        else:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = 'red',command = lambda i=i: changeColor(i,"acces"),font=('Helvetica bold',8))
                        buttonPlace.append(textButton)
                        textButton.place(x=xPlaceB1, y=100)
                        xPlaceB1 = xPlaceB1 + 42
            else :
                try:
                    self.MessageCenter.destroy()
                except AttributeError:
                    print("noError")
                self.MessageCenter = tk.Label(master,text="Parking plein",width=10,height=2,fg = 'red')
                self.MessageCenter.place(x=640,y=55)  
                    
        #Fonction pour quitter une place occuper            
        def quitPlace():
            if 1 in Places :
                try:
                    self.MessageCenter.destroy()
                except AttributeError:
                    print("noError")
                    
                destroy()
                
                xPlaceA1 = 0
                xPlaceB1 = 0
                
                self.buttonInPark.destroy()
                self.buttonOutPark.destroy() 
                self.MessageCenter = tk.Label(master,text="Veuillez quitter vôtre la place en cliquant dessus",width=40,height=2,fg = 'black', font=('Helvetica bold',10))
                self.MessageCenter.place(x=600, y=55)
                
                for i in range(70):
                    if i < 35 :
                        nameButton = "A"+str(i+1)
                        if Places[i] == 0:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = '#80b918', command = lambda i=i: changeColor(i,"quit"), font=('Helvetica bold',8))
                        else:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = 'red', command = lambda i=i: changeColor(i,"quit"), font=('Helvetica bold',8))
                        buttonPlace.append(textButton)
                        textButton.place(x=xPlaceA1, y=0)
                        xPlaceA1 = xPlaceA1 + 42
                    else:
                        nameButton = "B"+str(i+1)
                        if Places[i] == 0:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = '#80b918',command = lambda i=i: changeColor(i,"quit"), font=('Helvetica bold',8))
                        else:
                            textButton = tk.Button(master,text=nameButton,width=3,height=3,bg = 'red',command = lambda i=i: changeColor(i,"quit"), font=('Helvetica bold',8))
                        buttonPlace.append(textButton)
                        textButton.place(x=xPlaceB1, y=100)
                        xPlaceB1 = xPlaceB1 + 42
            else:
                try:
                    self.MessageCenter.destroy()
                except AttributeError:
                    print("noError")
                self.MessageCenter = tk.Label(master,text="Pas de place a quitter",width=20,height=2,fg = 'red', font=('Helvetica bold',10))
                self.MessageCenter.place(x=640,y=55)     
                         
                    
        
root = tk.Tk()
myapp = App(root)
root.title('Projet Parking')
root.geometry("1460x225")
myapp.mainloop()