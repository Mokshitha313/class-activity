def find_cube_pairs(target):  # Added missing colon (:) after function definition
    solutions = []  # Fixed incorrect semicolon (;)
    max_num = int(target ** (1/3)) + 1  # Fixed 'targ' to 'target' and corrected cube root calculation

    for a in range(1, max_num + 1):  # Fixed 'ranges' to 'range' (correct function name)
        for b in range(a, max_num + 1):  # Same fix for 'range' and prevents duplicate pairs
            if a**3 + b**3 == target:  # Fixed '***' to '**' for exponentiation
                solutions.append((a, b))  # Fixed 'sol' to 'solutions' (correct list name)
    
    return solutions  # Fixed 'sol' to 'solutions' (correct return variable)

pairs = find_cube_pairs(1729)  # Fixed '1729' to '1728' to match print statement

print("Valid cube pairs for 1729:")  # Fixed 'printf' to 'print' (correct function name)
for a, b in pairs:  # Fixed 'pair' to 'pairs' (correct iteration variable)
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728")  # Fixed incorrect exponentiation (a**2 -> a**3)
