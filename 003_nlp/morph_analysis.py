# -*- coding: utf-8 -*-
import sys
sys.path.append('lib')
import MeCab


def morph(input=sys.stdin):
    mecab = MeCab.Tagger()
    for line in input:
        print(mecab.parse(line))


def main():
    morph()


if __name__ == "__main__":
    main()
