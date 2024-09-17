import qrcode
import cv2
import subprocess

# Function to generate a QR code from text
def generate_qr(data, file_name='qr_code.png'):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Function to scan and decode QR code using ZXing
def scan_qr(image_path):
    try:
        # Using ZXing to decode QR code
        result = subprocess.run(['zxing', image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        qr_data = result.stdout.decode('utf-8').strip()
        
        if qr_data:
            print(f"QR Code Data: {qr_data}")
            return qr_data
        else:
            print("No QR code found or could not decode")
            return None
    except Exception as e:
        print(f"Error scanning QR code: {e}")
        return None

# Main function to choose between generating and scanning QR code
def main():
    print("1. Generate QR Code")
    print("2. Scan QR Code")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        data = input("Enter the data for the QR code: ")
        file_name = input("Enter file name to save QR code (with .png extension): ")
        generate_qr(data, file_name)
    
    elif choice == '2':
        image_path = input("Enter the image file path to scan QR code: ")
        scan_qr(image_path)
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the main function
if __name__ == '__main__':
    main()
