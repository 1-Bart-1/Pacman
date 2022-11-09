All variables in the file have to be declared inside functions,
 To do this you can use input and return statements in functions:

 def foo(var1, var2, var3):
    var3 += 1
    return var3

instead of

 var1, var2, var3 = 0
 def foo(): var3 += 1

If we don't do this, you only update variables inside the file you are working in, and the variable in pacman.py won't be updated



Try not to use sensehat set_pixel outside of main. Update position variables instead, and return the position variables.
This way it is easy to call the functions from main and clear the entire screen and draw everything at the same time.