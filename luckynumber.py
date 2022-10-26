def lucky_numbers(numbers):
        del numbers[::-2]   # Delete even numbers
        while int(numbers[1]) < len(numbers):
            x = int(numbers[1])
            del numbers[-1::x]
            print(numbers)
            return
        return
    lucky_numbers(numbers)
