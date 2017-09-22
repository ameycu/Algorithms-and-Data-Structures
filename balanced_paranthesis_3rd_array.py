def balanced(a_str):
  stack = []
  pushChars, popChars = "({[", ")}]"
  for c in a_str :
    if c in pushChars :
      stack.append(c)
    elif c in popChars :
      if not len(stack) :
        return False
      else :
        stackTop = stack.pop()
        balancingBracket = pushChars[popChars.index(c)]
        if stackTop != balancingBracket :
          return False
    else :
      continue
  return not len(stack)
print balanced('asdas(ds{sd}asda{asdasd})')

def prime_factors(n):
  return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def products(current_product, current_list, aim, factors):

    if current_product == aim:
        yield tuple(sorted(current_list))

    elif 0 < current_product < aim:
        for factor in factors:
            if factor != 1:
                for product in products(current_product * factor, current_list + [factor], aim, factors):
                    #print 'courrent product = ',current_product * factor,'\tcurrent list = ',current_list + [factor]
                    yield product

def product_sets(n):
    return set(products(1, [], n, prime_factors(n)))

def  is_3d_array_size( a_size):
    is_3d = False 
    final_list = list(product_sets(a_size))
    for tuple in final_list:
        if len(tuple)==3:
            is_3d = True
        #print tuple
    return is_3d


def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n % i == 0: return False
  return True

def is_3d_array_size_2(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      if not is_prime(n/i): return True
  return False


for n in range(2,5000):
  if is_3d_array_size(n) != is_3d_array_size_2(n): print 'fail'
print 'end'