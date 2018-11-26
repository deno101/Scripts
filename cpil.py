#!/usr/bin/env python3
############################################################################
########### This is a Script that compiles and builds c programs ###########
########### The resultant executable has the same name as the source file ##
############################################################################

import subprocess
import sys


class App:
        def __init__(self,args):
            try:
                self.args = args[1]
            except IndexError:
                support()
                return
            self.output = self.rmext()
            self.main()

        def rmext(self):
            temp = self.args.split('.')
            fin = temp[0]
            return fin

        def main(self):
            output = subprocess.call(['gcc','-o',self.output,self.args])
            if not output == 0:
                sys.exit()
            else:
                extcmd = './'+str(self.output)
                subprocess.call(extcmd)


class support:
    def __init__(self,args):
        self.args = args[1]
        if self.args == '-h':
            self.help()
        elif self.args == '-v':
            self.version()
        else:
            print('Unsupported command\n'
                  'try cpil -h')

    def help(self):
        print("This Program compiles and executes c code\n"
              "Hoe to use:-\n"
              "\t cpil 'c file'\n"
              "('-v','-h')")

    def version(self):
        print("cpil version 1.0.0\n"
              "@author : Denniz101<Dennizwarui@gmail.com>")

def main():
    args = sys.argv
    ls = list(args[1])
    if ls[0] == '-':
        support(args)
    else:
        App(args)



if __name__ == '__main__':
    main()
