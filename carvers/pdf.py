import os

# Settings
drive = ""  # Path to the binary file or drive
output_dir = ""  # Directory to save extracted pdf files
size = 4096 # Buffer size for reading chunks

# pdf file markers
pdf_START = b'%PDF'  # pdf start signature
pdf_END = b'%%EOF'      # pdf end signature

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to extract pdf files
def extract_pdf():
    offset = 0
    received = 0
    with open(drive, "rb") as fileD:
        while True:
            byte_chunk = fileD.read(size)
            if not byte_chunk:
                break  # End of file

            # Search for the pdf start marker
            found = byte_chunk.find(pdf_START)
            if found >= 0:
                # Start of a new pdf
                print(f"=== Found pdf at location: {hex(found + (size * offset))} ===")
                pdf_data = byte_chunk[found:]
                with open(os.path.join(output_dir, f"{received}.pdf"), "wb") as fileN:
                    fileN.write(pdf_data)

                    # Read until the pdf end marker is found
                    while True:
                        next_chunk = fileD.read(size)
                        if not next_chunk:
                            break

                        end_pos = next_chunk.find(pdf_END)
                        if end_pos >= 0:
                            # End of the pdf file
                            fileN.write(next_chunk[:end_pos + len(pdf_END)])
                            print(f"=== Wrote pdf to location: {received}.pdf ===\n")
                            received += 1
                            break
                        else:
                            fileN.write(next_chunk)

            offset += 1

# Extract pdf files
print("Starting pdf extraction...")
extract_pdf()
print("pdf extraction completed.")
