import os
import platform as pl
import datetime as dt


class Logger:
    def __init__(self):
        global now
        now = dt.datetime.now()
        filename = pl.node() + '_' + now.strftime('%Y%m%d')+'.txt'
        self.fileName = filename

    def checkLogFilePath(self):
        result = ''
        try:
            if os.path.exists(os.getcwd()+'\\LogFiles'):
                if os.path.exists(os.getcwd()+'\\LogFiles\\' + self.fileName):
                    result = os.getcwd()+'\\LogFiles\\' + self.fileName
                else:
                    logfile = open(self.fileName, 'xt')
                    logfile.close()
                    result = os.getcwd()+'\\LogFiles\\' + self.fileName
            else:
                os.mkdir(os.getcwd()+'\\LogFiles')
                logfile = open(os.getcwd()+'\\LogFiles\\' +
                               self.fileName, 'xt')
                logfile.close()
                result = os.getcwd()+'\\LogFiles\\' + self.fileName
        except:
            result = 'Error during file or folder creation'
        finally:
            return result

    def logIt(self, msgText):
        result = ''
        currentlogFile = self.checkLogFilePath()
        try:
            if currentlogFile != 'Error during file or folder creation':
                logfile = open(currentlogFile, 'a')
                logfile.writelines(now.strftime('%H%M%S')+'\t'+msgText + '\n')
                logfile.close()
                result = True
            else:
                result = False
        except:
            result = 'Error happend during appending log to file'
        finally:
            return result

    def removeLogFile(self, filepath):
        delresult = ''
        try:
            result = os.remove(filepath)
            if str(result) == 'None':
                delresult = 'File Deleted!'
            else:
                delresult = 'File is not Deleted!'
        except:
            delresult = 'Error happend durign deleting proccess.'
        finally:
            return delresult
