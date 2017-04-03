"""
remember
========
A function decorator that injects saved variables to a file.

Once a variable has been provided to a function, it will be saved and
re-injected on following calls unless explicitly overridden.

Example use case:

    @remember('keywords', 'to', 'remember')
    def lookup(keywords='to', remember='unless provided explicitly'):
        print(keywords)

    >>> lookup(keywords='caffeine')
    caffeine
    >>> # Now, call it again w/o the keyword argument:
    >>> lookup()
    caffeine
    >>> # Magic!

Requirements:
    * Lazy loading
    * Singleton memory DB per program
    * Remember on a per-function basis

Issues:
    * If you change the function signature, it won't know.
    * If you only want certain kwargs passed, you'll need to provide the rest
      of them with whatever passes for a no - op.
"""
import atexit
import shelve


memory = None


def save_memory():
    """Save our modifications back to disk."""
    memory.close()


# Register saving and closing our DB on normal program exit
atexit.register(save_memory)


def remember():
    global memory
    if not memory:
        memory = shelve.open('memory.db')

    def wrap(fn, *keywords):

        def wrapped(*args, **kwargs):
            # Remember these keyword arguments
            memory[fn.__qualname__].update(kwargs)
            # Pass all previously seen keyword arguments
            out = fn(*args, **memory[fn.__qualname__])
            return out

        return wrapped

    return wrap
