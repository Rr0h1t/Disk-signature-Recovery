import os
import re

# Settings
drive_path = ""  # Path to the binary file or disk image
output_dir = ""  # Directory to save extracted log files
buffer_size = 4096  # Buffer size for reading chunks

# Log file signature: regex for common timestamp formats (YYYY-MM-DD HH:MM:SS)
LOG_PATTERN = re.compile(rb'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to extract log files
def extract_logs():
    offset = 0
    log_count = 0
    with open(drive_path, "rb") as drive:
        while chunk := drive.read(buffer_size):
            matches = list(LOG_PATTERN.finditer(chunk))
            for i, match in enumerate(matches):
                start = match.start() + offset

                # Extract potential log entry from start position
                log_data = bytearray()
                log_data.extend(chunk[match.start():])

                with open(drive_path, "rb") as drive_reseek:
                    drive_reseek.seek(start)

                    while True:
                        next_chunk = drive_reseek.read(buffer_size)
                        if not next_chunk:
                            break

                        log_data.extend(next_chunk)

                        # Stop reading if no new log-like content is found
                        if not LOG_PATTERN.search(next_chunk):
                            break

                # Save the extracted log data
                log_file_path = os.path.join(output_dir, f"log_{log_count}.txt")
                with open(log_file_path, "wb") as log_file:
                    log_file.write(log_data)

                print(f"Extracted log file: {log_file_path}")
                log_count += 1

            offset += len(chunk)

    print(f"Extraction completed. Total log files extracted: {log_count}")

# Run the log extraction
if __name__ == "__main__":
    print("Starting log extraction...")
    extract_logs()
    print("Log extraction finished.")
