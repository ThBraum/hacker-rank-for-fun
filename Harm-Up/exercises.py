# 1. Enunciado: Escreva uma função que receba uma string e retorne True se ela for um palíndromo (lê-se igual de trás para frente) e False caso contrário. Desconsidere espaços e diferenças de maiúsculas/minúsculas.

# Exemplo: "Ana" -> True, "Casa" -> False.

# Desafio: Tente fazer isso sem criar uma nova string invertida (economia de memória).



# # def palindromo(word):
# #     i = 0
# #     j = len(word) - 1

# #     while i < j:
# #         while i < j and word[i] == " ":
# #             i += 1
# #         while i < j and word[j] == " ":
# #             j -= 1

# #         if word[i].lower() != word[j].lower():
# #             return False

# #         i += 1
# #         j -= 1

# #     return True


# # word = input()
# # print(palindromo(word))

# # time complexity: O(n)
# # space complexity: O(1)


# # 2. Encontrar Duplicata (Arrays/Sets)

# # Enunciado: Dada uma lista de números inteiros onde apenas um número se repete, encontre qual é esse número.

# # Exemplo: [1, 3, 4, 2, 2] -> 2.

# # Dica: Pense em como fazer isso muito rápido usando uma estrutura de dados auxiliar (como um set ou dicionário).

# # def get_duplicated(lista):
# #     seen = set()
# #     duplicated_set = set()
    
# #     duplicated = []
    
# #     for item in lista:
# #         if item in seen:
# #             duplicated.append(item)
# #             duplicated_set.add(item)
# #         else:
# #             seen.add(item)
            
# #     return duplicated_set.pop() if duplicated_set else None

# # items = [1, 3, 4, 2, 2] 

# # print(get_duplicated(items))

# # time complexity: O(n)
# # space complexity: O(n)



# # 3. Two Sum (Hash Maps)

# # Enunciado: Dada uma lista de números inteiros e um valor alvo (target), retorne os índices dos dois números que somados resultam no alvo. Você pode assumir que sempre haverá exatamente uma solução.

# # Exemplo: nums = [1, 2, 3, 4], alvo = 9 -> Retorno: `` (pois 2 + 7 = 9).

# # Obs: A solução ingênua usa dois loops (for dentro de for). Tente encontrar a solução otimizada que percorre a lista apenas uma vez.

# def two_sum(nums, target):
#     seen = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[num] = i
        
#     return []

# # nums = [1, 2, 3, 4]
# # target = 9

# # print(two_sum(nums, target))

# # time complexity: O(n)
# # space complexity: O(n)


# def palindromo(word):
#     cleaned = word.replace(" ", "").lower()
#     return cleaned == cleaned[::-1]

# # time complexity: O(n)
# # space complexity: O(n)


# def result_target(target, values):
#     for value in values:
#         if (values[value] + (values[value] + 1)) == target:
#             return (value, value + 1)
        
#     return -1

# nums = [1, 2, 3, 4]
# alvo = 9

# print(result_target(alvo, nums))

# # time complexitu Big(0)
# # spcace comeplecxity  Big(1)


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def is_palindrome(word):
    cleaned = "".join(ch.lower() for ch in word if not ch.isspace())
    return cleaned == cleaned[::-1]

print(f"Usando a função is_palindrome('Ana'): {is_palindrome('Ana')}")
print(f"Usando a função is_palindrome('Casa'): {is_palindrome('Casa')}")

# 4. Validar Parênteses (Pilhas/Stacks)

# Enunciado: Dada uma string contendo apenas os caracteres (, ), {, }, [ e ], determine se a string é válida. Uma string é válida se:

# Parênteses abertos são fechados pelo mesmo tipo.

# Parênteses abertos são fechados na ordem correta.

# Exemplo: "{}" -> True, "{[}]" -> False.

# Contexto: Esse tipo de algoritmo é usado em compiladores e parsers, muito comum na área de sistemas.

def is_valid_parentheses(s):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys(): # o key faz a função de verificar se o char é um parêntese fechado
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(f"Verificando se os parenteses abertos são fechados pelo mesmo tipo. Uso atual: {is_valid_parentheses('{}')}")
print(f"Verificando se os parenteses abertos são fechados na ordem correta. Uso atual: {is_valid_parentheses('{[}]')}")