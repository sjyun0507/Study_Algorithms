from array import array

def find_max_occurred_alphabet(string):

# 1. a, b, c 처럼 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 알파벳으로 변환한다.
#     alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     max_occurrance = 0
#     max_alphabet = alphabet_array[0] #a
#
#     for alphabet in alphabet_array:
#         occurance = 0
#
#         for char in string:
#             if char == alphabet:
#                 occurance += 1
#         # print("alphabet = ", alphabet, "occurance = ", occurance)
#
#         if occurance > max_occurrance:
#             max_alphabet = alphabet
#             max_occurrance = occurance
#     return max_alphabet

# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만들고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.
    alphabet_occurrence_array = [0] *26

    for char in string:
        if not char.isalpha(): #알파벳인지 검사
            continue
        arr_index = ord(char) - ord('a') #해당 문자를 인덱스로 치환  'a' 'b' -> 0,1
        alphabet_occurrence_array[arr_index] += 1 #빈도수 배열에 인덱스로 찾아가서 추가

    # print("alphabet_occurrence_array = ", alphabet_occurrence_array)

    max_occurance = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurance:
            max_occurance = alphabet_occurrence
            max_alphabet_index = index
    # print("max_alphabet_index = ", max_alphabet_index)

    return chr(max_alphabet_index + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))