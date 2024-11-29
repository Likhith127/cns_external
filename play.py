class PlayfairCipher:
    def __init__(self, key_matrix):
        self.key_matrix = key_matrix
    def remove_whitespace(self, s):
        return s.replace(' ', '')
    def make_pairs(self, pt):
        pt = self.remove_whitespace(pt).replace('j', 'i')
        pairs = []
        i = 0
        while i < len(pt):
            a = pt[i]
            if i + 1 < len(pt):
                b = pt[i + 1]
                if a == b:
                    pairs.append((a, 'x'))
                    i += 1
                else:
                    pairs.append((a, b))
                    i += 2
            else:
                pairs.append((a, 'x'))
                i += 1
        return pairs
    def find_positions(self, a, b):
        pos = [0, 0, 0, 0]
        for i in range(5):
            for j in range(5):
                if self.key_matrix[i][j] == a:
                    pos[0], pos[1] = i, j
                if self.key_matrix[i][j] == b:
                    pos[2], pos[3] = i, j
        return pos
    def encrypt(self, pt):
        pairs = self.make_pairs(pt)
        encrypted_text = []
        for a, b in pairs:
            pos = self.find_positions(a, b)
            if pos[0] == pos[2]:
                encrypted_text.append(self.key_matrix[pos[0]][(pos[1] + 1) % 5])
                encrypted_text.append(self.key_matrix[pos[2]][(pos[3] + 1) % 5])
            elif pos[1] == pos[3]:
                encrypted_text.append(self.key_matrix[(pos[0] + 1) % 5][pos[1]])
                encrypted_text.append(self.key_matrix[(pos[2] + 1) % 5][pos[1]])
            else:
                encrypted_text.append(self.key_matrix[pos[0]][pos[3]])
                encrypted_text.append(self.key_matrix[pos[2]][pos[1]])
        return ''.join(encrypted_text)
    def display_key_matrix(self):
        for row in self.key_matrix:
            print(' '.join(row))
if __name__ == "__main__":
 key_matrix = [
 ['m', 'o', 'n', 'a', 'r'],
 ['c', 'h', 'y', 'b', 'd'],
 ['e', 'f', 'g', 'i', 'k'],
 ['l', 'p', 'q', 's', 't'],
 ['u', 'v', 'w', 'x', 'z']
 ]

 pt = "instruments"
 cipher = PlayfairCipher(key_matrix)
 print("Key Matrix:")
 cipher.display_key_matrix()

 encrypted_text = cipher.encrypt(pt)
 print("Encrypted Text:", encrypted_text)