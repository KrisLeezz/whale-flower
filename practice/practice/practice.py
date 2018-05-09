import time

name=raw_input("what's your name? *_*\n")
print "Hi,"+name
message=raw_input("Do u want to say something to me? yes or no\n")
if message=='no':
    print "Okay~T_T"
    message= raw_input("Do you want to have lunch with me? yes or no")
    if message=='yes':
        for i in range(0,3):
            message=raw_input("guess where I am?\n")
            print "No, one more time"
        print 'emmmm...'
        print 'fool you fool, I am in your heart'
    else:
        print "Oh, Naughty Girl, I guess you'd like to have lunch with me. "
        for i in range(0,3):
            message=raw_input("guess where I am?\n")
            print "No, one more time"
        print 'emmmm...'
        print 'fool you fool, I am in your heart♥'
else:
    message=raw_input("Okay, I am listening~\n")
    print "you are right"
    message= raw_input("emmm...Do you want to have lunch with me? yes or no\n")
    if message=='yes':
        for i in range(0,3):
            message=raw_input("guess where I am?\n")
            print "No, one more time"
        print 'emmmm...'
        print 'fool you fool, I am in your heart'
    else:
        print "Oh, Naughty Girl, I guess you'd like to have lunch with me. "
        for i in range(0,3):
            message=raw_input("guess where I am?\n")
            print "No, one more time"
        print 'emmmm...'
        print 'fool you fool, I am in your heart- -'

print "GO, I'm waitting for you."
message=raw_input('Please input ok/n')