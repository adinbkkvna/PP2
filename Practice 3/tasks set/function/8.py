def spy_game(numbers):
    required_numbers=[0,0,7]
    current_index=0

    for number in numbers:
        if number==required_numbers[current_index]:
            current_index+=1

            if current_index==len(required_numbers):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))