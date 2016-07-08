import os
import difflib

if __name__ == '__main__':

    a = open(os.path.join(os.path.dirname(__file__), 'A.txt'), 'r').readlines()
    b = open(os.path.join(os.path.dirname(__file__), 'B.txt'), 'r').readlines()

    diff = difflib.SequenceMatcher(None, a, b)

    for tag, alo, ahi, blo, bhi in diff.get_opcodes():
        print ""
        print "-"*60
        print tag.upper()
        print "A[%d:%d]: " % (alo, ahi) + str(a[alo:ahi])
        print "B[%d:%d]: " % (blo, bhi) + str(b[blo:bhi])

    print "Finished"

    # print ""
    #
    # diff = difflib.Differ()
    # for line in diff.compare(a, b):
    #     print line.rstrip()
    #     if not line.startswith(' '):
    #         pass
    #
    # print "Finished"