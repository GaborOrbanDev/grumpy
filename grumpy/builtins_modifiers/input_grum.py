import builtins


def set_grumpy_input() -> None:
    original_input = builtins.input

    def __grumpy_input(prompt: str = '') -> str:
        grumpy_prompt = f"😾🍽️  {prompt}"
        return original_input(grumpy_prompt)

    builtins.input = __grumpy_input


if __name__ == '__main__':
    set_grumpy_input()
    print(input('Give me food: '))