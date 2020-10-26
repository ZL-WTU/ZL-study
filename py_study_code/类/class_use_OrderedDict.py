from collections import OrderedDict
vocabulary=OrderedDict()
vocabulary['beautiful']='美丽的'
vocabulary['happy']='快乐的'
vocabulary['sad']='悲伤的'
for k,v in vocabulary.items():
    print(k+"'s mean is "+v)