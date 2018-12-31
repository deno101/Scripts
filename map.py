#!/usr/bin/env python3.7


class Map:
    # Initialize vars to be used in program
    def __init__(self, word):
        self.word = word
        self.length = self.getlen()
        self.wordlen = len(self.word)
        self.fin_array = []
        self.temp_array = []
        self.rvsword = self.word[::-1]
        self.Main()

    # Get the length of the vertical array
    def getlen(self):
        ret = (6 * len(self.word)) - 5
        return ret

    # Function to produce the first line
    def printF(self):
        self.populate()
        cont_1 = 0
        cont_2 = 0
        for x in range(0, self.length, 1):
            if x >= self.wordlen-1 and x < (2 *self.wordlen)-1:
                self.temp_array[x] = self.rvsword[cont_1]
                cont_1 += 1

            if x >= (4 * self.wordlen)-4 and x <= (5 * self.wordlen)-5:
                self.temp_array[x] = self.word[cont_2]
                cont_2 += 1
        temp_str = ''
        for x in self.temp_array:
            temp_str += x

        self.fin_array.append(temp_str)
        self.temp_array = []

    # Function to print the middle part
    def print_mid(self):
        self.populate()
        cont_1 = 1
        posl1 = self.wordlen - 2
        posl2 = (2 * self.wordlen) - 1
        posl3 = (4 * self.wordlen) - 5
        posl4 = (5 * self.wordlen) - 4
        for x in range(1,self.wordlen,1):
            self.temp_array[posl1] = self.rvsword[cont_1]
            self.temp_array[posl2] = self.word[cont_1]
            self.temp_array[posl3] = self.word[cont_1]
            self.temp_array[posl4] = self.rvsword[cont_1]
            cont_1 += 1
            posl1 -= 1
            posl2 += 1
            posl3 -= 1
            posl4 += 1
            temp_str = ''
            for s in self.temp_array:
                temp_str += s

            self.fin_array.append(temp_str)
            self.temp_array = []
            self.populate()

    def Main(self):
        self.printF()
        self.print_mid()
        self.printdown()
        for x in self.fin_array:
            print(x)

    # print the down part since the down part is a mirror of the upper part
    def printdown(self):
        array = self.fin_array
        cont = len(self.fin_array)-2
        for x in range(0, self.wordlen-1, 1):
            self.fin_array.append(array[cont])
            cont -= 1


    def populate(self):
        for x in range(0, self.length, 1):
            self.temp_array.append(' ')


def main():
    word = input('Enter word here: ')
    Map(word)


if __name__ == '__main__':
    main()
