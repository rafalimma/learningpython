"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

ex:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                soma = nums[i] + nums[j]
                if soma == target:
                    return [i, j]

intlist = [2,7,11,15]
print(twoSum(intlist, 9))

'''
Como você comentou que vai fazer o teste da Turing, eles esperam que você resolva esse problema de forma eficiente.
Em vez de dois loops, usamos um dicionário para "lembrar" dos números que já vimos.
'''

def twoSum(nums, target):
    vistos = {}  # Dicionário para guardar {valor: indice}
    
    for i, num in enumerate(nums):
        complemento = target - num
        
        # Se o que falta para chegar no alvo já foi visto antes...
        if complemento in vistos:
            return [vistos[complemento], i]
        
        # Se não, guarda o número atual e sua posição no dicionário
        vistos[num] = i

# Teste
print(twoSum([2, 7, 11, 15], 9)) # [0, 1]

