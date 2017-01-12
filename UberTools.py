from PyQt5.QtWidgets import *
from PyQt5.Qt import QFileDialog
from PyQt5.Qt import QIcon
from window1 import Ui_MainWindow
from window2 import Ui_Dialog
from window3 import Ui_Dialog1
import sys
import os
import subprocess
import glob
import stat

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setWindowIcon(QIcon(r'C:\Users\abraham.cacoulides\PycharmProjects\UberTools\app.ico'))
        self.setupUi(self)
        self.dwgs_list = []
        self.ok_button.clicked.connect(self.OnButtonClick)
        self.go_button.clicked.connect(self.OnButtonClick1)
        self.browse_cb.clicked.connect(self.cb)
        self.browse_button.clicked.connect(self.load_file)
        self.browse_button_2.clicked.connect(self.load_file1)
        self.ok_button_2.clicked.connect(self.WblockScriptGenerator)
        self.go_button_2.clicked.connect(self.OnGoButtonClick)
        self.lock_unlocked_pb.clicked.connect(self.UnlockButtonClick)
        self.actionAbout.triggered.connect(self.About)
        self.actionHow_to_use.triggered.connect(self.HowTo)
        self.toerase=[]
        self.blocked = False

    def About(self):
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def HowTo(self):
        dialog = QDialog()
        dialog.ui = Ui_Dialog1()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def cb(self):
        if self.browse_cb.isChecked():
            self.browse_button.setEnabled(True)
        else:
            self.browse_button.setDisabled(True)

    def OnButtonClick(self):
        self.ScriptGenerator()

    def OnButtonClick1(self):  
        os.chdir(ultimate_path)
        try:
            subprocess.call (['C:\\r13\\win\\acad.exe', 'TITLE.dwg', scr_location + scr_name])
        except:
            subprocess.call(['C:\\Program Files\\Autodesk\\AutoCAD 2014\\acad.exe', 'TITLE.dwg', scr_location + scr_name])
        self.dialog_label.setText("The Titles for Job #"+ job_number + separator1 + u" had been updated")
        self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
        if scr_location  + scr_name in self.toerase:
            pass
        else:
            self.toerase.append(scr_location  + scr_name)

    def UnlockButtonClick(self):
        for i in self.dwgs_list:
            os.chmod(i, stat.S_IWRITE)
        self.dialog_label.setText("Your dwgs have been unlocked,\n If you'd like to change the titles now click 'Go!'")
        self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
        self.lock_unlocked_pb.setDisabled(True)
        self.go_button.setEnabled(True)
        self.blocked=False

    def OnGoButtonClick(self):
        os.chdir(self.path)
        try:
            subprocess.call (['C:\\r13\\win\\acad.exe', 'TITLE.dwg', self.path + 'wblockscript.scr'])
        except:
            subprocess.call(
                ['C:\\Program Files\\Autodesk\\AutoCAD 2014\\acad.exe', 'TITLE.dwg', self.path + 'wblockscript.scr'])
        self.dialog_label.setText("The drawings had been updated")
        self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
        if self.path + 'wblockscript.scr' in self.toerase:
            pass
        else:
            self.toerase.append(self.path + 'wblockscript.scr')

    def load_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        os.chdir(r'C:\r13\dwg\\')
        self.directory = dialog.getExistingDirectory(self, 'Choose Folder', os.path.curdir)
        self.browse_edit.setText(self.directory)

    def load_file1(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        os.chdir(r'C:\r13\dwg\\')
        self.directory = dialog.getExistingDirectory(self, 'Choose Folder', os.path.curdir)
        self.browse_edit_2.setText(self.directory)
        self.dialog_label_2.setText("Click 'OK!'")
        self.dialog_label_2.setStyleSheet("color:#ffffff;background-color:#0000ff;")
        self.ok_button_2.setEnabled(True)

    def ScriptGenerator(self):
        self.dialog_label.setText("Let's generate that Script")
        self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
        global job_number
        global separator1
        job_number= self.job_num_edit.text()#job_number lo uso para eliminar lo que esta antes del -
        separator= self.separator_edit.text()#separator se inluye para poder determinar si el job es simplex o duplex o group
        global job_number_separator
        job_number_separator=job_number+separator
        if self.separator_edit.text()=="-":
            separator1=""
        else:
            separator1= self.separator_edit.text()#separator se inluye para poder determinar si el job es simplex o duplex o group
        n=0 #variable usada para llevar la cuenta del while que crea la lista del numero de pagina
        if job_number=="" or len(job_number) != 5 or separator=="" or len(separator) != 1:
            self.dialog_label.setText("Please review your inputs")
            self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
            self.job_num_edit.focusWidget()
        elif self.browse_cb.isChecked() and self.browse_edit=="":
            self.dialog_label.setText("Please provide a path to the Job")
            self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
            self.browse_edit.focusWidget()
        else:
            global scr_location
            global scr_name
            global ultimate_eng_path
            global ultimate_path
            if self.browse_cb.isChecked():
                scr_location = self.browse_edit.text() + '\\'
            else:
                scr_location=r'C:\r13\dwg'+'\\'+job_number+'\\'
            scr_name = 'TitleScript'+separator1+'.scr'
            eng_path=scr_location+'eng'+separator1+'.eng'
            eng_path1=scr_location+job_number+"\\"+'eng'+separator1+'.eng'
            if os.path.exists(eng_path)==True:
                ultimate_eng_path=eng_path
                ultimate_path=scr_location
            elif os.path.exists(eng_path1)==True:
                ultimate_eng_path = eng_path1
                ultimate_path = scr_location+job_number+"\\"
            else:
                pass
            try:
                with open(scr_location+scr_name, "w") as t:#abre text.txt en escribir
                    try:
                        with open(ultimate_eng_path,"r") as eng:#abre eng.txt en leer
                            lines_lst = [ line.split('\t') for line in eng.read().splitlines() ] #inserta cada linea de eng en una lista
                            pg_num_lst = []
                            while n < len(lines_lst):
                                if lines_lst[n][0] == "Printed" or lines_lst[n][0] == "":#este if es para brincarse las lineas vacias y omitir la palabra Printed
                                    n+=1
                                else:
                                    pg_num_lst.append((str(lines_lst[n][0]).split(str(job_number)+separator.lower()))[1])
                                    n+=1
                            c=0#lleva la cuenta para seguir escribiendo codigo al archivo
                            for line in lines_lst:
                                if line[0] == str(job_number)+separator.lower()+"CP" or line[0] == str(job_number)+separator.lower()+"N" or line[0] == "Printed":#este if es para no ponerle title block a la portada ni a la N
                                    c+=1
                                    if line[0] != "Printed":
                                        self.dwgs_list.append(ultimate_path + str(line[0]) + '.dwg')
                                elif c < len(pg_num_lst):
                                    t.write("fileopen"+"\n")
                                    t.write('"'+ultimate_path+str(line[0])+'.dwg"'+"\n")
                                    t.write("(load "+'"DDTITLE"'+")(TITLE 'INS)"+"\n")
                                    t.write(pg_num_lst[c]+"\n")
                                    t.write("_qsave"+"\n")
                                    t.write("\n"+"\n")
                                    c+=1
                                    self.dwgs_list.append(ultimate_path+str(line[0])+'.dwg')
                                    if (os.access(ultimate_path+str(line[0])+'.dwg', os.W_OK) == 0):
                                        self.lock_unlocked_pb.setEnabled(True)
                                        self.blocked = True
                            t.write("quit"+"\n")
                            if self.blocked:
                                self.dialog_label.setText("Done, the script has been generated but your dwgs are READ-ONLY. \n Press the lock to unlock them")
                                self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
                            else:
                                self.dialog_label.setText("Done, the script has been generated. \n If you'd like to change the titles now click 'Go!'")
                                self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
                                self.go_button.setEnabled(True)
                    except:
                        self.dialog_label.setText("Unable to locate ENG File")
                        self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")
            except:
                self.dialog_label.setText("Unable to locate Folder")
                self.dialog_label.setStyleSheet("color:#ffffff;background-color:#0000ff;")

    def WblockScriptGenerator(self):
        path1 = self.browse_edit_2.text()+'\\'+'*.dwg'
        self.path = self.browse_edit_2.text()+'\\'
        with open(self.path+'\\'+'wblockscript.scr', "w") as w:
            for fname in glob.glob(path1):
                if fname == self.path+'TITLE.dwg':
                    pass
                else:
                    w.write('OPEN\n')
                    w.write('"'+fname+'"'+'\n')
                    w.write("WBLOCK\n")
                    w.write('"'+fname+'"'+'\n')
                    w.write("Y\n")
                    w.write("\n")
                    w.write("0,0\n")
                    w.write("ALL\n")
                    w.write("\n")
                    w.write("QUIT\n")
                    w.write("Y\n")
        self.go_button_2.setEnabled(True)
        self.dialog_label_2.setText("Click 'Go!'")
        self.dialog_label_2.setStyleSheet("color:#ffffff;background-color:#0000ff;")

    def closeEvent(self, event):
        for i in range(0,len(self.toerase)):
            try:
                os.remove(self.toerase[i])
            except:
                print("except")
        event.accept()
    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())