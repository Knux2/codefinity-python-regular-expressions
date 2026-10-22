import re

def mask_credit_card_numbers(text):
    def masker(m):
        s = m.group()
        # Count digits only
        digits = re.sub(r'[- ]', '', s)
        if len(digits) != 16:
            return s
        result = []
        count = 0
        # Walk backwards to mask all but last 4 digits
        for ch in reversed(s):
            if ch.isdigit():
                count += 1
                if count > 4:
                    result.append('*')
                else:
                    result.append(ch)
            else:
                result.append(ch)
        return ''.join(reversed(result))

    pattern = r'((?:\d{4}[- ]?){3}\d{4})'
    return re.sub(pattern, masker, text)


print(mask_credit_card_numbers("Pay with 4111 1111 1111 1111 or 5500-0000-0000-0004 today."))
print(mask_credit_card_numbers("Card: 1234-5678-9012-3456; Backup: 4444 3333 2222 1111."))
