import base64
import hashlib
import hmac
import os


_ALGORITHM = "pbkdf2_sha256"
_ITERATIONS = 600_000
_SALT_BYTES = 16


def is_hashed_password(stored_password):
    return stored_password.startswith(f"{_ALGORITHM}$")


def hash_password(password):
    salt = os.urandom(_SALT_BYTES)
    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        _ITERATIONS,
    )
    salt_text = base64.urlsafe_b64encode(salt).decode("ascii")
    key_text = base64.urlsafe_b64encode(derived_key).decode("ascii")
    return f"{_ALGORITHM}${_ITERATIONS}${salt_text}${key_text}"


def verify_password(password, stored_password):
    if not is_hashed_password(stored_password):
        return hmac.compare_digest(password, stored_password)

    try:
        algorithm, iteration_text, salt_text, expected_text = stored_password.split("$", 3)
        if algorithm != _ALGORITHM:
            return False
        iterations = int(iteration_text)
        if iterations < 1 or iterations > 2_000_000:
            return False
        salt = base64.urlsafe_b64decode(salt_text.encode("ascii"))
        expected_key = base64.urlsafe_b64decode(expected_text.encode("ascii"))
    except (ValueError, TypeError):
        return False

    actual_key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )
    return hmac.compare_digest(actual_key, expected_key)
