def scramble(s1, s2):
    # first = "".join(sorted(s1))
    # second = "".join(sorted(s2))
    index = 0
    if len(s2) > len(s1):
        return False
    if sorted(s2) == sorted(s1):
        return True

    while(index < len(s2)):
        try:
            found = s1.index(s2[index])
        except ValueError:
            return False
        else:
            f = list(s1)
            f.remove(f[found])
            s1 = "".join(f)
            index += 1
    return True


print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('scriptjavx', 'javascript'))
