#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 01:10:55 2017

@author: vicz
"""
print '''

     +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+    
     |A|s|p|e|c|t| |b|a|s|e|d| |s|e|n|t|i|m|e|n|t| |a|n|a|l|y|s|i|s|    
     +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+    
                                                               |b|y|    
                                                               +-+-+-+-+
                                                               |v|i|c|z|
                                                               +-+-+-+-+
    

'''
from textblob import TextBlob
import sys

def main():
    blob=TextBlob(sys.argv[1])
    word=[]
    sent=[]
    c=0
    for words,pos in blob.tags:
        if pos=='JJ' or pos=='NN' or pos=='JJR':
            word.append((words,pos))
            c=c+1
        if c==2:
            i=blob.find(words)
            sent.append(blob[:i+len(words)])
            blob=blob[i+len(words):]
            c=0
    print "Noun and polarity"    
    for sentence in sent:
        for word, tag in sentence.tags:
            if tag=='NN':
                print word,sentence.polarity
                
if __name__=='__main__':
    main()
    