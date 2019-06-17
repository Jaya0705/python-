# 7.
# Program
# to
# prompt
# to
# the
# user
# for input and print the same till a keyboard interrupt(ctrl+c) is caused.

while True:
    try:
        s = raw_input("enter something:")
        print s
        ns = str(s)
    except:
        print "\nerror"
        break
