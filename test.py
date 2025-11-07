# -------------------------------
#  Sub-message splitter
message_sizes = {
    "10hz": [
        10, 10, 8, 10, 8, 8, 10, 12, 10, 8, 8, 10, 10, 54, 24, 22, 60, 26, 46, 18, 18, 46,
        16, 16, 16, 18, 18, 30, 22, 30, 54, 54, 54, 24, 24, 24, 22, 22, 22, 60, 60, 60,
        10, 26, 26, 26, 26, 26, 26, 26, 18, 18, 18, 18, 18, 18, 30, 30, 30, 8, 8, 8, 8,
        8, 14, 8, 22, 34, 8, 106, 104, 104, 104, 72, 62, 62, 62, 80, 32, 80, 34, 30, 10, 8
    ]}
def split_messages(hex_data):
    for rate, sizes in message_sizes.items():
        split_msgs, j = [], 0
        try:
            for size in sizes:
                if j + size > len(hex_data):
                    break
                if (extract_dic(hex_data[j:j + size][0:4]) == None):
                    break
                split_msgs.append(hex_data[j:j + size])
                
                j += size
            # return first one that yields multiple valid messages
            if len(split_msgs) > 40:
                return rate, split_msgs
        except Exception:
            continue
    return None, []

line_count = 0
message_sizes = {
    "5hz": [
        10, 10, 8, 10, 8, 8, 10, 12, 10, 8, 8, 10, 10, 54, 24, 22, 60, 24, 26, 46, 18, 18, 46,
        16, 16, 16, 14, 18, 18, 30, 22, 30, 54, 54, 54, 24, 24, 24, 22, 22, 22, 60, 60, 60, 10,
        26, 26, 26, 26, 26, 26, 26, 18, 18, 18, 18, 18, 18, 30, 30, 30, 8, 8, 8, 8, 8, 14, 14,
        14, 8, 22, 22, 34, 8, 22, 106, 104, 104, 104, 72, 62, 62, 62, 80, 32
    ]}
decoded_records = []
for file in os.listdir(source_folder):
    if not file.endswith(".txt"):
        continue

    file_path = os.path.join(source_folder, file)
    print(f"\n📄 Decoding {file_path}...")

    with open(file_path, "r") as f:
        for line in f:
            line = f.read().splitlines()
        for i in range(0, len(line), 2):
            try:
                hex_line = line[i + 4].strip().replace("-", "")
                timestamp_line = line[i+2].strip()
                gcs_time = timestamp_line.split(",")[0][0:12]
                gcs_time = timestamp_line.split(",")[0]
                hex_line = hex_line.replace("-", "")
                # Parse the 0109 header
                header_fields = extract_dic("0109")
                header = parse_fixed_packet(hex_line[:71], header_fields)
                mission_time = header.get("Mission Time")
                uav_id = header.get("UAV ID")
                # Split sub-messages
                hex_data = hex_line[48:].replace("-", "")
                rate, split_msgs = split_messages(hex_data)
                print(rate,split_msgs)
                for submsg in split_msgs:
                    sub_type = submsg[0:4]
                    print(sub_type)
                    fields = extract_dic(sub_type)
                    decoded = parse_fixed_packet(submsg, fields)
                    print(decoded)
                    decoded.update({
                        "GCS Time": gcs_time,
                        "Mission Time": mission_time,
                        "UAV ID": uav_id,
                        "Rate": rate,
                        "File": file
                    })
                decoded_records.append(decoded)
                print(decoded_record)
            except:
                continue
