"""Copyright (c) 2017 * Keith Cestaro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import string
import random


def main():
    print("Please input a number 0-32 for how long you want the hash: ")
    length = int(input())
    if length > 0 and length <= 32:
        print("Please input whether you would like numbers, letters or both \
(nums/lets/both)")
        hashType = input()
        if hashType == "nums":
            genHash = []
            i = 0
            while i < length:
                randNumber = random.randint(0, 9)
                genHash.append(str(randNumber))
                i += 1
            print("".join(genHash))
        elif hashType == "lets":
            genHash = []
            i = 0
            while i < length:
                randLetter = random.choice(string.ascii_letters)
                genHash.append(randLetter)
                i += 1
            print("".join(genHash))
        elif hashType == "both":
            genHash = []
            i = 0
            while i < length:
                numAlphaRoll = random.randint(1, 2)
                if numAlphaRoll == 1:
                    randLetter = random.choice(string.ascii_letters)
                    genHash.append(randLetter)
                elif numAlphaRoll == 2:
                    randNumber = random.randint(0, 9)
                    genHash.append(str(randNumber))
                i += 1
            print("".join(genHash))
        else:
            print("Input invalid")
    else:
            print("Input invalid")

main()
