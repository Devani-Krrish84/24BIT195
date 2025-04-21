def bytes_to_kb_mb_gb(bytes):
    kb = bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    return kb, mb, gb

# Example usage
bytes = float(input("Enter the size in bytes: "))
kb, mb, gb = bytes_to_kb_mb_gb(bytes)
print(f"{bytes} bytes is equal to:")
print(f"{kb} KB")
print(f"{mb} MB")
print(f"{gb} GB")