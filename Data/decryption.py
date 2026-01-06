import numpy as np

# ==========================================
# 1. CONFIGURATION & INVERSE KEY
# ==========================================
# The INVERSE Matrix (K^-1) calculated modulo 26
# This reverses the effect of the original Key Matrix
K_inv = np.array([
    [2, 18, 5],
    [20, 11, 22],
    [21, 4, 1]
])

INPUT_FILENAME = "encrypted_sherlock.txt"
OUTPUT_FILENAME = "decrypted_output.txt"

# ==========================================
# 2. DECRYPTION ENGINE
# ==========================================
def decrypt_hill_cipher(ciphertext, inverse_matrix):
    if not ciphertext: return ""
    
    n = inverse_matrix.shape[0]  # Matrix size (3)
    
    # 1. Map letters to numbers (A=0, B=1, ... Z=25)
    numeric_text = [ord(char) - 65 for char in ciphertext]
    
    # 2. Reshape into matrix of column vectors
    # Note: We don't need to pad because the encrypted text 
    # is already a perfect multiple of 3 from the encryption step.
    text_matrix = np.array(numeric_text).reshape(-1, n).T
    
    # 3. Matrix Multiplication: P = K_inv * C (mod 26)
    decrypted_matrix = np.dot(inverse_matrix, text_matrix) % 26
    
    # 4. Convert back to linear list
    decrypted_numeric = decrypted_matrix.T.reshape(-1)
    
    # 5. Map numbers back to letters
    decrypted_text = "".join([chr(num + 65) for num in decrypted_numeric])
    
    return decrypted_text

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print(f"Reading encrypted text from {INPUT_FILENAME}...")
    
    try:
        with open(INPUT_FILENAME, 'r') as f:
            encrypted_text = f.read()
            
        print("Decrypting...")
        decrypted_text = decrypt_hill_cipher(encrypted_text, K_inv)
        
        # Save result
        with open(OUTPUT_FILENAME, "w") as f:
            f.write(decrypted_text)
            
        print(f"\nSuccess! Decrypted text saved to '{OUTPUT_FILENAME}'")
        print("--- SNIPPET ---")
        print(decrypted_text[:100])
        
    except FileNotFoundError:
        print(f"Error: Could not find '{INPUT_FILENAME}'. Run the encryption script first!")