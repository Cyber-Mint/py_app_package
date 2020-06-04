#from io import StringIO
#from contextlib import redirect_stdout
import app

def main():
   print(app.say_hello())

#f = StringIO()
#with redirect_stdout(f):
#    print('foobar')
#    print(12)
#print('Got stdout: "{0}"'.format(f.getvalue()))

