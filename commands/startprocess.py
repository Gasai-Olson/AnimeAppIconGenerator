from os import path, mkdir, rename
import sys
import shutil
from createicon import create

def startsetup(project, icon, image):
    icon = str(project[2])
    image = str(project[3])
    project = str(project[1])

     #create path to icon
    if path.isdir('../icons/' + project) == True:
        print('path already exist')
        overwrite = input("would you like to overwrite path? y/n")
        if overwrite == 'y' or overwrite == 'yes':
            shutil.rmtree('../icons/' + project)
        else:
            sys.exit()
    print(project)
    mkdir('../icons/' + project)
    newpath = '../icons/' + project + '/'

    #move images to icon file if exist == True
    icon = '../images/' + icon
    image = '../images/' + image
    if path.isfile(icon) == True and path.isfile(image) == True:
        rename(image, newpath + 'image.png')
        rename(icon, newpath + 'icon.png')
    else:
        #deletes folder to prevent duplicates
        shutil.rmtree('../icons/' + project)
        raise Exception('images do not exist in directory(../images/)')
    create(project)

startsetup(sys.argv,sys.argv,sys.argv)
