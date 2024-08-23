import builtins


def set_grumpy_print() -> None:
    original_print = builtins.print

    def __grumpy_print(*args, **kwargs):
        grumpy_args = ('😾🔊',) + args
        original_print(*grumpy_args, **kwargs)

    builtins.print = __grumpy_print


if __name__ == '__main__':
    set_grumpy_print()
    print('Meow')