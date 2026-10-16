# atexit

## atexit.register(func, /, *args, **kwargs)

func - function to be called at exit
args - optional arguments to pass to func
kwargs - optional keyword arguments to pass to func

func is returned to facilitate usage as a decorator.

## atexit.unregister(func, /)

Unregister an exit function which was previously registered using atexit.register func - function to be unregistered
