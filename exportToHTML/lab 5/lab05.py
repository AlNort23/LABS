def is_valid_part(part: str) -> bool:
    if not part or part.isspace():
        return False
    if len(part) > 1 and part[0] == '0':
        return False

    try:
        num = int(part)
        return 0 <= num <= 255
    except ValueError:
        return False

def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b: str) -> int:
    if len(b) == 1:
        return int(b)
    else:
        return int(b[-1]) + 2 * binary_to_decimal(b[:-1])

def ip_to_binary(ip: str) -> str:
    def convert_part(part: str) -> str:
        if not is_valid_part(part):
            return "Invalid"
        binary = decimal_to_binary(int(part))
        return binary.zfill(8)  # Ensure each part is 8 bits

    def recursive_convert(parts: list) -> str:
        if not parts:
            return ""
        converted = convert_part(parts[0])
        if converted == "Invalid":
            return "Invalid IP"
        if len(parts) == 1:
            return converted
        return converted + "." + recursive_convert(parts[1:])

    return recursive_convert(ip.split("."))

def binary_to_ip(binary: str) -> str:
    def convert_part(part: str) -> str:
        if len(part) != 8 or not all(bit in '01' for bit in part):
            return "Invalid"
        decimal = binary_to_decimal(part)
        return str(decimal)

    def recursive_convert(parts: list) -> str:
        if not parts:
            return ""
        converted = convert_part(parts[0])
        if converted == "Invalid":
            return "Invalid Binary IP"
        if len(parts) == 1:
            return converted
        return converted + "." + recursive_convert(parts[1:])

    return recursive_convert(binary.split("."))

def ip_convert(ip: str) -> str:
    def is_binary_ip(ip: str) -> bool:
        parts = ip.split(".")
        return len(parts) == 4 and all(len(part) == 8 and all(bit in '01' for bit in part) for part in parts)

    if is_binary_ip(ip):
        return binary_to_ip(ip)
    else:
        return ip_to_binary(ip)

# Test cases for binary conversion
binary_conversion_test_cases = [
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (5, "101"),
    (10, "1010"),
    (15, "1111"),
    (42, "101010"),
    (100, "1100100"),
    (255, "11111111"),
    (256, "100000000"),
    (1000, "1111101000")
]

# Test cases for is_valid_part function
valid_part_test_cases = [
    ("0", True),
    ("00", False),
    ("01", False),
    ("1", True),
    ("10", True),
    ("100", True),
    ("255", True),
    ("256", False),
    ("-1", False),
    ("a", False),
    ("", False)
]

# Test cases for ip_convert function
ip_convert_test_cases = [
    ("192.168.0.1", "11000000.10101000.00000000.00000001"),
    ("10.0.0.0", "00001010.00000000.00000000.00000000"),
    ("11000000.10101000.00000000.00000001", "192.168.0.1"),
    ("00001010.00000000.00000000.00000000", "10.0.0.0"),
    ("256.1.2.3", "Invalid IP"),
    ("1.2.3.4.5", "Invalid IP"),
    ("192.168.0", "Invalid IP"),
    ("....", "Invalid IP"),
    ("11111111.11111111.11111111.11111111", "255.255.255.255"),
    ("01010101.01010101.01010101.01010101", "85.85.85.85")
]

print("\nTesting decimal_to_binary function:")
all_correct_d2b = True
for decimal, expected_binary in binary_conversion_test_cases:
    result = decimal_to_binary(decimal)
    correct = result == expected_binary
    all_correct_d2b = all_correct_d2b and correct
    print(f"{decimal} -> {result} (Expected: {expected_binary}) {'✓' if correct else '✗'}")

print("\nTesting binary_to_decimal function:")
all_correct_b2d = True
for expected_decimal, binary in binary_conversion_test_cases:
    result = binary_to_decimal(binary)
    correct = result == expected_decimal
    all_correct_b2d = all_correct_b2d and correct
    print(f"{binary} -> {result} (Expected: {expected_decimal}) {'✓' if correct else '✗'}")

print("\nTesting is_valid_part function:")
all_correct_valid = True
for case, expected in valid_part_test_cases:
    result = is_valid_part(case)
    correct = result == expected
    all_correct_valid = all_correct_valid and correct
    print(f"{case} -> {result} (Expected: {expected}) {'✓' if correct else '✗'}")

print("\nTesting ip_convert function:")
all_correct_ip_convert = True
for input_ip, expected_result in ip_convert_test_cases:
    result = ip_convert(input_ip)
    correct = result == expected_result
    all_correct_ip_convert = all_correct_ip_convert and correct
    print(f"{input_ip} -> {result} (Expected: {expected_result}) {'✓' if correct else '✗'}")

print(f"\nAll decimal_to_binary tests {'passed' if all_correct_d2b else 'failed'}")
print(f"All binary_to_decimal tests {'passed' if all_correct_b2d else 'failed'}")
print(f"All is_valid_part tests {'passed' if all_correct_valid else 'failed'}")
print(f"All ip_convert tests {'passed' if all_correct_ip_convert else 'failed'}")