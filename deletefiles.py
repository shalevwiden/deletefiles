import os
import subprocess


def clearfiles(folderpath,filetype,avoid):
    '''
    This function will delete any file with a given filetype parameter in the path specified by the folderpath parameter.
    In addition it will avoid files in a list passed in the avoid parameter.
    '''

    
    for root,folders,files in os.walk(folderpath):
        # print(f'Root:{root}\n')
        # print(f'Folder {folders}\n')
        # print(f'Files {files}\n')
        for file in files:
            if file.endswith(filetype):
                fullpath=os.path.join(root,file)

            
                print(f'{filetype} file:\n     {fullpath}')
                # os.remove must take a full path
                if not any(avoiditem in file for avoiditem in avoid):
                    os.remove(fullpath)


avoid=['important.txt']

