
import pexpect
import subprocess
import sys
import os


class osprocess:

    ADD_USER_COMMAND = "adduser"
    DELETE_USER_COMMAND = "deluser"
    CHANGE_USER_PASS_COMMAND = "changepasswd"
    ADD_GROUP_COMMAND = "addgroup"
    DELETA_GROUP_COMMAND = "delgroup"
    ADD_USER_TO_GROUP_COMMAND = "addusergrp"
    DELETE_USER_FROM_GROUP_COMMAND = "delusergrp"
    output = ""
    erroroutput = ""
    execResult = True
    testMode = True # CHANGE TO False TO EXECUTE LINUX COMMANDS

    def __init__(self):
        self.command = None

    def execCommand(self):
        if (self.getCommand() != None and not self.testMode):
            self.execResult = False
            self.output = ""
            self.erroroutput = ""
            process = subprocess.Popen(self.getCommand(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.output = process.stdout.readline()
            self.erroroutput = process.stderr.readline()
            result = process.wait()
            print >> sys.stdout, "output: %s " % (self.output)
            print >> sys.stdout, "erroroutput: %s " % (self.erroroutput)
            print >> sys.stdout, "result: %s " % (result)
            if (len(self.erroroutput.rstrip()) == 0):
                self.execResult = True
            else:
                self.execResult = False
        return self.execResult

    def addUser(self, userName, userPass):
        self.command = []
        self.command.append("super")
        self.command.append(self.ADD_USER_COMMAND)
        self.command.append(userName)
        self.command.append(userPass)
        self.setCommand(self.command)
        return self.execCommand()

    def changeUserPass(self, userName, userPass):
        self.command = []
        self.command.append("super")
        self.command.append(self.CHANGE_USER_PASS_COMMAND)
        self.command.append(userName)
        self.command.append(userPass)
        self.setCommand(self.command)
        return self.execCommand()

    def deleteUser(self, userName):
        self.command = []
        self.command.append("super")
        self.command.append(self.DELETE_USER_COMMAND)
        self.command.append(userName)
        self.setCommand(self.command)
        return self.execCommand()

    def addGroup(self, nombreGrupo):
        self.command = []
        self.command.append("super")
        self.command.append(self.ADD_GROUP_COMMAND)
        self.command.append(nombreGrupo)
        self.setCommand(self.command)
        return self.execCommand()

    def deleteGroup(self, nombreGrupo):
        self.command = []
        self.command.append("super")
        self.command.append(self.DELETA_GROUP_COMMAND)
        self.command.append(nombreGrupo)
        self.setCommand(self.command)
        return self.execCommand()

    def addUserToGroup(self, userName, nombreGrupo):
        self.command = []
        self.command.append("super")
        self.command.append(self.ADD_USER_TO_GROUP_COMMAND)
        self.command.append(userName)
        self.command.append(nombreGrupo)
        self.setCommand(self.command)
        return self.execCommand()


    def deleteUserFromGroup(self, userName, nombreGrupo):
        self.command = []
        self.command.append("super")
        self.command.append(self.DELETE_USER_FROM_GROUP_COMMAND)
        self.command.append(userName)
        self.command.append(nombreGrupo)
        self.setCommand(self.command)
        return self.execCommand()


    def getCommand(self):
        return self.command


    def setCommand(self, command):
        self.command = command

    def getErrorMenssage(self):
        return self.errorMessage

    def setErrorMenssage(self, errorMessage):
        self.errorMessage = errorMessage
