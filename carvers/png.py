import os

# Settings
drive = ""  # Path to the binary file or drive
output_dir = ""  # Directory to save extracted PNG files
size = 4096 # Buffer size for reading chunks

# PNG file markers
PNG_START = b'\x89PNG\r\n\x1a\n'  # PNG start signature
PNG_END = b'IEND\xaeB`\x82'       # PNG end signature

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to extract PNG files
def extract_png():
    offset = 0
    received = 0
    with open(drive, "rb") as fileD:
        while True:
            byte_chunk = fileD.read(size)
            if not byte_chunk:
                break  # End of file

            # Search for the PNG start marker
            found = byte_chunk.find(PNG_START)
            if found >= 0:
                # Start of a new PNG
                print(f"=== Found PNG at location: {hex(found + (size * offset))} ===")
                png_data = byte_chunk[found:]
                with open(os.path.join(output_dir, f"{received}.png"), "wb") as fileN:
                    fileN.write(png_data)

                    # Read until the PNG end marker is found
                    while True:
                        next_chunk = fileD.read(size)
                        if not next_chunk:
                            break

                        end_pos = next_chunk.find(PNG_END)
                        if end_pos >= 0:
                            # End of the PNG file
                            fileN.write(next_chunk[:end_pos + len(PNG_END)])
                            print(f"=== Wrote PNG to location: {received}.png ===\n")
                            received += 1
                            break
                        else:
                            fileN.write(next_chunk)

            offset += 1

# Extract PNG files
print("Starting PNG extraction...")
extract_png()
print("PNG extraction completed.")
