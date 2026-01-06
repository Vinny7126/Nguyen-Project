import numpy as np
import re
import matplotlib.pyplot as plt
from collections import Counter

# ==========================================
# 1. CONFIGURATION & KEY MATRIX
# ==========================================
# The Key Matrix (K) defined in the Project Plan
K = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# The name of the file you uploaded
FILENAME = "1661-0.txt"

# ==========================================
# 2. DATA LOADING & CLEANING
# ==========================================
def load_and_clean_text(filename):
    print(f"Reading text from {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please ensure the text file is in the same folder as this script.")
        return ""

    # Remove Gutenberg Headers/Footers (approximate markers)
    # This methodology is required by your Chapter 5.2
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
    
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    
    # If markers exist, strip them. If not, use the whole text.
    if start_idx != -1 and end_idx != -1:
        text = text[start_idx + len(start_marker):end_idx]
    
    # Filter: Keep only alphabetic characters and convert to Uppercase
    # This maps to the "Alphabet Space" Z_26
    clean_text = re.sub(r'[^A-Z]', '', text.upper())
    
    print(f"Original Text Length (cleaned): {len(clean_text)} characters")
    return clean_text

# ==========================================
# 3. ENCRYPTION ENGINE (The Hill Cipher)
# ==========================================
def encrypt_hill_cipher(plaintext, key_matrix):
    if not plaintext: return ""
    
    n = key_matrix.shape[0]  # Matrix size (3)
    
    # 1. Map letters to numbers (A=0, B=1, ... Z=25)
    numeric_text = [ord(char) - 65 for char in plaintext]
    
    # 2. Padding
    # The text length must be divisible by the matrix size (3).
    padding_len = (n - len(numeric_text) % n) % n
    numeric_text.extend([23] * padding_len) # 23 is 'X'
    
    # 3. Reshape into a matrix of column vectors (3 x m)
    text_matrix = np.array(numeric_text).reshape(-1, n).T
    
    # 4. Matrix Multiplication: C = K * P (mod 26)
    # This implements the equation from Chapter 3.2
    encrypted_matrix = np.dot(key_matrix, text_matrix) % 26
    
    # 5. Convert back to linear list
    encrypted_numeric = encrypted_matrix.T.reshape(-1)
    
    # 6. Map numbers back to letters
    encrypted_text = "".join([chr(num + 65) for num in encrypted_numeric])
    
    return encrypted_text

# ==========================================
# 4. VISUALIZATION (Histograms)
# ==========================================
def plot_histograms(original, encrypted):
    if not original or not encrypted: return

    # Calculate frequencies
    orig_counts = Counter(original)
    enc_counts = Counter(encrypted)
    
    alphabet = [chr(i + 65) for i in range(26)]
    orig_freq = [orig_counts.get(char, 0) for char in alphabet]
    enc_freq = [enc_counts.get(char, 0) for char in alphabet]
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Original Histogram
    axes[0].bar(alphabet, orig_freq, color='blue', alpha=0.7)
    axes[0].set_title('Original Text Frequency (English)')
    axes[0].set_xlabel('Letter')
    axes[0].set_ylabel('Frequency')
    
    # Encrypted Histogram
    axes[1].bar(alphabet, enc_freq, color='red', alpha=0.7)
    axes[1].set_title('Encrypted Text Frequency (Hill Cipher)')
    axes[1].set_xlabel('Letter')
    axes[1].set_ylabel('Frequency')
    
    plt.tight_layout()
    
    # --- CHANGE IS HERE ---
    # Save the graph as an image file
    output_image = "histogram_results.png"
    plt.savefig(output_image)
    print(f"Graph saved as '{output_image}'")
    # ----------------------
    
    # Show the graph on screen (optional, depends on your setup)
    # plt.show() 

    print("Histograms generated.")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Get Data from LOCAL FILE
    plaintext = load_and_clean_text(FILENAME)
    
    if plaintext:
        # 2. Encrypt
        print("Encrypting...")
        ciphertext = encrypt_hill_cipher(plaintext, K)
        
        # 3. Show a snippet
        print("\n--- SAMPLE ENCRYPTION ---")
        print(f"Original (First 50 chars):  {plaintext[:50]}")
        print(f"Encrypted (First 50 chars): {ciphertext[:50]}")
        
        # 4. Save to file
        output_filename = "encrypted_sherlock.txt"
        with open(output_filename, "w") as f:
            f.write(ciphertext)
        print(f"\nFull encrypted text saved to '{output_filename}'")
        
        # 5. Analysis
        plot_histograms(plaintext, ciphertext)