def caesar_cipher(s, n):
  ans = ''
  lower = s.lower()
  for i in range(len(lower)):
    if lower[i].isalpha():
      if lower[i] == s[i]:
        ans += chr((ord(lower[i])+n-96)%26+96)
      else:
        ans += chr((ord(lower[i])+n-96)%26+96).upper()
    else:
      ans += lower[i]
  return ans
  
def reverse_sentence(s):
  return ' '.join(s.split(' ')[::-1])

def reverse_word_in_sentence(s):
  return ' '.join([i[::-1] for i in s.split()])
  
print caesar_cipher('Zoo Keeper',1)
print reverse_sentence('Zoo Keeper',1)
print reverse_word_in_sentence('Zoo Keeper',1)