import base64

def encode_to_base64(file_path):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    base64_encoded_data = base64.b64encode(encrypted_data)
    return base64_encoded_data

def main():
    ecb_base64 = encode_to_base64('output_ecb.des')
    with open('output_ecb_base64.txt', 'wb') as file:
        file.write(ecb_base64)

    cbc_base64 = encode_to_base64('output_cbc.des')
    with open('output_cbc_base64.txt', 'wb') as file:
        file.write(cbc_base64)

if __name__ == "__main__":
    main()
