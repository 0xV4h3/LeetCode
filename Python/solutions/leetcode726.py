# 726. Number of Atoms
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(i):
            atom_count = {}
            while i < len(formula):
                if formula[i] == '(':
                    i, inner_map = parse(i + 1)
                    count = ''
                    while i < len(formula) and formula[i].isdigit():
                        count += formula[i]
                        i += 1
                    count = int(count) if count else 1
                    for atom in inner_map:
                        if atom not in atom_count:
                            atom_count[atom] = 0
                        atom_count[atom] += inner_map[atom] * count
                elif formula[i] == ')':
                    return i + 1, atom_count
                else:
                    atom = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        atom += formula[i]
                        i += 1
                    count = ''
                    while i < len(formula) and formula[i].isdigit():
                        count += formula[i]
                        i += 1
                    count = int(count) if count else 1
                    if atom not in atom_count:
                        atom_count[atom] = 0
                    atom_count[atom] += count
            return i, atom_count

        _, total_atoms = parse(0)
        result = ''
        for atom in sorted(total_atoms):
            result += atom
            if total_atoms[atom] > 1:
                result += str(total_atoms[atom])
        return result

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.countOfAtoms(formula = "H2O") # H2O
    print(example1)
    example2 = sol.countOfAtoms(formula = "Mg(OH)2") # H2MgO2
    print(example2)
    example3 = sol.countOfAtoms(formula = "K4(ON(SO3)2)2") # K4N2O14S4
    print(example3)