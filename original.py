#  Frequency message sizes
import os
# -------------------------------

# -------------------------------
#  Main decoder
# -------------------------------
def decode_logs(source_folder):
    all_dfs = []

    for file in os.listdir(source_folder):
        if not file.endswith(".txt"):
            continue

        file_path = os.path.join(source_folder, file)
        print(f"\n📄 Decoding {file_path}...")
        with open(file_path, "r") as f:
            lines = f.read().splitlines()

        decoded_records = []
        for i in range(0, len(lines), 4):
            timestamp_line = lines[i].strip()
            hex_line = lines[i + 3].strip()
            gcs_time = timestamp_line.split(",")[0]
            hex_line = hex_line.replace("-", "")
            # Parse the 0109 header
            header_fields = extract_dic("0109")
            header = parse_fixed_packet_fast(hex_line[:71], header_fields)
            mission_time = header.get("Mission Time")
            uav_id = header.get("UAV ID")
            msg_type = hex_data[0:4]
            i = 0
            while True:
                print(msg_type)
                result,msg_length= extract_dic(msg_type)
                print(result,msg_length)
                sub_msg = hex_data[i: i + msg_length*2]
                decoded = parse_message(sub_msg, result)
                i = i + msg_length*2
                msg_type = hex_data[i:i + 4]
                decoded.update({
                    "GCS Time": gcs_time,
                    "Mission Time": mission_time,
                    "UAV ID": uav_id,
                    "Rate": rate,
                    "File": file
                })
                decoded_records.append(decoded)

        df = pd.DataFrame(decoded_records)
        all_dfs.append(df)
        print(f"✅ {file} → {len(df)} messages decoded ({len(df.columns)} fields)")

    return pd.concat(all_dfs, ignore_index=True)


# -------------------------------
#  Run
# -------------------------------
if __name__ == "__main__":
    source = r"C:\Users\AIRSHOW\Downloads\experiment\35DH Decoder\test\\"
    df_all = decode_logs(source)
    print("\n🔥 Final combined DataFrame shape:", df_all.shape)
    print(df_all.head())
