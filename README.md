# Nguyen Project
Nguyên - Linear Algebra Group Project

```markdown
# Hill Cipher Encryption Project 🔐
### Linear Algebra Course Project | Group 08

![Language](https://img.shields.io/badge/Language-Python_3.x-blue)
![University](https://img.shields.io/badge/University-HCMUT-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📋 Project Overview
This project applies **Linear Algebra** to Cryptography by implementing the **Hill Cipher**. It uses matrix multiplication and modular arithmetic to encrypt text, rendering it secure against basic frequency analysis attacks. 

The repository includes:
1.  **Python Implementation:** Scripts to encrypt and decrypt text files.
2.  **Visualization:** Histograms showing the effectiveness of the encryption.
3.  **Final Report:** A comprehensive LaTeX report explaining the math and methodology.

---

## 👥 Team Members
**University of Technology, Ho Chi Minh City (HCMUT)**
*Academic Year 2025 - 2026*

| ID | Name | Role |
| :--- | :--- | :--- |
| **2551444** | **Ngo Binh Nguyen** | **Leader** |
| 2551824 | Truong Hanh Nguyen | Member |
| 2551326 | Tran Phuong Dung | Member |
| 2551328 | Tran Minh Hien | Member |
| 2551333 | Duong Gia Minh | Member |

---

## 📂 Project Structure
The project is organized into two main folders:

```text
├── Data/                     # Source Code & Datasets
│   ├── encryption.py         # Main script to encrypt text & plot histograms
│   ├── decryption.py         # Script to decrypt the ciphertext
│   ├── sherlock.txt          # The original plaintext file
│   ├── encrypted_sherlock.txt# The output ciphertext (generated)
│   ├── decrypted_output.txt  # The recovered text (generated)
│   └── histogram_results.png # Frequency analysis graph
│
├── Latex/                    # Final Report Files
│   ├── report.pdf            # The compiled project report
│   ├── report.tex            # LaTeX source code
│   └── ...                   # Images and auxiliary files
│
└── README.md                 # Project documentation

```

---

## ⚙️ Requirements & Setup

### 1. Prerequisites

You need **Python 3** installed on your computer.

### 2. Install Dependencies

This project relies on `numpy` for matrix math and `matplotlib` for graphing. Install them via terminal:

```bash
pip install numpy matplotlib

```

---

## 🚀 How to Use

### Step 1: Encrypt the Text

1. Navigate to the `Data` folder:
```bash
cd Data

```


2. Run the encryption script:
```bash
python encryption.py

```


* **Input:** Reads `sherlock.txt`.
* **Output:** Creates `encrypted_sherlock.txt` and displays/saves `histogram_results.png`.



### Step 2: Decrypt the Text

To verify the cipher works, run the decryption script:

```bash
python decryption.py

```

* **Input:** Reads `encrypted_sherlock.txt`.
* **Output:** Creates `decrypted_output.txt`.

> **Note:** The `decrypted_output.txt` should match the content of the original file (converted to uppercase/stripped of punctuation).

---

## 📊 Project Details

### The Key Matrix ()

We utilize a  invertible matrix in :

### Results

The encryption successfully "flattens" the letter frequency of the English text, hiding the statistical patterns (like the common letters 'E', 'T', 'A') and securing the message.

---

## 📄 License & Credits

* **Dataset:** *The Adventures of Sherlock Holmes* by Arthur Conan Doyle (Source: Project Gutenberg).
* **Course:** Linear Algebra (Sem 251CC02), HCMUT.

```

```